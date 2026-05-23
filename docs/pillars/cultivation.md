# Pillar 2 — Cultivation Progression (Idle / AdCap Spine)

The long power curve. Asymmetric gating with realm progression (see [risk-map.md](risk-map.md)).

---

## Stages

- **12 stages total.** Names TBD, generic xianxia/wuxia (no IP infringement).
- Each stage has **3 cycling milestones** (functional "tiers").
- The 3 cycles per stage are about **purifying and condensing qi** — expanding the pool, refining the essence each time.

---

## Eras (Visual / Power Brackets)

| Era | Stages | Status | Geographic Scope |
|---|---|---|---|
| Mortal | 1–3 | Still human | Provinces of a country |
| Transcendent | 4–7 | Beyond human, can still die | Countries of a continent |
| Immortal | 8–10 | True immortal | Continents of a world |
| Divine | 11 | Demi-god | Worlds of a galaxy |
| Eternal | 12 | God / beyond | Galaxies / existence |

Era names are placeholders.

---

## Cycling Mechanics

**Cycling is the shape of qi circulation through the body's meridians.** Mechanically: a % bonus to the head's qi gathering rate (idle + run-derived).

- **8 cycling techniques total in the entire game.** Each is a distinct circulation pattern through some number of meridians.
- **Only one cycle active at a time.** Switching is free and instant.
- **Meridian count gates access.** More refined meridians = more shapes accessible.
- **Each cycle has a cap.** Pavilion T8 upgrades climb a cycle toward its cap.
- **Head-only mechanically.** Disciples do not run cycles in any way that affects the game.

### The 8 Cycles

**Unlock rule: every cycle unlocks from a specific stage breakthrough.** Single source, in numerical order. No Library gates, no rare drops, no late-game events.

| Cycle | Stage gate | Mer req | Cap (placeholder %) |
|---|---|---|---|
| Cycle 1 | Game start | 4 | +10% |
| Cycle 2 | Stage 2 breakthrough | 4 | +20% |
| Cycle 3 | Stage 4 breakthrough | 5 | +35% |
| Cycle 4 | Stage 6 breakthrough | 5 | +50% |
| Cycle 5 | Stage 8 breakthrough | 6 | +75% |
| Cycle 6 | Stage 9 breakthrough | 6 | +110% |
| Cycle 7 | Stage 10 breakthrough | 7 | +160% |
| Cycle 8 | Stage 12 breakthrough | 8 | +250% |

Meridian pacing (5th end-R3, 6th end-R5, 7th end-R7, 8th end-R10) means the required meridian count arrives just before or in step with each cycle's stage gate. Player almost never has a cycle they can't use.

Cycle effects are pure qi-gathering-rate bonuses. No archetypes, no theme bonuses.

**Cycle upgrades happen at the Ascension Pavilion T8** (flat-cap surface, see [systems/building-tier-curves.md](../systems/building-tier-curves.md)). A newly-learned cycle starts at ~30% of its cap. Pavilion T8 upgrades climb each known cycle toward its full cap.

---

## Meridian Refinement

Meridians refine at the Personal Sanctum. Refinement is non-combat, ceremonial.

**Pacing (locked):**

| Refinement | Triggered | Material tier | Currency gates |
|---|---|---|---|
| 5th meridian | end-R3 | T2 (any theme) | Essence |
| 6th meridian | end-R5 | T3 (any theme) | Essence |
| 7th meridian | end-R7 | T4 (any theme) | Essence + Spirit Stones |
| 8th meridian | end-R10 | T5 (any theme) | Essence + Spirit Stones (large) |

**Notes:**
- "Any theme" — refinement accepts any of the 12 themed materials at the required tier, consistent with the unified materials rule in [systems/economy.md](../systems/economy.md)
- Material tier maps to realm pair (R1–R2=T1, R3–R4=T2, etc.); refinement uses the tier of the realm at which it triggers
- Spirit stones gate the 7th and 8th refinements as part of the "high-meridian refinement" stone sink locked in economy.md
- Specific quantities (material counts, essence amounts, stone counts) are tuning placeholders — refined during build/playtest

---

## Qi Pool

- Qi pool fills via idle generation (Sect Power-driven, from conquered regions), run-derived input (raw qi from enemy kills), and cycling multiplier
- Pool **caps**; player must "hit the button" to advance a tier
- Qi never decays or is lost
- Each stage requires 3 full cycles to be ready for stage breakthrough

### Pool Cap is Inherent to Current Stage

The qi pool cap is **NOT a tunable building surface**. It is an inherent property of the player's current cultivation stage. Within a stage, the cap stays fixed — fill it three times via the cycling cadence to be stage-ready. The cap only rises when the player breaks through to the next stage.

This was deliberately locked: cycling is the "fill three times to advance" mechanic; making the cap upgradeable would only add friction without changing the cadence.

**Cap curve:** `cap(stage) = 1,000 × 2^(stage-1)`

| Stage | Pool cap |
|---|---|
| 1 | 1,000 |
| 2 | 2,000 |
| 3 | 4,000 |
| 4 | 8,000 |
| 5 | 16,000 |
| 6 | 32,000 |
| 7 | 64,000 |
| 8 | 128,000 |
| 9 | 256,000 |
| 10 | 512,000 |
| 11 | 1,024,000 |
| 12 | 2,048,000 |

Doubling matches the AdCap shape — idle qi output across realms climbs ~2.4× per realm (per [risk-map.md](risk-map.md)), so cap-fill time stays roughly constant across stages. The "fill three times" cadence holds at every era.

---

## Tier Breakthroughs (Within a Stage)

Small ceremonies. Click-to-advance once requirements are met.
- 3 per stage
- Performed at the Personal Sanctum
- No combat

---

## Stage Breakthroughs

- **Stages 1–3:** just press the button.
- **Stages 4–12:** require **inspiration** as a prereq.
- Non-combat ceremonial moments at the Personal Sanctum.

---

## Inspiration

- Drops only from **realm-final bosses** (first-time defeat only)
- Cannot be banked ahead (realm gating prevents access to higher-stage inspiration outside cultivation reach)
- Self-regulating progression gate

---

## Stage Rewards

- Bigger numbers
- More cards added to the draft pool (~2 per stage)
- Occasional cycle unlocks
- (Future scope: new run mechanics per stage. Not in v1 to keep scope manageable.)

---

## The Asymmetric Gating Rule

- **Cultivation gates realm progression.** Stage X required to enter Realm X.
- **Realm progression does NOT gate cultivation.** (Patient player could max cultivation in R1 in theory.)
- **EXCEPT** — once stage 4+ requires inspiration, you must engage with the appropriate realm.
- **Additionally** — advancing to the next realm requires defeating the current realm's final boss (see [risk-map.md](risk-map.md)). Map completion = all 6 objectives banked, and boss is objective #6.
