# William T. Ziemba & Donald B. Hausch: *Beat the Racetrack* (1984) / *Dr. Z's Beat the Racetrack* (1987)
## RC Synthesis Document for TAT1
**Compiled by RC — March 2026**
**Source Status:** Out of print but listed on Archive.org (access intermittent). Academic papers extensively document the methodology. This document synthesises the Dr. Z system from peer-reviewed literature, the book's own abstract descriptions, and academic commentary. The second edition (1987, retitled *Dr. Z's Beat the Racetrack*) is the definitive version, with a foreword by Ed Thorp (author of *Beat the Dealer* and *Beat the Market*).

---

## About Ziemba and Hausch

**William T. Ziemba** is a Professor of Financial Modelling and Stochastic Optimization at the University of British Columbia (and later the London School of Economics). He is one of the world's leading authorities on the application of mathematical finance to gambling markets. His work on racetrack betting is considered foundational in the academic literature on market efficiency.

**Donald B. Hausch** is a Professor of Business at the University of Wisconsin-Madison, specialising in game theory and decision analysis.

Together, they published the original *Beat the Racetrack* in 1984, following their landmark academic paper "Efficiency of the Market for Racetrack Betting" (1981, *Management Science*). The 1987 revised edition, *Dr. Z's Beat the Racetrack*, expanded the original with additional data, refined the system, and added the foreword by Ed Thorp.

> *"This is one of the only gambling systems that actually works."* — Ed Thorp (foreword to *Dr. Z's Beat the Racetrack*, 1987)

---

## The Central Discovery: Place and Show Pool Inefficiency

The Dr. Z system is built on a single, empirically verified observation: **the win pool at a racetrack is highly efficient, but the place and show pools are systematically inefficient**.

### Why the Win Pool is Efficient

The win pool is the most heavily bet pool at any racetrack. Millions of dollars flow into it from thousands of bettors, each with their own assessment of each horse's winning probability. The result, as Ziemba and Hausch demonstrated mathematically, is that **the win odds closely approximate the true probability of winning** for each horse. The favourite-longshot bias exists (longshots are slightly overbet, favourites slightly underbet), but the win pool is broadly efficient.

This means: **you cannot consistently profit from win betting based solely on tote board information**. To beat the win pool, you need superior handicapping — information that the market does not have.

### Why the Place and Show Pools are Inefficient

The place and show pools are smaller and less heavily bet. More importantly, **bettors in these pools do not adjust their bets rationally based on the win odds**. A bettor who likes Horse A to win will often also bet Horse A to place, without carefully calculating whether the place odds represent value.

The result is a systematic inefficiency: **horses that are heavily bet in the win pool are often underbet in the place and show pools relative to their true probability of finishing in the top two or three**. Conversely, horses that are lightly bet in the win pool are often overbet in the place and show pools by bettors seeking "safety."

This inefficiency is the foundation of the Dr. Z system.

---

## The Harville Formula: The Mathematical Engine

The Dr. Z system uses the **Harville formula** (developed by David Harville of the US Army Research Institute) to calculate the probability of each horse finishing in the top two (place) or top three (show) positions, given only the win probabilities derived from the win pool.

**The Harville Formula:**

If horse i has win probability p_i, then:

**Probability of horse i finishing 2nd (given horse j won):**
P(i 2nd | j 1st) = p_i / (1 - p_j)

**Probability of horse i finishing 2nd (unconditional):**
P(i 2nd) = Σ_j≠i [p_j × p_i / (1 - p_j)]

**Probability of horse i finishing in top 2 (place):**
P(i places) = p_i + P(i 2nd)

**Probability of horse i finishing in top 3 (show):**
P(i shows) = p_i + P(i 2nd) + P(i 3rd)

Where P(i 3rd) is calculated analogously.

This formula allows the analyst to derive theoretical place and show probabilities for every horse in the race, using only the information available on the tote board (the win odds).

---

## The Dr. Z System: Step-by-Step

### Step 1: Read the Win Odds from the Tote Board

Shortly before the race closes, read the win odds for every horse. Convert these to win probabilities:

Win Probability = (Amount bet on horse to win) / (Total win pool)

Or equivalently: Win Probability ≈ 1 / (Win Odds + 1), adjusted for the track take.

### Step 2: Calculate Place and Show Probabilities Using the Harville Formula

Using the win probabilities from Step 1, apply the Harville formula to calculate the theoretical probability of each horse finishing in the top 2 (place) or top 3 (show).

### Step 3: Calculate the Expected Return for Place and Show Bets

**For a place bet on horse i:**

Expected Return = [P(i places) × (Place Pool / Number of place bettors on i)] - 1

More precisely, using the pari-mutuel structure:

Expected Return (Place) = [P(i places) × (1 - track take) × Total Place Pool] / (Amount bet on i to place) - 1

**For a show bet on horse i:**

Expected Return (Show) = [P(i shows) × (1 - track take) × Total Show Pool] / (Amount bet on i to show) - 1

### Step 4: Identify Positive Expected Value Bets

A bet has positive expected value when the Expected Return > 0. In practice, Ziemba and Hausch found that only bets with an Expected Return of at least 10–15% were worth making, to account for estimation error and transaction costs.

**The key signal:** A horse that is heavily bet in the win pool (short win odds) but relatively lightly bet in the place or show pool. This creates a situation where the theoretical place/show probability (derived from the win odds) is higher than the actual place/show odds imply.

### Step 5: Size the Bet Using the Kelly Criterion

Once a positive expected value bet is identified, the Dr. Z system uses a modified Kelly criterion to determine the optimal bet size:

**Kelly Fraction = (Edge) / (Odds)**

Where:
- Edge = Expected Return (from Step 3)
- Odds = The net odds on the place or show bet

In practice, Ziemba and Hausch recommend betting a **fraction of the full Kelly amount** (typically 25–50%) to account for estimation error and to reduce variance.

**Critical constraint:** The bet itself changes the odds. In a pari-mutuel pool, every dollar you bet reduces the return for everyone else. The maximum profitable bet is the amount at which the marginal expected return from an additional dollar falls to zero. This maximum can be surprisingly small in thin pools.

---

## Empirical Results

Ziemba and Hausch tested the Dr. Z system on data from multiple US racetracks in the early 1980s. Their findings:

- The system identified positive expected value bets approximately **3–5% of the time** (i.e., most races offered no opportunity).
- When bets were made according to the system, the **average profit was approximately 10–15% on capital wagered**.
- The most common bet was a **show bet on a heavily-backed favourite** — the scenario where the favourite is so heavily bet in the win pool that the show pool underestimates its probability of finishing in the top three.

The academic review by R.J. Henery in the *Journal of the Royal Statistical Society* (1985) confirmed: *"The system is based on the fact that the odds quoted in horse races reflect very closely the horses' true chances of winning. In Tote pools for example the win odds are an excellent guide to the true winning chances."*

---

## Limitations and Subsequent Research

The Dr. Z system has been extensively tested and critiqued in the academic literature. Key findings:

**1. Pool size matters critically.** The system works best in large pools where the bettor's own bet does not significantly affect the odds. In small pools (common at Australian provincial meetings), the system's own bets can destroy the edge.

**2. The Harville formula has known biases.** Subsequent research (Lo, 1992; Stern, 1990) showed that the Harville formula tends to **overestimate the probability of longshots finishing in the top two or three** and **underestimate the probability of favourites**. Modified versions of the formula (the Stern model, the Lo model) produce more accurate estimates.

**3. The favourite-longshot bias affects the calculation.** Since win odds slightly overestimate longshot probabilities, the Harville formula compounds this error when calculating place and show probabilities for longshots.

**4. Modern pool efficiency has increased.** The 1984 data showed larger inefficiencies than modern data. As more sophisticated bettors have entered the market, the place and show pools have become more efficient, reducing the size and frequency of opportunities.

**5. The system does not work in Australian TAB pools without modification.** Australian racing uses a different pool structure (the TAB), and the "each-way" betting common in Australia (where place means top 2 or top 3 depending on field size) requires adjustment to the Harville formula.

---

## The Broader Contribution: A Framework for Thinking About Pools

Beyond the specific place-and-show system, *Beat the Racetrack* makes a contribution to handicapping philosophy that is more valuable than any specific formula:

**1. The win pool is your friend.** The win pool is the best available estimate of each horse's true winning probability. Rather than fighting the market, use it as your prior estimate and look for opportunities where other pools diverge from it.

**2. Market inefficiency is pool-specific.** A market can be efficient in one pool (win) and inefficient in another (place, show, exacta). The analyst's job is to find which pools are mispriced relative to the win pool.

**3. Positive expected value is the only criterion.** A bet is good if and only if it has positive expected value. Strike rate, "form," and gut feeling are irrelevant without this foundation.

**4. Kelly criterion for bet sizing.** The Kelly criterion (or a fractional version of it) is the mathematically optimal staking strategy for a bettor with a genuine edge. Overbetting (full Kelly or more) leads to ruin; underbetting leaves money on the table.

**5. The bettor's own impact on the market.** In pari-mutuel betting, every bet changes the odds. A successful bettor must account for this — their edge decreases as their bet size increases.

---

## The Kelly Criterion: TAT1's Staking Framework

The Kelly criterion, which Ziemba and Hausch apply to racetrack betting, is the same framework used by Ed Thorp in blackjack and by the most sophisticated quantitative investors. Its application to TAT1's betting decisions is direct:

**Full Kelly:** f* = (bp - q) / b

Where:
- f* = fraction of bankroll to bet
- b = net odds received (e.g., $4.00 = b of 3)
- p = probability of winning (your assessed probability)
- q = probability of losing (1 - p)

**Example:** TAT1 assesses a horse at 30% probability. The market offers $5.00 (b = 4).
- f* = (4 × 0.30 - 0.70) / 4 = (1.20 - 0.70) / 4 = 0.50 / 4 = 12.5% of bankroll

**Fractional Kelly (recommended):** In practice, Ziemba recommends betting 25–50% of the full Kelly amount to account for estimation error. At 25% Kelly, the above bet would be 3.125% of bankroll.

The critical insight: **overbetting is more dangerous than underbetting**. If you overestimate your edge by a factor of two, full Kelly betting will destroy your bankroll. Fractional Kelly provides a substantial margin of safety.

---

## TAT1 Integration Notes

**Direct applications to TAT1's handicapping framework:**

**1. Use the win market as your calibration benchmark.** Before assessing any race, note the market prices. These represent the collective wisdom of thousands of bettors and are a strong prior estimate of each horse's winning probability. TAT1's job is to identify where its own assessment diverges from the market — and to bet only when that divergence is both significant and justified.

**2. Look for place pool inefficiencies.** The Dr. Z system is most applicable in Australian racing when a heavily-backed favourite is available at relatively generous place odds. This occurs most often in small fields where the favourite is dominant but the place pool has not fully adjusted.

**3. Apply Kelly staking.** TAT1 should never bet a fixed amount regardless of edge. The bet size should be proportional to the assessed edge. A horse where TAT1 has high confidence in a significant market mispricing deserves a larger bet than one where the edge is marginal.

**4. The ROI data from the Rosehill Intelligence Brief is a Dr. Z application.** The Hyeronimus/Pride combination at +203% ROI is precisely the kind of market inefficiency that Ziemba and Hausch identified — a connection that the market systematically underestimates. The Dr. Z framework explains *why* this inefficiency persists: bettors anchor on the jockey's overall record, not their specific record with a given trainer at a given track. This is a behavioural bias that creates a repeatable edge.
