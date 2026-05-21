# Economy

The currency model, material model, and Sect Power multiplier — the resource math that drives every progression sink in the game.

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
