<div align="center">

![header](https://capsule-render.vercel.app/api?type=rect&color=0:060a0f,100:0a0f1a&height=3)

</div>

<!-- HERO PANEL -->
<table width="100%" cellspacing="0" cellpadding="0">
<tr>
<td>

![typing](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=14&pause=1000&color=00FF88&width=700&height=22&lines=//+TARGET%3A+chamika-r+%E2%80%94+RECON+INITIALIZING...;[+SCAN+COMPLETE+]+8+security+tools+built+from+scratch;[+CRITICAL+]+SQL+injection+confirmed+on+DVWA;[+LIVE+]+CVE+dashboard+deployed+%E2%80%94+online+now;[+97.20%25+]+phishing+detection+accuracy;[+STATUS+]+actively+building+%E2%80%94+never+stopping.)

</td>
<td align="right">

[![TryHackMe](https://img.shields.io/badge/TryHackMe-seasonsofyjinn-212C42?style=flat-square&logo=tryhackme&logoColor=red)](https://tryhackme.com/p/seasonsofyjinn)
[![Live Demo](https://img.shields.io/badge/CVE_Dashboard-LIVE-00ff88?style=flat-square&logo=render&logoColor=black)](https://cve-dashboard-pup2.onrender.com)

</td>
</tr>
</table>

<br>

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  TARGET     ::  CHAMIKA RANAWEERA                                           ║
║  ROLE       ::  Cybersecurity Undergraduate @ SLIIT — Sri Lanka             ║
║  OBJECTIVE  ::  Junior SOC Analyst — foreign security teams                 ║
║  APPROACH   ::  Don't just study attacks — build the tools that detect them ║
║  STATUS     ::  [ ACTIVELY BUILDING ] — 8 tools shipped, more incoming      ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

<br>

<!-- STAT BADGES -->
<div align="center">

![Tools](https://img.shields.io/badge/Tools_Built-08_from_scratch-00ff88?style=for-the-badge&labelColor=0a0f1a)
![Accuracy](https://img.shields.io/badge/ML_Accuracy-97.20%25-00bcd4?style=for-the-badge&labelColor=0a0f1a)
![Severity](https://img.shields.io/badge/Highest_Finding-CRITICAL_SQLi-ff4081?style=for-the-badge&labelColor=0a0f1a)
![Vulns](https://img.shields.io/badge/Vulns_Confirmed-9_on_DVWA-ffd54f?style=for-the-badge&labelColor=0a0f1a)
![CVEs](https://img.shields.io/badge/CVEs_Found-80_in_one_scan-b388ff?style=for-the-badge&labelColor=0a0f1a)
![SBOM](https://img.shields.io/badge/SBOM-EO_14028_Compliant-00bcd4?style=for-the-badge&labelColor=0a0f1a)

</div>

<br>

---

## `$ ls -la ~/security-tools/ --sort=impact`

<br>

| &nbsp; | Project | What it does | Result |
|--------|---------|-------------|--------|
| 🟢 | **[phishing-detector](https://github.com/chamika-r/phishing-detector)** `Python · sklearn · Flask` | ML classifier trained on 5,172 real emails — Flask REST API with confidence scores | ![](https://img.shields.io/badge/97.20%25_accuracy-00ff88?style=flat-square) |
| 🔴 | **[web-vulnerability-scanner](https://github.com/chamika-r/web-vulnerability-scanner)** `Python · OWASP · ReportLab` | OWASP Top 10 scanner — tested on DVWA, found 9 real vulns, generates PDF pentest reports | ![](https://img.shields.io/badge/CRITICAL_SQLi-ff4081?style=flat-square) |
| 🔵 | **[cve-dashboard](https://github.com/chamika-r/cve-dashboard)** `Flask · SQLite · Chart.js` | Real-time NIST NVD feed — severity filtering, trend charts, 24h refresh | [![LIVE](https://img.shields.io/badge/LIVE_NOW-00bcd4?style=flat-square)](https://cve-dashboard-pup2.onrender.com) |
| 🟡 | **[email-auth-analyzer](https://github.com/chamika-r/email-auth-analyzer)** `dnspython · Flask` | BEC detection — SPF/DKIM/DMARC via live DNS, Levenshtein lookalike domains, 0-100 risk score | ![](https://img.shields.io/badge/BEC_Detection-ffd54f?style=flat-square) |
| 📡 | **[network-analyzer](https://github.com/chamika-r/network-analyzer)** `Scapy · Rich` | Live packet capture — ARP spoof + port scan detection, Rich terminal dashboard 0.5s refresh | ![](https://img.shields.io/badge/Real--time_Alerts-00ff88?style=flat-square) |
| 🟣 | **[dependency-scanner](https://github.com/chamika-r/dependency-scanner)** `OSV API · Flask` | Python + Node.js CVE scanner — Google OSV database, same as GitHub Dependabot | ![](https://img.shields.io/badge/80_CVEs_Found-b388ff?style=flat-square) |
| 📋 | **[sbom-scanner](https://github.com/chamika-r/sbom-scanner)** `CycloneDX · OSV API` | CycloneDX 1.4 SBOM generator + OSV scanner — satisfies US EO 14028 + EU CRA 2024 | ![](https://img.shields.io/badge/EO_14028-00bcd4?style=flat-square) |
| 🔐 | **[digital-security-toolkit](https://github.com/chamika-r/digital-security-toolkit)** `HIBP · Pillow` | Password breach check (k-anonymity) + image EXIF metadata stripper | ![](https://img.shields.io/badge/Privacy_First-00ff88?style=flat-square) |

<br>

---

## `$ cat ops_status.log`

<br>

```
╔══ COMPLETED ════════════════════════════════════════════════════════════════╗
║                                                                             ║
║  [✔] phishing-detector        97.20% accuracy · 5,172 real emails          ║
║  [✔] network-analyzer         ARP spoof + port scan detection live          ║
║  [✔] web-vulnerability-scanner  CRITICAL SQLi · 9 vulns · PDF report       ║
║  [✔] cve-dashboard            LIVE on Render · NIST NVD real-time feed      ║
║  [✔] email-auth-analyzer      BEC detection · live DNS · 0-100 risk score  ║
║  [✔] dependency-scanner       80 CVEs found · fix versions · PDF reports   ║
║  [✔] sbom-scanner             CycloneDX 1.4 · EO 14028 · EU CRA 2024      ║
║  [✔] digital-security-toolkit  k-anonymity · GPS EXIF stripper             ║
║  [✔] quantum-computing-report  Shor's algo · NIST PQC 2024 standards       ║
║  [✔] vulnapp-recon-assessment  5 findings · IDOR · admin panel · no TLS   ║
║                                                                             ║
╠══ IN PROGRESS ══════════════════════════════════════════════════════════════╣
║                                                                             ║
║  [▶] cloud-security-scanner   AWS S3 · IAM misconfigs · security groups    ║
║      ████████░░░░░░░░  55%                                                  ║
║                                                                             ║
║  [▶] llm-prompt-injection     AI red-teaming · jailbreak taxonomy          ║
║      ██████░░░░░░░░░░  40%                                                  ║
║                                                                             ║
║  [▶] cyber-attack-encyclopedia  60+ topics · OWASP · MITRE ATT&CK         ║
║      ████░░░░░░░░░░░░  25%                                                  ║
║                                                                             ║
╠══ PLANNED ══════════════════════════════════════════════════════════════════╣
║                                                                             ║
║  [○] research-paper-01  Sinhala/Tamil phishing — first dataset worldwide   ║
║  [○] research-paper-02  LLM prompt injection taxonomy — IEEE/arXiv target  ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

<br>

---

## `$ nmap -sV --skills chamika-r`

<br>

<table>
<tr>
<td width="50%" valign="top">

**`// SECURITY`**
```
[████████░░]  OWASP Top 10 · Pentest
[███████░░░]  MITRE ATT&CK · Kill Chain
[████████░░]  BEC · Email Auth Analysis
[███████░░░]  SBOM · Supply Chain Sec
[██████░░░░]  Cloud Security · AWS
[████████░░]  Vulnerability Assessment
[███████░░░]  Threat Intelligence
```

</td>
<td width="50%" valign="top">

**`// TOOLS & STACK`**
```
Python · Flask · scikit-learn · Scapy
Wireshark · Nmap · SQLMap · Burp Suite
Kali Linux · Ubuntu · Git · Docker
MySQL · SQLite · REST APIs · Chart.js
CycloneDX · OSV API · HIBP · dnspython
ReportLab · Pillow · BeautifulSoup
Java · C · HTML · PHP
```

</td>
</tr>
</table>

<br>

---

## `$ cat github_stats.sh && bash github_stats.sh`

<br>

<div align="center">

<img height="175" src="https://github-readme-stats.vercel.app/api?username=chamika-r&show_icons=true&theme=github_dark&hide_border=true&bg_color=060a0f&title_color=00ff88&icon_color=00bcd4&text_color=8892a4&ring_color=00ff88&hide=prs,issues" />
&nbsp;
<img height="175" src="https://github-readme-stats.vercel.app/api/top-langs/?username=chamika-r&layout=compact&theme=github_dark&hide_border=true&bg_color=060a0f&title_color=00ff88&text_color=8892a4&langs_count=6" />

<br><br>

<img width="68%" src="https://github-readme-streak-stats.herokuapp.com/?user=chamika-r&theme=github-dark-blue&hide_border=true&background=060a0f&ring=00ff88&fire=ff4081&currStreakLabel=00ff88&sideLabels=8892a4&dates=8892a4&stroke=1e3a5f" />

<br><br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=chamika-r&theme=github-compact&hide_border=true&bg_color=060a0f&color=00ff88&line=00bcd4&point=ff4081" />

</div>

<br>

---

## `$ cat education.txt`

<br>

```
[2024 → 2028]  BSc (Hons) IT — Cyber Security Specialisation
               Sri Lanka Institute of Information Technology (SLIIT)
               Year 02 | Cyber Security · Network Programming · AI & ML · OS Admin

[2024]         G.C.E Advanced Level · Lyceum International School
               Accounting: A  |  ICT: B  |  General English: B

[2026]         Cyber Security Bootcamp · STEMLink
```

<br>

---

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   "Don't just study attacks — build the tools that detect them."        │
│                                                                         │
│                                          — chamika-r                    │
│                                                                         │
│   Open to: Junior SOC Analyst · Security Engineer · AppSec roles        │
│   Markets: UK · Australia · Singapore · Remote                          │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

<br>

[![Email](https://img.shields.io/badge/chamikaranaweera30@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:chamikaranaweera30@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/chamikaranaweera)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chamika-r)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?style=for-the-badge&logo=tryhackme&logoColor=red)](https://tryhackme.com/p/seasonsofyjinn)

<br>

![visitors](https://komarev.com/ghpvc/?username=chamika-r&style=flat-square&color=00ff88&label=profile+views)

</div>

<div align="center">

![footer](https://capsule-render.vercel.app/api?type=rect&color=0:0a0f1a,100:060a0f&height=3)

</div>