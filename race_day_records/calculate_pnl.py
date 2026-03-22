"""
TAT1 Post-Race P&L Calculator — 14 March 2026
All results sourced from Racenet, Racing Post, Sky Racing World, Racing and Sports.
"""

OPENING_BANK = 66.73

# ============================================================
# SELECTIONS AND RESULTS
# ============================================================
# Format: {meeting, race, horse, stake, result, sp, placed, notes}

SELECTIONS = [
    # ---- ROSEHILL (COMMITTED TO BANK) ----
    {
        "meeting": "Rosehill",
        "race": 3,
        "race_name": "Tresemmé Magic Night Stakes (Gr3)",
        "horse": "Lumbini",
        "stake": 2.00,
        "result": "2nd",  # 2nd of 8 (Pembrey won, Lumbini 2nd 1.37L, By Choice 3rd)
        "sp": None,  # SP not yet confirmed — est $8-$10
        "won": False,
        "notes": "Engine #1. Ran 2nd. Beaten by Pembrey (T.J.Gollan/J.B.McDonald). By Choice (Clark/WB) ran 3rd — negative signal horse placed."
    },
    {
        "meeting": "Rosehill",
        "race": 6,
        "race_name": "Racing NSW Country Mile Series Final (BM80)",
        "horse": "King's Secret",
        "stake": 2.00,
        "result": "3rd",  # Flying For Fun won, Mal Coupe 2nd, King's Secret 3rd
        "sp": None,  # est $10-$12
        "won": False,
        "notes": "Joseph Pride stable signal. Ran 3rd. Flying For Fun (Bryce Heys stable) won. Positive result — Pride stable placed."
    },
    {
        "meeting": "Rosehill",
        "race": 8,
        "race_name": "Coolmore Classic (Gr1)",
        "horse": "Cinsault",
        "stake": 2.00,
        "result": "Lost",  # Lazzura won (Waller/McDonald $5), Arctic Glamour 2nd, Vivy Air 3rd
        "sp": None,  # est $10-$12
        "won": False,
        "notes": "Strongest engine signal. Lazzura (Waller/McDonald) won at $5. Cinsault unplaced. Freedman stable beaten by Waller."
    },

    # ---- CAULFIELD (COMMITTED TO BANK) ----
    {
        "meeting": "Caulfield",
        "race": 6,
        "race_name": "Barastoc Country Mile Series Final (BM80)",
        "horse": "Sakakibara",
        "stake": 2.00,
        "result": "13th",  # Sir Atlas won, Nic's Choice 2nd, Torn 3rd. Sakakibara 13th.
        "sp": None,
        "won": False,
        "notes": "Engine #1 ran last. Sir Atlas (B2, L Smith) won. Complete engine failure — Sakakibara clearly not suited."
    },
    {
        "meeting": "Caulfield",
        "race": 9,
        "race_name": "IRT VOBIS Platinum Guineas",
        "horse": "Salty Pearl",
        "stake": 2.00,
        "result": "1st",  # Salty Pearl won at $2.00 (Maher/Allen)
        "sp": 2.00,
        "won": True,
        "notes": "Engine #1 won at $2.00 SP. Confirmed winner. Maher/Allen combination. Strong favourite."
    },
    {
        "meeting": "Caulfield",
        "race": 10,
        "race_name": "Yulong VOBIS Gold Sprint",
        "horse": "Ndola",
        "stake": 2.00,
        "result": "3rd",  # Jigsaw won ($2.60), She's Bulletproof 2nd, Ndola 3rd 4.25L
        "sp": None,  # est $2.80 SP
        "won": False,
        "notes": "Engine #1 ran 3rd. Jigsaw (B7, Alderson/Bates) won. Ndola beaten 4.25L. Engine rated Ndola #1 but Jigsaw was B7 — wide draw winner."
    },

    # ---- MORPHETTVILLE PARKS (COMMITTED TO BANK) ----
    {
        "meeting": "Morphettville Parks",
        "race": 2,
        "race_name": "M&J Chickens (BM72)",
        "horse": "Sir Myka",
        "stake": 2.00,
        "result": "5th",  # Oak Park Maddison won, Kalmana 2nd, Light The Night 3rd, Sir Myka 5th
        "sp": None,
        "won": False,
        "notes": "Engine #1 ran 5th. Oak Park Maddison (B6, Travis Doudle) won — a rank outsider. Engine failed completely."
    },
    {
        "meeting": "Morphettville Parks",
        "race": 4,
        "race_name": "Adelaide Galvanising Industries Hcp (C2)",
        "horse": "You'resogolden",
        "stake": 2.00,
        "result": "6th",  # Autumn Frost won, Synthesise 2nd, Tripod Terror 3rd
        "sp": None,
        "won": False,
        "notes": "Engine #1 ran 6th. Autumn Frost (B5, R&C Jolly) won. Engine failure."
    },
    {
        "meeting": "Morphettville Parks",
        "race": 7,
        "race_name": "Craig Fitzy's 60 Fireball Classic (BM68)",
        "horse": "No Rumours",
        "stake": 2.00,
        "result": "Lost",  # Burning Bright won (B4, Gluyas), Theodor 2nd, Tyusix 3rd
        "sp": None,
        "won": False,
        "notes": "Engine #1 lost. Burning Bright (B4, Gluyas) won. No Rumours was also B4 — same barrier. Engine failure."
    },
]

# ============================================================
# PAPER SELECTIONS (not committed to bank — for learning only)
# ============================================================
PAPER_SELECTIONS = [
    # Rosehill
    {"meeting": "Rosehill", "race": 5, "horse": "Soul Of Spain", "result": "2nd", "notes": "Vauban won (Clark/WB — negative signal horse WON). Soul Of Spain ran 2nd at $3.80. Our fade of Vauban was WRONG."},
    {"meeting": "Rosehill", "race": 7, "horse": "Soverato", "result": "Lost", "notes": "Sixties won (Gollan/McDonald). Soverato unplaced."},
    {"meeting": "Rosehill", "race": 9, "horse": "Cristal Clear", "result": "1st", "notes": "CRISTAL CLEAR WON. Archibald trainer signal (+148% ROI) was correct. Contrarian play vindicated."},
    # Caulfield
    {"meeting": "Caulfield", "race": 2, "horse": "Soft Love", "result": "3rd", "notes": "Gentle Steel won. Soft Love ran 3rd."},
    {"meeting": "Caulfield", "race": 7, "horse": "Lagunanini", "result": "Lost", "notes": "Big Wigs won. Lagunanini scratched."},
    {"meeting": "Caulfield", "race": 8, "horse": "Chief Little Rock", "result": "Lost", "notes": "Birdman won (Waller/Melham $3.30). Chief Little Rock scratched."},
    # Morphettville Parks
    {"meeting": "Morphettville Parks", "race": 1, "horse": "Tikkamos", "result": "3rd", "notes": "Never Ordinary won. Tikkamos ran 3rd."},
    {"meeting": "Morphettville Parks", "race": 3, "horse": "She Rex", "result": "6th", "notes": "Sicilian Princess won. She Rex 6th."},
    {"meeting": "Morphettville Parks", "race": 10, "horse": "Grinzinger Ace", "result": "Lost", "notes": "One More Song / Cuban Waters area — need to check."},
]

# ============================================================
# P&L CALCULATION
# ============================================================
def calculate_pnl():
    total_staked = sum(s['stake'] for s in SELECTIONS)
    total_returns = 0.0
    winners = []
    losers = []

    for s in SELECTIONS:
        if s['won']:
            # Return = stake * SP
            ret = s['stake'] * s['sp']
            total_returns += ret
            winners.append(s)
        else:
            losers.append(s)

    net_pnl = total_returns - total_staked
    closing_bank = OPENING_BANK + net_pnl

    print("=" * 60)
    print("TAT1 POST-RACE P&L — 14 MARCH 2026")
    print("=" * 60)
    print(f"\nOpening Bank:    ${OPENING_BANK:.2f}")
    print(f"Total Staked:    ${total_staked:.2f}")
    print(f"Total Returns:   ${total_returns:.2f}")
    print(f"Net P&L:         ${net_pnl:+.2f}")
    print(f"Closing Bank:    ${closing_bank:.2f}")
    print(f"\nWinners: {len(winners)}/{len(SELECTIONS)}")
    print(f"Strike Rate: {len(winners)/len(SELECTIONS)*100:.1f}%")

    print("\n--- WINNERS ---")
    for s in winners:
        ret = s['stake'] * s['sp']
        print(f"  ✓ {s['meeting']} R{s['race']} {s['horse']} @ ${s['sp']:.2f} — Stake ${s['stake']:.2f} → Return ${ret:.2f} (Profit ${ret - s['stake']:.2f})")

    print("\n--- LOSERS ---")
    for s in losers:
        print(f"  ✗ {s['meeting']} R{s['race']} {s['horse']} — {s['result']} — Stake ${s['stake']:.2f} lost")

    print("\n--- PAPER SELECTIONS ---")
    for p in PAPER_SELECTIONS:
        print(f"  {'★' if 'WON' in p['notes'] or '1st' in p['result'] else '·'} {p['meeting']} R{p['race']} {p['horse']} — {p['result']}")
        print(f"    {p['notes']}")

    return {
        'opening_bank': OPENING_BANK,
        'total_staked': total_staked,
        'total_returns': total_returns,
        'net_pnl': net_pnl,
        'closing_bank': closing_bank,
        'winners': len(winners),
        'total_bets': len(SELECTIONS),
    }

if __name__ == "__main__":
    results = calculate_pnl()
