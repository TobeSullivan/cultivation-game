# Open Questions & Deferred Items

For locked design (currency model, building tier curves, partner passive distribution, per-map rewards, material model, etc.), see the design files under `docs/`.

---

## Open Questions Still Worth Resolving

### High-Priority — Blocking Polish

- **Scaling math pass.** Forge upgrade semantics are now locked (see [pillars/sect-management.md](pillars/sect-management.md) and [systems/building-tier-curves.md](systems/building-tier-curves.md)) but introduce another multiplicative stacking layer on top of Teahouse buffs, card draft level 1–8, Sect Power, and Path tier effects. Per-building T1/T4/T8 unlock values now locked too (tranche 2). Card draft mechanics + filter / weighting now locked too (tranche 3). Wave system + realm rosters now locked too (tranche 4). The full stack needs modeling and tuning before prototype tuning ships. Target curve: VS / Brotato / Halls of Torment tension in R1–R3 (player has to play well) climbing to dopamine-explosion power in R10–R12 (player has *earned* breaking the game). Better in spreadsheet than chat. **Next major session.** Spreadsheet items flagged across tranches: Cycle 1 L1 essence cost (1,000) and per-cycle ×1.5 escalation factor; per-cycle cap-percent values; per-leaf cost escalation within surfaces (including Storehouse T4 reroll/skip/banish track costs locked tranche 3 — structure done, costs TBD); tech/passive weighting +1/+2 floor specifics; skip-essence amounts (10 / 5×chest_size baseline); per-map wave content overrides per [scope.md](prototype/scope.md).

- **Boss-HP-doesn't-scale-within-run** — locked unilaterally in tranche 1 (2026-05-22). Flag for user confirmation. Rationale: speedrunner who pops boss at min 10 fights same Yun as slow player at min 25, but with less card growth. Skill signal preserved without `1.10^25 = ~10×` HP inflation feeling artificial.

- **Within-run ambient drops don't scale** — locked unilaterally in tranche 2 (2026-05-22) pending playtest confirmation. Drop values fixed per kill regardless of minute. Preserves early-game-feels-rewarding pacing. Revisit after first tuning pass if minute-25 feels low-yield.

- **Within-run HP scaling `HP(t) = base × 1.10^minute`** — locked tranche 1 but **genre-divergent** from VS Normal mode, which derives in-run difficulty entirely from wave content (enemy types, density) rather than a hidden per-minute multiplier. User noted (2026-05-22 tranche 4) "we have a different game shape, but in this slice it's very adjacent — might need to revisit." **Revisit after first playtest** — if the multiplicative `1.10^min × realm × Forge × Teahouse × card-level × Sect Power × Path` stack overshoots, this is the first lever to pull. If wave-density-only difficulty feels insufficient given our realm progression, keep as-is.

- **R12 chain capstone "evolution" effect.** Each chain's R12 boss (8 building + 12 theme) should do something special on defeat — an evolution-style payoff that marks the chain conclusion. Per-chain mechanic TBD. Distinct from the chain prerequisite (which gates recruitment) and exotic gating (which may layer on top per drift pattern #14 / locked decision). See [systems/boss-roster.md](systems/boss-roster.md) Chain Progression Rules.

- **Full title-ladder pass.** Define low / mid / R12-capstone title rungs across all 20 chains (8 building + 12 theme). Existing R1–R3 names that already sit mid-rung at rating 5 (*Master Pao*, *Magistrate Hong*) constrain their chains' capstone titles — narrative cover exists but the constraint is real and must be respected. See drift pattern #15 in [CLAUDE.md](../CLAUDE.md) and Chain Progression Rules in [systems/boss-roster.md](systems/boss-roster.md).

### Other Open

- **Per-boss exotic gate distribution.** Mechanic is locked (visible up-front, draw outcome, re-fight required) — what's open is which bosses get gates, how many, what kinds. Likely ~5-15% of non-critical-path map bosses.
- **Cycle cap values.** Placeholder %s in [pillars/cultivation.md](pillars/cultivation.md). Multiplier formula locked tranche 2 (`qi_gain_rate = base × (1 + Σ cycle_climb_%)`); per-cycle cap percent values open. Better in spreadsheet/playtest.
- **Trigger values for special-event recruits.** Placeholders only. Constraint (2026-05-21): triggers are deterministic (never RNG), not reputation-based (reputation isn't a mechanic in this game — listed as Sect Power thresholds in [systems/boss-roster.md](systems/boss-roster.md)), and not building-tier-tunable (you can't increase or decrease how often they appear via building upgrades — they're conditional events like exotic gates).
- **Path Sprout/Grove/Forest/Worldroot effect designs.** 48 effects to design eventually (12 themes × 4 tiers beyond Sapling). Pacing during development TBD. Each effect must also specify **what +10% Forge upgrade scales on it** (damage, radius, frequency, count, etc.) — newly required by the locked Forge path semantics.
- **Pairing convention universality.** Whether the Strike↔Vitality-style pairing convention is truly consistent across all 12 themes or whether some themes should deliberately break for variety.
- **Spirit stone exchange rate / sink list.** Rough 1 stone ≈ 1,000 essence locked, specific sinks TBD beyond locked ones (high-meridian refinement, T5+ building costs, generic recruitment, fodder 0.1% drop, mini-boss 1 guaranteed, boss 3–5, realm-final 15).

- **Painterly architecture vs flat-vector backdrop coexistence (NEW 2026-05-23 session 4).** Session 3 locked flat vector for buildings after Main Hall v1 came back flat. Session 4 user-chose v3 painterly (Studio Ghibli–register) which retired that lock. Backdrop layers (mountains, mist) remain flat vector. Current hub_test composites both styles. Three paths: (a) regenerate backdrop in painterly to match, (b) regenerate buildings in flat vector to match backdrop, (c) accept cross-style as intentional. **Deferred until 2–3 more buildings exist** — single building isn't enough surface to judge the full-scene cohesion vs jarring read. See [design-pass.md open questions](prototype/design-pass.md#open-questions-post-design-pass).

- **Head-only building tier states** — pre-existing discrepancy carried forward. Surface 5 specs "10 buildings × 2 visual stages = 20" but Art Inventory lists Main Hall + Personal Sanctum as single state each (= 18 total). Skyline architecture pivot didn't resolve. Main Hall v3 currently locked as single-state — decision pending on whether head-only buildings progress through tier visuals or stay static. Lower priority than the painterly coexistence question.

---

## Deferred for Later (Design Work, Not Open Questions)

- **Stage-tied new run mechanics**
- **Teahouse recipe specifics** — variety, exact buff slot counts (16 tracks locked, internal track contents open), brewing UX. Brew time confirmed not applicable: Teahouse buffs are persistent passive modifiers with instant track upgrades + instant specialist assignment (locked tranche 2).
- **Forge per-card tuning curves** — Forge semantics now locked at +10%/level structure; per-card / per-path *tuning* (which cards scale faster, which have steeper cost curves) is still open. Lives in scaling math pass and post-playtest.
- **Generic visualization** — open creative question
- **Material naming** — 8 prototype materials named; 64 remaining deferred
- **Total path count beyond Sapling** — 12 themes × 4 additional tiers = 48 layered effects
- **Per-specialty rating arc tables** — Smith was sketched in v4; Brewer / Trainer / Organizer / Charisma / Administrator / Scholar / Heaven-Reader all need full arcs spec'd (Heaven-Reader now known to be 4 members at 7→8→9→10)
- **Theme assignment for the post-prototype boss roster** (R4-R12)
- **The mid-game Heaven-Reader** — specific realm and signature technique (now constrained to ~R6, ~R9, R12 given 4-member arc starting at R3)
- **Specific region-objective passive unlocks for R4+**
- **Specific R5 and R9 region identities** for special-event recruit triggers
- **Signature technique mechanics for the 9 non-trigger realm-finals**
- **Building visual-growth art rubric** — art-direction-doc per-building rubric for T1/T4/T8 base-art evolution (system locked in [pillars/sect-management.md](pillars/sect-management.md) Visual Growth section; per-building art rubric still TBD)
- **R12 realm-final identity** — Universe-scope mastery boss; theme and specialty open
- **The 12 path Sprout effects** — first layered manifestation beyond Sapling
- **48 evolution effects** (each evolvable pair has a unique evolved technique form)
- **Per-card variance within archetype baselines** (archetype baselines are locked)
- **Naming pass on all 96 day-1 cards** — current names are placeholders
- **R11 and R12 design** — beyond "mastery realms," what specifically are they
- **NG+ ("Cultivation Rebirth")** — outlined as concept, not designed. Endgame consideration only.
- **R12 apex callback track** — Suno track for R12 apex moment that callbacks the title screen melody. Open: vocal language (constructed cultivation tongue vs Mandarin vs other), specific instrumentation, where exactly it triggers.
- **Evolution-eligibility rules per card** — which of the 96 day-1 cards have evolved forms, conditions to evolve, paired-passive requirements. Affects evolved card art count and Forge track structure. Card draft *mechanics* locked tranche 3, but per-card eligibility rules are content-authoring work.
- ~~**Hub building layout**~~ → **RESOLVED 2026-05-23 session 2** via the architecture pivot to front-facing skyline. Building placement is emergent per-building in Godot (horizontal x + depth-layer assignment), not pre-planned. hub_test scene session 4 validates the approach with the first locked building (Main Hall).
- **Mobile virtual button positioning** — VS-style fixed-position auto-fade locked as the model. Specific button placements / sizes / fade behavior TBD when mobile port becomes active scope.
- **Era-evolution art passes** — all prototype assets are Mortal-era. Transcendent/Immortal/Divine/Eternal era visual identities need passes for MC sprites, hub compound aesthetic, and (eventually) building art. Post-prototype.
- **Run-start screen UI layout** — requirements locked tranche 3 (theme tabs primary, archetype sub-filter, favorites pin, search box, card preview pane, <30sec browse target). Specific layout / animation / controller focus state / mobile touch targets deferred to prototype UI pass.
- **R12 void-aspected elite reuse (asset-saving idea, 2026-05-22 tranche 4).** Concept: R12 (Void realm, Eternal era) fields all elite mob types from R1–R11 as **void-aspected variants** — purple-glow shader treatment, "the Void has corrupted everything before" narrative thread. Saves a massive amount of asset production at the highest tier (no new elite designs for R12) and threads xianxia cosmology cleanly. Decision deferred but flagged for R12 design work. Implementation question: do void-aspected variants get stat boosts beyond R12 ×N scaling, or new mechanics, or just the shader?

---

## Build-Blocking for Prototype (Specific Remaining Work)

1. **T2-T5 leaf content** for 6 buildings: Recruitment / Training / Storehouse / Outer Court / Library / Forge (T1/T4/T8 unlock values locked tranche 2; per-leaf-level content within surfaces still open — Storehouse T4 charge-track structure locked tranche 3, per-leaf cost curves open)
2. **Per-map wave content overrides** — default wave template + per-map slot-fire counts + realm rosters locked tranche 4. Per-map authoring of *which specific enemies* appear in each minute's active-enemies list (vs the realm pool) deferred to per-map content pass alongside scaling math
3. **Per-card content for 96 day-1 cards** — individual effects and per-level values
4. **Pavilion cycle climb economy** — Cycle 1 baseline cost curve locked tranche 2; per-cycle ×1.5 escalation factor and cap-percent values flagged for scaling math pass
5. **Naming pass — partial.** R1–R3 bosses + 8 signature techniques + 8 partner passives + 8 region resources LOCKED via polish pass (2026-05-21). Still placeholder: 96 day-1 cards, post-prototype bosses (R4–R12), 64 remaining material names. Full title-ladder pass deferred — see high-priority section above.

Items 2-4 are largely content-authoring better suited to spreadsheet work than chat-based design sessions.

---

## Resolved 2026-05-23 Session 4 (Claude Code Kickoff)

For reference; do not re-open without new information.

- **Godot project bootstrap** → Done. `game/` directory created with `project.godot` (viewport 1920×1080, GL Compatibility renderer, smooth texture filter), `scenes/`, `scripts/`, `assets/` (mirrored from repo root for res:// import), `resources/`, `data/`. Project loads without errors, runs in editor and headless mode.

- **hub_test scene composite** → Validated. Front-facing skyline composition assembles correctly at 1920×1080. Layer stack: gradient sky / mountains (y=350 scaled 1.43×) / mist (3 sprites programmatic radial gradient with normal alpha blend, drifting 4/6/9 px/sec) / grey ground (y=935–1080 slate) / black horizon platform (y=895–935, 40px) / Main Hall v3 (centered, 0.45× scale, bottom flush with platform) / CrowdFG (18 silhouettes scattered y=1020–1045, scales 0.08–0.14, bob/shuffle one-at-a-time on 1.5–5s random interval).

- **Reusable scene scripts written** → `drift.gd` (horizontal-drift component with wrap, used by mist; also tunable for future cloud / parallax sprites). `crowd_bob.gd` (sparse bob controller, asymmetric 1.2s/1.0s SINE ease-in-out tween, 5px amplitude, one figure per pick). `screenshot_and_quit.gd` (dev utility for headless renders, supports `repo://` scheme to land outputs in repo root).

- **Clouds asset state corrected** → `assets/hub/clouds.png` was discovered to have a solid white opaque background (not the baked checkerboard documented in session 2). Keyed in session 4 via existing key script (white pixels pass the desaturated + bright selector identically to checkerboard pixels). Now true RGBA. 8 individual cloud forms extracted to `assets/hub/clouds/cloud_NN.png` via new `tools/extract_cloud_pieces.py` (scipy connected-components labeling). Currently unused in hub_test — single-cloud-sprite drift exposed sparse coverage; user opted to defer clouds until better individual-cloud asset variety lands.

- **9 crowd silhouettes keyed** → All passed through `tools/key_out_checkerboard.py`. Dimensions vary 429–790 wide × 716–768 tall. Bbox-cropped to figure. In game in `game/assets/hub/crowd/`. Each used twice in hub_test composition (half horizontally flipped via negative scale.x for variation, 18 total figures).

- **Main Hall locked v3 painterly** → Replaces both v1 navy roof (locked session 3) and v2 warm olive (interim session 4). Painterly Studio Ghibli–register, includes baked bonsai tree and stone shrine. Keyed and in game at `assets/buildings/main_hall.png` (1327×613). v1 + v2 preserved as versioned files for reference. Style coexistence with flat-vector backdrop is now open (see Other Open).

- **Cook-before-code rule established** → Memory file at `memory/feedback_cook_before_code.md`. Project-specific rule: propose plan and wait for explicit approval before any Edit/Write/Bash that mutates state. Established mid-session after a cluster of unilateral iterations on hub_test composition burned through tokens.

- **Python toolchain set up** → Python 3.12.10 installed via winget. `pip install Pillow numpy scipy` complete. `tools/key_out_checkerboard.py` (existing) + `tools/extract_cloud_pieces.py` (new this session) both runnable.

---

## Resolved 2026-05-22 (Gap-Closing Tranche 4)

For reference; do not re-open without new information.

- **Spawn density curve shape** → Resolved. Wave-based system, one wave per in-game minute, VS / HoT convention. Each wave specs `min_alive` + `spawn_interval` + active enemy types + optional slot enemy. Default wave template locked (R1 M1 baseline, 25-min run). Non-monotonic — breather waves punctuate the climb. Numbers grounded in VS Mad Forest wave data. Locked in [pillars/run-loop.md](pillars/run-loop.md) Wave Composition section.

- **Global enemy alive cap** → Resolved. 300 enemies on screen at once. Engine ceiling per VS convention. Frame-rate driver — past ~300, lag and frame-drops degrade play quality. Locked in [pillars/run-loop.md](pillars/run-loop.md).

- **Per-realm density modifier** → Resolved. R1 ×1.0 / R2 ×1.5 / R3 ×2.0 / R4+ scales with realm. Modifier applied to wave `min_alive`, result capped at 300 (so R3 saturates the alive cap earlier in the run than R1). Same factors as HP/dmg per-realm scaling locked tranche 1.

- **Elite / mini-boss slot timing** → Resolved. Slots are scripted per-minute in the wave template (8 elite slots, 4 mini-boss slots). Per-map authoring picks which slots fire — gentle maps fire few, realm-finals fire most. Per-map slot-fire table locked across all 8 prototype maps. Locked in [prototype/scope.md](prototype/scope.md) Per-Map Slot-Fire Counts.

- **Per-enemy XP variance within category** → Resolved (flat). For prototype, every fodder = 1 gem, every elite = 5, every mini-boss = 20, every boss = 100. Per-enemy variance desired long-term, deferred to behavior-quirks pass per [scope.md](prototype/scope.md).

- **Per-enemy damage variance within category** → Resolved (flat). Same locks as XP — flat per category for prototype, per-enemy flavor desired long-term, deferred to behavior-quirks pass.

- **Aggro / pursuit logic** → Resolved. Pure pursuit (enemies path directly at player at assigned speed, no wander / no aggro range / no biome behavior). Off-screen + >1000 units → despawn (matches VS). Bosses arena-locked, do not despawn. Per-enemy-type behavior quirks (ranged attacks, charges, pack tactics, summons) explicitly deferred. Locked in [pillars/run-loop.md](pillars/run-loop.md) Aggro / Pursuit section.

- **Boss-fight spawn behavior** → Resolved. **All wave activity continues during boss fight** — fodder, elite slots, mini-boss slots all fire as scheduled while boss is alive. Boss is a target inside the ongoing wave, not a 1v1 isolation. Design intent: layered tension. Speedrunner who pops boss early trades chest loot for time; slow player fights through every slot they didn't bank. Locked in [pillars/run-loop.md](pillars/run-loop.md) Boss-Fight Spawn Behavior section.

- **Per-map fodder / elite / mini-boss rosters** → Resolved per realm, not per map. Realm-pool structure with biome-specific swaps mirrors VS / HoT genre convention (138 normal + 58 boss enemies across 54 stages with heavy cross-stage reuse). Bosses stay 1-per-map (119 unique across full game, 8 in prototype). R1 roster = 5 fodder + 3 elites + 2 mini-bosses. R2 roster = 7 fodder + 4 elites + 3 mini-bosses. R3 roster = 8+1 fodder + 4 elites + 3 mini-bosses. Prototype total: 48 unique enemy designs across 8 maps + 8 bosses. Universal climbing-fodder convention: humanoid/ghost/beast trio reskins per realm (Footpath Bandit → Hill Bandit → Rogue Apprentice; Stray Spirit → Frontier Shade → Wandering Shade; Wandering Mongrel → Plains Stalker → Beast-Spirit). Locked in [prototype/scope.md](prototype/scope.md) Realm Enemy Rosters section.

- **Schema housekeeping from tranche 4** → **Deferred to next session opening.** Schema.md was not in context this session — additions for Wave entity, EnemyRoster entity, EnemySlotConfig entity, Boss-fight wave continuity invariant, per-realm density modifier on min_alive invariant, and CUT list addition (continuous-exponential-spawn-curve, per-enemy-XP-variance, per-enemy-damage-variance) are first housekeeping task of next session.

---

## Resolved Previous Sessions (Reference)

### Gap-Closing Tranche 3 (2026-05-22)

- **Card draft Storehouse-charge values** → Resolved. Three independent leaf tracks at Storehouse T4 (reroll / skip / banish), 10 leaves each. T4 unlock = 3/3/3 charges per run. Each leaf adds +1 charge to its track. T4 maxed = 13/13/13. Charges do NOT scale with apprentice ratings — apprentice compounding feeds offline cap only (compounding-template exception explicit in [systems/building-tier-curves.md](systems/building-tier-curves.md)). Locked across [pillars/run-loop.md](pillars/run-loop.md), [systems/building-tier-curves.md](systems/building-tier-curves.md), and [data/schema.md](data/schema.md).

- **Reroll scope** → Resolved. Re-spins entire offer. 1 charge = full draft re-spin (3 cards for level-up, 3–7 for chest). VS / HoT / Brotato convention. Pick-1-reroll explicitly cut — would multiply effective budget by chest size and break pacing. Added to schema.md CUT list.

- **Banish scope** → Resolved. This-run scope only. Card removed from this run's draft pool, returns on next run. Global banish considered and rejected for simplicity and regret-prevention (13+ banish charges × many runs would chew up the 444-card pool with permanent exclusions and require a meta-unban system to be sane). Build-tinkerers re-banish per run cheaply. Added to schema.md CUT list.

- **Skip rewards** → Resolved. Small essence cache scaled to draft size. Level-up draft (3 cards): 10 essence. Chest draft (3–7 cards): `5 × chest_size` essence. Flavor: the Storehouse keeper redirects unused resources. Charge cap prevents skip-everything farming.

- **Conditional-slot interaction (evolution + path culmination in same chest)** → Resolved. Both can coexist. Path takes 1 chest slot, evolution takes 1 chest slot, remaining slots fill from filtered/weighted pool. The "one evolution slot per draft" rule prevents two evolutions, not one evolution + one path. Locked in [pillars/run-loop.md](pillars/run-loop.md) Conditional-Slot Interaction subsection.

- **Path culmination slot occupancy** → Resolved. Occupies 1 chest slot, not a bonus +1. Same visual treatment as evolution (distinct frame, "PATH" tag). Player chooses culmination or one of the other offers in the chest.

- **Already-maxed card draft behavior** → Resolved. L8 cards are filtered from draft offers. Once a card reaches max level, it stops appearing in level-up drafts and chests. Once entire 16-slot loadout is at L8 (8 tech + 8 passive at max meridians), level-ups silently grant +1 Atk each (no draft UI — the flex bonus from XP and Leveling). Filter fallback for the rare edge case where filtered pool can't fill draft: random empty-slot picks from full pool.

- **Tech-vs-passive draft weighting** → Resolved. Weighted toward empty slots with a floor of 1: `weight_tech = (empty_tech + 1) / (empty_tech + empty_passive + 2)`. Starter loadout (3 empty tech / 4 empty passive): ~44% tech / ~56% passive. Once all slots filled, pure 50/50 between tech and passive level-ups. Prevents the bad-pacing case of 3 passives offered when player has 3 empty tech slots.

- **Chest contents level (mirror VS)** → Resolved. Cards behave identically whether new pickup or level-up. Card not in loadout → enters first empty slot of matching type at L1. Card already at LN → goes to L(N+1). UX is identical in both cases; player doesn't track "new vs level-up" — card just progresses. UI shows current level on the card face.

- **Run-start screen UI for 444-card endgame pool** → Resolved (requirements locked, layout deferred). Primary filter: theme (12 tabs). Secondary filter: archetype (8 sub-tabs). Favorites pin row. Search box. Card preview pane (L1 stats, evolution partner if discovered, paths card belongs to, Forge level if any). Browse-to-pick target <30 sec at endgame. Most-recent run-start pick preselected. Locked / undiscovered cards not shown. Layout / animation / controller focus / mobile touch targets deferred to prototype UI pass. Locked in [prototype/rewards.md](prototype/rewards.md) Run-Start Screen UI Requirements section.

- **Schema housekeeping from tranche 3** → Done in tranche 3 wrap. Added CardDraft entity (per-event draft instance with offered cards, conditional slot flags, charges spent, outcome). Added Storehouse_DraftChargeState entity (per-run charge availability, banished cards this run). Added LeafTrack sub-object on BuildingTier (generic, used by Storehouse T4 charges and other multi-track surfaces). Extended Player entity with `loadout` (per-run 16-slot state) and `pinned_run_start_cards` fields. Extended Card entity with `max_level` constant (8). Updated Schema Invariants with five new tranche-3 invariants. Updated CUT list with pick-1-reroll, global banish, and apprentice-charge-scaling cuts. Updated Schema Gaps Still Open with the open per-leaf cost curves and tech/passive weighting playtest items.

### Gap-Closing Tranche 2 (2026-05-22)

- **Currency ambient drops** → Resolved. Per-kill drop table locked for R1 M1 minute 0 (Fodder 1 XP/1 qi/0.1% stone, Elite 5/5/3 essence/1 themed mat, Mini-boss 20/20/15 essence/1 stone/3 mats, Boss replay 100/100/50 essence/3 stones/5 mats). XP gem and raw qi collapse into single pickup. Essence is VS-gold-style (no fodder drop). Materials are 100% region-themed for ambient. Per-realm scaling matches enemy scaling (1× / 1.5× / 2× / 2.4× per realm). Within-run ambient scaling: none (locked pending playtest). Cycling multiplier formula: `qi_gain = base × (1 + Σ cycle_climb_%)`. Locked in [systems/economy.md](systems/economy.md).

- **Per-building idle base rates** → Resolved. T1/T4/T8 unlock values locked for all 8 buildings. Library T1 = +10% head qi accumulation; Recruitment T1 = 1 generic per 4hrs; Storehouse T1 = offline cap 12h→24h; etc. Amplifier vs Generator classification locked: Library/Outer Court/Pavilion amplify region streams; Recruitment T1 / Library T8 generate new streams. Composition rule locked: `inbox_per_hour_R = ((region_R_base × Π(amplifier_mults)) + Σ(generator_outputs_R)) × (1 + sqrt(SP/100))`. Storehouse offline cap progression locked from 12h base to 14d at T8 maxed. Pavilion T8 cycle climb economy locked: 10 leaf levels per cycle, Cycle 1 cost curve from 1K to 640K essence, per-cycle ×1.5 escalation flagged for scaling math pass. Locked in [systems/building-tier-curves.md](systems/building-tier-curves.md).

- **Teahouse brew time** → Confirmed not applicable. Teahouse buffs are persistent passive modifiers; track upgrades instant on purchase, specialist assignment instant. Universal mechanic for flat-cap template. Locked in [systems/building-tier-curves.md](systems/building-tier-curves.md) Teahouse Brew Mechanics.

- **Recruitment Hall T8 "Cost reduction / qi yield"** → Drift pattern #17 resolved. "Qi yield" framing was brainstorm-era content with no mechanism behind it. T8 surface is cost reduction only (−10% at unlock, leaves climb to −40%). "Qi yield" dropped from per-building tier surface table in [systems/building-tier-curves.md](systems/building-tier-curves.md) and added to schema.md CUT list.

- **Mini-boss inspiration drop stale text** → Cleaned from risk-map.md. Already cleaned in scope.md and cultivation.md during 2026-05-21 audit; risk-map.md had the same stale text that survived the audit pass. Inspiration is realm-final-only — locked invariant.

- **Risk-map.md HP-relative drift** → Cleaned. Enemy Categories table updated with absolute HP values (Fodder 8, Elite 100, Mini-boss 400, Boss 800) and the within-run scaling exemption note for bosses. Mirrors the scope.md fix from tranche 1.

- **Schema housekeeping from tranche 1** → Done. Added Player entity with all locked baseline fields, CultivationStage entity with `qi_pool_cap = 1000 × 2^(stage−1)` formula, EnemyCategory now has `hp_absolute` / `contact_damage_absolute` / `within_run_hp_scaling` / `xp_gem_value` / `realm_scaling_multiplier` / `ambient_drops` fields. BuildingTier gained `surface_label` / `unlock_effect_description` / `classification` / `cost_spirit_stones` fields. Boss gained `hp_absolute` / `contact_damage_absolute` / `hp_within_run_scaling_exempt`. CyclingTechnique gained `multiplier_formula`.

### Gap-Closing Tranche 1 (2026-05-22)

- **Player baselines** → Locked. R1 M1 minute 0: Atk 10, HP 100, move speed 100 u/s, pickup 50, paint 30, hitbox 16, defense 0, regen 0, iframes 0.5s, crit 0%/1.5×, attack speed none global, qi pool cap 1000, qi accum 5/sec. Starter loadout 1 player-chosen tech at L1. XP curve placeholder `floor(5 × 1.12^(n−1))`. Gem values 1/5/20/100, 30-sec persistence. No hard level cap; +1 Atk per level past all-slots-L8.

- **Boss baseline absolute anchor** → Locked. Lady Yun (R1 M1) = 800 HP, 8 contact dmg. All 8 prototype bosses back-solve from this. Enemy absolute baselines: Fodder 8/3, Elite 100/6, Mini-boss 400/10. Damage ratios vs Yun's 8: 0.4× / 0.8× / 1.2× / 1.0×.

- **Within-run scaling exemption** → Locked. `HP(t) = base × 1.10^minute` applies to fodder/elite/mini-boss only. Boss HP absolute at encounter. Preserves speedrunner skill signal.

- **Qi pool cap home** → Locked. Cap is inherent to current cultivation stage, NOT a tunable building surface. Formula `cap(stage) = 1,000 × 2^(stage−1)`. Stage 1 = 1,000; Stage 12 ≈ 2,048,000. Doubling matches AdCap idle output growth (~2.4× per realm). Confirmed by prior user statement (2026-05-11): "If you hit your cap you cycle. If you cycle three times you progress."

### Earlier session (open-question sweep, 2026-05-21)

- **Re-fight vs auto-unlock for late-completed boss recruits** → Resolved via exotic recruit gate mechanic. Map completion requires boss defeat (boss is objective #6). Exotic-gated bosses that defeat the player but escape (draw outcome) require re-fight after gate is satisfied. Locked in [pillars/risk-map.md](pillars/risk-map.md).
- **Skip / reroll / banish housed in Storehouse vs Library** → Locked Storehouse. Already correct in sect-management.md.
- **Meridian refinement material identities** → Locked: any-theme materials at the realm's tier. Spirit stones gate 7th+. Quantities deferred. Table in [pillars/cultivation.md](pillars/cultivation.md).
- **Apprentice contribution coefficient** → Locked 0.10 for compounding buildings, with per-building tuning caveat. Flat-cap buildings have no apprentice term. Locked in [pillars/sect-management.md](pillars/sect-management.md).
- **Heaven-Reader arc 3 vs 4 members** → Locked 4 members, 7→8→9→10, Pavilion T1–T10. Locked in [pillars/sect-management.md](pillars/sect-management.md) and [systems/building-tier-curves.md](systems/building-tier-curves.md).
- **Cycle upgrades location** → Locked at Pavilion T8 (flat-cap surface), NOT Library.

### Later session (Forge + Library joint, 2026-05-21)

- **Library three-surface reconciliation** → Resolved. Library's three functions ARE its three tier surfaces — (a) head's cultivation speed (T1), (b) region material drop rate (T4), (c) generic disciple qi rate sect-wide (T8). Path Codex is a UI feature that lives at Library, not a tier-scaling function. General rule (drift pattern #14): compounding building functions = three tier surfaces.
- **Evolution model** → Resolved. VS-style: technique transforms into evolved form (occupies same technique slot); paired passive persists unchanged in its passive slot. Not "consumed or fused."
- **Forge upgrade semantics** → Resolved across all three tracks (Techniques T1, Passives T4, Paths T8). See [systems/building-tier-curves.md](systems/building-tier-curves.md).
- **Scaling math interaction** → Flagged as high-priority open question (above).

### Latest session (R1–R3 polish + design pass scoping, 2026-05-21)

- **Mei naming collisions** → Resolved. *Edict of Many Blades* → *Ledger of Many Blades*; region resource *sealed scrolls* → *brass tablets*.
- **Title-ladder principle** → Locked as drift pattern #15. *Forge-Lord Tian* → *Smith Tian*; *Sergeant Bao* → *Warden Bao*.
- **Chain prerequisite** → Locked as separate rule from exotic gates.
- **Exotic-gate clarification** → Refined. R12 building-chain capstones MAY be exotic-gated *in addition to* the chain prereq.
- **R12 chain capstone "evolution" effect** → Flagged as high-priority open question.
- **Full title-ladder pass** → Flagged as high-priority open question.
- **Prototype scope expanded in writing** → Includes shippable opening flow + per-surface art + audio assets.
- **Pre-code sequencing locked** → design pass → audit pass → gap-closing → scaling math → Claude Code kick-off.

### Audit Pass session (2026-05-21)

Audit-pass session covering scope.md / tech-stack.md / run-loop.md / schema.md plus supplementary deep-read of bosses.md / building-tier-curves.md / economy.md / sect-management.md / rewards.md / risk-map.md / cultivation.md / unlock-web.md / boss-roster.md / path-system.md.

Audit pass deliverable (gap list) added to High-Priority — now mostly resolved via tranches 1 + 2 + 3. Additional drift surfaced during audit was resolved that session:

- **Compounding-building three-functions drift** → Resolved. Aligned Recruitment / Training / Outer Court / Pavilion to match building-tier-curves.md T1/T4/T8 surfaces.
- **Reputation/Influence as a concept** → Cut. No sink, no mechanic. Cleaned from risk-map.md (item 7), sect-management.md (Outer Court row), boss-roster.md (renamed to "Sect Power thresholds").
- **Monster cores stale references** → Cleaned in scope.md and cultivation.md.
- **Inspiration source contradictions** → Resolved. Realm-final-only is canonical. (Risk-map.md still had stale text — cleaned in tranche 2.)
- **unlock-web.md cultivation source entries** → Cleaned.
- **Drift pattern #17 added** → Exploratory framings drift into locked status during long brainstorm sessions.
