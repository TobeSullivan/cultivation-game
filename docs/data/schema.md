# Data Schema

Format-agnostic entity/relationship model for the cultivation game. Built out during the prototype design pass. Engineering handoff target.

---

## Core Entities

### Realm
- `id` (R1–R12)
- `scope` (Province / Region / Kingdom / Empire / Continent / Sea / World / Sky / Heavens / Star / Galaxy / Universe)
- `era` (Mortal / Transcendent / Immortal / Divine / Eternal)
- `map_count` (R1=2 through R12=20, total 119)
- `stage_gate` (cultivation stage required to enter)
- `gateway_map_id` (which map the player enters first)
- `reward_multiplier` (R1=1×, R2=1.5×, R3=2× — used for objective rewards and enemy scaling)

### Map
- `id`
- `name` (placeholder for now)
- `realm_id`
- `position` (map / realm_final)
- `biome_description`
- `building_unlocked` (optional, FK to Building — only the 8 R1–R3 maps)
- `unlock_prerequisites` (array of map_ids; empty for gateway maps)
- `is_starting_map` (boolean)
- `enemy_roster` (array of EnemyType references)
- `themed_resource_id` (FK to Resource — the region's theme-tagged material)
- `boss_id` (FK to Boss)
- `recommended_stage` (1–12)
- `recommended_tier_within_stage` (1–3)

### Objective
- `id`
- `map_id`
- `type` (Survival / Kills / Targets / Territory / Resources / Boss) — enum, exactly 6 per map
- `target_value` (number)
- `first_time_reward` (enum: essence_bundle, monster_cores_and_qi, materials_bundle, region_resource_cache, partner_passive, signature_technique_and_disciple, etc.)
- `partner_passive_unlock_id` (FK to Card, when this objective is designated as the passive-dropper)
- `banked_state` (boolean — per-player)

### Boss
- `id`
- `name` (placeholder)
- `portrait_ref`
- `realm_id`
- `position` (map / realm_final / special_event)
- `specialty_id` (FK to Specialty)
- `starting_rating` (1–10, integer)
- `meridian_count` (4–8)
- `signature_card_id` (FK to Card)
- `recruitment_gate` (default 'defeat'; rare exotics defined per-boss; none in R1–R3)
- `building_unlocked` (optional FK to Building)
- `hp_relative` (1.0 = R1 M1 baseline)
- `contact_damage_relative`
- `ability_damage_relative`
- `armor_percent`
- `movement_speed_vs_player`
- `phase_structure` (array of phase definitions with HP thresholds)
- `attack_set` (array of Attack objects)
- `telegraph_generosity` (relative scale)
- `arena_interaction` (none / static_hazard / dynamic_hazard / boss_becomes_arena)

### Attack (sub-object of Boss)
- `id`
- `name`
- `type` (basic / passive_aura / projectile / anti_kite / phase_special)
- `telegraph_time_seconds`
- `damage_value`
- `cooldown_seconds`
- `phase_active_in` (array of phase numbers)
- `foreshadowing_note` (does this attack preview a signature mechanic)

### EnemyCategory
- `id` (Fodder / Elite / Mini-boss)
- `hp_relative`
- `damage_relative`
- `speed_relative`
- `spawn_rate`
- `drop_table` (array of resource references with weights)

### EnemyType
- `id`
- `name`
- `category_id` (FK to EnemyCategory)
- `visual_ref`
- `biome_compatibility` (array of biome tags)

### Card
- `id`
- `name` (placeholder)
- `type` (technique / passive)
- `theme_id` (FK to Theme)
- `archetype` (Strike / Projectile / Orbital / Zone for techniques; Vitality / Utility / Offense / Special for passives)
- `body_part_variant` (Head / Arms / Legs / Body — and 4 advanced TBD)
- `variant_role` (foundation / support / damage / exotic — soft tag for design clarity)
- `base_effect_description`
- `per_level_scaling` (level 1 → 8 numeric tables — DEFERRED to tuning pass)
- `evolution_partner_id` (FK to Card; 1-to-1)
- `evolved_form_effect`
- `path_recipe_membership` (optional FK to PathTier — null if off-recipe)
- `unlock_source` (day-1 / boss_signature / region_objective / stage_breakthrough / etc.)
- `visual_ref`

### Theme
- `id` (Wood / Earth / Fire / Water / Metal / Wind / Ice / Lightning / Shadow / Spirit / Star / Void)
- `name`
- `era_intro` (era when this theme starts appearing meaningfully; the 8 elementals from R1, the 4 advanced from Transcendent)
- `sapling_effect_description`
- `sprout_effect_description` (DEFERRED)
- `grove_effect_description` (DEFERRED)
- `forest_effect_description` (DEFERRED)
- `worldroot_effect_description` (DEFERRED)
- `color_ref`
- `icon_ref`

### Specialty
- `id`
- `family` (building / theme)
- `name`
- `building_id` (FK, only for building specialties)
- `member_count_total` (e.g., Smith = 6, Heaven-Reader = 3)
- `rating_arc` (ordered list of [encounter_source, starting_rating] for each member in the chain)

### Archetype
- `id` (Strike / Projectile / Orbital / Zone / Vitality / Utility / Offense / Special)
- `card_type` (technique / passive)
- `pairing_partner` (FK to Archetype — Strike↔Vitality, Projectile↔Offense, Orbital↔Utility, Zone↔Special)
- `mechanic_family_description`

### BodyPartVariant
- `id` (Head / Arms / Legs / Body, plus 4 advanced TBD: Eyes / Hands / Feet / Heart?)
- `is_core` (boolean — Head/Arms/Legs/Body are core; advanced are not)
- `lore_flavor`
- `mechanic_flavor`

### EvolutionPair
- `id`
- `technique_id` (FK to Card)
- `passive_id` (FK to Card)
- `evolved_form_effect`
- `path_recipe_membership` (optional FK to PathTier)
- `discovery_state` (per-player: undiscovered / discovered)

### Path
- `id`
- `theme_id` (FK to Theme — except for Righteous Path, which is special)
- `is_capstone_path` (boolean — true for Righteous Path only)
- `tiers` (array of 5 PathTier objects: Sapling, Sprout, Grove, Forest, Worldroot)
- `discovery_state` (per-player, per tier)

### PathTier
- `id`
- `path_id`
- `tier_name` (Sapling / Sprout / Grove / Forest / Worldroot)
- `meridian_gate` (4 / 5 / 6 / 7 / 8)
- `loadout_size_required` (matches meridian gate doubled — 8 / 10 / 12 / 14 / 16)
- `layered_effect_description` (additive on top of previous tiers)
- `recipe_pairs` (array of EvolutionPair references)

### Building
- `id`
- `name`
- `master_specialty_id` (FK to Specialty — null for Main Hall and Personal Sanctum, which are head-only)
- `functions` (array of role descriptions — most buildings hold ~3)
- `tier_count` (working assumption 5–8; for Heaven-Reader-gated Ascension Pavilion likely up to 10 with jumps)
- `tiers` (array of BuildingTier objects)
- `unlocks_on_recruit_id` (FK to Boss — the building-trigger boss)

### BuildingTier
- `id`
- `building_id`
- `tier_number` (1, 2, 3, ...)
- `purchasable_when_recruited_id` (FK to Boss — Nth specialist in the chain whose recruitment unlocks this tier as purchasable)
- `cost_essence`
- `cost_materials` (array of { material_id, tier, quantity })
- `purchased` (per-player state, boolean)

### Disciple
- `id`
- `boss_id` (FK — the boss they used to be)
- `current_tier` (integer 1–12, trainable)
- `current_specialty_rating` (integer 1–10, trainable)
- `assignment` (region / building / training_hall_trainer / training_hall_student / unassigned)
- `assignment_target_id`
- `is_master_of_building_id` (optional FK to Building)

### CyclingTechnique
- `id` (8 total in game)
- `name`
- `meridian_requirement` (4–8)
- `cap_percent` (placeholder — bonus to head's qi gathering rate)
- `current_climb_percent` (per-player)
- `unlock_source` (specific stage breakthrough — in order)
- `visual_ref`

### Resource
- `id`
- `name`
- `tier` (1–12, integer — gates upgrade applicability)
- `theme_id` (optional FK to Theme — present on themed materials, null on generic)
- `source_descriptions` (idle output / Territory objective first-time / elite drops / etc.)

### Material (subtype of Resource)
- Inherits all Resource fields
- **All materials are themed.** 12 themes × 6 material tiers = 72 materials total
- Realm pairs share material tier: R1-R2=T1, R3-R4=T2, R5-R6=T3, R7-R8=T4, R9-R10=T5, R11-R12=T6
- `use_cases` — building upgrades + meridian refinement accept any theme at correct tier; forge theme-card upgrades require matching theme

### Essence (universal upgrade currency)
- `quantity` (per-player)
- Sources: from-play drops (VS-gold-style) + idle output from conquered regions + Survival objective first-time bonus
- Uses: all major progression sinks (building upgrades, forge upgrades, meridian refinements, library cycle upgrades base cost, leaf-level purchases within buildings)

### RawQi (personal cultivation pool)
- `quantity` (per-player, capped by qi pool size)
- Sources: enemy kills, idle from conquered regions, Kills objective first-time, cycling multiplier
- Uses: tier breakthroughs (within stages 1-3 and ongoing)

### SpiritStone (higher-tier currency)
- `quantity` (per-player)
- **NOT premium MTX** — gold→platinum tier, all earned through play
- Sources: boss defeats (5/map boss, 15/realm-final), rare idle drops, special-event recruit arrivals (gift bundles)
- Uses: generic recruitment at Recruitment Hall, cycle climb stones component, top-tier building upgrades (T5+), high-meridian refinement (8th especially), reroll/reset operations
- Rough tuning intuition: 1 stone ≈ 1,000 essence value (not interchangeable; for tuning sense only)

### Inspiration (gating resource)
- `quantity` (per-player)
- Sources: realm-final bosses (first-time defeat only)
- Uses: stage 4+ breakthroughs only
- Cannot be banked ahead (realm gating prevents access to higher-stage inspiration outside cultivation reach)

### CUT from earlier versions
- **MonsterCore** — fully removed. Was a fiddly intermediate ("kill drops core, core processes to qi"). Now kills drop raw qi directly.
- "Spirit Stones as universal currency" framing — replaced. Essence is the universal, Spirit Stones are tier-up.
- "Cycling boosters / time crystals" (v3-v5 language) — these ARE Spirit Stones; same mechanic, locked name.

---

## Key Relationships

- **Realm 1→N Map**
- **Map 1→6 Objective**; 1→1 Boss; 0..1→1 Building unlock; 0..1→1 themed Resource
- **Boss 1→1 Signature (Card)**; 1→1 Specialty; on-defeat-becomes 1→1 Disciple
- **Boss → Building tier unlock**: starting_rating of the Nth specialist = which tier they make purchasable
- **Card 1→1 Theme**; 1→1 Archetype; 1→1 BodyPartVariant; 1→1 Evolution Partner (another Card)
- **EvolutionPair 0..1→1 PathTier (recipe membership)**; 1→1 evolved-form effect
- **Path 1→5 PathTier**
- **PathTier 4..8→N EvolutionPair** (Sapling = 4 pairs; Worldroot = 8 pairs; additive)
- **Building 1→N BuildingTier**; 1→N Disciple (specialty-matched, defaulted home); 1 Master designation
- **Specialty 1→0..1 Building** (only building specialties)
- **EnemyCategory 1→N EnemyType**
- **Map N→N EnemyType (roster)**

---

## Schema Invariants

- **Every evolvable card has its evolution partner reachable through normal play.** The unlock web ensures no card is stranded as "evolvable in theory, partnerless in practice."
- **Pairing convention:** Strike↔Vitality, Projectile↔Offense, Orbital↔Utility, Zone↔Special. Pairings consistent across all themes. Body parts match within each pair.
- **Path culmination is all-or-nothing:** every loadout slot evolved AND every evolved pair is a recipe member for the targeted tier.
- **Building tier ceiling is gated by the Master's starting rating** (highest rated specialist in that family). Recruiting higher-rated specialist extends ceiling.
- **Specialist count drives visual building growth** independent of tier.
- **First-time objective rewards only.** Replays produce ambient drops only.
- **Resources are unified** — single tier-graded pool, all theme-tagged. 72 materials total (12 themes × 6 tiers).
- **Uniform reward type per objective:** Survival=Essence, Kills=Raw qi, Targets=mixed-theme materials, Territory=themed material cache, Resources=designated partner passive, Boss=tech+stones+(realm-finals only)inspiration.
- **Building tier cost pattern:** essence + materials at appropriate tier (+ spirit stones at T5+).

---

## Persistent State (Per-Player)

- Banked objectives (which maps' which objectives)
- Conquered regions (boolean per map)
- Recruited disciples (full roster snapshot)
- Building tiers purchased per building
- Building leaf-level purchases per tier per track
- Cards in pool (which day-1 + which unlocks acquired)
- Evolution pairs discovered
- Path tiers discovered (per theme × per tier)
- Codex state (entries unlocked)
- Cycling techniques learned and their climb %
- Current meridian count
- Current cultivation stage and tier-within-stage
- Resource inventories: essence, raw qi (capped), spirit stones, inspiration; materials per tier per theme
- Master designations per building
- Disciple assignments
- Paint % per region (persistent across runs)

---

## Schema Gaps Still Open

- Training Hall's "training rating does what at the building" — resolved via specialist amplification model (compounding rate formula), specific coefficient TBD
- Advanced theme body-part assignments (Shadow / Spirit / Star / Void day-1 cards)
- Sprout / Grove / Forest / Worldroot effect descriptions per theme
- Righteous Path recipe (8 R4–R11 realm-final signatures + 8 partner passives — specific cards, themes, effects)
- R12 capstone identity (theme, specialty, signature)
- T2-T5 leaf content for 6 non-Teahouse / non-Pavilion buildings
- Per-card per-level variance within archetype baselines
- Exotic gate distribution (post-prototype)
- 20 special-event recruit trigger values (placeholders only)
- 64 material names (8 of 72 named via prototype-spec)
