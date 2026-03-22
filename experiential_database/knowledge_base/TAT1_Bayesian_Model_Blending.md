_# TAT1 Knowledge Base: Bayesian Model Blending

**Source:** RC Research Report, ISSUE-014 (2026-03-20)

---

## Core Principle

The most theoretically sound approach to blending a private model with a public market price is the **Bayesian framework**.

*   The **market price** is the **prior** (the collective wisdom).
*   The **private model** is the **likelihood function** (the proprietary edge).
*   The **blended probability** is the **posterior** (the updated estimate).

## Practical Implications

The weight given to the private model should be proportional to the quality and uniqueness of the information it contains. As the private model incorporates more proprietary data (pace maps, sectional data, trainer signatures), its weighting in the blend can increase.

## Weighting Schemes

| Scheme | Description | Best Used When |
| :--- | :--- | :--- |
| **Fixed Split (e.g., 70/30)** | A fixed percentage of the final probability comes from the private model (70%) and the market (30%). | A reasonable starting point for a new model. Simple to implement. Should be treated as a hypothesis to be tested. |
| **Dynamic Weighting** | The weight given to the private model varies based on a confidence measure (e.g., the model's historical accuracy in similar race types). | When the model has a track record and its accuracy can be measured across different race types, distances, and conditions. |
| **Kelly-Informed Blending** | The blend is calibrated so that the resulting edge, when staked using the Kelly Criterion, produces a historically positive expected value. | The most rigorous approach. Requires extensive backtesting data. |

## Common Pitfalls

1.  **Overfitting the blend:** Optimising the blend ratio on historical data can lead to a ratio that is perfectly calibrated for the past but performs poorly on new data. Use out-of-sample testing.
2.  **Ignoring market efficiency:** The market is efficient in aggregate. A private model that simply replicates publicly available information will not produce a positive edge, regardless of the blend ratio.
3.  **Static assumptions:** The optimal blend ratio is likely to change over time. The blend should be reviewed regularly.
