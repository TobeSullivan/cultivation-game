# Economy

The currency model, material model, ambient drop rates, and Sect Power multiplier — the resource math that drives every progression sink in the game.

---

## Currency Model — 4 Currencies + Materials

| Currency | Tier | Earned from | Spent on |
|---|---|---|---|
| **Qi** | Personal pool | Enemy kills, idle, cycling multiplier | Tier breakthroughs only |
| **Essence** | Common currency | VS-style run drops + idle from regions | Most upgrades (buildings, forge, leaves, meridians, cycle climb base) |
| **Spirit Stones** | Higher currency (gold→platinum, NOT premium MTX) | Boss defeats, rare idle, special-event arrivals | High-impact sinks: generic recruitment, cycle climb stones component, top-tier building upgrades (T7+), high-meridian refinement, reroll/reset operations |
| **Inspiration** | Gating resource | Realm-final bosses (first-time) | Stage 4+ breakthroughs only |

---

## Qi vs Essence — The Conceptual Split

- **Qi** = personal cultivation energy. INTERNAL to the head. The cultivator getting stronger.
- **Essence** = condensed value extracted from the world. EXTERNAL infrastructure. The sect's operation growing.
- Both must flow for progression. Lots of essence + low qi = stuck at current stage. High qi + no essence = no upgrades.

**Spirit Stones rough tuning intuition:** 1 stone ≈ 1,000 essence value. Not interchangeable; just for tuning sense.

---

## Cuts From Earlier Doc Versions

- **Monster Cores** — removed; kills drop raw qi directly
- "Spirit Stones as universal currency" — replaced; essence is the universal, stones are tier-up
- Cycling boosters / time crystals — these ARE spirit stones; same mechanic, new name

---

## Sect Power Multiplier

Sub-linear, anchored to AdCap/Cookie Clicker/NGU Idle case studies:

```
multiplier = 1 + sqrt(Sect_Power / 100)
```

Late-game still huge but not absurd. Permanent multipliers from any future NG+ would layer on top.

### Per-Realm SP Envelope (Locked 2026-05-22)

Cumulative SP at each realm conquered. Roughly geometric growth (~3×/realm) tamed by the sqrt in the formula. Conquest contribution sums with other SP sources (building levels + Master ratings, named disciple BIS placements, macro progression — see [pillars/sect-management.md](../pillars/sect-management.md) Sect Power).

| Realm conquered | Cumulative SP from conquest | SP multiplier |
|---|---|---|
| Game start | 0 | ×1.00 |
| R1 conquered | 25 | ×1.50 |
| R2 conquered | 75 | ×1.87 |
| R3 conquered | 200 | ×2.41 |
| R4 conquered | 450 | ×3.12 |
| R6 conquered | 1,500 | ×4.87 |
| R9 conquered | 5,000 | ×8.07 |
| R12 conquered | 10,000 | ×11.00 |

**Anchors:**
- **R1 = ×1.50.** First realm conquered = noticeable bump but not a wall against R2 enemies. Soft warning territory honored.
- **R12 = ×11.** Endgame target — meaningful but not the dominant multiplier at full stack (path bundle does heavier lifting per [systems/path-system.md](path-system.md) Path Bundle Math Envelope).

**Within-realm interpolation:** Cumulative SP grows roughly linearly across regions within a realm. Mid-realm checkpoint estimates use linear interpolation between adjacent realm anchors.

**Per-region distribution within realms** (R1 has 2 regions, R12 has 20) and whether per-region contribution scales with realm tier or stays roughly flat with region count doing the scaling — flagged for [risk-map.md](../pillars/risk-map.md) cross-check pass. Envelope numbers above are cumulative; per-region distribution can shift without affecting checkpoint math.

### NG+ Architecture (Deferred)

The sqrt formula extends naturally past R12 — no cap, scales sub-linearly forever. NG+ design is forward-compatible with three patterns:

| Pattern | Source game | How it stacks with SP |
|---|---|---|
| Separate multiplier (Angels model) | AdCap angel investors | Adds new stack component; SP stays as-is |
| Extended SP (Realm Grinder mythics) | Realm Grinder | NG+ unlocks R13+, SP keeps accumulating |
| Reset with carry (Prestige model) | Cookie Clicker, NGU Idle | Resets SP; permanent Karmic multiplier outside SP |

Decision deferred to a dedicated NG+ design session. The R12 = ×11 anchor stays meaningful as the "first lifetime" endgame target regardless of which pattern is chosen — NG+ multiplies it.

---

## Material Model

- All materials themed; no generic/universal category
- 12 themes × 6 material tiers = **72 materials total**
- Material tier ≠ realm. Realm pairs share tier:

| Material Tier | Realms |
|---|---|
| T1 | R1, R2 |
| T2 | R3, R4 |
| T3 | R5, R6 |
| T4 | R7, R8 |
| T5 | R9, R10 |
| T6 | R11, R12 |

- Building upgrades + meridian refinement accept any theme at the required tier
- Forge theme-card upgrades require matching theme
- All 12 themes have materials at every tier (Lightning T1 exists even though Lightning isn't an R1–R2 boss theme)

8 of the 72 materials are named in the prototype (bamboo shoots, alchemy reagents, iron ore, sealed scrolls, sealed writs, ancient manuscripts, tribulation feathers, frost-iron ingots — see [prototype/bosses.md](../prototype/bosses.md)). Remaining 64 deferred to the naming pass.

---

## Currency Ambient Drops

Per-kill drops during runs. First-time objective rewards live in [prototype/rewards.md](../prototype/rewards.md); this section covers what every kill drops on top of (or instead of, on replay) those.

### Per-Kill Drop Table (R1 M1 minute 0, replay mode)

| Category | XP gem | Raw qi | Essence | Spirit stones | Materials |
|---|---|---|---|---|---|
| Fodder | 1 | 1 | — | 0.1% chance (1 stone) | — |
| Elite | 5 | 5 | 3 | — | 1 region-themed |
| Mini-boss | 20 | 20 | 15 | 1 | 3 region-themed |
| Boss (first-time named) | 100 | 100 | 100 | 5 | signature + recruit (per rewards.md) |
| Boss (replay generic) | 100 | 100 | 50 | 3 | 5 region-themed |

**Pickup collapse:** XP gem and raw qi grant from the same pickup orb. One orb per kill, walking over it grants both. Reduces visual clutter. 30-sec persistence (matches XP gem rule in [pillars/run-loop.md](../pillars/run-loop.md)).

**Essence is VS-gold-style:** doesn't drop from fodder. Common from elites onward. Genre-correct (VS gold comes from chests + boss aliens, not every enemy).

**Materials are 100% region-themed for ambient drops.** Off-theme variety stays exclusive to the Targets first-time reward (mixed materials). Keeps routing strategy clean — player picks region for its theme, ambient drops reinforce that choice.

**First-time stacking:** Ambient drops stack with first-time objective rewards. The boss's 100 qi + 100 essence ambient drops happen on top of the [rewards.md](../prototype/rewards.md) first-time bundle.

### Per-Realm Ambient Scaling

R1 = 1×, R2 = 1.5×, R3 = 2×, R4+ = 2.4× per realm (matching idle output scaling in [pillars/risk-map.md](../pillars/risk-map.md) and enemy HP/damage scaling in [prototype/scope.md](../prototype/scope.md)). Applies to all four resource streams (qi / essence / stones / materials).

### Within-Run Ambient Scaling

**None.** Drop values fixed per kill regardless of minute. Only HP scales within run (`1.10^minute`, fodder/elite/mini-boss only — boss exempt).

Means later minutes are harder per-kill but yield the same. Reward density increases through spawn-rate ramping, not per-kill inflation. Preserves early-game-feels-rewarding pacing.

*Locked pending playtest confirmation.* Alternative (drops scale with minute) considered but rejected for diluting the early-game feel; revisit after first tuning pass if minute-25 feels low-yield.

### Spirit Stone Drop Specifics

- Fodder: 0.1% chance × 1 stone. ~1–3 stones per 25-min R1 run from fodder.
- Elite: no stones (clean — boss is the primary stone source).
- Mini-boss: 1 stone guaranteed.
- Boss: 5 stones first-time named, 3 stones replay generic.
- Realm-final boss: 15 stones first-time named (per [data/schema.md](../data/schema.md) SpiritStone source list).

### Cycling Multiplier Formula

Cycling techniques layer additive bonuses to qi gathering rate. With cycle climb percentages summed across all learned cycles:

```
qi_gain_rate = base × (1 + Σ cycle_climb_%)
```

8 cycles all maxed at average 25% cap each ≈ 3× qi gain. Endgame buff; per-cycle cap values tunable at playtest. Per-cycle Pavilion T8 climb economy lives in [building-tier-curves.md](building-tier-curves.md).

---

## Idle Composition Rule

Region idle output, building amplification, generator buildings, and the Sect Power multiplier compose as follows:

```
inbox_per_hour_R = ((region_R_base × Π(amplifier_multipliers)) + Σ(generator_outputs_R)) × (1 + sqrt(SP/100))
```

Where:
- `region_R_base` = locked region idle output for resource R ([risk-map.md](../pillars/risk-map.md) baseline × 2.4^(realm−1) for realm scaling)
- `amplifier_multipliers` = stacking multiplicative buffs (Library T1/T4/T8, Outer Court T4, Pavilion T1)
- `generator_outputs_R` = additive contributions from buildings that produce their own streams (Recruitment Hall T1 generic recruits, Library T8 sect qi from disciples)
- Sect Power multiplier applies to the total

Two compositional patterns:
- **Amplifier buildings** multiply region idle streams.
- **Generator buildings** add new streams to inbox.

Per-building base values and amplifier/generator classification live in [systems/building-tier-curves.md](building-tier-curves.md) under Per-Building Base Rates.
