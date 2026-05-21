# Building Tier Curves

Two templates govern how buildings scale with tier. Both anchored to the Building Tier Unlock Rule: Master's starting rating IS the tier ceiling.

---

## Templates

### Compounding Template

Used by: Recruitment, Storehouse, Library, Training, Outer Court, Pavilion.

- Three surfaces unlock at T1, T4, T8
- Each surface holds multiple tracks with their own caps (cap-10 / cap-5 / cap-3 / cap-2)
- All specialists at the building amplify all unlocked surfaces collectively
- Each new tier adds levels to existing tracks AND unlocks new caps on those tracks
- Visual: building grows in scope, density, complexity with tier

### Flat-Cap-By-Tier Template

Used by: Teahouse, Soul Forge.

- A many-knob upgrade economy where each track caps individually
- Building tier determines the ceiling of each track
- Each upgrade track can have ONE specialist assigned; per-level output = `base × max(rating_assigned, 1)`
- Visual: building grows in capacity, equipment, refinement with tier

---

## Per-Building Tier Surfaces

| Building | Template | T1 Surface | T4 Surface | T8 Surface |
|---|---|---|---|---|
| Recruitment Hall | Compounding | Generic recruit tick rate | Amount per tick | Cost reduction / qi yield |
| Storehouse | Compounding | Idle resource cap | Run charges (skip/reroll/banish) | Chest size (5→6→7) |
| Teahouse | Flat-cap | 16 tracks (5 cap-10 / 6 cap-5 / 3 cap-3 / 2 cap-2) | Caps grow with tier | Caps grow with tier |
| Soul Forge | Flat-cap | Technique upgrades (+1 per tier max +10) | Passive upgrades unlock (+1 per tier max +10) | Path strengthening unlocks (Sapling→Worldroot) |
| Library | Compounding | Head's qi rate | Material drop rate (regions) | Generic qi rate (steep) |
| Training Hall | Compounding | Generic throughput | Named-disciple training | New generic starting stage |
| Outer Court | Compounding | Building upgrade cost reduction | Named disciple effectiveness | Pop cap multiplier |
| Ascension Pavilion | Compounding (+flat-cap T8) | Qi accumulation speed | Tier breakthrough speed | Cycling technique upgrades (flat-cap) |

---

## Building Tier Cost Table

| Tier | Essence | Material Tier | Quantity (any theme) | Spirit Stones |
|---|---|---|---|---|
| T1 | 0 (unlocked) | — | — | — |
| T2 | 500 | T1 | 50 | — |
| T3 | 1,500 | T1 | 100 | — |
| T4 | 4,000 | T2 | 150 | — |
| T5 | 10,000 | T2 | 200 | 20 |
| T6 | 25,000 | T3 | 250 | 60 |
| T7 | 60,000 | T3 | 300 | 150 |
| T8 | 150,000 | T4 | 350 | 350 |
| T9 | 350,000 | T4 | 400 | 800 |
| T10 | 800,000 | T5 | 500 | 1,800 |

Spirit stones kick in at T5+. Material tier increments every 2 building tiers (covers realm pair).

---

## Soul Forge — Three Upgrade Tracks

1. **Techniques** — individual run technique upgrades
2. **Passives** — individual passive upgrades
3. **Paths** — discovered path-tier strengthening (Sapling → Worldroot effects per theme)

Path upgrades work per-discovered-tier. Upgrading the Wood Path lifts ALL discovered Wood tiers proportionally.

Forge purchases fire Minor unlocks like all other building purchases — silent "new" indicator on the building screen, no popup.

---

## Library — Cycle Upgrades

The Library hosts cycle upgrades. A newly-learned cycle starts at ~30% of its cap; Library tier upgrades climb each unlocked cycle toward its full cap. The Library's other two jobs (head cultivation speed, path Codex) remain.

---

## Tier Counts Per Building

- **Most building specialties** (6-member arc, ratings 5→10): T1–T10
- **Heaven-Reader's short arc** (3–4 members): Pavilion likely T1–T9 to T1–T10 depending on arc length decision (open question)

Specialist count drives visual building growth independent of tier. Pao alone = tiny tea hut. 6 Brewers = full tea complex.
