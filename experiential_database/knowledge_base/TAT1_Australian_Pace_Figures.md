# TAT1 Knowledge Base: Australian Pace Figures

**Source**: RC Research Report, ISSUE-016 (2026-03-22), referencing the Wholistic Quality Ratings (WQR) framework.

---

## 1. Core Principle

The goal is to create a single, normalised number that represents a horse's performance, adjusted for all relevant variables. This is the Australian equivalent of the Beyer or Timeform speed figures.

## 2. The Australian Pace Figure Formula (Conceptual)

**Final Pace Figure = (Raw Time + Track Speed Adj. + Weight Adj. + Margin Adj.) -> Normalised Scale**

## 3. Step 1: Calculate the Track Speed Adjustment (Australian Track Variant)

This is the most critical step. It quantifies how fast or slow the track was on a given day compared to its historical average.

**Methodology:**

1.  For each race on the card, calculate the winner's speed in metres per second (`mps = distance / time`).
2.  Compare this to the historical **par speed** for that track, distance, and going.
3.  The average percentage deviation across all races on the card is the **Track Speed Adjustment**.

## 4. Step 2: Adjust for Weight and Beaten Margin

*   **Weight:** The standard adjustment is approximately **0.1 seconds per 1kg** of weight carried above or below a par weight (e.g., 55kg).
*   **Beaten Margin:** The value of a length varies by distance. The common approximation is **0.17 seconds per length**.

## 5. Step 3: Convert to a Normalised Figure

Once an adjusted time is calculated, it can be converted to a final figure on a normalised scale (e.g., 100 = par).

**Formula: Speed Figure**

```
Speed Figure = (par_time_for_distance / adjusted_time) * 100
```

## 6. Early (E1, E2) and Late (LP) Pace Figures

These are calculated using the same methodology, but applied to sectional times instead of the final time. This allows for the profiling of a horse's pace distribution (e.g., fast early, slow late).
