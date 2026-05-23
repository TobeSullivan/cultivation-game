# Building Tier Curves

Two templates govern how buildings scale with tier. Both anchored to the Building Tier Unlock Rule: Master's starting rating IS the tier ceiling.

---

## Templates

### Compounding Template

Used by: Recruitment, Storehouse, Library, Training, Outer Court, Pavilion.

- Three surfaces unlock at T1, T4, T8
- Each surface holds multiple tracks with their own caps (cap-10 / cap-5 / cap-3 / cap-2)
- All specialists at the building amplify all unlocked surfaces collectively: `compound rate = base × (1 + Σ(specialist ratings) × 0.10)` (per [pillars/sect-management.md](../pillars/sect-management.md))
- Each new tier adds levels to existing tracks AND unlocks new caps on those tracks
- Visual: building grows in scope, density, complexity with tier

**Compounding exception — Storehouse draft charges.** The Storehouse T4 draft-charge tracks (reroll / skip / banish) are leaf-driven only and do NOT scale with apprentice ratings. Apprentice compounding on Storehouse feeds the offline-cap surface (T1) instead. Charges are discrete integers per run; mixing in the apprentice multiplier would inflate them unmanageably. Locked tranche 3.

### Flat-Cap-By-Tier Template

Used by: Teahouse, Soul Forge.

- A many-knob upgrade economy where each track caps individually
- Building tier determines the ceiling of each track
- Each upgrade track can have ONE specialist assigned; per-level output = `base × max(rating_assigned, 1)`
- Track upgrades are **instant on purchase**. Specialist assignment is **instant**. Effects are **persistent passive modifiers** — once unlocked and leveled, always on. No timers, no expiration, no brew time.
- Visual: building grows in capacity, equipment, refinement with tier

---

## Per-Building Tier Surfaces

| Building | Template | T1 Surface | T4 Surface | T8 Surface |
|---|---|---|---|---|
| Recruitment Hall | Compounding | Generic recruit tick rate | Amount per tick | Cost reduction |
| Storehouse | Compounding | Idle resource cap | Run charges (skip/reroll/banish) — 3/3/3 to 13/13/13 | Chest size (5→6→7) |
| Teahouse | Flat-cap | 16 tracks (5 cap-10 / 6 cap-5 / 3 cap-3 / 2 cap-2) | Caps grow with tier | Caps grow with tier |
| Soul Forge | Flat-cap | Technique upgrades (one track per discovered card-family) | Passive upgrades (one track per discovered passive) | Path strengthening (one track per discovered path tier) |
| Library | Compounding | Head's cultivation speed | Region material drop rate | Generic disciple qi rate (sect-wide) |
| Training Hall | Compounding | Generic throughput | Named-disciple training | New generic starting stage |
| Outer Court | Compounding | Building upgrade cost reduction | Named disciple effectiveness | Pop cap multiplier |
| Ascension Pavilion | Compounding (+flat-cap T8) | Qi accumulation speed | Tier breakthrough speed | Cycling technique upgrades (flat-cap) |

Library's three surfaces match its three functions in [pillars/sect-management.md](../pillars/sect-management.md). The Path Codex lives at Library as a UI feature, not as a tier-scaling surface — it's the same UI at T1 and T10.

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

## Per-Building Base Rates

Unlock values at each tier — what the building does at T1/T4/T8 with no leaves purchased, R1-era baseline. Leaves climb above these base values up to each track's cap. Composition with region idle and Sect Power multiplier defined in [economy.md](economy.md) Idle Composition Rule.

### Per-Building Unlock Values

| Building | T1 unlock | T4 unlock | T8 unlock |
|---|---|---|---|
| Library | +10% head qi accumulation rate | +10% region material drop rate | Each generic disciple +0.5 qi/hr to sect pool |
| Recruitment Hall | 1 generic recruit per 4 hours | 1 recruit per tick (leaves climb to 3) | −10% recruitment cost (leaves climb to −40%) |
| Teahouse | 0% base; 16 tracks activate via paid leaves | Caps grow with tier | Caps grow with tier |
| Soul Forge | 0% base; technique tracks activate via paid leaves | Passive tracks activate | Path tracks activate |
| Training Hall | +5% disciple training speed sect-wide | Named-disciple training unlocked | Generics start +1 stage above current sect average |
| Outer Court | −5% building tier costs | +5% disciple effectiveness sect-wide | Pop cap +5 generic slots |
| Storehouse | Offline idle cap 12h → 24h | 3 reroll + 3 skip + 3 banish charges per run (climbs to 13/13/13) | Chest size 5 cards (climbs to 7 at L10) |
| Ascension Pavilion | +5% head qi accumulation (stacks with Library) | +10% tier breakthrough speed | Cycle climb track unlocks per learned cycle |

### Amplifier vs Generator Classification

Per the composition rule in [economy.md](economy.md):

- **Amplifiers** multiply region idle streams: Library T1/T4/T8, Outer Court T4, Pavilion T1.
- **Generators** add new streams to inbox: Recruitment Hall T1 (generic recruits), Library T8 (sect qi contribution from generic disciples).
- **Run-only surfaces** apply during runs only, not idle: Storehouse T4 charges, all 16 Teahouse buff tracks, Pavilion T4 breakthrough speed (applies at breakthrough time), Soul Forge upgrades (permanent multipliers applied at run start).
- **Cap-extenders** modify caps not flows: Storehouse T1 (offline idle cap), Outer Court T8 (pop cap).
- **Cost-reducers** modify upgrade costs: Outer Court T1, Recruitment Hall T8.

### Storehouse Offline Idle Cap Progression

| Storehouse state | Offline cap |
|---|---|
| Not built | 12 hours |
| T1 unlock | 24 hours |
| T1 maxed | 48 hours |
| T4 unlock | 72 hours |
| T4 maxed | 5 days |
| T8 unlock | 7 days |
| T8 maxed | 14 days |

When the offline cap is hit, idle accumulation pauses until the player re-opens the game. No spoilage, just halt.

### Storehouse T4 Draft Charge Tracks (Locked Tranche 3, 2026-05-22)

The Storehouse T4 surface holds three independent leaf tracks: Reroll, Skip, Banish. Each has 10 leaf levels. T4 unlock = 3 charges per track baseline. Each purchased leaf adds +1 charge per run to that track only. T4 maxed (10 leaves on all three) = 13 / 13 / 13 charges per run.

| Storehouse T4 state | Reroll / Skip / Banish charges per run |
|---|---|
| T4 unlock | 3 / 3 / 3 |
| 1 leaf on a track | +1 to that track |
| All three tracks maxed (L10 each) | 13 / 13 / 13 |

**Charges do NOT scale with apprentice ratings.** Compounding-template exception called out at the top of this doc. Apprentice multiplier feeds the offline-cap surface (T1) only.

**Charges are per-run consumable.** Reset to full at run start. Unspent charges do NOT carry over.

**Charge mechanics (cross-ref):** Reroll re-spins the entire offer (full draft, not pick-1). Banish removes a card from this run's draft pool only — not global. Skip closes the draft and awards a small essence cache (10 for level-up drafts, 5 × chest_size for chests). Full mechanics in [pillars/run-loop.md](../pillars/run-loop.md) Level-Up Draft section.

Per-leaf essence costs for the three tracks: flagged for the scaling math pass spreadsheet alongside the other per-leaf curves.

### Teahouse Brew Mechanics

Track upgrades are **instant on purchase**. Specialist assignment is **instant**. Teahouse buffs are **persistent passive modifiers** — once unlocked and leveled, always on. No brew timer, no expiration, no refresh interval.

Universal mechanic for the flat-cap template: pay essence + materials → leaf level applies immediately → buff runs continuously sect-wide.

---

## Teahouse — Sixteen Tracks (Locked 2026-05-22)

16 buff tracks, each capping individually. Cap distribution: 5 cap-10 / 6 cap-5 / 3 cap-3 / 2 cap-2. Cap-10 tracks are foundational (every player wants them maxed). Cap-2 tracks are niche / situational. No overlap with Storehouse charges or Forge tracks.

### Track Inventory

| # | Track | Cap | Stat affected |
|---|---|---|---|
| 1 | Attack | 10 | atk multiplier |
| 2 | HP | 10 | max HP |
| 3 | Defense | 10 | flat damage reduction |
| 4 | Move speed | 10 | % |
| 5 | Pickup radius | 10 | % |
| 6 | Attack speed | 5 | global AS % |
| 7 | Crit chance | 5 | flat % |
| 8 | Crit damage | 5 | × modifier |
| 9 | HP regen | 5 | rate |
| 10 | Paint radius | 5 | % |
| 11 | XP gain | 5 | % |
| 12 | iframes | 3 | sec |
| 13 | Essence drops | 3 | run % |
| 14 | Material drops | 3 | run % |
| 15 | Revival | 2 | charges per run |
| 16 | Boss damage bonus | 2 | % vs boss-tier only |

### Composition Rule

- **Within a stat:** additive. Multiple sources affecting the same stat (e.g. Attack track + Boss-damage bonus while fighting a boss) sum, treated as `1 + Σ%`.
- **Across stats:** each stat is its own multiplier in the broader damage stack ([run-loop.md](../pillars/run-loop.md) Card Damage Envelope).
- **Specialist rating multiplies per-leaf output:** `effective_per_leaf = base × max(rating_assigned, 1)`. Per the flat-cap template above. Unstaffed tracks use the rating-1 floor — still progress, just slower.

Only 6 Brewers exist in the chain (ratings 5–10), so at most 6 of 16 tracks are staffed at any time. Player chooses which 6 matter for their build. The other 10 still climb, just at 1/5th to 1/10th the rate.

### Per-Leaf Base Values

| Cap tier | Base % per leaf | Rating-5 maxed | Rating-10 maxed | Unstaffed maxed |
|---|---|---|---|---|
| cap-10 | 0.5% | +25% | +50% | +5% |
| cap-5 | 1% | +25% | +50% | +5% |
| cap-3 | 2% | +30% | +60% | +6% |
| cap-2 | 4% | +40% | +80% | +8% |

**Track 15 (Revival) exception:** non-% track. Cap-2 base = 1 charge per leaf, no rating multiplier. Caps at 2 revival charges per run regardless of assigned specialist.

### Tier Cap Growth (Flagged for Tuning Pass)

T1 caps are listed above (5 cap-10 / 6 cap-5 / 3 cap-3 / 2 cap-2). T4 and T8 grow caps per the "Caps grow with tier" rule in the Per-Building Tier Surfaces table. Specific growth shape (e.g., +1 cap per tier-surface unlock, or per-tier-leaf-density boost) flagged for the per-building leaf-content design pass — same pass that handles Recruitment / Training / Storehouse / Outer Court / Library T2–T5 leaf content.

---

## Soul Forge — Three Upgrade Tracks

1. **Techniques (T1)** — individual run technique upgrades
2. **Passives (T4)** — individual passive upgrades
3. **Paths (T8)** — discovered path-tier strengthening (Sapling → Worldroot effects per theme)

All three surfaces populate dynamically — only discovered content appears as tracks. As the pool grows through play, the Forge surfaces grow with it. Forge purchases fire Minor unlocks like all other building purchases — silent "new" indicator on the building screen, no popup.

### Forge Upgrade Semantics (locked)

**Techniques (T1).** One Forge track per card-family. Base form and evolved form are *chained* within a single track:

- Base form: levels 1–10, each +10% effectiveness, max +100%.
- Once base is at +10, the evolved form unlocks within the same track.
- Evolved form: levels 1–10, each +10%, stacking on the inherited base. Evolved +10 = +200% effectiveness on the evolved form.
- The base +100% keeps applying every future run base is drafted (not just when player evolves).

Rationale: chain prevents the degenerate "ignore base, max evolved" strategy; inheritance prevents Forge investment from evaporating at evolution time; the +200% cap on evolved rewards full commitment.

**Passives (T4).** One Forge track per passive card. Levels 1–10, each +10%, max +100%. Independent tracks, no inheritance chain (passives don't evolve — they persist unchanged through evolutions per the VS-model evolution rule in [pillars/run-loop.md](../pillars/run-loop.md)).

**Paths (T8).** One Forge track per *discovered path tier*. Wood Sapling is one track; Wood Sprout (when discovered) is a separate track; etc. 12 themes × 5 tiers = up to 60 path-tier tracks at endgame.

- Levels 1–10, each +10%, max +100% per tier.
- No inter-tier unlock gating. A 5-meridian player who's culminated Wood Sapling and Wood Sprout can forge both immediately.
- What +10% scales per effect is a designer call: heal amount for Wood Sapling, crit chance for Metal Sapling, explosion damage or radius for Fire Sapling, etc. For structural effects ("Worldtree manifests pulsing AoE"), the designer picks whether +10% applies to damage, radius, frequency, or all three. Flagged for the 48-path-effect design pass — each effect needs its scaling target spelled out.

### Scaling Math Interaction (flagged)

Forge stacks multiplicatively with:

- Teahouse sect-wide cultivation buffs
- Teahouse run buffs (attack / defense / pickup / paint)
- Run-internal card draft level (1–8, applied during the run via level-ups)
- Sect Power multiplier `1 + sqrt(Sect_Power / 100)`
- Path tier effects (each tier's effect runs simultaneously when culminated)

A full scaling pass is required before prototype tuning ships. Target curve: VS / Brotato / Halls of Torment tension in R1–R3 (player has to play well), climbing to dopamine-explosion power in R10–R12 (player has *earned* breaking the game). See [docs/open-questions.md](../open-questions.md).

---

## Cycle Upgrades — Pavilion T8

Pavilion T8 hosts cycle upgrades (flat-cap surface). A newly-learned cycle starts at ~30% of its cap; Pavilion T8 upgrades climb each unlocked cycle toward its full cap. See [pillars/cultivation.md](../pillars/cultivation.md) for cycle mechanics and the 8-cycle table.

This is Pavilion's hybrid surface: the building is compounding at T1 and T4, with a flat-cap track added at T8.

### Pavilion T8 Cycle Climb Economy

Per-cycle structure: 10 leaf levels per cycle, each granting `(cap − 30%) / 10` percentage points of climb toward cap. Starting climb when newly learned = 30% of cap (locked).

Per-leaf essence costs (Cycle 1 baseline):

| Leaf level | Essence cost |
|---|---|
| L1 | 1,000 |
| L2 | 2,500 |
| L3 | 5,000 |
| L4 | 10,000 |
| L5 | 20,000 |
| L6 | 40,000 |
| L7 | 80,000 |
| L8 | 160,000 |
| L9 | 320,000 |
| L10 | 640,000 |

**Total Cycle 1 climb cost = ~1.3M essence.**

**Per-cycle escalation:** Cycle N L1 cost = Cycle 1 L1 cost × 1.5^(N−1). Cycle 8 L1 ≈ 17K essence; Cycle 8 max ≈ 22M essence. **Total cycle climb endgame sink ≈ 40M essence.**

Specific ×1.5 multiplier and the cap-percent-per-cycle values flagged for the scaling math pass spreadsheet. Formula structure locked here.

---

## Tier Counts Per Building

- **Most building specialties** (6-member arc, ratings 5→10): T1–T10
- **Heaven-Reader's 4-member arc** (ratings 7→8→9→10): Pavilion T1–T10

Specialist count drives visual building growth independent of tier. Pao alone = tiny tea hut. 6 Brewers = full tea complex.
