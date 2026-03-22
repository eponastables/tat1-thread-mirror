_# TAT1 Knowledge Base: Feature Engineering & Discovery

**Source:** RC Research Report, ISSUE-014 (2026-03-20)

---

## Core Principle

Automated feature discovery in Australian horse racing is an unsolved problem. This is a major source of potential competitive advantage. The goal is to move beyond manually engineered features and discover non-obvious, predictive relationships in the data.

## Promising Techniques

| Technique | Description | Key Advantage |
| :--- | :--- | :--- |
| **Random Forest Feature Importance** | Ranks all engineered features by their contribution to the model's predictive accuracy. | Simple to implement and interpret. A good starting point. |
| **SHAP (SHapley Additive exPlanations)** | Assigns each feature a "Shapley value" — a measure of its marginal contribution to the model's prediction for each individual race. | Excellent for discovering **interaction effects** — cases where two features together are more predictive than either one alone. This is the key to Dynamic Rule Discovery. |
| **Recursive Feature Elimination (RFE)** | Systematically identifies the minimum set of features needed to achieve a given level of predictive accuracy. | Useful for simplifying the model and reducing noise. |

## The Research Gap

No published research applying SHAP or automated feature discovery to Australian horse racing data exists. The work this team does in this area will be original and potentially publishable.

## Implications for the Build

*   **Data Architecture:** The database must be designed to support SHAP analysis. This means storing all engineered features in a clean, queryable format.
*   **Unstructured Data:** Qualitative notes (e.g., veto reasons, track bias observations) are the fuel for SHAP analysis. The vector index must be able to link these notes to specific races and horses.
