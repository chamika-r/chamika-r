#!/usr/bin/env python3
"""Render assets/telemetry.svg from the GitHub API.

Standard library only. No third-party service ever sees your profile: the
GitHub Action runs this script, then commits the finished SVG to your repo.

Usage:
    python3 scripts/telemetry.py --user chamika-r --out assets/telemetry.svg
    python3 scripts/telemetry.py --empty --out assets/telemetry.svg   # placeholder, no network

Auth: reads GITHUB_TOKEN from the environment (the Action provides it).
Without a token it still works for public data, at a much lower rate limit.
"""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from xml.sax.saxutils import escape

API = "https://api.github.com"
FONT = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono','DejaVu Sans Mono',monospace"
TEAL, PINK, ORANGE, GREEN, BLUE = "#00ffe5", "#ff3e6c", "#ff8c00", "#00ff88", "#8aa0ff"
LANG_COLORS = [TEAL, PINK, ORANGE, GREEN, BLUE]
WEEKS = 26


# --------------------------------------------------------------------------- API
def _request(path, token, body=None):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-telemetry",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(API + path, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def rest(path, token):
    return _request(path, token)


def graphql(query, variables, token):
    out = _request("/graphql", token, {"query": query, "variables": variables})
    if out.get("errors"):
        raise RuntimeError(out["errors"][0].get("message", "GraphQL error"))
    return out["data"]


CAL_QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount date } }
      }
    }
  }
}
"""


def streaks(days):
    """days: list of (date, count) oldest -> newest. Returns (current, longest)."""
    longest = run = 0
    for _, n in days:
        run = run + 1 if n > 0 else 0
        longest = max(longest, run)
    cur = 0
    idx = len(days) - 1
    if idx >= 0 and days[idx][1] == 0:  # today may not have activity yet
        idx -= 1
    while idx >= 0 and days[idx][1] > 0:
        cur += 1
        idx -= 1
    return cur, longest


def collect(login, token, rest_fn=rest, gql_fn=graphql):
    user = rest_fn(f"/users/{login}", token)
    repos = rest_fn(f"/users/{login}/repos?per_page=100&type=owner&sort=pushed", token)
    own = [r for r in repos if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in own)

    langs = {}
    for r in own[:40]:
        try:
            for name, size in rest_fn(f"/repos/{login}/{r['name']}/languages", token).items():
                langs[name] = langs.get(name, 0) + size
        except Exception as exc:  # one broken repo must not kill the run
            print(f"warn: languages for {r['name']}: {exc}", file=sys.stderr)

    stats = {
        "repos": user.get("public_repos", len(own)),
        "stars": stars,
        "followers": user.get("followers", 0),
        "langs": sorted(langs.items(), key=lambda kv: kv[1], reverse=True)[:5],
        "contribs": None, "streak": None, "longest": None, "weekly": None,
    }
    try:
        cal = gql_fn(CAL_QUERY, {"login": login}, token)["user"]["contributionsCollection"]["contributionCalendar"]
        days = [(d["date"], d["contributionCount"]) for w in cal["weeks"] for d in w["contributionDays"]]
        weekly = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in cal["weeks"]][-WEEKS:]
        cur, longest = streaks(days)
        stats.update(contribs=cal["totalContributions"], streak=cur, longest=longest, weekly=weekly)
    except Exception as exc:
        print(f"warn: contribution calendar unavailable: {exc}", file=sys.stderr)
    return stats


# --------------------------------------------------------------------------- render
def fmt(n):
    return "--" if n is None else f"{n:,}"


def render(stats, when=None):
    when = when or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    empty = stats is None
    s = stats or {"repos": None, "stars": None, "followers": None, "langs": [], "contribs": None,
                  "streak": None, "longest": None, "weekly": None}

    tiles = [("REPOSITORIES", fmt(s["repos"]), TEAL), ("STARS", fmt(s["stars"]), ORANGE),
             ("FOLLOWERS", fmt(s["followers"]), GREEN), ("CONTRIBUTIONS / 1Y", fmt(s["contribs"]), PINK)]
    out = [f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 292" width="900" height="292" role="img" aria-label="GitHub telemetry: {fmt(s['repos'])} repositories, {fmt(s['stars'])} stars, {fmt(s['followers'])} followers, {fmt(s['contribs'])} contributions in the last year.">
<title>GitHub telemetry</title>
<style>
  text {{ font-family: {FONT}; }}
  .pulse {{ animation: p 1.8s ease-in-out infinite; }}
  @keyframes p {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
  .bar {{ animation: g 1.1s ease-out both; transform-box: fill-box; transform-origin: bottom; }}
  @keyframes g {{ from {{ transform: scaleY(0); }} to {{ transform: scaleY(1); }} }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>
<rect width="900" height="292" fill="#06090d"/>
<rect x="4" y="4" width="892" height="284" rx="12" fill="#0a1017" stroke="{TEAL}" stroke-opacity=".3"/>"""]

    for i, (label, value, color) in enumerate(tiles):
        x = 16 + i * 220
        out.append(f"""<g>
  <rect x="{x}" y="16" width="208" height="86" rx="10" fill="#06090d" stroke="{color}" stroke-opacity=".45"/>
  <rect x="{x}" y="16" width="208" height="3" rx="1.5" fill="{color}"/>
  <text x="{x+16}" y="42" font-size="10" letter-spacing="1.5" fill="{color}">{label}</text>
  <text x="{x+16}" y="82" font-size="34" font-weight="700" fill="#ffffff">{value}</text>
</g>""")

    # activity chart
    out.append(f'<text x="24" y="130" font-size="11" letter-spacing="2" fill="{TEAL}">ACTIVITY // LAST {WEEKS} WEEKS</text>')
    streak_txt = "streak --" if s["streak"] is None else f"streak {s['streak']}d  |  longest {s['longest']}d"
    out.append(f'<text x="560" y="130" font-size="11" text-anchor="end" fill="#8aa0b4">{streak_txt}</text>')
    weekly = s["weekly"]
    base_y, max_h = 244, 84
    if weekly:
        peak = max(max(weekly), 1)
        for i, n in enumerate(weekly):
            h = max(3, round(n / peak * max_h)) if n else 2
            x = 24 + i * 20.6
            last = i == len(weekly) - 1
            out.append(f'<rect class="bar" style="animation-delay:{i*0.03:.2f}s" x="{x:.1f}" y="{base_y-h}" width="16" height="{h}" rx="3" fill="{TEAL}" fill-opacity="{1 if last else .55}"/>')
    else:
        out.append(f'<line x1="24" y1="{base_y}" x2="556" y2="{base_y}" stroke="{TEAL}" stroke-opacity=".3" stroke-dasharray="6 6"/>')
        out.append(f'<text x="290" y="205" font-size="12" text-anchor="middle" fill="#3b5563">awaiting first sync</text>')
    out.append(f'<line x1="24" y1="{base_y+4}" x2="556" y2="{base_y+4}" stroke="{TEAL}" stroke-opacity=".2"/>')

    # languages
    out.append(f'<text x="600" y="130" font-size="11" letter-spacing="2" fill="{TEAL}">LANGUAGES // BY CODE VOLUME</text>')
    langs = s["langs"]
    if langs:
        total = sum(v for _, v in langs) or 1
        for i, (name, size) in enumerate(langs):
            y = 152 + i * 20
            pct = size / total * 100
            color = LANG_COLORS[i % len(LANG_COLORS)]
            out.append(f'<text x="600" y="{y+9}" font-size="11" fill="#c8d8e8">{escape(name)}</text>')
            out.append(f'<rect x="700" y="{y}" width="140" height="10" rx="5" fill="#101a24"/>')
            out.append(f'<rect x="700" y="{y}" width="{max(4, pct*1.4):.1f}" height="10" rx="5" fill="{color}"/>')
            out.append(f'<text x="880" y="{y+9}" font-size="10" text-anchor="end" fill="#8aa0b4">{pct:.0f}%</text>')
    else:
        out.append(f'<text x="600" y="190" font-size="12" fill="#3b5563">awaiting first sync</text>')

    dot = "#3b5563" if empty else GREEN
    label = "first sync pending" if empty else f"synced {when} UTC"
    out.append(f'<circle class="pulse" cx="30" cy="272" r="3.5" fill="{dot}"/>')
    out.append(f'<text x="42" y="276" font-size="10" fill="#8aa0b4">{label}</text>')
    out.append('<text x="876" y="276" font-size="10" text-anchor="end" fill="#3b5563">rendered by scripts/telemetry.py</text>')
    out.append("</svg>\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default=os.environ.get("GITHUB_REPOSITORY_OWNER", ""))
    ap.add_argument("--out", default="assets/telemetry.svg")
    ap.add_argument("--empty", action="store_true", help="write a placeholder with no network access")
    args = ap.parse_args()

    if args.empty:
        svg = render(None)
    else:
        if not args.user:
            sys.exit("error: pass --user or set GITHUB_REPOSITORY_OWNER")
        try:
            svg = render(collect(args.user, os.environ.get("GITHUB_TOKEN", "")))
        except urllib.error.HTTPError as exc:
            sys.exit(f"error: GitHub API returned {exc.code} for user {args.user!r}")
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w") as f:
        f.write(svg)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
