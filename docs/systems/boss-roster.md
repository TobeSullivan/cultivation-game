# Boss Roster

The named disciple roster is a designed system. Total: **~139 named disciples** = ~12 realm-finals (also map bosses) + ~119 other map bosses + ~20 special-event recruits.

---

## Specialty Taxonomy (Locked)

**Building specialties (8):**
- Brewer → Teahouse
- Trainer → Training Hall
- Smith → Soul Forge
- Charisma → Recruitment Hall
- Organizer → Storehouse
- Administrator → Outer Court
- Scholar → Library
- Heaven-Reader → Ascension Pavilion

**Theme specialties (12):**
- Wood, Earth, Fire, Water, Metal, Wind, Ice, Lightning, Shadow, Spirit, Star, Void

---

## Boss Schema (7 Attributes + Combat Profile)

Named disciple attributes (full list in [pillars/sect-management.md](../pillars/sect-management.md)):

1. Name + portrait
2. Realm + position
3. Tier (Stage 1–12)
4. Specialty (one tag, one family)
5. Specialty Rating (1–10)
6. Meridian count (4–8)
7. Signature technique

**Clarification on themes:** Building specialists (Brewer, Trainer, Smith, Charisma, Organizer, Administrator, Scholar, Heaven-Reader) carry NO theme tag. A Brewer is just a Brewer — brewing is a skill, not a theme. Their signature technique has a theme (since all cards are themed), but the disciple themselves is theme-less.

Theme specialists (Wood, Earth, Fire, etc.) carry their theme tag as their specialty. They have no building affinity.

Every named disciple has exactly one specialty, from one family (building or theme). Their signature technique is always themed.

### Boss Combat Profile (Additional Schema)

- HP scaling (relative to R1 M1 baseline)
- Contact damage
- Ability damage
- Armor %
- Movement speed vs. player
- Phase structure (count + HP thresholds)
- Attack set (each: type, telegraph time, damage, cooldown, foreshadowing note)
- Telegraph generosity (relative scale)
- Arena interaction (none / static hazard / dynamic hazard / boss-becomes-arena)

**Escalation principle:** R12 finals should have ~5 attacks across 3–4 phases. Escalation through tighter telegraphs, higher damage, attack overlap, arena interaction — NOT more moves. R1–R3 prototype curve documented in [prototype/bosses.md](../prototype/bosses.md) leaves headroom.

---

## R1–R3 Prototype Boss Roster + Partner Passives

Per-map details for the 8 R1–R3 building-trigger bosses (themes, archetypes, body-parts, signatures, partner passives, combat profiles, objectives) live in [prototype/bosses.md](../prototype/bosses.md) and [prototype/rewards.md](../prototype/rewards.md).

Partner passive distribution across the 8 prototype maps uses **forward-shift derangement**: each map's Resources objective drops the NEXT map's boss partner. R3 M3 wraps to R1 M1. No map drops its own boss's partner.

---

## Starting Rating Rules

- Monotonic per-specialty (each new chain recruit starts at rating ≥ all previous of that specialty)
- Building specialists start ≤5 (Heaven-Reader exception starts at 7)
- Theme specialists distributed across all realms; rating arcs follow specialty membership, not realm placement
- Realm-finals climb 5→10 across realms
- A specialist's starting rating IS the tier their building can be purchased up to (so the 1st Brewer at rating 5 unlocks Teahouse T1–T5; the 2nd Brewer at rating 6 extends to T6; etc.)

---

## The 12 Realm-Final Headliners

The realm-final boss roster from v4 remains, but **their themes are now free design choices** rather than realm-mandated. Building-trigger finals (R1 Brewer, R2 Administrator, R3 Smith) keep their specialties. The 9 non-building-trigger finals' themes are open.

Working table (themes flagged as TBD pending roster pass):

| Realm | Specialty | Theme | Rating | Mer | Notes |
|---|---|---|---|---|---|
| R1 | **Brewer** | TBD | 5 | 6 | Teahouse trigger |
| R2 | **Administrator** | TBD | 5 | 6 | Outer Court trigger |
| R3 | **Smith** | TBD | 5 | 7 | Soul Forge trigger |
| R4 | Theme specialist | TBD | 7 | 7 | |
| R5 | Theme specialist | TBD | 8 | 7 | |
| R6 | Theme specialist | TBD | 8 | 7 | |
| R7 | Theme specialist | TBD | 8 | 7 | |
| R8 | Theme specialist | TBD | 9 | 8 | |
| R9 | Theme specialist | TBD | 9 | 8 | |
| R10 | Theme specialist | TBD | 9 | 8 | |
| R11 | Theme specialist | TBD | 10 | 8 | |
| R12 | Theme specialist | TBD | 10 | 8 | Universe-scope mastery boss |

Theme distribution across realm-finals is a roster-design question — likely each of the 12 themes gets one realm-final somewhere across R1–R12, distributed for variety rather than concentration.

---

## The 8 R1–R3 Building-Trigger Bosses

Specialties locked; themes now free choices (since realms are no longer themed).

| # | Realm | Pos | Specialty | Notes |
|---|---|---|---|---|
| 1 | R1 | Map | Charisma | Recruitment Hall |
| 2 | R1 | Final | Brewer | Teahouse |
| 3 | R2 | Map | Trainer | Training Hall |
| 4 | R2 | Map | Organizer | Storehouse |
| 5 | R2 | Final | Administrator | Outer Court |
| 6 | R3 | Map | Scholar | Library |
| 7 | R3 | Map | Heaven-Reader | Ascension Pavilion |
| 8 | R3 | Final | Smith | Soul Forge |

All 8 defeat-gated. Every system online by end of R3.

**Note:** R1–R3 has exactly 8 maps (2+3+3), all of which are building triggers. There are no theme-specialist map bosses in the Mortal era. Theme variety in the day-1 player's pool comes from (a) the 96-card day-1 pool covering all 12 themes already, and (b) the building-trigger bosses' signature techniques — which carry theme tags (themes are assigned per signature, not per disciple — a Brewer disciple has Specialty Brewer, but their dropped signature technique has some theme).

---

## The 20 Special-Event Recruits

Deterministic triggers; never RNG. Always-join (decline not offered).

Roster structure carried forward from v4:
- 4 reputation thresholds
- 4 achievement-driven
- 3 region-specific
- 4 Grand Master
- 3 Relationship
- 2 composite

Specific triggers TBD.

---

## Theme Distribution Principle

**Even distribution across all 12 realms.** Every realm contributes to every theme through:
- Map boss signature techniques (theme-tagged techs added to pool)
- Region objective passive unlocks (theme-tagged passives added)
- Realm-final signatures (one theme's "stronger card" per realm)

Roster design ensures every theme's path arc is reachable by the meridian-pacing timeline:
- 4+4 Sapling recipe = day-1 pool (handled)
- +1 pair by R3 = Sprout recipe completion accessible
- +1 pair by R5 = Grove
- +1 pair by R7 = Forest
- +1 pair by R10 = Worldroot

Cross-checking the roster + region-objective design against this pacing is required.
