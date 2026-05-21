# Prototype Rewards — R1–R3

Per-objective rewards, partner-passive distribution, and per-map reward quantities for the 8-map prototype. Companion to [scope.md](scope.md) and [bosses.md](bosses.md).

---

## Per-Objective Rewards (R1–R3) — LOCKED

First-time completion only. Ambient drops continue on replay (essence-from-play, raw qi from kills, idle stream from conquered region).

**Uniform reward type per objective:**

| Objective | First-Time Reward |
|---|---|
| Survival | Essence bundle |
| Kills | Raw qi cache |
| Targets (elites) | Tier-appropriate materials, mixed-theme bundle |
| Territory | Region's themed material cache (single theme) |
| Resources | Designated partner passive (per forward-shift table below) |
| Boss | Signature technique + sect recruit + spirit stones + (realm-finals only) inspiration shard |

---

## Partner Passive Distribution — Forward-Shift Derangement (LOCKED)

Each map's Resources objective drops the NEXT map's boss partner. R3 M3 wraps to R1 M1. No map drops its own boss's partner.

| Map | Boss | Resources Objective Drops |
|---|---|---|
| R1 M1 Yun | (gets Blooming Garden from Boss) | **Steeped Form** (Pao's partner) |
| R1 M2 Pao | (gets Steeping Throw) | **Granite Footing** (Bao's) |
| R2 M1 Bao | (gets Mountain Stomp) | **Bound Records** (Mei's) |
| R2 M2 Mei | (gets Brass Ledger) | **Imperial Presence** (Hong's) |
| R2 M3 Hong | (gets Sovereign's Edict) | **Recited Sutra** (Wen's) |
| R3 M1 Wen | (gets Illuminated Verse) | **Foreseen Path** (Lin's) |
| R3 M2 Lin | (gets Augury Wheel) | **Tempered Body** (Tian's) |
| R3 M3 Tian | (gets Forge-Spirit Hammer) | **Verdant Vow** (Yun's) — wraps |

---

## Per-Map Reward Quantities — LOCKED

Formulas:
- Survival = `minutes × 20 × realm_mult` essence (R1=1×, R2=1.5×, R3=2×)
- Kills = `kills_target` raw qi (on top of per-fodder ambient ~1 qi)
- Targets = `elites_target × 7 × realm_mult` mixed-theme materials at realm tier
- Territory = `paint% / 2 × realm_mult` of region's themed material at realm tier
- Boss extras = ~5 stones map bosses, ~15 stones + inspiration shard realm-finals

| Map | Survival (Essence) | Kills (Qi) | Targets (Mixed Mats) | Territory (Themed Mat) | Boss (extras) |
|---|---|---|---|---|---|
| R1 M1 Yun | 200 essence | 200 qi | 20 T1 mixed | 30 Wood T1 (bamboo) | tech + 5 stones |
| R1 M2 Pao | 240 | 280 | 28 T1 mixed | 32 Water T1 (reagents) | tech + 15 stones + insp shard |
| R2 M1 Bao | 390 | 350 | 52 T1 mixed | 50 Earth T1 (iron ore) | tech + 5 stones |
| R2 M2 Mei | 420 | 380 | 52 T1 mixed | 52 Metal T1 (scrolls) | tech + 5 stones |
| R2 M3 Hong | 450 | 420 | 63 T1 mixed | 52 Fire T1 (writs) | tech + 15 stones + insp shard |
| R3 M1 Wen | 640 | 450 | 84 T2 mixed | 70 Lightning T2 (manuscripts) | tech + 5 stones |
| R3 M2 Lin | 640 | 460 | 84 T2 mixed | 72 Wind T2 (feathers) | tech + 5 stones |
| R3 M3 Tian | 720 | 500 | 98 T2 mixed | 75 Ice T2 (ingots) | tech + 15 stones + insp shard |

**Mixed-theme bundles** split equally across the 8 elementals (Wood/Earth/Fire/Water/Metal/Wind/Ice/Lightning). E.g., 20 T1 mixed ≈ 2.5 of each elemental T1 theme.

**Full R1–R3 banked haul:** ~3,700 essence + ~3,140 raw qi + ~215 T1 mixed + ~266 T2 mixed materials + region-themed caches + ~85 spirit stones + 3 inspiration shards + 16 cards (8 techniques + 8 partner passives) + 8 named disciple recruits + all 8 buildings unlocked at T1.
