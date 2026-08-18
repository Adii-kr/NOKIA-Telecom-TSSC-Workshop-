# NOKIA Telecom TSSC Workshop — Data Analytics Exercises & Capstone Projects

A collection of hands-on exercises and two capstone projects from a telecom data analytics workshop, covering the full pipeline from raw data to business recommendations: SQL fundamentals, Python data cleaning, ETL pipelines, machine learning (churn and ARPU prediction), time-series forecasting, real-time KPI monitoring, sentiment analysis, and support-ticket routing — all built around synthetic telecom operator data (subscribers, usage, network KPIs, billing, and support tickets).

## Repository Structure

Each `MoP-ExNN` folder is a self-contained "Method of Procedure" exercise: a PDF write-up of the exercise, one or more Jupyter notebooks (or SQL scripts) implementing it, and the CSV/database files it operates on.

```
WORKSHOP/
├── MoP-Ex01/   # SQL fundamentals — querying a telecom dataset in MySQL
├── MoP-Ex02/   # Python data cleaning — handling missing values, duplicates, inconsistent formats
├── MoP-Ex03/   # ETL mini-project — building a simple Extract-Transform-Load pipeline into MySQL
├── MoP-Ex04/   # Automated ETL pipeline — a scheduled Python job (auto_etl.py) that cleans and re-runs on a timer
├── MoP-Ex05/   # Churn prediction — a scikit-learn classification pipeline to flag at-risk subscribers
├── MoP-Ex06/   # ARPU prediction — modeling Average Revenue Per User from subscriber usage/tenure features
├── MoP-Ex07/   # Monthly traffic forecasting — per-cell forecasting with Facebook Prophet
├── MoP-Ex08/   # Live KPI feed & windowed aggregation — simulated real-time network KPI ingestion into SQLite
├── Mop-Ex09/   # Grafana live monitoring & alert engineering — SQL setup for dashboarding/alerting on the KPI data
├── MoP-Ex10/   # Sentiment analysis — classifying customer complaint/feedback text
├── MoP-Ex11/   # Support ticket routing — a TF-IDF + logistic regression classifier to route tickets by category
├── CapstonProject/    # Mini-Capstone 2: Subscriber Segmentation & Anomaly Detection
└── CapstonProject2/   # Final Capstone: Telecom Data Analytics — From Raw Data to Business Recommendation
```

### Exercise-by-exercise

| Folder | Topic | Key files |
|---|---|---|
| `MoP-Ex01` | SQL fundamentals | `MoP Essential SQL.sql` |
| `MoP-Ex02` | Python data cleaning (missing values, mixed date formats, casing, duplicates) | `PythonCleaning.ipynb`, `telecom_usage.csv` → `cleaned_telecom_usage.csv` |
| `MoP-Ex03` | ETL into MySQL (via `pymysql`) | `ETL Mini-Project-MySQL.ipynb`, `complaints.csv` → `etl_output.csv` |
| `MoP-Ex04` | Scheduled/automated ETL job | `auto_etl.py`, `auto_etl.ipynb`, `telecom_raw.csv` |
| `MoP-Ex05` | Churn prediction (scikit-learn pipeline: imputation, scaling, one-hot encoding) | `churn_model.ipynb`, `telecom_master.csv` |
| `MoP-Ex06` | ARPU prediction & feature engineering (tenure bands, usage ratios) | `Arpu Prediction.ipynb`, `telecom_master.csv` |
| `MoP-Ex07` | Per-cell monthly traffic forecasting with Prophet | `Monthly_Traffic_Forecasting.ipynb` |
| `MoP-Ex08` | Real-time KPI ingestion & windowed aggregation (SQLite) | `Live KPI Feed and Windowed Aggregation.ipynb`, `telecom_rt.db` |
| `Mop-Ex09` | Grafana dashboarding/alerting setup on live KPI data | `telecom_rt.sql` |
| `MoP-Ex10` | Sentiment analysis on synthetic customer feedback | `SentimentAnalysis.ipynb` |
| `MoP-Ex11` | Ticket routing classifier (TF-IDF + Logistic Regression) | `TicketRouting_Fixed.ipynb` |

### Capstone projects

- **`CapstonProject/`** — *Subscriber Segmentation and Anomaly Detection*: segments subscribers and flags anomalous/fraud-like usage patterns. Includes the write-up PDF, the analysis notebook, a slide deck, and a full presentation script.
- **`CapstonProject2/`** — *Telecom Data Analytics: From Raw Data to Business Recommendation* (also referred to as "TelecomIQ"): a broader capstone spanning subscriber, network KPI, billing, and support-ticket data, including churn prediction and retention strategy (Track A). Includes the project brief, a data dictionary, two notebook variants, a slide deck, and presentation scripts.

## Tech Stack

| Area | Tools |
|---|---|
| Languages | Python (Jupyter notebooks), SQL |
| Data handling | pandas, NumPy |
| Databases | MySQL (via `pymysql`), SQLite |
| Machine learning | scikit-learn (classification pipelines, `TfidfVectorizer`, `LogisticRegression`) |
| Forecasting | [Prophet](https://facebook.github.io/prophet/) (`cmdstanpy` backend) |
| Scheduling | [`schedule`](https://pypi.org/project/schedule/) (used in the automated ETL exercise) |
| Visualization / dashboarding | matplotlib (in-notebook), Grafana (external, configured against the SQL data in `Mop-Ex09`) |
| Deliverables | Jupyter notebooks, PDFs, PowerPoint decks, Markdown presentation scripts |

## Getting Started

### Prerequisites
- Python 3.9+ with Jupyter (`pip install jupyterlab` or use VS Code's notebook support)
- Core libraries used across exercises:
  ```bash
  pip install pandas numpy scikit-learn matplotlib pymysql schedule prophet
  ```
  (Individual notebooks may only need a subset of these — check the imports at the top of each one. `MoP-Ex07`'s notebook installs `prophet` itself at runtime if it isn't already present.)
- MySQL Server, only needed for `MoP-Ex01` and `MoP-Ex03` (SQL exercise and the ETL-into-MySQL exercise)
- [Grafana](https://grafana.com/), only needed if you want to reproduce the dashboard/alerting exercise in `Mop-Ex09`

### Running an exercise
1. `cd` into the relevant `MoP-ExNN` folder.
2. Open the accompanying PDF first — each one describes the exercise's goal and instructions.
3. Open the notebook (`jupyter lab` or `jupyter notebook`) and run the cells in order; each notebook reads from the CSV/DB file(s) sitting alongside it in the same folder.

### Running the capstone projects
Each capstone folder is similarly self-contained: start with the project brief/data dictionary PDF, then open the notebook. `CapstonProject2` includes two notebook variants (`TelecomIQ_Capstone.ipynb` and a `copy` version) — check both if one seems incomplete, as one may be a working draft of the other.

## Notes on the Data

All CSV and database files in this repository appear to be **synthetic/generated telecom data** (subscriber records, usage, network KPIs, billing, and support tickets) created for workshop purposes — not real customer data. If any of these files do turn out to contain real subscriber information, they should be removed or anonymized before this repository is made public.
