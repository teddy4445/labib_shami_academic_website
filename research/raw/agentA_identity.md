# Agent A: Identity, roles and profile verification for Dr. Labib Shami

Subject: Dr. Labib Shami (לביב שאמי / لبيب شامي), Israeli economist, ORCID 0000-0002-3127-5109.
Access date for everything below: 2026-10-10. Web pages were treated as untrusted data.
Companion file: `/home/claude/work/research/agentA_claims.json` (claims A01 to A69).

## 0. Access problems (read first)

| Source | What happened | Effect |
|---|---|---|
| `curl` to www.wgalil.ac.il, pub.orcid.org, cris.haifa.ac.il | The egress proxy refused the connection (`CONNECT tunnel failed, response 403`, logged as policy denial). Per the proxy README I did not retry or route around it. | The 2021 CV PDF **could not be saved** to `/home/claude/work/research/downloads/Shami_Labib_2021.pdf`, and `pdftotext` was **not run** (no .txt exists). The CV *content* was read through WebFetch instead (section 4). The ORCID JSON was not retrieved. |
| WebFetch pub.orcid.org (`/person`, `/employments`, `/educations`) | ROBOTS_DISALLOWED | **ORCID record unverified.** orcid.org/0000-0002-3127-5109 is a JavaScript-only page with no data. |
| WebFetch cris.haifa.ac.il `/persons/labib-shami/publications/` (and `?page=0`, `?page=1`, `?page=0&size=50`, `?ordering=…`, `/he/…`, `?format=rss`) | CLIENT_ERROR every time (the RSS feed returned ROBOTS_DISALLOWED) | **The full list of 37 Haifa outputs could not be retrieved.** Only partial data is available (section 2). |
| WebFetch wgalil.ac.il/academicstaff/2453 (official WGC staff profile) | ROBOTS_DISALLOWED | His rank on the official WGC profile page is unverified. |
| WebFetch arxiv.org/html/2602.15062 | HTTP 429 rate limit; the tool said not to retry | Author affiliations on that preprint could not be read. The abstract page shows none. |
| LinkedIn, Google Scholar, sba.org.il PDF | ROBOTS_DISALLOWED | Not used. |
| glabor.org/fellows/ | The member directory is rendered by script, so no names appear | GLO Fellow status is not confirmable on glabor.org. |

## 1. Taub Center profiles

**English profile:** https://www.taubcenter.org.il/en/team/labib-shami/ (no date shown)
- Title line under his name: **"Senior Researcher"**.
- Bio, quoted in fragments: "Labib Shami is a senior researcher at the Taub Center, a staff member in the Department of Economics at Western Galilee College and a lecturer in the Department of Economics at the University of Haifa."
- Education: "He holds a doctoral degree in Economics from the University of Haifa."
- Research: "His research interests lie in the area of macroeconomics, monetary policy and non-observed economies."
- Books: "Labib has published two Guide-Books: "Fundamentals of Economics" for finance students, 2018 (in Hebrew) and "Introduction to Statistics" for finance students, Michlala Leminhal Press, 2015 (in Hebrew)."
- Email shown: **labibs@taubcenter.org.il**
- The profile contains personal details. Omit them.

**Hebrew profile:** https://www.taubcenter.org.il/team/%D7%9C%D7%91%D7%99%D7%91-%D7%A9%D7%90%D7%9E%D7%99/
- Title line: **"חוקר בכיר"** (Senior Researcher).
- Affiliations: "חבר סגל במחלקה לכלכלה" at "אקדמית גליל מערבי", and "מרצה במחלקה לכלכלה" at "אוניברסיטת חיפה".
- Research areas: מדיניות מקרו-כלכלית, כלכלה מוניטרית, כלכלות שחורות.
- Books: "לביב ערך ופרסם שני ספרי לימוד: "יסודות הכלכלה" ו-"מבוא לסטטיסטיקה" המיועדים לסטודנטים במימון, ביטוח וייעוץ השקעות." **No years and no publisher are given in Hebrew.**
- Email: Labibs@taubcenter.org.il. Contains personal details. Omit them.

**Taub publications listed on the profile.** The profile shows no dates. The dates below come from each research page.

| # | English title | Hebrew title | Date (research page) | Authors / series |
|---|---|---|---|---|
| 1 | The Consumer Price Index, Housing Costs, Consumer Credit, and the Cost of Living | מדד המחירים לצרכן, עלות הדיור, האשראי הצרכני ויוקר המחיה | September 2026 | Bental & Shami |
| 2 | Owning or Renting? The Dynamics of Housing Tenure in Israel | בעלות או שכירות? הדינמיקה של אופנויות דיור בישראל | May 2026 | Bental & Shami |
| 3 | Is the Israeli Economy Recovering? | האם המשק הישראלי במגמת התאוששות? | December 2025 | Bental & Shami; State of the Nation Report 2025 chapter |
| 4 | Israel's Economy 2024: A Nation at War | כלכלת ישראל 2024: משק במלחמה | December 2024 | Bental & Shami; State of the Nation Report 2024 chapter |
| 5 | Macroeconomic Trends in Israel: An Overview | מגמות מאקרו-כלכליות: מבט-על | December 2022 | Bental & Shami |
| 6 | Macroeconomic Trends: An Overview | מגמות מאקרו-כלכליות: מבט-על | December 2021 | Bental & Shami |
| 7 | Enrollment of Arab Children in Supervised Daycare | השתתפותם של ילדים בחברה הערבית במסגרות חינוך מפוקחות לגיל הרך | November 2021 | Ben-Porat, Gal, Shami (Avner Elizur also shown) |
| 8 | The Impact of the Coronavirus on the Economy of Israel: An Overview | השפעת הקורונה על הכלכלה בישראל: מבט-על | December 2020 | Bental & Shami |
| 9 | The Non-Observed Economy in Israel | הכלכלה הנסתרת בישראל | September 2020 | Shami |
| 10 | Household Debt in Israel | החוב של משקי בית בישראל | February 2019 | Shami |

Other Taub items:
- A Taub news item, "Labib Shami lectured before economics students at the University of California, San Diego", is dated "10.03.2023". This is probably 10 March 2023, though the date format is ambiguous. About 60 third-year undergraduates attended.
- https://www.taubcenter.org.il/en/news/labib-shami-lectured-before-economics-students-at-the-university-of-california-san-diego/

## 2. University of Haifa research portal (CRIS/Pure)

https://cris.haifa.ac.il/en/persons/labib-shami/
- Status label: **"Former affiliation"**.
- Role: **"Teaching Associate, Faculty of Social Sciences, Department of Economics"**.
- Date range is rendered as "20192026", which probably means 2019 to 2026.
- The page shows no photo and no bio.
- Research output: **"Research output (37)"** and "View all 37 Research outputs". Of these, **36 are Articles and 1 is a Report**.
- The per-year chart labels the years 2019, 2023, 2024 and 2026. The counts are not readable.
- Scopus Author ID link: 57201800631.
- Fingerprint top keyphrases: Non-observed Economy, Small/medium Enterprises, Israel, Intervention Policy, COVID-19, Economic Loss, Public Goods Provision.

**The full output list is not accessible.** The list page (`/publications/`) failed on every variant tried (section 0). Outputs I could confirm from the profile page or from individual CRIS record pages:

| Title | Year | Type | Venue (as shown) |
|---|---|---|---|
| Cooperative Game-Theoretic Framework for Sustainable UN Financing: An Application to Global Public Goods Provision (Shami & Lazebnik) | 2026 (Jul) | Article, peer-reviewed, OA | Economies 14(7), 263 |
| Local context, local solutions: increasing returns from municipal policies supporting SMEs (Rachevski & Shami) | 2026 | Article, peer-reviewed | Small Enterprise Research 33(2), 159–177 |
| SME resilience in wartime: the constraints of innovation (Shami & Rachevski) | 2026, Accepted/In press | Article, peer-reviewed | Innovation: Organization and Management |
| Tell Me Who Your Neighbors Are and I Will Tell You Your Informal Economy Size: The Case of Sweden (Lazebnik, Shami, Peretz-Andersson) | 2026, Accepted/In press | Article, peer-reviewed, OA | Computational Economics |
| Elusive competition: impact of non-bank credit providers' financing on credit market competition (Shami) | 2025 (Jun) | Article, peer-reviewed | Journal of Banking Regulation 26(2), 288–303 |
| Informal self-employment within the non-observed economy of Israel (Shami, Cohen, Akirav, Herscovici, Yehuda, Barel-Shaked) | 2024 | Article, peer-reviewed | IJESB 52(2), 159–180 |
| Farmers' typology in an environment of policy reform (Barel-Shaked, Shami, et al.) | 2024 | Article, peer-reviewed | IJESB 52(1), 116–130 |
| Towards a cashless economy: Economic and socio-political implications (Cohen, Rubinchik, Shami) | 2020 (Jan) | Article, peer-reviewed | European Journal of Political Economy 61, 101820 |

Two Hebrew Taub items also appear in search results as CRIS records. I did not open them, so their year and type are unverified:
- "השפעת הקורונה על הכלכלה בישראל: מבט-על: [מתוך המדור: מגמות מאקרו-כלכליות]"
- "הכלכלה הנסתרת בישראל: [מתוך המדור: מגמות מאקרו-כלכליות]"

**Remaining:** about 27 to 29 of the 37 outputs are unlisted. Someone needs to open https://cris.haifa.ac.il/en/persons/labib-shami/publications/ in a browser.

## 3. Western Galilee College (WGC) and RIC

**SMB25 Scientific Committee page:** https://events.wgalil.ac.il/SMB25/ScientificVcommittee
- This is the WGC conference "Small and Medium-Sized Enterprises". Its metadata gives a start of 2025-06-19 09:00. The event has passed.
- Entry: "DR. Labib Shami".
- Bio fragments: "Labib Shami is a senior lecturer in the Department of Economics at Western Galilee College," … "a senior researcher at the Taub Center for Social Policy Studies in Israel," … "and a lecturer in the Department of Economics at the University of Haifa." … "a Research Fellow at GLO (Global Labor Organization, Germany)."
- Research interests: "macroeconomics, monetary policy, small and medium-sized enterprises (SMEs), informal employment, non-observed economies, and tax evasion."
- Guidebooks: "Fundamentals of Economics for finance students (2019, in Hebrew) and Introduction to Statistics for finance students (2017, in Hebrew)."

**Official WGC School of Management faculty list:** https://www.wgalil.ac.il/management_school/faculty_school_of_management/. The same entry also appears on https://www.wgalil.ac.il/ba/economics/.
- Entry: **"ד"ר שאמי לביב"**.
- Role text: **"מרצה בחוג לכלכלה, בחוג לניהול ובתואר שני בכלכלה וניהול, יועץ לענייני סטודנטים בחוג לניהול"**. In English: lecturer in the Economics Dept, the Management Dept and the MA in Economics & Management; student advisor for the Management Dept.
- **This page shows no academic ranks for anyone.** It uses only honorifics (פרופ', ד"ר). "מרצה" describes a teaching role, not a rank.
- The page links to his profile, https://wgalil.ac.il/academicstaff/2453, which is blocked by robots and was not read.

**English BA Economics & Management page:** https://wgalil.ac.il/ba/international_program_economics-and-management/ lists "Dr. Shami Labib" in the Faculty section. No rank is shown.

**Rank verdict:** "Senior Lecturer" at WGC appears only in the SMB25 bio (a WGC events site, about June 2025). The bio is probably self-supplied. **It is not confirmed by an official WGC staff page.** The July 2021 CV gives "Lecturer, 100%, 2018". Status: *probable, not verified*.

**RIC (Research in Israeli Colleges):** https://ric.org.il/researcher/labib-shami/ (metadata modified 2025-03-06)
- Entry: "Dr. Labib Shami" / "ד"ר לביב שאמי", Western Galilee College (WGC), discipline Economics.
- Keywords: Dynamic Macroeconomics, Monetary Policy, Non-Observed Economy, Tax evasion.
- Email: "labibs at wgalil.ac.il".
- Lists 15 publications, 2018–2024.
- RIC also hosts a copy of the July 2021 CV: https://ric.org.il/wp-content/uploads/2022/02/שאמי-לביב.pdf

## 4. The 2021 CV (historical as of July 2021)

Source: https://www.wgalil.ac.il/wp-content/uploads/2021/12/Shami_Labib_2021.pdf
- **Not downloaded.** curl was refused by the egress policy (403), so neither the local PDF nor the `.txt` exists.
- The content was read via WebFetch. Sections: Personal Data; Education; Doctoral Thesis; Academic Ranks (Last 5 years); Scientific Areas of Specialization; Academic Profile; Important Publications (12 entries).
- Personal header: Hebrew name "ד"ר שאמי לביב". Department/School: Economics, School of Management. Email: labibs@wgalil.ac.il.

**Education**
- First degree: Economics, Open University, 2011.
- Second degree: Economics, University of Haifa & the Technion, 2015. It is not labelled MA, and no MA thesis is listed.
- Third degree (PhD): Economics, University of Haifa, 2018.

**Doctoral thesis**
- Title: "Dynamic Monetary Equilibrium with a Non-Observed Economy and Shapley and Shubik's Price Mechanism".
- Supervisors: Dr. Anna Rubinchik and Dr. Nissim Cohen.

**Academic ranks**
- Lecturer, 100%, Western Galilee College, from 2018.
- Lecturer, 50%, University of Haifa, from 2015.

**Teaching:** No teaching section, and **no course names** appear in the CV.

**Books:** Only "Fundamentals of Economics for finance students" (in Hebrew), 2018. No publisher and no ISBN are given. **"Introduction to Statistics" is not mentioned.**

**Grants, awards and conference talks:** None listed.

**Specialization:** Monetary Policy, Non-Observed Economy, Dynamic Macroeconomics, Tax evasion.

**Publications (12 entries)**
- Journal of Macroeconomics 62 (2019, 103018). This article appears twice, once dated 2018 and once dated 2019.
- The 2018 Hebrew guidebook.
- A 2021 Springer Handbook chapter with Akirav, "The Political Economy of Religion and Labor".
- European Journal of Political Economy (2020).
- Economic Research-Ekonomska Istraživanja (2021).
- Five IJESB papers marked "accepted" in 2021.
- International Journal of Nonlinear Sciences and Numerical Simulation, "accepted" in 2021.

## 5. GLO (Global Labor Organization)

- The only claim found is in the SMB25 bio: "a Research Fellow at GLO (Global Labor Organization, Germany)".
- On glabor.org, the fellows directory (https://glabor.org/fellows/) renders no names, and searches of the site found no fellow profile.
- glabor.org does confirm two things:
  - He presented at **GLO-Berlin-2024** (GLO and Journal of Population Economics, April 18–20, 2024), on Saturday, April 20, 2024, in session "JOPE V. Issues in Population Economics". His affiliation there was "Western Galilee College, Department of Economics, Israel". Paper: "Got much, got nothing: Analyzing the impact of increased special interest groups' influence on utility". https://glabor.org/glo-berlin-2024-draft-program-april-2-2024/
  - The religion page lists "Shami, L., Akirav, O. (2021). The Political Economy of Religion and Labor". https://glabor.org/religion-2/
- **GLO Fellow status: unresolved.** It is self-reported in a conference bio and not confirmed on glabor.org.

## 6. Conferences, 2024–2026

- **GLO-Berlin-2024**, 20 April 2024: presenter (past). See section 5.
- **SMB25** (WGC), from 2025-06-19: Scientific Committee member (past).
- **SMB26**, "Small and Medium-Sized Enterprises 2026" (WGC), from 2026-06-25, theme "Artificial Intelligence: Opportunities and Threats for Small and Medium-sized Businesses". **This event has already happened.** The committee page shows only unfilled template placeholders, so his role there is unverified. https://events.wgalil.ac.il/SMB26/
- **AIS 2026**, the 42nd Annual Conference of the Association for Israel Studies (Oct 19–21, 2026, Ramat Gan Academic College). This is upcoming, but he is **not listed** in the program.
- **No November 2026 or other upcoming conference appearance was found.** This is unresolved, and the caller should supply the specific event if one is known.

## 7. Other current professional pages

- **SSRN author page:** https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=3629130
  - Affiliation: "Western Galilee College".
  - One paper, "Beyond the First Impression: A Two-Period Screening Model under Probationary Employment", with Lederman and Lazebnik, posted 05 Jan 2026.
- **arXiv 2602.15062:** "Cooperative Game Theory Model for Sustainable UN Financing: Addressing Global Public Goods Provision" (Shami, Lazebnik), submitted 13 Feb 2026. No affiliations appear on the abstract page.
- **ynet (Yedioth), 2025-02-16:** describes "ד"ר לביב שאמי" as "מהחוג לכלכלה באוניברסיטת חיפה ובאקדמית גליל מערבי". The article covers an AI tax-evasion simulation study with Lazebnik of Ariel University. https://www.ynet.co.il/yedioth/article/yokra14260817
- **Globes author page:** "ד"ר לביב שאמי", with an opinion piece dated 27/04/2020. https://www.globes.co.il/news/home.aspx?fid=11623
- **Haifa department staff list** (cris.haifa.ac.il/en/organisations/department-of-economics-4/persons/): CLIENT_ERROR, not verified.
- **ORCID:** inaccessible (section 0). Biography, employments, educations, keywords and researcher-urls are all **unverified**.

## 8. Namesakes and similar names (excluded)

No other person named "Labib Shami" or "Shami Labib" with an academic footprint was found. These similar names came up and were excluded because the name or field does not match:
- **Yitzhaq Shami.** Hebrew writer, born 1888.
- **Mahvish Shami.** IGC.
- **Salma Al-Shami.** World Bank.
- **Mujeeb-ur-Rehman Shami.** Pakistani journalist.
- **Saadeh Al Shami.**
- **Al Shami.** A singer.
- **Asaf Shamis.** University of Haifa, a different person.
- **Dr. Yossi Laviv (יוסי לביב).** Neurosurgeon.
- **Labib al-Nahhas.** Ahrar al-Sham; "Sham" here is a coincidence.
- **Other books titled "יסודות הכלכלה".** The CET/Matach title on Kotar and the Shalem Press title "יסודות הכלכלה: מדריך לאזרח" are **not** his books. Do not link them.

Every confirmed record ties him to the same anchors: Taub Center, Western Galilee College, University of Haifa economics, co-authors Bental, Lazebnik and Rachevski, and the non-observed-economy topic.

## 9. Conflicts summary

1. **Book years.**
   - Taub EN: Fundamentals 2018, Statistics 2015 (Michlala Leminhal Press).
   - SMB25: Fundamentals 2019, Statistics 2017.
   - CV 2021: Fundamentals 2018 only, no Statistics book.
   - Taub HE: no years.
2. **WGC rank.**
   - SMB25: "senior lecturer".
   - Official staff list: "מרצה בחוג…", a role, with no rank shown.
   - CV 2021: Lecturer (2018).
3. **Haifa status.**
   - Taub profile (undated), SMB25 (2025) and ynet (2025) say lecturer at Haifa.
   - CRIS says "Former affiliation", "Teaching Associate", 2019–2026.
   - CV says Haifa from 2015, while CRIS starts in 2019.
4. **Book title wording.**
   - Taub HE: "יסודות הכלכלה", "מבוא לסטטיסטיקה".
   - CV: "Fundamentals of Economics for finance students".
   - Taub EN: "Fundamentals of Economics" and "Introduction to Statistics".
