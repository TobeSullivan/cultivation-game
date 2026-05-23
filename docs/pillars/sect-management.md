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
- **Building Tier Unlock Rule (v6):** Master's starting rating IS the tier ceiling the building can reach with that specialist. Pao at rating 5 → Teahouse purchasable up to T5. Recruiting a higher-rated specialist of the same family extends the ceiling.
- **Tier count per building:** = max rating achievable in that specialty's arc. For most building specialties (6-member arc, ratings 5→10), buildings reach T1–T10. Heaven-Reader's 4-member arc (ratings 7→8→9→10) also reaches T1–T10.
- **Specialist count drives visual building growth** independent of tier. Pao alone = tiny tea hut. 6 Brewers = full tea complex. T1 + 6 specialists = sparse-but-populated; T6 + 1 specialist = expanded-but-empty.
- **Master amplification model:**
  - **Compounding buildings** (Recruitment, Storehouse, Library, Training, Outer Court, Pavilion): all specialists at the building amplify all unlocked surfaces collectively. Formula: `compound rate = base × (1 + Σ(specialist ratings) × 0.10)`. The 0.10 coefficient is universal across compounding buildings; per-building tuning may diverge during playtest. Master = narrative.
  - **Flat-cap buildings** (Teahouse, Soul Forge): each upgrade track can have ONE specialist assigned. Per-level output = `base × max(rating_assigned, 1)`. Master picks lead track first.
- Apprentices contribute to the compounding sum via their ratings; flat-cap buildings have no separate apprentice term
- Buildings grow visually with specialist count and tier (see Visual Growth below)

Detailed tier curves and per-building surface tables live in [systems/building-tier-curves.md](../systems/building-tier-curves.md).

---

## Visual Growth — Two Independent Axes

Buildings communicate progression visually through two orthogonal axes. Both run simultaneously.

### Axis 1 — Tier (drives base art)

Three base-art stages per building, keyed to the three tier surfaces:

- **T1 stage** — building's initial form (small, simple)
- **T4 stage** — refined form (expanded scope, new structural elements)
- **T8 stage** — grand form (full realization of the building's mature identity)

Tier breakthroughs at T1/T4/T8 trigger the visual upgrade. Tiers between (T2/T3, T5/T6/T7, T9/T10) share the base art of the most recent milestone — internal upgrades show as overlay flair (gilding, lanterns, banners) without requiring new base sprites.

**Prototype scope:** R1–R3 caps buildings at T5 (T7 for Pavilion). Prototype players see T1 + T4 visual stages only. T8 art is post-prototype work.

**Asset implication:** 10 buildings × 3 tier stages = 30 base building images full game. Prototype = 20 base images (T1 + T4 across 10 buildings).

### Axis 2 — Specialist count (drives dynamic overlay)

Specialist count grows the sect visually through dynamic Godot-side overlays, composed at runtime. **The implementation differs by hub architecture context — original per-building NPC overlay model was redesigned 2026-05-23 session 2 with the front-facing skyline pivot.**

**Current model (front-facing skyline, 2026-05-23 session 2 onward):**

- **Aggregate foreground crowd silhouette layer** — sect population is expressed as a foreground band of cultivator silhouettes facing the sect, in front of the building layer. Density, count, and figure variety scale with sect population.
- **Pool of 9 unique silhouettes** locked (variants on top-of-head, body mass, posture). Crowd composition in Godot draws from this pool, distributes across the FG band, applies sparse bob/shuffle tween (1-2 figures shifting weight every few seconds).
- **Per-building atmospheric overlays** (lit windows, particles) still apply at the per-building sprite level for building-specific activity reads.
- Drift pattern #18 still respected — buildings remain separable sprites with anchor points and click hotspots. Population is just expressed aggregate-style rather than per-building NPC.

**Original model (iso compound, abandoned 2026-05-23 session 2):**

- Per-building NPC sprites walking individual building grounds, count scaling per-building with specialist count. Was abandoned with the architecture pivot — front-facing skyline doesn't support per-building ground space the way iso compound did, and aggregate FG crowd reads more legibly for sect-size at a glance.

**Per-building activity overlays (both models):**

- **Lit windows / lanterns** — number lit scales with population at that building
- **Ambient particles** — smoke from chimneys, qi wisps, dust on training grounds; intensity scales with activity
- **Subtle lighting changes** — busier buildings glow warmer

This means **"Pao alone = tiny tea hut, 6 Brewers = full tea complex"** is delivered through:
- Tier-driven base art (building size and complexity)
- Per-building atmospheric overlays (lit windows, glow intensity, particles)
- Aggregate FG crowd density (sect-wide population read)

**Asset implication:** 9 crowd FG silhouettes locked + 5–6 atmosphere overlay assets (particles + lighting textures). All composable in Godot at runtime; no asset explosion.

### Combined matrix

| | 1 specialist | 3–4 specialists | 6+ specialists |
|---|---|---|---|
| T1 base art | Sparse + small | Populated + small | Bustling + small |
| T4 base art | Sparse + expanded | Populated + expanded | Bustling + expanded |
| T8 base art | Sparse + grand | Populated + grand | Bustling + grand |

Player visual reading: tier = "how built up is this place" / specialist count = "how busy is this place." Both axes always true.

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

Most buildings hold **~3 distinct functions**. The player learns each building as a place where specific kinds of work happen. **For compounding buildings, the three functions correspond to the three tier surfaces (T1, T4, T8) in [systems/building-tier-curves.md](../systems/building-tier-curves.md).** UI features that live at a building (Codex at Library, Sect Power widget at Main Hall) are noted separately and don't count as functions.

| # | Building | Run By (Master) | What it holds |
|---|---|---|---|
| 1 | **Main Hall** | Head only | Hub. Sect Power widget. Navigation to all other buildings. |
| 2 | **Personal Sanctum** | Head only | (a) Meridian refinement, (b) cycling assignment + switching, (c) tier and stage breakthroughs |
| 3 | **Recruitment Hall** | Charisma Master | (a) Generic recruit tick rate, (b) amount per tick, (c) cost reduction / qi yield per recruit. *Special-event recruit arrivals also happen here — non-scaling, triggered by external conditions, not a tier surface.* |
| 4 | **Training Hall** | Trainer Master | (a) Generic tier climb throughput, (b) named-disciple student slot effectiveness, (c) new generic starting stage (floor). *Sect Cap is set separately by the Ceiling Cascade rule below — it's a consequence of trainer assignments, not a tier-scaling surface.* |
| 5 | **Storehouse** | Organizer Master | (a) Idle resource cap, (b) run chest size cap, (c) run skip/reroll/banish charges |
| 6 | **Teahouse** *(Realm 1, foundational)* | Brewer Master | (a) Sect-wide cultivation buffs (in-service tea), (b) run buffs (atk/def/pickup/paint), (c) recipe collection (unlockable brews from materials) |
| 7 | **Soul Forge** | Smith Master | (a) Technique upgrades, (b) passive upgrades, (c) discovered-path strengthening |
| 8 | **Outer Court / Farmlands** | Administrator Master | (a) Sect-wide building upgrade cost reduction passive, (b) named disciple placement BIS amplification (yield boost when named assigned to region/building), (c) pop cap multiplier |
| 9 | **Library** | Scholar Master | (a) Head's cultivation speed, (b) region material drop rate, (c) generic disciple qi rate (sect-wide) |
| 10 | **Ascension Pavilion** | Heaven-Reader Master | (a) Qi accumulation speed, (b) tier breakthrough speed, (c) cycling technique upgrades (flat-cap T8). *Realm transition ceremonies happen at Pavilion as flavor/UX, not a tier-scaling surface.* |

### Soul Forge — Three Upgrade Tracks

1. **Techniques (T1)** — individual run technique upgrades. One Forge track per card-family (base + evolved chained). Base levels 1–10 unlock first; +1 = +10% effectiveness; max +10 = +100%. Once base is at +10, the evolved form's track unlocks. Evolved levels 1–10 stack on inherited base — evolved +10 = +200% effectiveness on the evolved form. Investment never evaporates: the base +100% keeps applying every future run base is drafted.
2. **Passives (T4)** — individual passive upgrades. One Forge track per passive card. +1 = +10% effectiveness; max +10 = +100%. Independent tracks, no inheritance chain.
3. **Paths (T8)** — discovered path-tier strengthening. One Forge track per discovered path tier (Wood Sapling is one track, Wood Sprout is another, etc.). +1 = +10% to that tier's effect; max +10 = +100%. No inter-tier unlock gating. What +10% scales per effect is a designer call (heal amount for Wood Sapling, crit chance for Metal Sapling, explosion damage/radius for Fire Sapling, etc.) — flagged for the 48-path-effect design pass.

Forge surfaces populate dynamically — only discovered techniques, passives, and path tiers appear as upgrade tracks. As the pool grows through play, the Forge surfaces grow with it.

Forge purchases fire Minor unlocks like all other building purchases — silent "new" indicator on the building screen, no popup.

**Scaling math interaction.** Forge stacks multiplicatively with Teahouse buffs (sect-wide + run), run-internal card draft level 1–8, Sect Power multiplier, and Path tier effects. A full scaling pass is flagged as follow-up (see [docs/open-questions.md](../open-questions.md)) — target curve is VS / Brotato / HoT tension in R1–R3 climbing to dopamine-explosion power in R10–R12.

### Library — Path Codex

The Path Codex (browsable path progress, recipe hints for partially-discovered paths, lore entries) is a UI feature that lives at Library. It is **not** a tier-scaling function — the Codex UI is the same at Library T1 and T10. Library's three tier surfaces are the three functions listed in the table above.

### Cycle Upgrades — At Pavilion T8

Cycle upgrades live at Ascension Pavilion T8 (flat-cap surface). A newly-learned cycle starts at ~30% of its cap; Pavilion T8 upgrades climb each unlocked cycle toward its full cap. See [pillars/cultivation.md](cultivation.md) and [systems/building-tier-curves.md](../systems/building-tier-curves.md).

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
