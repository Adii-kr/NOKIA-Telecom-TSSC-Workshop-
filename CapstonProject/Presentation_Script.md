# Mini-Capstone 2 — Presentation Script
---

## Slide 1 — Title: "Subscriber Segmentation, Finding Our Best Customers"
**Speaker: Presentation Lead** *(~20 sec)*

> Good [morning/afternoon] everyone. We're [team name], and today we're walking you
> through our Mini-Capstone project on subscriber segmentation and anomaly detection.
> I'm [name], and with me are [name] on data and setup, [name] on segmentation,
> [name] on anomaly and fraud detection, and [name] as our business analyst — each of
> us worked a different part of this, and we're all happy to take questions on any of
> it at the end.

*(Hand off to self for slide 2, or gesture to Data & Setup Lead to join at the front.)*

---

## Slide 2 — "The Problem: Losing Subscribers and Revenue"
**Speaker: Presentation Lead (opens), then Data & Setup Lead (data facts)**

**Presentation Lead** *(~20 sec)*
> Here's the problem we set out to solve. Telecom operators lose subscribers and often
> only find out after the fact — by the time churn shows up in a report, the
> subscriber is already gone. At the same time, fraud and billing faults are quietly
> leaking revenue, hidden inside routine monthly usage data. We had two jobs: find the
> natural groups of subscribers hiding in the data, and find the small number of
> accounts that don't look right.

**Data & Setup Lead** *(~25 sec)*
> To do that, we worked with two datasets: one row per subscriber covering things like
> monthly data use, tenure, spend, and complaints, and a second file with eighteen
> thousand monthly usage and revenue records across six months. Getting this right
> mattered — we cleaned the data, handled missing values, and made sure every number
> feeding into the models was on the same footing before any modeling started. That
> groundwork is what let the rest of the team trust their results.

---

## Slide 3 — "Four Subscriber Segments: Understanding Our Customer Profiles"
**Speaker: Segmentation Lead** *(~50 sec)*

> We grouped subscribers purely by behavior — not by what plan they were sold — and
> four clear segments came out of it.
>
> **Steady and Balanced** subscribers spend a moderate amount, have been with us a
> long time, and use both data and voice in a balanced way — this is our stable,
> loyal base.
>
> **Premium Loyal** is our highest-spending group, with the longest tenure and the
> fewest complaints. These are prime candidates for a loyalty program — the goal here
> is protection, not acquisition.
>
> **Budget and New** subscribers spend the least, have been with us the shortest
> time, and — as the name suggests — have the highest raw churn rate of any group. They
> need low-cost engagement, not expensive retention offers, because each individual
> subscriber here is lower value.

*(Pause, advance to slide 4 — same speaker continues.)*

---

## Slide 4 — "Subscriber Segment Analysis: Understanding the Data Heavy Young"
**Speaker: Segmentation Lead** *(~30 sec)*

> The fourth segment gets its own slide because it's the one that matters most for
> what comes next: **Data Heavy Young**. This group uses a lot of data — high
> engagement — but has a short tenure, which is a real risk. If we don't retain them
> proactively, they can leave quickly, and unlike Budget and New, losing one of these
> subscribers actually costs us something. I'll hand it over to [Business Analyst's
> name] to explain why this segment is the one we focused on.

---

## Slide 5 — "Most Worth Worrying About: Data Heavy Young Puts the Most Revenue at Risk"
**Speaker: Business Analyst** *(~40 sec)*

> Here's the key insight that connects segmentation to the business impact. Raw churn
> rate alone is misleading — a small, low-value segment can look scary on a churn
> chart and not actually matter much to revenue. So instead, we ranked every segment
> by **expected revenue at risk**: segment size, times churn rate, times average
> revenue per user.
>
> Budget and New technically has the single highest churn rate. But Data Heavy Young
> has a churn rate almost as high, combined with more than double the revenue per
> user. When you weigh both, **Data Heavy Young is the segment that puts the most
> revenue at risk** if we do nothing. That's why it's the one we built our
> recommendation around.

---

## Slide 6 — "Fraud Detection Patterns: Identifying Revenue Leaks and Risks"
**Speaker: Anomaly Lead** *(~50 sec)*

> Alongside segmentation, we went looking for the small number of accounts hidden in
> those eighteen thousand monthly records that simply don't look right. We used a
> model called an isolation forest — without going into the mechanics, its job is to
> find the records that stand out from everything else — and it surfaced three real
> patterns.
>
> **Bypass fraud** looks like enormous international minutes paired with almost no
> data usage, resulting in a suspiciously low bill for that much traffic.
>
> **Subscription fraud** shows usage climbing steadily, then suddenly dropping to
> zero alongside failed payments — a strong signal of fraudulent intent.
>
> **Revenue leakage** is different — it's real usage that gets billed at exactly
> zero. That's not fraud, that's a billing fault, and it needs a different fix.
>
> We also sized our alert sensitivity to what a two-person investigation team can
> realistically review every week, so this isn't just a list of flags — it's an
> operational process someone can actually run.

---

## Slide 7 — "Recommendations and Next Steps: Target At-Risk Segment and Run Fraud Alert Routinely"
**Speaker: Business Analyst** *(~35 sec)*

> Bringing it together: our recommendation is to target the Data Heavy Young segment
> with proactive retention — offers and outreach designed to keep them engaged before
> they hit that short-tenure churn window — and to run our fraud alert as a routine
> monthly job, not a one-time analysis. We costed this out: the value protected from
> retaining even a modest share of at-risk subscribers, plus the cases the fraud alert
> catches each month, comfortably outweighs the cost of running both programs.

---

## Slide 8 — "Conclusion: Moving Forward with Effective Strategies"
**Speaker: Presentation Lead** *(~20 sec)*

> To sum up: we found four behavioral segments, identified which one actually puts the
> most revenue at risk, and built a fraud detection process the business can run every
> month rather than after the fact. Thank you — we're happy to take any questions, and
> as I mentioned, all five of us can speak to any part of this.

---