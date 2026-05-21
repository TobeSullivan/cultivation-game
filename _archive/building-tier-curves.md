# Building Tier Curves

How each of the 10 buildings progresses through tiers. Locked in session 2026-05-11 ("Unlock web design next"). Missing from the master design doc (v3/v4/v5) — this file captures it so it's not lost again.

---

## Two Design Templates

The 10 buildings split into two structural templates, chosen by what kind of progression surface the building has.

### Compounding Template

- Three surfaces, unlocked at **T1 / T4 / T8**
- Each surface, once unlocked, compounds every subsequent tier
- "The building gets richer every tier"
- Applied where the building's surfaces are **features the building performs**

Applied to: Recruitment Hall, Storehouse, Library, Training Hall, Outer Court, Ascension Pavilion.

### Flat-Cap-by-Tier Template

- The building grants a **permanent ceiling on a many-knob upgrade economy**
- Each individual upgrade track has its OWN intrinsic cap
- Tier raises max purchasable rank across all tracks; each track stops at its cap
- Strategic depth = which tracks to pour resources into
- Applied where the building's surfaces are **individual upgrade tracks the player chooses from**

Applied to: Teahouse, Soul Forge. (Ascension Pavilion uses flat-cap pattern within its T8 surface.)

---

## All 10 Buildings — Tier Curve Summary

| # | Building | Template | T1 surface | T4 surface | T8 surface |
|---|---|---|---|---|---|
| 1 | Main Hall | None | Hub only — no tier curve | — | — |
| 2 | Personal Sanctum | None (meridian-driven) | 5th meridian @ R1 | 6th @ R3, 7th @ R6 | 8th @ R9 |
| 3 | Recruitment Hall | Compounding | Generic recruit tick rate | Amount per tick | Cost reduction / qi-yield per recruit |
| 4 | Storehouse | Compounding | Idle resource cap | Run charges (skip/reroll/banish) | Chest size (5→6→7) |
| 5 | **Teahouse** | **Flat-cap-by-tier** | 16 tracks open per cap table below | (same tracks, higher max ranks) | (same tracks, higher max ranks) |
| 6 | **Soul Forge** | **Flat-cap-by-tier** | Technique upgrades | Passive upgrades | Path upgrades |
| 7 | Library | Compounding | Head's qi rate (gentle) | Material drop rate from regions (medium) | Generic qi rate (steep: +100/200/300%) |
| 8 | Training Hall | Compounding | Generic throughput multiplier | Named disciple training | New generic starting stage |
| 9 | Outer Court / Farmlands | Compounding | Building upgrade cost reduction | Named disciple effectiveness multiplier | Pop cap multiplier (steep) |
| 10 | Ascension Pavilion | Compounding (+ flat-cap T8) | Qi accumulation speed | Tier breakthrough speed | Cycling technique upgrades (flat-cap within) |

Note on Training Hall: the **lead trainer sets Sect Cap**. That's a separate mechanic, not a tier surface.

Note on Recruitment Hall: in addition to the three tier surfaces, **one unique recruit per realm** surfaces at the Hall (~12 total Hall-uniques across the game).

---

## Teahouse — Full 16-Track Cap Table

Every track is purchasable when its first-available tier is reached. Subsequent Teahouse tiers raise the max rank purchasable on that track, up to its intrinsic cap.

| Track | Cap | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Atk | 10 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Crit dmg | 10 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Regen | 10 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Pickup radius | 10 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Paint radius | 10 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Defense | 5 | — | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| Crit chance | 5 | — | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| Max HP | 5 | — | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| Area | 5 | — | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| Projectile speed | 5 | — | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| Duration | 5 | — | 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 |
| Cooldown | 3 | — | — | — | 1 | 1 | 1 | 2 | 2 | 2 | 3 |
| Move speed | 3 | — | — | — | 1 | 1 | 1 | 2 | 2 | 2 | 3 |
| Luck | 3 | — | — | — | 1 | 1 | 1 | 2 | 2 | 2 | 3 |
| Amount (+projectile) | 2 | — | — | — | — | 1 | 1 | 1 | 1 | 1 | 2 |
| **Revival** | **2** | — | — | — | — | 1 | 1 | 1 | 1 | 1 | 2 |

**Design principle:** the more powerful the upgrade, the tighter the cap. Linear-gain stats cap at 10. Powerful stats cap at 5. Run-changing stats cap at 3. Build-defining stats cap at 2.

Each upgrade is cultivation-flavored as a tea recipe. Buff strength still scales with Sect Power on top of these flat upgrades.

**Revival** = retry mid-run mechanic. Player isn't "killed" in this game (they're "defeated"); revival is the in-run retry. Capped at 2; pencil-note from original session indicated playtest may push to 1.

---

## Soul Forge — Flat-Cap Specifics

- **Technique / passive upgrade cap:** +1 per Forge tier, max +10
- **Path upgrade cap:** +1 (T1-4), +2 (T5-8), +3 (T9-10) — path upgrades hit HARD, so the cap stays tight

Two scaling axes for tech/passive surfaces:
- **How many** distinct cards can have active upgrade tracks at once (more at higher tiers)
- **How high** each track can go (max upgrade level per card)

Example shape: T1 might allow 3 technique tracks each maxing at level 3. T5 might be 8 tracks at level 6. T10 might be 15 tracks at level 10. Compounding within the flat-cap structure.

---

## Why the Templates Split This Way

**Compounding** suits buildings where the surfaces are **features the building performs**. A Library that researches faster is a feature. A Recruitment Hall that recruits more per tick is a feature. The player doesn't choose between these — they all get better.

**Flat-cap** suits buildings where the surfaces are **upgrade tracks the player chooses among**. The Teahouse has 16 tracks; you can't pour into all of them with limited resources. The Forge has every technique and passive in your loadout as potential tracks. The strategic depth IS the choice of where to invest.

A compounding building would be problematic for Teahouse/Forge because flat power scaling on 16+ tracks would balloon quickly. A flat-cap structure on Library/Recruitment would feel flat — those buildings aren't supposed to be choice surfaces.

---

## Open / Unresolved Pencil-Notes from Original Session

1. **Named disciple BIS contribution math should scale exponentially with disciple stage.** Otherwise the training cycle doesn't pay off. Probably matching the trainer-throughput curve.

2. **Outer Court's "named disciple effectiveness multiplier" scope.** Does it affect BIS placement contribution only, or also training-throughput contribution and head-cycling support? Sub-question for when named contribution math is designed.

3. **Revival cap (currently 2)** may need playtest tuning down to 1.

4. **Pavilion specialty BIS** was TBD at the time of the original lock. Subsequently locked to Heaven-Reader.

5. **Building upgrades — instant or timed?** Original session locked "instant." Mentioned in case this is revisited.

---

## What This Doc Doesn't Cover (Defer to Future Sessions)

- Per-tier essence + material costs (the upgrade economy curve)
- How multiple specialists at a building interact with these tier curves (the open question this session is currently working through — slot model, contribution multipliers, etc.)
- Naming pass on individual upgrade tracks (current names are mechanic-descriptive placeholders)
- Per-cycle Pavilion T8 upgrade cap values
- Tooling for how the player visualizes "where can I invest right now" across compounding vs. flat-cap buildings

---

## Action Item for v6 Merge

This content needs to be referenced (or inlined) in the master design doc's Sect Management section. The v6 merge list should add an item:

> **Building Tier Curves** — locked in 2026-05-11 session, captured in `building-tier-curves.md`. Two templates (compounding + flat-cap-by-tier), all 10 building tier surfaces specified. Currently missing from v5 master doc.

---

*Source: locked in "Unlock web design next" conversation, 2026-05-11. Captured here 2026-05-20 after surfacing via past-conversation search.*
