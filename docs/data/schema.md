# Data Schema

Format-agnostic entity/relationship model for the cultivation game. Built out during the prototype design pass. Engineering handoff target.

---

## Core Entities

### Realm
- `id` (R1–R12)
- `scope` (Province / Region / Kingdom / Empire / Continent / Sea / World / Sky / Heavens / Star / Galaxy / Universe)
- `era` (Mortal / Transcendent / Immortal / Divine / Eternal)
- `map_count` (R1=2 through R12=20, total 119)
- `stage_gate` (cultivation stage required to enter — FK to CultivationStage)
- `gateway_map_id` (which map the player enters first)
- `reward_multiplier` (R1=1×, R2=1.5×, R3=2×, R4+=2.4× per realm — used for objective rewards, enemy scaling, and ambient drop scaling per [systems/economy.md](../systems/economy.md))

### CultivationStage
- `id` (1–12, integer)
- `name` (placeholder per stage)
- `realm_id` (FK to Realm — 1:1 stage-to-realm mapping)
- `qi_pool_cap` (locked formula: `1000 × 2^(stage − 1)`. Stage 1 = 1,000; Stage 12 ≈ 2,048,000)
- `requires_inspiration` (boolean — true for stages 4+)
- `cycling_techniques_unlocked` (array of CyclingTechnique IDs — Cycle 1 unlocks at Stage 1 breakthrough, etc., one per stage)
- `tier_within_stage_count` (3 per stage — Stage 1 has T1/T2/T3 then breakthrough to Stage 2)

### Player
Persistent player state. Captures the locked R1 M1 minute 0 baselines plus all in-play modifiable attributes. Values below are baseline; modified at runtime by Teahouse buffs, passive cards, Forge upgrades, Path tier effects, cycling multipliers, and stage breakthroughs.

- `current_stage_id` (FK to CultivationStage)
- `current_tier_within_stage` (1–3)
- `current_meridian_count` (4–8 per the meridian refinement pacing in [pillars/cultivation.md](../pillars/cultivation.md))
- `atk` (base 10)
- `hp_max` (base 100)
- `move_speed` (base 100 units/sec; 1.0× baseline)
- `pickup_radius` (base 50)
- `paint_radius` (base 30)
- `hitbox_radius` (base 16)
- `defense` (base 0; +X from Teahouse Defense tracks)
- `hp_regen_per_sec` (base 0; +X from Vitality L4+ leaves)
- `iframes_seconds` (base 0.5 sec after taking damage)
- `crit_chance_percent` (base 0; +X from Offense leaves / Metal Sapling path effect)
- `crit_damage_multiplier` (base 1.5×; +X from Offense L4+)
- `attack_speed_global` (none — per-technique cooldowns only. Wind Sapling path effect adds a global atk speed buff.)
- `qi_pool_current` (capped by current_stage.qi_pool_cap)
- `qi_accumulation_rate_per_sec` (base 5/sec; modified by Library T1 amplifier, Pavilion T1 amplifier, cycling multiplier per economy.md formula)
- `current_level_in_run` (per run; resets at run start)
- `starter_loadout` (one player-chosen technique at L1; 3 empty tech slots + 4 empty passive slots — populated through draft)
- `loadout` (per-run state: 16 slots total at max meridians — 8 tech + 8 passive; each slot holds {card_id, level} or empty. Used by L8-filter rule and tech/passive weighting formula in CardDraft below.)
- `pinned_run_start_cards` (array of Card IDs — player's pinned favorites for the run-start card selection screen, per rewards.md Run-Start Screen UI Requirements)

### Map
- `id`
- `name` (placeholder for now)
- `realm_id`
- `position` (map / realm_final)
- `biome_description`
- `building_unlocked` (optional, FK to Building — only the 8 R1–R3 maps)
- `unlock_prerequisites` (array of map_ids; empty for gateway maps)
- `is_starting_map` (boolean)
- `enemy_roster` (derived view: EnemyRoster lookup by `realm_id` filtered by this map's `biome_description`. Authoring lives on EnemyRoster, not Map, per tranche 4 realm-pool model. EnemySlotConfig overrides slot-fire and active-enemies-per-minute.)
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
- `hp_absolute` (R1 M1 anchor: Lady Yun = 800. All other bosses back-solve from this anchor. Locked 2026-05-22.)
- `contact_damage_absolute` (R1 M1 anchor: Lady Yun = 8. Damage ratios vs Yun: Fodder 0.4×, Elite 0.8×, Mini-boss 1.2×, Boss 1.0×.)
- `ability_damage_absolute`
- `armor_percent`
- `movement_speed_vs_player` (1.0× = match player)
- `phase_structure` (array of phase definitions with HP thresholds)
- `attack_set` (array of Attack objects)
- `telegraph_generosity` (relative scale)
- `arena_interaction` (none / static_hazard / dynamic_hazard / boss_becomes_arena)
- `hp_within_run_scaling_exempt` (boolean — TRUE for all bosses. Boss HP is absolute at encounter, does NOT scale with spawn minute. Preserves skill signal. Locked 2026-05-22.)

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
- `hp_absolute` (R1 M1 minute 0: Fodder 8, Elite 100, Mini-boss 400. Locked 2026-05-22.)
- `contact_damage_absolute` (R1 M1: Fodder 3, Elite 6, Mini-boss 10. Damage ratios vs Yun's 8: 0.4× / 0.8× / 1.2×.)
- `speed_relative` (Fodder 0.5–0.9× player, Elite 0.4×, Mini-boss 0.5×)
- `spawn_rate_description` (Fodder continuous, Elite ~every 90s, Mini-boss 1/min past 10:00)
- `within_run_hp_scaling` (`HP(t) = base × 1.10^minute` — applies to all three enemy categories. Boss is exempt.)
- `realm_scaling_multiplier` (R1=1×, R2=1.5×, R3=2×, R4+=2.4× per realm. Applies to HP, damage, and ambient drop values 1:1.)
- `xp_gem_value` (Fodder 1, Elite 5, Mini-boss 20, Boss 100. Locked 2026-05-22.)
- `gem_persistence_seconds` (30)
- `ambient_drops` (per-category drop table; full specs in [systems/economy.md](../systems/economy.md) Currency Ambient Drops)

### EnemyType
- `id`
- `name`
- `category_id` (FK to EnemyCategory)
- `visual_ref`
- `biome_compatibility` (array of biome tags)

### Wave (default template entity)
The locked 26-minute prototype wave template. Authored once, instantiated per-map via EnemySlotConfig (slot-fire overrides) and the map's realm EnemyRoster (active enemy resolution). Grounded in VS Mad Forest wave data. Mechanics locked tranche 4 (2026-05-22). Full table in [pillars/run-loop.md](../pillars/run-loop.md) Wave Composition.

- `minute` (0–25, integer — wave index; one wave per in-game minute)
- `min_alive` (integer — base minimum alive cap at this wave. Per-realm density modifier `R1×1.0 / R2×1.5 / R3×2.0` multiplies this at runtime, hard-capped at the global 300 cap.)
- `spawn_interval_seconds` (float — spawn cadence at this minute; peaks at 0.1s late game)
- `active_enemies` (array of EnemyType references — fodder/elite types active in this minute's general spawn pool. Resolved per-map by intersecting the map's realm EnemyRoster with biome compatibility; EnemySlotConfig.active_enemies_per_minute may override.)
- `slot_elite` (boolean — does the template schedule an elite-slot fire this minute. 8 total `true` rows across the 26-row template.)
- `slot_miniboss` (boolean — does the template schedule a mini-boss-slot fire this minute. 4 total `true` rows across the 26-row template.)

### EnemyRoster (per-realm enemy pool)
Per-realm pool of enemies available for spawn within the realm's maps. Realm-pool authoring (not per-map) per [prototype/scope.md](../prototype/scope.md) Realm Enemy Rosters — VS / HoT convention of cross-stage reuse with light biome-specific swaps. Locked tranche 4 (2026-05-22).

- `realm_id` (FK to Realm — one EnemyRoster per realm)
- `fodder_pool` (array of EnemyType references — R1=5, R2=7, R3=8+1)
- `elite_pool` (array of EnemyType references — R1=3, R2=4, R3=4)
- `miniboss_pool` (array of EnemyType references — R1=2, R2=3, R3=3)
- `climbing_fodder_trio` (3 EnemyType references — the universal humanoid / ghost / beast convention reskinned per realm, per [CLAUDE.md](../../CLAUDE.md) Realm Roster Structure. R1 = Footpath Bandit / Stray Spirit / Wandering Mongrel.)

Prototype total across R1+R2+R3: 48 unique enemy designs + 8 bosses.

### EnemySlotConfig (per-map slot-fire authoring)
Per-map override layer on top of the default Wave template. Determines which template-scheduled elite/mini-boss slot rows actually fire on this map and which enemies fill them. Per-map slot-fire counts ramp R1 M1 (4 elites / 1 mini-boss) → R3 M3 (8 elites / 4 mini-bosses) per [prototype/scope.md](../prototype/scope.md) Per-Map Slot-Fire Counts. Locked tranche 4 (2026-05-22).

- `map_id` (FK to Map)
- `elite_slots_fired` (array of integers — which of the template's 8 elite-slot minutes fire on this map. R1 M1 fires 4 of 8; R3 M3 fires all 8.)
- `miniboss_slots_fired` (array of integers — which of the template's 4 mini-boss slot minutes fire on this map. R1 M1 fires 1 of 4; R3 M3 fires all 4.)
- `slot_enemy_assignments` (object mapping each fired slot occurrence → EnemyType ID, drawn from the map's realm `elite_pool` or `miniboss_pool` filtered by biome compatibility)
- `active_enemies_per_minute` (optional override array — per-minute active fodder/elite type lists for this map; defaults to realm roster filtered by biome if unspecified. Authored content per map flagged for the scaling math pass.)

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
- `max_level` (constant 8 — used by L8-filter rule in CardDraft below)

### CardDraft (per-event entity, instantiated each draft moment)
Captures the moment of decision. One instance per level-up or chest. Mechanics locked tranche 3 (2026-05-22).

- `id`
- `player_id` (FK to Player)
- `trigger` (level_up / chest_elite / chest_mini_boss / chest_objective_completion / chest_boss)
- `chest_size` (integer — always 3 for level_up; 3–7 for chests, derived from Storehouse T8 leaf level)
- `offered_card_ids` (array of Card references, length = chest_size)
- `conditional_slot_flags` (array of length chest_size; values: card / evolution_slot / path_culmination_slot — at most one of each conditional type per draft)
- `charges_spent_this_event` (object tracking { rerolls: int, banishes: int }; skip increments a separate counter and ends the event)
- `outcome` (taken_card_id / skipped / pending)
- `outcome_essence_awarded` (integer — populated on skip; 10 for level_up, `5 × chest_size` for chest)

**Filter and weighting rules** (per [pillars/run-loop.md](../pillars/run-loop.md) Level-Up Draft):

- **L8 filter:** Cards present in `Player.loadout` at level 8 are excluded from `offered_card_ids`. Once `loadout` is entirely at level 8 (all 16 slots at max meridians), level-ups skip the draft entirely and silently grant +1 Atk per level (the locked flex bonus from XP and Leveling).
- **Tech/passive weighting:** `weight_tech = (empty_tech_slots + 1) / (empty_tech_slots + empty_passive_slots + 2)`. Floor of 1 prevents zero-weight starvation when one slot side fills up. Applied to all `offered_card_ids` except conditional slots.
- **Filter fallback:** If the filtered pool can't fill `chest_size`, fall back to random empty-slot picks from the full unlocked pool. Rare edge case at endgame.
- **Conditional slot interaction:** Evolution and path culmination can coexist in the same chest. Path takes 1 slot, evolution takes 1 slot, remaining slots fill from filtered/weighted pool. The "one evolution slot per draft" rule prevents two evolutions, not one evolution + one path.
- **Card behavior on pick (VS convention):** Card not in `loadout` → enters first empty slot of matching type at level 1. Card already in `loadout` at level N → advances to level N+1. UX is identical in both cases.

### Storehouse_DraftChargeState (per-player per-run state)
Tracks reroll / skip / banish charge availability during a run. Reset at run start; not persistent across runs.

- `player_id`
- `current_run_id`
- `reroll_charges_total` (derived from `Storehouse.t4_reroll_track_leaves`: `3 + leaves`. T4 unlock = 3, T4 maxed = 13.)
- `reroll_charges_remaining` (integer, decrements on reroll)
- `skip_charges_total` (derived: `3 + Storehouse.t4_skip_track_leaves`)
- `skip_charges_remaining`
- `banish_charges_total` (derived: `3 + Storehouse.t4_banish_track_leaves`)
- `banish_charges_remaining`
- `banished_card_ids_this_run` (array of Card IDs excluded from this run's draft pool. Reset at run end — banish is this-run scope only, NOT global.)

**Reroll semantics:** 1 charge = full draft re-spin (all `offered_card_ids` regenerated). NOT pick-1-reroll. Conditional slot flags persist across reroll — banishing the evolved-card position is not how you opt out of evolution.

**Apprentices do NOT scale charges.** Apprentice compounding on Storehouse (`compound rate = base × (1 + Σ ratings × 0.10)`) feeds the offline-cap surface (T1) only. Charges are leaf-driven discrete integers — see [systems/building-tier-curves.md](../systems/building-tier-curves.md) Storehouse T4 Draft Charge Tracks.

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
- `template` (compounding / flat_cap / hybrid — per [systems/building-tier-curves.md](../systems/building-tier-curves.md) Templates)
- `tier_count` (working assumption 5–10; max 10 for Heaven-Reader-gated Pavilion)
- `tiers` (array of BuildingTier objects)
- `unlocks_on_recruit_id` (FK to Boss — the building-trigger boss)

### BuildingTier
- `id`
- `building_id`
- `tier_number` (1, 2, 3, ...)
- `surface_label` (T1/T4/T8 only — names which surface this tier opens, e.g., "Head's cultivation speed" for Library T1)
- `unlock_effect_description` (the locked unlock value — see [systems/building-tier-curves.md](../systems/building-tier-curves.md) Per-Building Unlock Values)
- `classification` (amplifier / generator / run_only / cap_extender / cost_reducer — per the composition rule in [systems/economy.md](../systems/economy.md))
- `purchasable_when_recruited_id` (FK to Boss — Nth specialist in the chain whose recruitment unlocks this tier as purchasable)
- `cost_essence`
- `cost_materials` (array of { material_id, tier, quantity })
- `cost_spirit_stones` (T5+ only)
- `purchased` (per-player state, boolean)
- `track_leaves` (array of LeafTrack sub-objects — at minimum used by Storehouse T4 charge tracks; generally applicable to all surfaces with sub-tracks)

### LeafTrack (sub-object of BuildingTier)
Used wherever a tier surface has multiple sub-tracks with independent leaf progression. Storehouse T4 has three (reroll / skip / banish). Other surfaces may have their own.

- `id`
- `building_tier_id`
- `track_name` (e.g., "reroll", "skip", "banish" for Storehouse T4; "cultivation_speed", "defense" etc. for Teahouse tracks)
- `max_leaves` (10 for Storehouse T4 charges; varies by track type elsewhere)
- `cost_curve_per_leaf` (array — per-leaf essence/material costs; flagged for scaling math pass for Storehouse T4)
- `current_leaves_purchased` (per-player state, 0 to max_leaves)
- `effect_per_leaf` (declarative: e.g., for Storehouse T4 reroll, "+1 reroll charge per run")
- `applies_compound_rate` (boolean — TRUE for most compounding surfaces; FALSE for Storehouse T4 charge tracks per the locked exception)

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
- `cap_percent` (per-cycle cap value — bonus to head's qi gathering rate when fully climbed. Specific values open per playtest.)
- `current_climb_percent` (per-player; newly-learned cycle starts at 30% of cap per [systems/building-tier-curves.md](../systems/building-tier-curves.md))
- `unlock_source` (specific stage breakthrough — in order)
- `visual_ref`
- `multiplier_formula` (additive across all learned cycles: `qi_gain_rate = base × (1 + Σ cycle_climb_%)`. Locked 2026-05-22.)

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
- **Ambient material drops are 100% region-themed** — off-theme variety only via Targets first-time reward (mixed materials). Locked 2026-05-22.

### Essence (universal upgrade currency)
- `quantity` (per-player)
- Sources: from-play drops (VS-gold-style: no fodder, elite 3, mini-boss 15, boss 50–100) + idle output from conquered regions + Survival objective first-time bonus + **draft skip rewards (tranche 3: 10 essence per level-up skip, `5 × chest_size` per chest skip)**
- Uses: all major progression sinks (building upgrades, forge upgrades, meridian refinements, library cycle upgrades base cost, leaf-level purchases within buildings, Pavilion T8 cycle climb)

### RawQi (personal cultivation pool)
- `quantity` (per-player, capped by `current_stage.qi_pool_cap`)
- Sources: enemy kills (fodder 1, elite 5, mini-boss 20, boss 100; pickup collapsed with XP gem), idle from conquered regions (~20/hr R1, ×2.4 per realm), Kills objective first-time, cycling multiplier
- Uses: tier breakthroughs (within stages 1-3 and ongoing)

### SpiritStone (higher-tier currency)
- `quantity` (per-player)
- **NOT premium MTX** — gold→platinum tier, all earned through play
- Sources: fodder drop 0.1% chance × 1; mini-boss guaranteed 1; map boss 5 first-time / 3 replay; realm-final boss 15 first-time; rare idle drops; special-event recruit arrivals (gift bundles)
- Uses: generic recruitment at Recruitment Hall, cycle climb stones component, top-tier building upgrades (T5+), high-meridian refinement (8th especially), reroll/reset operations
- Rough tuning intuition: 1 stone ≈ 1,000 essence value (not interchangeable; for tuning sense only)

### Inspiration (gating resource)
- `quantity` (per-player)
- Sources: realm-final bosses (first-time defeat only). NOT mini-bosses. NOT idle.
- Uses: stage 4+ breakthroughs only
- Cannot be banked ahead (realm gating prevents access to higher-stage inspiration outside cultivation reach)

### CUT from earlier versions
- **MonsterCore** — fully removed. Was a fiddly intermediate ("kill drops core, core processes to qi"). Now kills drop raw qi directly.
- "Spirit Stones as universal currency" framing — replaced. Essence is the universal, Spirit Stones are tier-up.
- "Cycling boosters / time crystals" (v3-v5 language) — these ARE Spirit Stones; same mechanic, locked name.
- "Mini-boss sometimes drops inspiration fragment" — stale text in older risk-map.md / cultivation.md / scope.md versions. Inspiration is realm-final-only. Corrected during 2026-05-21 audit and reaffirmed in tranche 1 lock.
- **Recruitment Hall T8 "qi yield"** — dropped 2026-05-22 (tranche 2). T8 surface is cost reduction only; the "qi yield" framing was brainstorm drift with no mechanism behind it (drift pattern #17).
- **Pick-1-reroll** — dropped 2026-05-22 (tranche 3). Reroll is full draft re-spin only. Pick-1 would effectively multiply the budget by chest size and break pacing.
- **Global banish** — dropped 2026-05-22 (tranche 3). Banish is this-run scope only. Global considered and rejected for simplicity and regret-prevention; build-tinkerers re-banish per run cheaply.
- **Apprentice scaling on Storehouse charges** — never adopted, explicitly excepted from compounding template. Compound rate exception called out in [systems/building-tier-curves.md](../systems/building-tier-curves.md).
- **Continuous-exponential-spawn-density-curve** — dropped 2026-05-22 (tranche 4). Initial proposal mid-session was a continuous exponential curve for spawn density. User pushed back: "look up how VS and HoT do it. Don't reinvent the wheel." VS is wave-based, one wave per minute, with non-monotonic per-minute authoring (Mad Forest wave table confirmed). Replaced with the locked 26-row wave template.
- **Per-enemy XP variance** — deferred 2026-05-22 (tranche 4). XP gem values are flat per category for the prototype (Fodder 1 / Elite 5 / Mini-boss 20 / Boss 100). Per-enemy-type variance desired long-term, not in scope for prototype.
- **Per-enemy damage variance** — deferred 2026-05-22 (tranche 4). Contact damage is flat per category for the prototype (Fodder 3 / Elite 6 / Mini-boss 10 / Boss 8 at R1 M1). Per-enemy-type variance desired long-term, not in scope for prototype.

---

## Key Relationships

- **Realm 1→1 CultivationStage** (one stage per realm, R1↔Stage 1, R12↔Stage 12)
- **CultivationStage 1→N CyclingTechnique unlock** (one cycle unlocks per stage breakthrough)
- **Realm 1→N Map**
- **Map 1→6 Objective**; 1→1 Boss; 0..1→1 Building unlock; 0..1→1 themed Resource
- **Boss 1→1 Signature (Card)**; 1→1 Specialty; on-defeat-becomes 1→1 Disciple
- **Boss → Building tier unlock**: starting_rating of the Nth specialist = which tier they make purchasable
- **Card 1→1 Theme**; 1→1 Archetype; 1→1 BodyPartVariant; 1→1 Evolution Partner (another Card)
- **EvolutionPair 0..1→1 PathTier (recipe membership)**; 1→1 evolved-form effect
- **Path 1→5 PathTier**
- **PathTier 4..8→N EvolutionPair** (Sapling = 4 pairs; Worldroot = 8 pairs; additive)
- **Building 1→N BuildingTier**; 1→N Disciple (specialty-matched, defaulted home); 1 Master designation
- **BuildingTier 1→1 classification** (amplifier / generator / run_only / cap_extender / cost_reducer)
- **BuildingTier 1→N LeafTrack** (Storehouse T4 has 3 leaf tracks; many other tier surfaces have leaf tracks too)
- **Specialty 1→0..1 Building** (only building specialties)
- **EnemyCategory 1→N EnemyType**
- **Map N→N EnemyType (roster)** — derived from Realm 1→1 EnemyRoster, filtered by Map.biome_description
- **Realm 1→1 EnemyRoster** (one roster per realm; one of R1=5/3/2, R2=7/4/3, R3=8/4/3 pool shapes)
- **EnemyRoster N→N EnemyType** (fodder_pool, elite_pool, miniboss_pool — each EnemyType belongs to exactly one pool slot within its realm)
- **Map 1→1 EnemySlotConfig** (per-map slot-fire authoring on top of the shared Wave template)
- **EnemySlotConfig N→N EnemyType** (slot_enemy_assignments draws from the map's realm EnemyRoster elite/miniboss pools, biome-filtered)
- **Wave (global template)** — 26 rows shared across all 8 prototype maps. Per-map instantiation applies EnemySlotConfig overrides + realm density modifier.
- **Player 1→1 CultivationStage** (current); 1→N CyclingTechnique (learned, with climb percentages)
- **Player 1→0..1 Storehouse_DraftChargeState** (one active per run; resets at run end)
- **CardDraft N→1 Player** (each draft event belongs to one player; many drafts per run)

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
- **Boss HP is absolute at encounter** — does NOT scale within run. Fodder/elite/mini-boss HP scales `× 1.10^minute`. (Locked 2026-05-22, drift pattern source: tranche 1 scaling exemption.)
- **Ambient drops are region-themed** for materials; fixed per kill (no within-run scaling). Realm scaling applies 1:1.
- **Qi pool cap is inherent to current cultivation stage**, not a tunable building surface. Formula `cap(stage) = 1000 × 2^(stage−1)`. (Locked 2026-05-22.)
- **Compounding building functions = three tier surfaces** (drift pattern #14): T1, T4, T8 surfaces match the three functions in [pillars/sect-management.md](../pillars/sect-management.md). Exceptions: Main Hall and Personal Sanctum are head-only buildings with no specialty chain, no tier scaling.
- **Card max level = 8.** L8 cards are filtered from draft offers. Once entire 16-slot loadout is at L8, level-ups silently grant +1 Atk each (flex bonus). (Locked tranche 3, 2026-05-22.)
- **Reroll = full draft re-spin only.** Pick-1-reroll explicitly cut. (Locked tranche 3.)
- **Banish scope = this-run only.** Global banish considered and rejected. (Locked tranche 3.)
- **Apprentice compounding does NOT apply to Storehouse draft charges.** Charges are leaf-driven discrete integers. Exception explicit in [systems/building-tier-curves.md](../systems/building-tier-curves.md). (Locked tranche 3.)
- **Evolution and path culmination can coexist in same chest.** Path takes 1 slot, evolution takes 1 slot, remaining slots from filtered pool. The "one evolution slot per draft" rule prevents two evolutions, not one evo + one path. (Locked tranche 3.)
- **Per-realm density modifier applies to wave `min_alive`, capped at global 300.** Modifier values: R1×1.0 / R2×1.5 / R3×2.0 (same factors as per-realm HP/damage scaling). Hard cap is the engine ceiling — new spawns suppressed at 300 alive regardless of `min_alive`. (Locked tranche 4, 2026-05-22.)
- **Wave activity continues unmodified during boss-alive period.** All scheduled elite/mini-boss slot fires for minutes during the boss fight execute as scheduled. Fodder waves continue. Layered tension is the design intent — boss is a target inside the ongoing wave, not 1v1 isolation. (Locked tranche 4, 2026-05-22.)
- **Bosses are arena-locked and do not despawn.** General aggro/pursuit rule is pure pursuit + off-screen despawn (>1000u, both conditions); bosses are exempt from despawn. (Locked tranche 4, 2026-05-22.)

---

## Persistent State (Per-Player)

Captured by the Player entity above, plus the following relational/inventory state:

- Banked objectives (which maps' which objectives)
- Conquered regions (boolean per map)
- Recruited disciples (full roster snapshot)
- Building tiers purchased per building
- Building leaf-level purchases per tier per track (LeafTrack.current_leaves_purchased)
- Cards in pool (which day-1 + which unlocks acquired)
- Evolution pairs discovered
- Path tiers discovered (per theme × per tier)
- Codex state (entries unlocked)
- Cycling techniques learned and their climb % (per CyclingTechnique.current_climb_percent)
- Resource inventories: essence, raw qi (capped by stage), spirit stones, inspiration; materials per tier per theme
- Master designations per building
- Disciple assignments
- Paint % per region (persistent across runs)
- Player baseline modifiers (Forge stacks per card, Teahouse leaf levels, Path culminations active)
- Pinned run-start cards (per rewards.md UI requirements)

---

## Schema Gaps Still Open

- Training Hall's "training rating does what at the building" — resolved via specialist amplification model (compounding rate formula), specific coefficient TBD
- Advanced theme body-part assignments (Shadow / Spirit / Star / Void day-1 cards)
- Sprout / Grove / Forest / Worldroot effect descriptions per theme
- Righteous Path recipe (8 R4–R11 realm-final signatures + 8 partner passives — specific cards, themes, effects)
- R12 capstone identity (theme, specialty, signature)
- T2-T5 leaf content for 6 non-Teahouse / non-Pavilion buildings (the per-leaf-level effect content within each surface; Storehouse T4 leaf tracks structurally locked but per-leaf cost curve open)
- Per-card per-level variance within archetype baselines
- Exotic gate distribution (post-prototype)
- 20 special-event recruit trigger values (placeholders only)
- 64 material names (8 of 72 named via prototype-spec)
- Cycle cap percentages per CyclingTechnique (placeholder; tuning pass)
- Per-leaf-level cost escalation factor within each surface (per-track cost curves, distinct from the inter-tier cost table) — Storehouse T4 reroll/skip/banish costs explicitly flagged for the scaling math pass
- Specific essence amounts for skip rewards (10 / 5×chest_size locked but flagged for playtest tuning)
- Tech/passive weighting +1/+2 floor formula values (shape locked, specifics flagged for playtest tuning)
