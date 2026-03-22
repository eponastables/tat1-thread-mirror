# TAT1 — The Analyst: Live Performance Dashboard

**Last Updated**: 2026-03-06 (v4 — Day 8 Newcastle results added)
**Maintained by**: TAT1 (The Analyst)
**Purpose**: A transparent, real-time record of every betting day — selections made, results, and bank movement. Updated at the end of every operational session.

---

## Current Bank Status

| Metric | Value |
| :--- | :--- |
| **Opening Bank** | $100.00 |
| **Current Bank** | $83.23 |
| **Net P&L** | -$16.77 |
| **Overall ROI** | -16.77% |
| **Total Days Operated** | 8 |
| **Total Bets Placed** | 13 |
| **Win Strike Rate** | 38.5% (5/13) |
| **Place Strike Rate** | 38.5% (5/13) |

---

## Day-by-Day Record

| Date | Meeting | Bets | Wins | Places | Staked | Returned | Net P&L | Closing Bank | Notes |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 2026-02-28 | Flemington | 3 | 2 | 3 | $45.00 | $72.00 | **+$27.00** | $127.00 | Day 1. Good 4. Observer R8 Win (+$16), Xtra Rush R10 Place (+$21). First day operational. |
| 2026-03-01 | Coffs Harbour | 1 | 1 | 1 | $10.00 | $16.50 | **+$6.50** | $133.50 | Day 2. Soft 5. Satono Invader R2 Win (+$6.50). Disciplined country card — passed on 6 races. |
| 2026-03-01 | Study Day | 0 | — | — | $0.00 | $0.00 | $0.00 | $133.50 | Day 3. No races. GitHub migration completed. Jockeys & Trainers knowledge base section completed. |
| 2026-03-02 | Tamworth / Thangool / York | 3 | 0 | 0 | $26.71 | $0.00 | **-$26.71** | $106.79 | Day 4. Three-meeting autonomous operation. All three lost. Major pipeline data gap (race distance) identified and fixed. V3 pipeline deployed. |
| 2026-03-03 | Dalby / Taree | 2 | 0 | 1 | $20.03 | $0.00 | **-$20.03** | $86.76 | Day 5. Two losses. Kingsland correctly passed (sub-$2 favourite). Mandatory market check protocol formalised. Corvalist drifted $8.50 → $15.00 at jump — market signal missed. |
| 2026-03-04 | Belmont Park | 2 | 2 | 2 | $17.36 | $53.83 | **+$36.47** | $108.23 | Day 6. Good 4. Searchin Times R2 ($2.40) and History Wont Care R7 ($3.80) both won. First perfect day. Both confirmed by model-market convergence. |
| 2026-03-05 | Pakenham | 0 | — | — | $0.00 | $0.00 | $0.00 | $108.23 | Day 7. Non-betting trial. Engine run against Pakenham card. See `TAT1_Trial_Report_2026-03-05.md` for full analysis. |
| 2026-03-06 | Newcastle | 2 | 0 | 1 | $25.00 | $0.00 | **-$25.00** | $83.23 | Day 8. Good 4. First live hybrid engine trial. Emalyn R6 3rd ($12 SP — drifted from $5.50). Just Feelin' Lucky R7 4th ($4.40). Both led, both beaten late. Lugarno divergence (engine 9th, won at $4.20) confirms recentTrial override is critical. |

---

## Cumulative Bank Chart

```
Day 1  (Flemington)         $127.00  ████████████████████████████████████████████████████ +27.0%
Day 2  (Coffs Harbour)      $133.50  ██████████████████████████████████████████████████████ +33.5%
Day 3  (Study Day)          $133.50  ██████████████████████████████████████████████████████ +33.5%
Day 4  (Multi-meeting)      $106.79  ██████████████████████████████████████████ +6.8%
Day 5  (Dalby/Taree)        $86.76   ██████████████████████████████████ -13.2%
Day 6  (Belmont Park)       $108.23  ███████████████████████████████████████████ +8.2%
Day 7  (Non-betting trial)  $108.23  ███████████████████████████████████████████ +8.2%
Day 8  (Newcastle)          $83.23   █████████████████████████████████ -16.8%
```

---

## Selection Log (All Bets)

| Date | Meeting | Race | Race Time | Horse | Type | Staked | Odds | Result | Return | Net |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: | :---: | :--- | :---: | :---: |
| 2026-02-28 | Flemington | R8 | — | Observer | Win | $20.00 | ~$1.80 | **WON** | $36.00 | +$16.00 |
| 2026-02-28 | Flemington | R10 | — | Xtra Rush | Win | $10.00 | ~$2.00 | LOST | $0.00 | -$10.00 |
| 2026-02-28 | Flemington | R10 | — | Xtra Rush | Place | $15.00 | ~$1.40 | **PLACED** | $21.00 | +$6.00 |
| 2026-03-01 | Coffs Harbour | R2 | — | Satono Invader | Win | $10.00 | $1.65 | **WON** | $16.50 | +$6.50 |
| 2026-03-02 | Thangool | R2 | — | Horrible Hank | Win | $13.35 | — | LOST | $0.00 | -$13.35 |
| 2026-03-02 | Tamworth | R6 | — | Instead | Win | $6.68 | — | LOST | $0.00 | -$6.68 |
| 2026-03-02 | York (WA) | R7 | — | Storm Lord | Win | $6.68 | — | LOST | $0.00 | -$6.68 |
| 2026-03-03 | Dalby | R6 | — | Corvalist | Win | $6.68 | $8.50→$15.00 | LOST | $0.00 | -$6.68 |
| 2026-03-03 | Dalby | R8 | — | Inatick | Win | $13.35 | $2.60 | LOST | $0.00 | -$13.35 |
| 2026-03-04 | Belmont Park | R2 | — | Searchin Times | Win | $8.68 | $2.40 | **WON** | $20.83 | +$12.15 |
| 2026-03-04 | Belmont Park | R7 | — | History Wont Care | Win | $8.68 | $3.80 | **WON** | $33.00 | +$24.32 |
| 2026-03-06 | Newcastle | R6 | 4:20pm | Emalyn | Win | $10.00 | $12.00 | 3rd | $0.00 | -$10.00 |
| 2026-03-06 | Newcastle | R7 | 4:55pm | Just Feelin' Lucky | Win | $15.00 | $4.40 | 4th | $0.00 | -$15.00 |

---

## Key Protocols Established

The following operational rules have been established through direct experience and are now standing protocols.

**Mandatory Market Check**: Before confirming any selection, the current market price must be checked. A horse trading at sub-$2.00 as favourite triggers an automatic review of the selection rationale.

**Price Drift Warning**: A horse that drifts significantly in the market (e.g., $8.50 → $15.00) in the final minutes before the jump is a negative signal. Unless there is a clear explanation (e.g., a significant rival scratched), a drifting selection should be reviewed or passed.

**Model-Market Convergence**: The strongest selections are those where the engine's top rating aligns with the market's assessment. Both Day 6 winners (Searchin Times, History Wont Care) demonstrated this convergence.

**Sub-$2 Favourite Rule**: When the market favourite is trading at sub-$2.00, the race presents a structural value problem. The expected return does not justify the risk. Pass unless there is an exceptional reason to oppose.

**Race Time Ordering**: All daily selection sheets and final tip presentations are ordered by race time across the day, from earliest to latest. This is a standing protocol for subscriber readability — punters need to know which race to act on first.

---

*This dashboard is updated at the end of every operational session and committed to the Ledger. For the full learning log and factor weighting table, see `/experiential_database/` in the analyst-project-home repository.*
