# Track A Mini Capstone — Churn Prediction & Retention Strategy

## Presentation Script

**Duration:** Approximately 6–8 minutes  
**Track:** Track A — Churn Prediction and Retention Strategy

---

## Slide 1 — Title
### Churn Prediction & Retention Strategy

**Script:**

Good morning everyone.

Our project is **Telecom Churn Prediction and Retention Strategy**, and we worked on **Track A** of the Telecom Data Analytics capstone.

The main idea of our project is simple: **we want to identify customers who are likely to leave the telecom company and decide which customers should be targeted with a retention offer.**

Our team worked on different parts of the project, including data preparation, machine learning, business analysis, operations, and presentation.

In this presentation, we will explain the problem, how we prepared and analysed the data, what we found, and finally what action we recommend.

**Transition:**

> So first, let's understand the actual business problem.

---

## Slide 2 — The Problem
### Customers leave before we act

**Script:**

The main problem is **customer churn**.

Churn simply means that a customer stops using the telecom service.

From a telecom company's point of view, losing customers means losing future revenue.

But the company cannot simply contact every customer and give them an offer. The retention team has limited time and budget.

So our three main questions were:

**First**, which customers are likely to leave?

**Second**, which of these customers are actually worth saving?

And **third**, what should we spend to try to keep them?

So our goal was not just to build a machine-learning model.

Our goal was to turn the model's output into a **practical retention strategy**.

In simple terms:

**Find the right customer → understand their risk → take the right action → reduce customer loss.**

**Transition:**

> To answer these questions, we first needed clean and reliable data.

---

## Slide 3 — Data & Preparation
### Making the data ready

**Script:**

We mainly worked with two Track A datasets.

The first was the **subscriber data**, which contained customer information and their six-month behaviour.

The second was the **monthly usage data**, which contained six months of usage and revenue information.

Initially, the data was not completely clean.

We found duplicate records, inconsistent region names, and missing values.

For example, different versions of region names had to be standardised into a smaller set of common region names.

Instead of simply deleting every problematic record, we cleaned and repaired the data wherever possible and kept useful information about missing values.

After cleaning and joining the data, we created one usable customer-level dataset.

So our overall pipeline was:

**Raw data → Clean data → Join the data → Create useful features → Build the model.**

This gave us a consistent dataset of around **3,200 unique subscribers**.

This step was very important because if the input data is wrong, the model and the business decision will also be wrong.

**Transition:**

> Once the data was ready, we moved to the most important part — building an honest churn model.

---

## Slide 4 — Model
### Using the honest model result

**Script:**

We trained a churn prediction model to estimate which customers were likely to leave.

But before trusting the model, we performed an important check called a **data leakage check**.

Data leakage means giving the model information that it would not actually have when making a real prediction.

We found that some columns, such as **retention offer sent** and **total charges**, could give the model information that was too closely related to the final outcome.

When this information was included, the model achieved a very high ROC-AUC of **0.946**.

But this result was misleading.

After removing the leakage, the honest model score was **0.729 ROC-AUC**.

This is a much more realistic result.

We also compared the model with a simple baseline. The baseline accuracy was already around **76 percent**, which shows why accuracy alone is not enough for this problem.

The important lesson here is:

**We should prefer an honest model that can work in the real world rather than a very high score caused by leaked information.**

**Transition:**

> After getting the churn risk, we then looked for groups of customers that could be targeted together.

---

## Slide 5 — Key Finding
### The high-risk complaint segment

**Script:**

This was one of the most important findings from our analysis.

We divided customers into different behaviour-based segments.

One segment clearly stood out.

This segment represents about **12.2 percent of the customer base**, but its churn rate is around **40 percent**.

In comparison, the overall churn rate is about **24.1 percent**.

So this group's churn rate is much higher than the average.

Another important point is that this segment is mainly identified by **customer complaints**, rather than simply being a high-spending group.

This gives the telecom company a clear target.

Instead of sending the same campaign to everyone, the company can focus on customers who show strong signs of dissatisfaction and high churn risk.

We also combined **churn risk with customer value**, such as ARPU, so that the retention team can focus first on customers where saving the customer is more valuable.

**Transition:**

> Now the question becomes: what should the company actually do with this group?

---

## Slide 6 — Costed Options
### Three possible actions

**Script:**

We compared three possible choices.

The first option is **do nothing**.

This gives us a baseline. It has no additional retention cost, but we also don't actively try to save these customers.

The second option is a **retention call**, costing about **₹300 per customer**.

In our project calculation, we used a **15 percent churn reduction as an assumption**.

The third option is a **bill credit plus a retention call**, costing about **₹550 per customer**.

Here we used a **25 percent churn reduction assumption**.

But there is an important point here.

These 15 and 25 percent numbers are **not actual measured campaign results**. They are assumptions provided in the project framework.

So we should not claim that the campaign will definitely reduce churn by those percentages.

Instead, the correct approach is to **test the retention campaign on a small group first** and measure the real result.

**Transition:**

> Based on the analysis, our recommendation can be summarised using the SIAV structure.

---

## Slide 7 — SIAV Recommendation
### Situation → Insight → Action → Value

**Script:**

Our recommendation follows the **SIAV structure**.

### Situation

The telecom company is losing subscribers and often finds out too late.

### Insight

We found a specific customer segment representing **12.2 percent of the base**, with a much higher churn rate of **40 percent**. Complaints are a major signal in this group.

### Action

We recommend routing these high-risk customers to a **proactive retention campaign before renewal**.

The customers should be prioritised using both their **churn risk and customer value**.

### Value

A retention call has a lower estimated cost of around **₹300 per customer** compared with the bill-credit option.

But because the campaign effect is still an assumption, we recommend starting with a **small pilot**, measuring the real results, and only then scaling the campaign.

So our main recommendation is:

> **Don't target everyone. Start with the high-risk complaint segment, test a low-cost retention call, measure the result, and scale if it works.**

---

## Slide 8 — Outputs, Limitation & Next Step

**Script:**

Finally, these are the main outputs of our project.

We produced a **clean customer dataset**, churn risk scores, a target customer segment, a risk-and-value based priority list, and a cost comparison for different retention actions.

We also created a clear business recommendation from the analysis.

However, we have one honest limitation.

**We did not have real campaign results.**

So the expected retention improvement is based on assumptions rather than an actual experiment.

Also, the model's default threshold does not give us a perfect balance between finding churners and the number of customers the retention team can actually contact.

Therefore, our next step would be to run a **controlled retention pilot**.

We would measure:

- How many customers were saved
- How much the campaign cost
- How much revenue was protected

Then we could improve the model threshold and decide whether the campaign should be expanded.

So, to conclude:

> **Our project moves from prediction to action — identify the customers most at risk, focus on the right segment, test a practical retention action, and use the real results to improve the strategy.**

Thank you.

---

# Suggested Timing

| Slide | Topic | Time |
|---|---|---:|
| 1 | Introduction | 40 sec |
| 2 | Problem | 55 sec |
| 3 | Data & Preparation | 55 sec |
| 4 | Model | 1 min |
| 5 | Key Finding | 1 min |
| 6 | Costed Options | 1 min |
| 7 | SIAV Recommendation | 1 min |
| 8 | Outputs & Conclusion | 1 min |
| **Total** | | **~7–8 min** |

---

## Presentation Flow

The main story to remember is:

**Problem → Data → Prediction → Finding → Cost → Recommendation → Business Action**

Do not spend too much time explaining Python, algorithms, or code. The presentation should be understandable to a campaign manager without seeing the code.

The focus should remain on:

**What is the problem? → What did we find? → What should the telecom company do? → Why is that action useful?**
