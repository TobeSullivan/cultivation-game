# Prototype Spec — R1–R3

Build-ready details for the 8-map prototype. Scope: R1 (2 maps) + R2 (3 maps) + R3 (3 maps) = 8 maps + 3 realm-finals. All 8 building unlocks compressed into this range. Stages 1–3 complete (no inspiration required). 5th meridian refined at end of R3.

---

## The 8 Maps — Master Table

| # | Map | Boss | Specialty | Building | Theme | Archetype | Body-Part | Starting Rating | Meridian Count |
|---|---|---|---|---|---|---|---|---|---|
| 1 | R1 M1 | Lady Yun | Charisma | Recruitment Hall | Wood | Zone | Legs | 5 | 5 |
| 2 | R1 M2 | Master Pao | Brewer | Teahouse | Water | Projectile | Arms | 5 | 6 |
| 3 | R2 M1 | Sergeant Bao | Trainer | Training Hall | Earth | Strike | Legs | 5 | 5 |
| 4 | R2 M2 | Steward Mei | Organizer | Storehouse | Metal | Orbital | Body | 5 | 5 |
| 5 | R2 M3 | Magistrate Hong | Administrator | Outer Court | Fire | Zone | Head | 5 | 6 |
| 6 | R3 M1 | Archivist Wen | Scholar | Library | Lightning | Projectile | Head | 5 | 6 |
| 7 | R3 M2 | Augur Lin | Heaven-Reader | Ascension Pavilion | Wind | Orbital | Body | **7** | **7** |
| 8 | R3 M3 | Forge-Lord Tian | Smith | Soul Forge | Ice | Strike | Arms | 5 | 7 |

Coverage check:
- Themes: 8 of 8 elementals used, all unique. Shadow/Spirit/Star/Void reserved for Transcendent+.
- Archetypes: Strike ×2, Projectile ×2, Orbital ×2, Zone ×2.
- Body parts: Head ×2, Arms ×2, Legs ×2, Body ×2.
- All names are placeholders.

---

## Realm Adjacency

**R1 (2 maps):** Linear.
- M1 = starting map
- M2 = unlocks after M1 conquered

**R2 (3 maps):** Gateway + branch + final.
- M1 = starting map (gateway from R1)
- M2 = unlocks after M1
- M3 (realm-final) = unlocks after **both** M1 and M2

**R3 (3 maps):** Same pattern as R2.
- M1 = starting map (gateway from R2)
- M2 = unlocks after M1
- M3 (realm-final) = unlocks after **both** M1 and M2

---

## Building Unlock Order

1. Recruitment Hall (R1 M1)
2. Teahouse (R1 M2)
3. Training Hall (R2 M1)
4. Storehouse (R2 M2)
5. Outer Court (R2 M3)
6. Library (R3 M1)
7. Ascension Pavilion (R3 M2)
8. Soul Forge (R3 M3)

All buildings at T1 by end of R3. Higher tiers become purchasable as the next specialist in each chain is recruited (post-prototype for most). Ascension Pavilion alone has T2–T7 purchasable once Augur Lin is recruited (Heaven-Reader exception, rating 7 unlocks the full ceiling for that arc's first member).

---

## Per-Map Details

### R1 M1 — Lady Yun / Bamboo Hollow Province / Recruitment Hall

**Boss identity:** Teahouse keeper who drew followers through warmth and patience, accidentally became powerful. First boss in the game.

**Region biome:** Forested province, bamboo groves, footpath bandits and stray spirits as enemy fodder.

**Signature technique:** *Blooming Garden* — Wood Zone, Legs-variant. Drops a slow-pulsing flower-bloom zone underneath player. Enemies inside are slowed. Player gains small HoT while standing in it.

**Off-recipe evolution:** *Eternal Garden* — zone becomes permanent (no fade timer), motes pulse healing AND damage waves outward on pickup.

**Evo-partner passive:** *Verdant Vow* — Wood Special, Legs-variant. While you have a Zone effect active under your feet, gain +X% damage and +Y% qi regen. Enemies killed inside any of your zones drop healing motes.

**Recommended cultivation:** Stage 1, Tier 1.

**Boss combat profile:**
- HP 1.0 (baseline), contact 0.8, ability 1.0, armor 0, speed 0.6× player
- Single phase
- 2 attacks:
  1. **Bloom Pulse** (basic) — pulses slow-expanding flower-petal ring outward, 1.2-sec windup. Used every ~5 sec.
  2. **Pollen Drift** (passive aura) — continuously emits a slow-pulsing aura at ~150% character radius. Ticks tiny damage, slowly heals her.
- Telegraph: Maximum. The teaching fight.
- Foreshadows the *Blooming Garden* signature directly.

**Region objectives:**
1. Survival: 10 minutes
2. Kills: 200 enemies
3. Targets: 3 elites
4. Territory: 60% paint
5. Resources: gather 50 bamboo shoots
6. Boss: defeat Lady Yun

**Region-themed resource produced (idle + Territory):** bamboo shoots (Wood-themed, Tier 1).

---

### R1 M2 — Master Pao / Cauldron Springs Province / Teahouse (R1 Realm-Final)

**Boss identity:** Port-town alchemist who perfected his craft through decades of patient experimentation, ascended without noticing.

**Region biome:** Hot springs, alchemical pools, steam vents winding through forested hills. Water spirits, hot-spring boars, mischievous brew-imps from spilled experiments, alchemy-mishap creatures.

**Signature technique:** *Steeping Throw* — Water Projectile, Arms-variant. Arcing bottle on impact + small splash, applies "Steeped" debuff: +X% damage from Water for 5 sec, stacks to 5.

**Off-recipe evolution:** *Reservoir Toss* — bottles become larger, splash radius doubles, each impact applies 3 Steeped stacks instead of 1.

**Evo-partner passive:** *Steeped Form* — Water Offense, Arms-variant. Steeped enemies take +X% damage from ALL sources (not just Water). Steeped stacks up to 5, refresh duration on each application.

**Recommended cultivation:** Stage 1, Tier 2.

**Boss combat profile:**
- HP 1.3, contact 0.9, ability 1.1, armor 0, speed 0.7×
- Single phase
- 2 attacks:
  1. **Bottle Lob** (basic) — arcs bottle at player's predicted position, 1.0-sec airtime, splash + Steeped puddle on impact. Used every ~4 sec.
  2. **Brew Spill** (passive) — drops Steeped puddles around himself every ~8 sec, persist 6 sec.
- Telegraph: Very generous.

**Region objectives:**
1. Survival: 12 minutes
2. Kills: 280 enemies
3. Targets: 4 elites
4. Territory: 65% paint
5. Resources: gather 75 alchemy reagents
6. Boss: defeat Master Pao

**Region-themed resource:** alchemy reagents (Water-themed, Tier 1).

---

### R2 M1 — Sergeant Bao / Iron Ridge Region / Training Hall

**Boss identity:** Hard-bitten drill instructor from a hill garrison, taught generations of mortal soldiers how to push past their limits.

**Region biome:** Rocky highlands, terraced training grounds carved into cliffsides, scree fields. Stone wolves, mountain bandits, training-dummy constructs gone rogue, rockslide spirits.

**Signature technique:** *Mountain Stomp* — Earth Strike, Legs-variant. Periodic heavy stomp around player's feet — small radius, heavy damage, brief knockback. Slower fire rate than typical Strike, higher per-hit damage.

**Off-recipe evolution:** *Quaking Earth* — every stomp creates an expanding shockwave ring that knocks back and damages enemies on a delay.

**Evo-partner passive:** *Granite Footing* — Earth Vitality, Legs-variant. While standing still for 1+ sec, gain +X armor and +Y% damage to Strikes. Damage taken while still reduced by Z%.

**Recommended cultivation:** Stage 1 Tier 3 / Stage 2 baseline.

**Boss combat profile:**
- HP 1.5, contact 1.0, ability 1.3, armor 5%, speed 0.7×
- Single phase
- 2 attacks:
  1. **Drill Stomp** (basic) — slow heavy stomp at his feet with shockwave ring, 1.4-sec windup. Used every ~5 sec.
  2. **Hardened Stance** (passive) — while standing still, gains +20% damage reduction. Punish-window is his chase movement.
- Telegraph: Generous.

**Region objectives:**
1. Survival: 13 minutes
2. Kills: 350 enemies
3. Targets: 5 elites
4. Territory: 65% paint
5. Resources: gather 80 iron ore
6. Boss: defeat Sergeant Bao

**Region-themed resource:** iron ore (Earth-themed, Tier 1).

---

### R2 M2 — Steward Mei / Brassgate Region / Storehouse

**Boss identity:** Magistrate who turned a chaotic frontier prefecture into a clockwork-precise administrative engine through sheer force of will.

**Region biome:** Walled administrative cities, grid-pattern streets, brass-and-stone courthouses. Rogue clerks gone bandit, corrupt officials' enforcers, paperwork-bound golems, record-keeper spirits.

**Signature technique:** *Brass Ledger* — Metal Orbital, Body-variant. Four small floating ledger-tablets rotating around the player's torso, standard orbital contact damage.

**Off-recipe evolution:** *Edict of Many Blades* — tablets double to 8, rotation speed increases, tablets occasionally fling outward at distant enemies before returning.

**Evo-partner passive:** *Bound Records* — Metal Utility, Body-variant. +X% pickup radius. Each pickup grants stacking +Y% Orbital damage buff for 4 sec (max 10 stacks).

**Recommended cultivation:** Stage 2, Tier 1.

**Boss combat profile:**
- HP 1.6, contact 1.0, ability 1.2, armor 10%, speed 0.5× (very slow)
- Single phase
- 2–3 attacks:
  1. **Ledger Cast** (passive constant) — four tablet-blades extend out, rotating around her torso at constant range (~3 character radii). Player dodges through gaps or fights from outside orbit.
  2. **Sealed Decree** (projectile) — periodically launches one tablet outward as homing projectile, 0.9-sec lock-on telegraph. Returns to orbit.
- Telegraph: Generous on the projectile; rotating tablets are positional puzzle.

**Region objectives:**
1. Survival: 14 minutes
2. Kills: 380 enemies
3. Targets: 5 elites
4. Territory: 70% paint
5. Resources: gather 80 sealed scrolls
6. Boss: defeat Steward Mei

**Region-themed resource:** sealed scrolls (Metal-themed, Tier 1).

---

### R2 M3 — Magistrate Hong / Stone Keep Region / Outer Court (R2 Realm-Final)

**Boss identity:** Magistrate-king who governs his stone keep with iron procedure and absolute authority. Every word treated as natural law within his prefecture.

**Region biome:** Walled border-region with central administrative citadel, watchtower network, magistrate's compound, surrounding farmland-and-checkpoint sprawl. Corrupt subordinate officials, prisoner-uprising spirits, rogue tax-collectors, sigil-bound enforcer constructs.

**Signature technique:** *Sovereign's Edict* — Fire Zone, Head-variant. Stationary command field projects from where player stops moving. Enemies inside take stacking damage that ramps the longer they stay. Field persists 4 sec after player moves on.

**Off-recipe evolution:** *Iron Decree* — fields become permanent until you place a new one (max 2 active simultaneously), ramp accelerates.

**Evo-partner passive:** *Imperial Presence* — Fire Special, Head-variant. Enemies within line-of-sight take stacking burn DoT (ramps with sight duration). Placing a Sovereign's Edict zone transfers all current burn stacks into the zone's ramp counter.

**Recommended cultivation:** Stage 2, Tier 2.

**Boss combat profile:**
- HP 2.2, contact 1.1, ability 1.4, armor 10%, speed 0.6×
- **Two phases** (R2 realm-final earns multi-phase)
- Phase 1 (100%-50% HP):
  1. **Sovereign's Gaze** (basic) — cone-of-fire telegraph (0.9 sec), then 0.3-sec sustained burn line. Stacks burn-DoT.
  2. **Edict Field** — drops damaging zone at his current location, 1.5-sec telegraph (calligraphy seal on ground), 5-sec persistent zone.
- Phase 2 (sub-50% HP): plants himself center-arena, stops chasing. Edict Fields appear at fixed compass-point locations (no telegraph but predictable pattern). Sovereign's Gaze telegraph tightens to 0.6 sec. Adds:
  3. **Decree of Banishment** — every ~12 sec, large pulsing ring expands from him outward; player must reach arena edge in 2 sec or take heavy damage.
- Telegraph: Generous in phase 1, tightened in phase 2. Phase 2 = predictable but tighter — pattern established here.

**Region objectives:**
1. Survival: 15 minutes
2. Kills: 420 enemies
3. Targets: 6 elites
4. Territory: 70% paint
5. Resources: gather 90 sealed writs
6. Boss: defeat Magistrate Hong

**Region-themed resource:** sealed writs (Fire-themed, Tier 1).

---

### R3 M1 — Archivist Wen / Ash Archives Kingdom / Library

**Boss identity:** Wandering scholar who reads forbidden texts in deep vaults. Her power expressed as the flash of recognition when an idea finally connects.

**Region biome:** Kingdom built around vast underground libraries — surface monasteries, deep vaults, lightning-struck spires as archive rods, courtyards where scholars walk reading scrolls. Dust-spirits, text-golems, rogue apprentices, knowledge-hungry shades.

**Signature technique:** *Illuminated Verse* — Lightning Projectile, Head-variant. Glowing calligraphy-characters fire outward in a fan, weaving toward nearby enemies. On impact, brand enemy with lightning sigil for 3 sec. Multiple sigils chain lightning between branded enemies.

**Off-recipe evolution:** *Annotated Manuscript* — projectiles split on impact, branding multiple nearby enemies. Sigil duration doubles.

**Evo-partner passive:** *Recited Sutra* — Lightning Offense, Head-variant. Each unique enemy type killed during a run grants +X% projectile damage for the rest of the run (caps at 10 types). Branded enemies count as different types per brand.

**Recommended cultivation:** Stage 2 Tier 3 / Stage 3 baseline.

**Boss combat profile:**
- HP 2.0, contact 1.0, ability 1.5, armor 5%, speed 0.8× (faster than other map bosses)
- Single phase
- 3 attacks:
  1. **Verse Flurry** (basic) — fan of 5 calligraphy-projectiles outward in player direction, 0.7-sec windup. Each brands on hit, persists 3 sec. Every ~4 sec.
  2. **Chained Sigil** — when 3+ branded targets exist, calls down lightning chaining between them, 1.0-sec telegraph (vertical light pillars on each).
  3. **Recursive Recitation** (anti-kite) — if player kites at long range >5 sec, ports near player (0.5-sec dissolve telegraph).
- Telegraph: Tight on the flurry, generous on chain.

**Region objectives:**
1. Survival: 16 minutes
2. Kills: 450 enemies
3. Targets: 6 elites
4. Territory: 70% paint
5. Resources: gather 100 ancient manuscripts
6. Boss: defeat Archivist Wen

**Region-themed resource:** ancient manuscripts (Lightning-themed, Tier 2).

---

### R3 M2 — Augur Lin / Skygate Kingdom / Ascension Pavilion

**Boss identity:** Temple-augur who reads tribulation-omens in the sky, her body a platform for celestial signs to align against. **Heaven-Reader exception** — starts at rating 7, 7 meridians.

**Region biome:** High-altitude kingdom of cliffside temple-observatories, sky-paths between peaks, augur-monasteries. Sky-bound spirits, wind-riding shades, tribulation-marked rogue apprentices, cloud-wraiths.

**Signature technique:** *Augury Wheel* — Wind Orbital, Body-variant. Slow-rotating ring of glowing celestial signs orbits player at torso height. Periodically a sign detaches and lashes outward as a wind-blade slash to a random nearby enemy — high single-target damage, brief stagger. Number of signs scales with level. **Higher mid-tier** (rating 7 boss).

**Off-recipe evolution:** *Tribulation Wheel* — signs no longer detach; entire ring periodically expands to maximum radius slashing all enemies in outward ring-wave. Ring rotates faster permanently, signs sometimes mark enemies for delayed follow-up detonation.

**Evo-partner passive:** *Foreseen Path* — Wind Utility, Body-variant. +X% movement speed. While moving, the Augury Wheel rotates Y% faster. Standing still grants brief stacking dodge chance.

**Recommended cultivation:** Stage 3, Tier 1.

**Boss combat profile:**
- HP 2.3, contact 1.0, ability 1.5, armor 10%, speed 0.7×
- Single phase but harder than typical (rating 7)
- 3 attacks:
  1. **Wheel of Signs** (passive constant) — ring of celestial signs orbits her. Each sign occasionally detaches and flies outward at random nearby target, 0.6-sec telegraph.
  2. **Tribulation Mark** — designates player position with sky-marker, 2.0-sec telegraph (visible beam from sky to ground), then heavy lightning bolt on marked spot.
  3. **Sky Tide** (anti-kite) — periodic wide wind-current sweeping across arena, 1.2-sec telegraph (wind streaks visible). Light damage + pushes player to specific edge.
- Telegraph: Reasonable. Constant positional awareness required.

**Region objectives:**
1. Survival: 16 minutes
2. Kills: 460 enemies
3. Targets: 6 elites
4. Territory: 72% paint
5. Resources: gather 100 tribulation feathers
6. Boss: defeat Augur Lin

**Region-themed resource:** tribulation feathers (Wind-themed, Tier 2).

---

### R3 M3 — Forge-Lord Tian / Frostforge Kingdom / Soul Forge (R3 Realm-Final, Prototype Capstone)

**Boss identity:** Smith who works only at the highest mountain forge where the air freezes the breath but his hammer never cools. Forges souls into steel; his enemies are tempered by their own destruction.

**Region biome:** High-altitude kingdom built around a vast volcanic-vent forge — paradox is the point. Steaming hot springs surrounded by perma-frost, mountain monasteries clinging to obsidian cliffs, forge-temples where steel is quenched in glacier-melt. Forge-bound spirits, hammer-broken apprentices, frost-iron golems, escaped Soul Forge experiments gone feral.

**Signature technique:** *Forge-Spirit Hammer* — Ice Strike, Arms-variant. Heavy hammer-swing animation in melee range, slower fire rate than standard Strike. Each hit deposits "Cold Forging" stack on enemy. At 5 stacks, enemy detonates in frost-shock (damage + brief slow nearby). High per-hit damage; detonation is the payoff. **Higher mid-tier** (R3 realm-final = strongest of the 8 prototype signatures).

**Off-recipe evolution:** *Anvil-Sundering Strike* — every hit also generates stack on all enemies within melee range (not just target), detonations chain (detonated enemy's frost-shock applies 2 stacks to all enemies in blast).

**Evo-partner passive:** *Tempered Body* — Ice Vitality, Arms-variant. Each Cold Forging stack you apply also grants you +1 temporary armor (max 30, decays 1/sec when not applying stacks). When an enemy detonates from full stacks, you gain brief +X% Strike damage burst.

**Recommended cultivation:** Stage 3, Tier 2.

**Boss combat profile:**
- HP 3.0, contact 1.2, ability 1.6, armor 15%, speed 0.6×
- **Two phases** (was three in earlier draft, downscaled to leave R4–R12 escalation room)
- Phase 1 (100%-50% HP):
  1. **Hammer Slam** (basic melee) — heavy swing in front of him, 1.0-sec windup. High damage. Applies Cold Forging on hit.
  2. **Forge Spark** (ranged) — throws glowing ember-shard toward player, 0.7-sec telegraph. Applies Cold Forging on hit.
  3. **Anvil Shockwave** (anti-kite) — slams anvil-arm down, outward ring of frost-shockwave with 1.3-sec telegraph. Wide AoE.
- Phase 2 (sub-50%): grows additional spectral hammer-arm. Hammer Slam becomes 2-hit combo. Forge Spark becomes 3-shard spread. Adds:
  4. **Detonation Mark** — marks player with 3 Cold Forging stacks on each Hammer Slam hit; at 5 stacks player detonates (heavy damage + brief slow). Encourages immediate damage clears.
- Telegraph: Generous in phase 1, tight in phase 2. Never untelegraphed.

**Region objectives:**
1. Survival: 18 minutes (longest in prototype)
2. Kills: 500 enemies
3. Targets: 7 elites
4. Territory: 75% paint
5. Resources: gather 110 frost-iron ingots
6. Boss: defeat Forge-Lord Tian

**Region-themed resource:** frost-iron ingots (Ice-themed, Tier 2).

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

**Partner Passive Distribution — Forward-Shift Derangement (LOCKED):**

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

**Per-Map Reward Quantities — LOCKED:**

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

**Full R1-R3 banked haul:** ~3,700 essence + ~3,140 raw qi + ~215 T1 mixed + ~266 T2 mixed materials + region-themed caches + ~85 spirit stones + 3 inspiration shards + 16 cards (8 techniques + 8 partner passives) + 8 named disciple recruits + all 8 buildings unlocked at T1.

---

## Prototype Tier State (LOCKED)

| Building | Master | Starting Rating | Tiers Purchasable in Prototype |
|---|---|---|---|
| Recruitment Hall | Yun | 5 | T1-T5 |
| Teahouse | Pao | 5 | T1-T5 |
| Training Hall | Bao | 5 | T1-T5 |
| Storehouse | Mei | 5 | T1-T5 |
| Outer Court | Hong | 5 | T1-T5 |
| Library | Wen | 5 | T1-T5 |
| Ascension Pavilion | Lin | **7** (Heaven-Reader exception) | **T1-T7** |
| Soul Forge | Tian | 5 | T1-T5 |

Tier ceiling = Master's starting rating. Purchasing tiers costs essence + materials (+ spirit stones at T5+) per the building tier cost table in the v6 master design doc.

---

## Enemy Categories

Each map has 4–6 fodder types + 2–3 elite types (visual/biome variation; mechanically baseline).

**Fodder:** HP 0.05× boss baseline, damage 0.4, speed 0.5–0.9× player. Drops monster cores, raw qi, occasional spirit stones.

**Elite:** HP 0.5×, damage 0.8, speed 0.4×. Spawn ~every 90 sec. Drops chest (3–5 cards) + tier-appropriate materials.

**Mini-boss:** HP 1.2×, damage 1.0, speed 0.5×. Spawn once per minute past 10-min mark. Drops larger chest (5 cards) + better materials + sometimes inspiration fragment.

**Per-realm scaling:** R1 = 1×, R2 = 1.5×, R3 = 2×. Both HP and damage scale; speed/behavior constant.

**Generic boss on replay:** the named realm-final doesn't respawn. Generic boss with mini-boss stats × ~2 appears at 5- or 10-min mark instead.

---

## Difficulty Curve Check

| Map | HP | Phases | Attacks | Telegraph |
|---|---|---|---|---|
| R1 M1 | 1.0 | 1 | 2 | Maximum |
| R1 M2 | 1.3 | 1 | 2 | Very generous |
| R2 M1 | 1.5 | 1 | 2 | Generous |
| R2 M2 | 1.6 | 1 | 2-3 | Generous |
| R2 M3 | 2.2 | 2 | 3 | Generous→Tight |
| R3 M1 | 2.0 | 1 | 3 | Tight on basics |
| R3 M2 | 2.3 | 1 | 3 | Reasonable |
| R3 M3 | 3.0 | 2 | 4 | Generous→Tight |

Curve holds. Each realm-final is the toughest in its realm. Each new realm's gateway boss is slightly tougher than the previous realm's final. No spikes.

Headroom preserved for R4–R12 escalation: attack count grows slowly to ~5 by R12, phases reach 3-4 at most. Escalation is primarily through tighter telegraphs, attack overlap, and arena interaction, not more moves.

---

## What's Deferred for the Tuning Pass

- Exact HP/damage numbers (relative baselines locked; absolute numbers anchored to player baseline Atk 10, HP 100, fodder HP 8 R1 baseline)
- Per-card per-level variance within archetypes (archetype baselines locked in v6 master doc)
- Per-enemy-type behavior quirks (does brew-imp lob bottles, does stone-wolf charge in packs)
- Drop rate % within categories
- Forge upgrade cost curves beyond Forge T1
- T2-T5 leaf content for 6 buildings (Recruitment / Training / Storehouse / Outer Court / Library / Forge); Teahouse + Pavilion fully spec'd in building-tier-curves
- Wave composition per map (fodder/elite spawn timing)
- Library cycle climb economy
- Naming pass (all current names are placeholders)
