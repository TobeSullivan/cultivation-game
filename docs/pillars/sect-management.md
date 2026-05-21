# Pillar 4 — Sect Management

The sect is the engine that makes everything else move faster.

---

## Core Principle

**Manual play wins through optimization. Auto play is the mercy button.**

---

## Decision Cadences

- **Per-run** (every 10–30 min): claim inbox, glance at sect status. ~30 seconds.
- **Per-session** (couple times an hour): start Forge upgrades, queue Teahouse brews, reassign disciples, spend currency. 2–5 minutes.
- **Per-milestone** (after realm conquest, stage breakthrough, big recruit): restructure. 10–20 minutes.

---

## Maintainability Rules (Hard Constraints)

- Progressive disclosure
- One inbox, one screen
- Notifications rare and obvious
- No upkeep, no decay
- Default behavior always reasonable
- One decision at a time
- No FOMO

---

## Disciples — Two Tiers

**Named disciples** (~140 across the game):
- ~12 realm-final bosses
- ~119 map bosses
- ~20 special-event recruits

Note: realm-finals are also map bosses; total named ≈ 139. Full roster in [systems/boss-roster.md](../systems/boss-roster.md).

**Generics** (millions at endgame):
- Aggregate population, not individuals
- Capped by territory
- Tier-trained passively via Training Hall

---

## Named Disciple Attributes (7)

1. **Name + portrait**
2. **Realm + position**
3. **Tier** — Stage 1 through Stage 12. Trainable up to Stage 12.
4. **Specialty** — one tag, one family.
5. **Specialty Rating (1–10)** — mastery. Trainable to 10.
6. **Meridian count (4–8)** — fixed at recruitment.
7. **Signature technique** — unique run-pool addition on first defeat.

Plus: Recruitment gate (property of how the player got them, not a stat).

---

## Specialty Rating Mechanics

- Drives BIS contribution
- Visible on card as 1–10 integer
- Trainable via Training Hall student slots
- Monotonic per-specialty starting-rating arcs (each new recruit of a specialty has starting rating ≥ all previous of that specialty)
- Building specialists start ≤5 (Heaven-Reader exception, starts at 7)
- Theme specialists scale across realms but theme assignment is no longer realm-locked
- Realm-finals climb 5→10 across the 12 realms

---

## Building Specialist Master System

- All specialists default-home to their specialty's building
- One Master per building; player designates; free and instant to swap
- **Building Tier Unlock Rule (v6):** Master's starting rating IS the tier ceiling the building can reach with that specialist. Pao at rating 5 → Teahouse purchasable up to T5. Lin (Heaven-Reader exception) at rating 7 → Pavilion up to T7. Recruiting a higher-rated specialist of the same family extends the ceiling.
- **Tier count per building:** = max rating achievable in that specialty's arc. For most building specialties (6-member arc, ratings 5→10), buildings reach T1–T10. For Heaven-Reader's short arc (3–4 members), Pavilion likely reaches T1–T9 to T1–T10 depending on arc length decision.
- **Specialist count drives visual building growth** independent of tier. Pao alone = tiny tea hut. 6 Brewers = full tea complex. T1 + 6 specialists = sparse-but-populated; T6 + 1 specialist = expanded-but-empty.
- **Master amplification model:**
  - **Compounding buildings** (Recruitment, Storehouse, Library, Training, Outer Court, Pavilion): all specialists at the building amplify all unlocked surfaces collectively. Formula: `compound rate = base × (1 + Σ(specialist ratings) × coefficient)`. Master = narrative.
  - **Flat-cap buildings** (Teahouse, Soul Forge): each upgrade track can have ONE specialist assigned. Per-level output = `base × max(rating_assigned, 1)`. Master picks lead track first.
- Apprentices contribute supplementary effect on Master's terms
- Buildings grow visually with specialist count and tier

Detailed tier curves and per-building surface tables live in [systems/building-tier-curves.md](../systems/building-tier-curves.md).

---

## What Named Disciples Do (3 Roles)

1. **Region duty** — contribute to region's idle output. Specialty match boosts yield.
2. **Building duty** — Master designation or apprentice support.
3. **Training Hall duty** — either **trainer** (lifts generic tier) or **student** (own tier + rating climb).

---

## Training Math

**Rule 1 — Ceiling Cascade.** Stage caps trainer assignments at (stage − 1).

**Rule 2 — Dynamic Sect Cap.** Sect Cap = min(highest stage in Training Hall, stage − 1).

**Rule 3 — Cumulative Throughput.** Total training points (exponential stage curve) = rate generics + students climb.

**Student Slots:** named disciples can be placed in student slots. Tier and Specialty Rating both climb toward 10. Slow but unbounded. Manual-only.

---

## Sect Power

- Composition-weighted
- Single number visible on Main Hall hub
- Clicking widget deep-links to Management screen
- Affected by: generic distribution, building levels + Master ratings + apprentice counts, named disciple BIS placements (including Specialty Rating), macro progression unlocks

**Multiplier formula** lives in [systems/economy.md](../systems/economy.md): `multiplier = 1 + sqrt(Sect_Power / 100)` (sub-linear).

---

## Buildings — The 10 Buildings

**Building Upgrade Requirements:** Specialist with rating ≥ tier + Materials + Essence (+ Spirit Stones at T5+).

**Tier visibility is realm-gated.** Entering Realm N reveals tiers gated to Realm N across unlocked buildings.

Most buildings hold **~3 distinct functions**. The player learns each building as a place where specific kinds of work happen.

| # | Building | Run By (Master) | What it holds |
|---|---|---|---|
| 1 | **Main Hall** | Head only | Hub. Sect Power widget. Navigation to all other buildings. |
| 2 | **Personal Sanctum** | Head only | (a) Meridian refinement, (b) cycling assignment + switching, (c) tier and stage breakthroughs |
| 3 | **Recruitment Hall** | Charisma Master | (a) Generic population generation (at currency cost), (b) special-event recruit arrivals, (c) recruitment lead processing (region-sourced wandering cultivator events) |
| 4 | **Training Hall** | Trainer Master | (a) Sect Cap (set by highest trainer), (b) generic tier climb (via trainer throughput), (c) named-disciple student slots (tier + Specialty Rating climb) |
| 5 | **Storehouse** | Organizer Master | (a) Idle resource cap, (b) run chest size cap, (c) run skip/reroll/banish charges |
| 6 | **Teahouse** *(Realm 1, foundational)* | Brewer Master | (a) Sect-wide cultivation buffs (in-service tea), (b) run buffs (atk/def/pickup/paint), (c) recipe collection (unlockable brews from materials) |
| 7 | **Soul Forge** | Smith Master | (a) Technique upgrades, (b) passive upgrades, (c) discovered-path strengthening |
| 8 | **Outer Court / Farmlands** | Administrator Master | (a) Pop cap multiplier, (b) sect-wide passive bonuses, (c) reputation/influence generation (feeds rep-threshold special-event recruits) |
| 9 | **Library** | Scholar Master | (a) Head's cultivation speed, (b) path Codex (browsable progress), (c) cycle upgrades (climb each unlocked cycle toward its cap) |
| 10 | **Ascension Pavilion** | Heaven-Reader Master | (a) Inspiration drop rate, (b) qi pool cap, (c) realm transition ceremonies |

### Soul Forge — Three Upgrade Tracks

1. **Techniques** — individual run technique upgrades
2. **Passives** — individual passive upgrades
3. **Paths** — discovered path-tier strengthening (Sapling → Worldroot effects per theme)

Path upgrades work per-discovered-tier. Upgrading the Wood Path lifts ALL discovered Wood tiers proportionally.

Forge purchases fire Minor unlocks like all other building purchases — silent "new" indicator on the building screen, no popup.

### Library — Cycle Upgrades

The Library hosts cycle upgrades. A newly-learned cycle starts at ~30% of its cap; Library tier upgrades climb each unlocked cycle toward its full cap. The Library's other two jobs (head cultivation speed, path Codex) remain.

### Teahouse — Foundational Food Building

R1 foundational. Sect-wide + run buffs. "In service" tea = permanent buff while brewed.

---

## How the Pillars Connect Through the Sect

- **Territory** → **Population cap** → **Sect size**
- **Trainers** → **Sect Cap** → **Generic tier**
- **Sect size + Sect tier** → **Sect Power**
- **Sect Power** → head's cultivation speed, passive qi flow, idle output rates
- **Buildings + Master ratings** → run buffs, charges, chest size, paint radius
- **Named disciple BIS placements** → bonus output on specific regions/buildings
- **Student slots** → long-term investment in favorite named disciples
- **Central trade-offs:** Local bonus vs. Building Master/apprentice vs. Sect-wide lift vs. Long-term investment. Four viable strategies.
