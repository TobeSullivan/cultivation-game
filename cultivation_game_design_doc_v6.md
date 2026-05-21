# Cultivation Game — Design Doc (v6)

A premium idle-survivor cultivation game. Vampire Survivors as the core active loop, with Adventure Capitalist (idle), Risk (territorial conquest), and sect management layered on top. No compromise on depth in any of the four pillars; everything funnels through the VS run loop because that's the only thing the player actually plays.

---

## Version Notes (v6)

v6 consolidates v3/v4/v5/v5.1 into a single source of truth. Specific v6 locks added on top of v5:

1. **Body parts as variant axis.** Cards have a body-part variant tag (Head/Arms/Legs/Body + advanced). Pairing convention extends — pairs share body part. Day-1 pool architecture: 8 cards per theme = 4 archetype-paired cards × 4 core body-part variants, with each theme weighted toward 2 variants out of the 4.
2. **Building tier mechanic clarified.** Master's starting rating IS the tier ceiling for that building. Recruiting a higher-rated specialist extends the ceiling. Tier count per building = max rating achievable in that specialty's arc (typically T1-T10; Heaven-Reader short-arc = T1-T7 to T1-T10 depending on arc length). Specialist count drives visual building growth independent of tier.
3. **Unified materials economy.** Single tier-graded pool, optionally theme-tagged. 12 themes × 6 material tiers = 72 materials total. Realm pairs share material tier (R1-R2=T1, R3-R4=T2, ..., R11-R12=T6). No separate building vs card material pools.
4. **Righteous Path = 13th path.** Capstone path combining all 12. Recipe: 8 specific evolution pairs sourced from R4-R11 realm-final signatures + their evo-partner passives. Discoverable only in infinite/endgame mode after R12 conquered. R12 realm-final = the capstone fight; final boss tier resolved.
5. **Currency model (4 + materials).** Qi (personal cultivation pool, tier breakthroughs), Essence (universal upgrade currency), Spirit Stones (higher-tier currency — gold→platinum, not premium MTX — for high-impact sinks), Inspiration (Stage 4+ gating). Plus Materials. Monster Cores cut.
6. **Building Tier Curves locked.** Two templates: Compounding (3 surfaces unlock at T1/T4/T8) and Flat-cap-by-tier. See Building Tier Curves section.
7. **Boss combat profile schema** added: HP scaling, contact dmg, ability dmg, armor%, speed vs player, phase structure, attack set, telegraph generosity, arena interaction.
8. **Map adjacency pattern.** R1 linear (2 maps), R2/R3 gateway + branch + final (3 maps each).
9. **Enemy categories.** Fodder (HP 0.05, dmg 0.4, speed 0.5-0.9× player), Elite (HP 0.5, dmg 0.8, every ~90s), Mini-boss (HP 1.2, dmg 1.0, past 10min). Per-realm: R2=1.5×, R3=2×.
10. **Partner passive distribution locked** for 8 prototype maps (forward-shift derangement — see prototype-spec.md).
11. **Per-map reward quantities locked** for 8 prototype maps (formulas + per-map values — see prototype-spec.md).
12. **Uniform reward type per objective.** Survival=Essence, Kills=Raw qi, Targets=mixed materials bundle, Territory=themed material cache, Resources=designated partner passive, Boss=signature + recruit + spirit stones + (realm-finals only) inspiration shard.
13. **Sect Power multiplier formula** locked at sub-linear sqrt: `multiplier = 1 + sqrt(Sect_Power / 100)`. Matches AdCap/Cookie Clicker/NGU Idle case study patterns; tames late-game runaway.

---

## High-Level Vision

- **Genre:** idle-survivor / cultivation power fantasy
- **Inspiration:** Vampire Survivors + Adventure Capitalist + Risk + sect-management games. Saplings borrow from VS, Brotato, Halls of Torment, ARPGs.
- **Cultivation flavor:** Cradle (Will Wight) for progression-ladder shape; Infinite Realm (Ivan Kal) for cultivation-specific mechanics (qi, cycling, tiers, paths). Generic xianxia/wuxia naming throughout — no IP infringement.
- **Tone:** never hard. Power fantasy. Defeat (not death) is part of the cycle. Players are never punished, always accommodated.
- **Scope:** hundreds of hours of content. Achievement-web depth.
- **Pricing:** premium. $5–$10. Pay once, get everything. No microtransactions, no ads, no F2P dark patterns.
- **Platforms:** PC first, with Steam Deck and consoles as first-class citizens (not afterthoughts). Mobile considered later as a thoughtful port, not the source.
- **Story:** minor but present. Frame and flavor. Designed after core systems are locked.
- **Endgame:** infinite/leaderboard mode is on the roadmap, TBD.
- **Player character:** one. The sect head. Singular protagonist throughout the entire game.

---

## Core Design Principles

1. **VS run is the only verb.** Every other system feeds into or out of the run loop.
2. **Every run unlocks something new.** Achievement-web philosophy — kills, survival, drops, milestones all feed the unlock web.
3. **Defeat is part of the cycle.** No game-over screens. Failed runs still bank progress.
4. **Player agency over grind.** If a player replays a region, it's their choice; the game doesn't second-guess them.
5. **Conquered territory is permanent.** The game never pulls players back to maintain what they've earned.
6. **Selection-based UI, not hover.** Steam Deck and console first. Persistent detail panels.
7. **Pause-friendly everywhere.** The game waits for the player.
8. **Premium respect.** No engagement traps, no FOMO timers, no daily login anxiety.
9. **Maintainability.** The game must never feel overwhelming. Progressive disclosure throughout. Notifications are rare and obvious, never spammy. No notification badges. No upkeep, no decay. New systems unlock when the player is ready.
10. **One decision at a time.** When the player engages manually with a system, the screen presents one thing to think about, not a wall of sliders.
11. **All unlocks visible, surfacing weighted to scope.** Every unlock the player earns is visible somewhere. *How* it's surfaced depends on how much it opens up — see the Unlock Web section.
12. **Front-loaded systems, deepening content.** Every major game system comes online during R1–R3 (the Mortal era). R4–R12 is content depth within revealed infrastructure, not new mechanical surface area.
13. **Builds, not cards, do the work.** Individual cards are tools. The expressive depth lives in evolutions and path culminations, not in card-level differentiation. No rarity tiers, no chase cards, no "this Common version is worse than the Rare version" framing.

---

## The Four Pillars

### 1. VS Run Loop (Active)

**The only thing the player plays.** Movement only — autofire combat. Mobile-friendly even though PC-first.

#### Run Structure

- **Length:** up to 30 minutes, hard cap.
- **End conditions:** complete all 6 universal objectives + defeat the boss = territory conquered.
- **Pacing:** parallel objectives + boss-trigger. Boss spawns when all other objectives are complete OR at the 25-minute mark, whichever comes first. Skilled/powered players can finish in 10 minutes; slower players take the full 30. Both paths win.
- **Pause-friendly:** runs can be paused/resumed cleanly. Generous handling on quit/disconnect — completed objectives bank even if the player drops out mid-run.

#### Six Universal Objectives

Every map has all six. Question is *how much* / *how many*, not *if*:

1. **Survival** — last X minutes
2. **Kills** — defeat X enemies
3. **Targets** — kill X elites/mini-bosses
4. **Territory** — paint X% of the map
5. **Resources** — gather X of a thing
6. **Boss** — defeat the final encounter

#### Per-Objective Banking

- Each objective is independently completable
- Complete = banked forever (across all future runs)
- In-progress = resets on run end (win or lose)
- 3/3 elites in one run = done permanently for that region
- 2/3 elites = back to 0/3 next run
- All 6 banked = region conquered
- Speedrun-friendly *and* casual-friendly: chip away over multiple runs, or hammer it all in one efficient run.

#### Region Objectives as Card Unlock Source

Region objectives are a primary source of evolution-partner passive unlocks. Map bosses drop techniques (their signature) on first defeat; the evolution partner passive that pairs with that technique unlocks from a region objective on a different map. This decouples technique-from-passive unlocking and prevents bosses from feeling like the only meaningful unlock source.

- The "gather X resources" and "paint X%" objectives are good candidates for evo-partner passive unlocks (least directly tied to combat narrative)
- Every evolvable card in the pool has its partner reachable through normal play — the unlock web ensures no card is stranded as "evolvable in theory, partnerless in practice"
- Cross-checking the roster + region-objective design is required to maintain this invariant

#### Painting / Territory Mechanic

- Movement paints the map (Splatoon-style territory claim)
- Paint accumulates **persistently across runs** — it doesn't reset between runs
- Paint radius is unlockable (like VS pickup radius); starts small, grows over time
- Pure objective tracker for now (does nothing functional beyond filling the % bar). Functional effects can be added later if they earn it.
- Once a region's paint % objective is met, that objective banks. Other objectives still need completing for full conquest.

#### Mission Select Screen

Player picks region from the Risk map. Pre-run screen shows:
- Region name, biome
- Full objective list (numbers, types)
- Enemy types / hints
- Boss preview (silhouette until first encounter)
- Rewards on success
- Recommended cultivation tier (soft warning, never a block)

Same objectives are pinned in the in-run HUD.

#### Wave Composition

VS-classic continuous spawn baseline + objective-flavored wave shifts. Difficulty scales with **kill count / progression within the run**, not pure timer (so speedrunners don't fight baby enemies the whole run).

#### Replays of Conquered Regions

- Same map, same enemies, same boss, same drops
- Banked objectives stay banked (no FOMO on missing unlocks)
- Resources, XP, materials still flow normally
- The named realm-final boss does **not** respawn after defeat. A generic boss appears at the 5- or 10-minute mark instead.
- Replays are 100% player choice — they grind because they want to (XP, materials, flexing, nostalgia). The game doesn't push or pull them.

#### Level-Up Draft

The mid-run decision-making layer.

- **Triggers:** level-up (always 3 cards) AND chests (3-7 cards, variable, dopamine moment).
- **Chest sources:** elites, mini-bosses, objective completions.
- **Chest cap:** 5 cards default; 7 unlockable through macro progression. Never higher than 7.
- **Card types (two pool types only):**
  1. Techniques (auto-firing weapons / damage-dealing abilities)
  2. Passives (stat / rule modifiers)
- **Evolution is a conditional draft slot, not a pool entry.** See below.
- **Path culmination is a conditional chest-only offer.** See Path System.
- **No consumables, no pets/companions as a separate type.** Pet-like effects exist as cultivation-flavored techniques.
- **Card max level:** 8.
- **Slot layout:** two visible rows (techniques on top, passives on bottom). Both rows scale together with meridian count.
- **Run-start pick:** first card is selected before the run begins via a card selection screen (not via an awkward instant-level-up at run start, which VS handles poorly). The selection pool is the player's full currently-unlocked card pool — day-1 sees 96 cards, endgame sees ~444. The player picks any one card (technique or passive) to start the run with at level 1.
- **Skip / Reroll / Banish:** all exist, all start at 0, all earned via macro progression. Per-run charges.

#### Evolution Slots (Conditional, Not Pool Entries)

Evolutions are not draft cards in the pool. They're a conditional slot that takes over one of the offered card positions when the trigger conditions are met.

- **Trigger condition:** technique X and its paired passive Y both reach level 8 (max).
- **Slot appearance:** on the next level-up draft AND on the next chest draft after the pairing becomes evo-eligible, one of the offered card positions becomes the evolution offer. Persists across every subsequent draft until taken.
- **Player choice:** the player can take the evolution or pick one of the other cards. If skipped, the evolution offer remains and reappears in every future draft until accepted.
- **Multiple evo-eligible pairings:** queue, oldest first. One evo slot per draft, never two simultaneously.
- **Effect of taking it:** the technique transforms into its evolved form, consuming or fusing with the paired passive depending on the pairing's design.
- **Discovery:** pairings are hidden until first triggered. After the player first evolves Vine Whip + Rooted Stance, all future drafts tag both cards with "evolves with [partner]" hint text. Codex logs the discovery.

#### Path Culmination Offer (Conditional, Chest-Only)

When the player has evolved the specific set of pairs that form a theme's path-tier recipe — AND every loadout slot is filled with one of those recipe pairs — the next **chest** offers a Path Culmination card.

- **Chest-only.** Level-up drafts never offer path culminations. This makes the culmination an event, paced by chest cadence.
- **All-or-nothing trigger.** Every tech slot must be evolved AND every passive slot must be evolved AND every evolved pair must be a recipe member for the targeted path tier. No partial paths. Got 3 of 4 right? No culmination. Got 4 right but one wrong evolution? No culmination. Full commit or nothing.
- **The recipe matches the meridian count.** At 4 meridians (4+4 slots), the only triggerable path tier is Sapling (4 specific pairs). At 5 meridians (5+5 slots), the only triggerable tier is Sprout (Sapling's 4 + 1 specific new pair). And so on through Worldroot at 8 meridians (8 specific pairs).
- **Effect of taking it:** the path activates. All evolved techs in the loadout visually fuse under the path's identity. The tier's effect applies. First-time discovery fires the celebration cinematic. Codex logs the path tier as discovered.
- **Player can skip.** Decline is offered (functional, not punished) — the offer reappears on every subsequent chest until taken or the run ends.
- **Not every evolution leads to a path.** Every card has an evolution partner, but only the specific recipe pairs trigger culmination. The player can evolve off-recipe pairs purely for in-run power — those evolutions still hit hard, they just don't contribute to a path. Build-tinkerers have real space here.

#### Day-1 Pool — 96 Cards

The starter pool is 12 themes × 4 techniques + 4 passives = 96 cards. Every card is evolvable. Every theme has exactly the 4 evolved pairs that form its Sapling recipe.

**Archetype taxonomy** — locked, consistent across all 12 themes:

| Card Type | Archetype | Job |
|---|---|---|
| Technique | Strike | Close-range melee swing/aura |
| Technique | Projectile | Forward-firing ranged attack |
| Technique | Orbital | Rotating weapon around player |
| Technique | Zone | Drop/area/companion effect |
| Passive | Vitality | HP, regen, defense |
| Passive | Utility | Movement, pickup, XP gain |
| Passive | Offense | Damage modifier, crit, attack speed |
| Passive | Special | Theme-flavored unique effect |

**Evolution pairing convention (consistent across all themes):**

- Strike ↔ Vitality
- Projectile ↔ Offense
- Orbital ↔ Utility
- Zone ↔ Special

The pairing convention is consistent so that once a player learns one theme's pattern they can experiment in others. Pairings still must be DISCOVERED — the player isn't told the convention; they figure it out through play.

**Card naming** (placeholders, full naming pass later):

| Theme | Strike | Projectile | Orbital | Zone |
|---|---|---|---|---|
| Wood | Vine Whip | Wooden Spear | Wandering Sapling | Spore Burst |
| Earth | Stone Fist | Crag Shard | Boulder Companion | Tremor Pulse |
| Fire | Ember Palm | Cinder Bolt | Phoenix Talisman | Ember Field |
| Water | Tide Lash | Rain Needle | Mist Spirit | Whirlpool |
| Metal | Cleaving Edge | Iron Spear | Floating Saber | Shrapnel Burst |
| Wind | Gale Strike | Cutting Gust | Cyclone Wisp | Wind Tunnel |
| Ice | Frost Claw | Icicle Shard | Glacier Shard | Frozen Field |
| Lightning | Thunder Fist | Lightning Bolt | Storm Sphere | Static Field |
| Shadow | Yin Touch | Shadow Dart | Phantom Twin | Umbral Pool |
| Spirit | Soul Strike | Ghost Lance | Wandering Soul | Spirit Veil |
| Star | Comet Strike | Star Lance | Constellation Mote | Nebula Pulse |
| Void | Hollow Palm | Null Bolt | Void Echo | Origin Mark |

| Theme | Vitality | Utility | Offense | Special |
|---|---|---|---|---|
| Wood | Rooted Stance | Quick Sap | Sapling Growth | Verdant Renewal |
| Earth | Stone Skin | Steady Step | Crushing Weight | Mountain's Endurance |
| Fire | Burning Heart | Restless Pace | Searing Edge | Cinder Spread |
| Water | Flowing Form | Smooth Current | Tidal Pressure | Reflective Surface |
| Metal | Sharpened Body | Honed Movement | Bladed Intent | Cutting Aura |
| Wind | Lithe Frame | Swift Step | Slicing Wind | Following Breeze |
| Ice | Frozen Vigor | Glide Step | Numbing Strike | Frost Coating |
| Lightning | Charged Body | Surge Step | Crackling Edge | Arcing Current |
| Shadow | Veiled Vigor | Silent Step | Backstab Edge | Shadow Shroud |
| Spirit | Soul Vigor | Drifting Step | Soul Edge | Soul Resonance |
| Star | Stellar Frame | Cosmic Step | Aligned Strike | Constellation Pull |
| Void | Hollow Frame | Empty Step | Erasing Edge | Null Field |

#### Pool Growth Across the Game

Day-1 pool: 96 cards (Sapling recipes for all 12 themes).

Cards added across the game's progression:

| Source | Cards added |
|---|---|
| 119 map bosses (signature technique each, first defeat) | ~119 techs |
| Region objectives (evo-partner passive unlocks) | ~119 passives |
| 20 special-event recruits (signatures) | ~20 |
| 12 stage breakthroughs (~2 cards each) | ~24 |
| 36 tier breakthroughs (1 card each) | ~36 |
| Library / Forge / achievement tail | ~30 |
| **Total added** | **~348** |
| **Total pool by endgame** | **~444** |

Per theme: ~37 cards / ~18 pairs by endgame. Each theme's full path arc requires 8 pairs (Sapling 4 + Sprout 1 + Grove 1 + Forest 1 + Worldroot 1 = 8). The remaining ~10 pairs per theme are alternative evolutions, decoys, and exotic builds — content for the build-tinkerer.

**Theme distribution across realms is EVEN.** Every realm contributes cards to every theme. No realm is the "Void realm" or the "Wood realm." This means any path can be built from day-1 and grown across the entire game, paced naturally by meridian refinements.

#### Synergies — The Path System (Revised in v5)

Paths are the build mechanic. Themes have no DoT or damage-type mechanics — they're identity markers for path membership.

- **One path per theme. 12 themes = 12 paths.**
- **Each path manifests at 5 tiers**, gated by meridian count: Sapling (4 mer), Sprout (5), Grove (6), Forest (7), Worldroot (8).
- **Tiers are additive.** Sapling's effect persists; Sprout adds a new effect on top of Sapling; Grove adds on top of those; etc. By Worldroot the path expresses all 5 layered effects simultaneously.
- **Trigger:** the player must evolve the SPECIFIC pairs that form the current meridian tier's recipe. Drafting any 4 theme pairs isn't enough — it has to be the right 4. The recipe is additive: Sapling = 4 specific pairs, Sprout = those 4 + 1 specific new pair, etc.
- **Discovery-driven.** Recipes are hidden until first culminated. When the player evolves the right combination in a run, the path culmination chest offer appears. Codex logs the discovery. Future drafts tag those cards with "contributes to [Path Name]" hints.
- **Chest-only offer.** Path culminations never appear in level-up drafts. Only chests.
- **First-time discovery = celebration moment.** Camera zooms, world dims, character glows in path's theme color, calligraphy-styled name reveal, brief audio sting, ~1.5 sec.
- **Discovered paths can be permanently strengthened at the Soul Forge** (see Pillar 4).

#### The 12 Sapling Effects

All combat-focused. All borrow proven mechanics from VS / Brotato / Halls of Torment / ARPGs.

| Theme | Sapling effect | Genre lineage |
|---|---|---|
| **Wood** | Heal small amount per kill | VS Garlic/Pummarola style |
| **Earth** | Hits knockback enemies + small shockwave AoE | HoT Ground Pound style |
| **Fire** | Kills explode, damaging nearby enemies | VS Skull O'Maniac style |
| **Water** | Attacks pierce through enemies in a line | VS pierce mechanic |
| **Metal** | +crit chance and +crit damage | Brotato crit stat |
| **Wind** | +attack speed across all techniques | VS Empty Tome / Brotato |
| **Ice** | Slow on hit; enemies dying while slowed shatter for AoE | PoE Cold mechanics |
| **Lightning** | Hits chain to 2–3 nearby enemies at reduced damage | Chain Lightning |
| **Shadow** | Damage scales with number of enemies near you | Hades-style proximity reward |
| **Spirit** | Kills spawn temporary spirit allies | Necromancer / summoning |
| **Star** | Hits fill a meter; full meter triggers screen-wide starfall | Brotato meter / charge mechanics |
| **Void** | Small chance per hit to instantly erase non-elite enemies | VS Death's Bell / ARPG execute |

Sprout/Grove/Forest/Worldroot effects per theme: TBD when those tiers are reached in development.

#### The Wood Path (worked example)

| Tier | Meridians | Loadout requirement | Layered effect added |
|---|---|---|---|
| **Wood: Sapling** | 4 | 4+4 specific Wood pairs evolved | Heal small amount per kill |
| **Wood: Sprout** | 5 | Sapling + 1 specific new Wood pair evolved | + Evolved Wood techs gain damage boost |
| **Wood: Grove** | 6 | Sprout + 1 specific new Wood pair evolved | + Entangling vines spawn on hit, briefly rooting enemies |
| **Wood: Forest** | 7 | Grove + 1 specific new Wood pair evolved | + Worldtree manifests, pulsing AoE damage periodically |
| **Wood: Worldroot** | 8 | Forest + 1 specific new Wood pair evolved | + All Wood tech effects double in size; healing motes restore qi |

Same identity (renewal, growth, entanglement, life) at every tier; the scale and richness grow with the player.

#### The Righteous Path (13th Path, Capstone)

The capstone path that sits outside the 12-theme framework.

- 13th path, structurally separate from Sapling→Worldroot. Combines all 12 themed paths into one.
- **Recipe:** 8 specific evolution pairs sourced from R4-R11 realm-final signatures + their evo-partner passives
- Each of the 8 component pairs is of a different existing theme (8 of 12 themes contribute; which 8 deferred)
- **Discoverable only in infinite/endgame mode after R12 conquered**
- Codex tracks separately (sits outside the 12-path framework)
- R12 realm-final is the **capstone fight** — final boss tier resolved (R12 IS the final boss tier)
- R12 realm-final still drops a normal themed signature like every other boss (per the disciple schema) — that signature is an ordinary R12-power off-recipe card, not a Righteous Path component
- Culmination effect: fundamentally new layer (e.g., all 8 techniques chain across themes, or every kill triggers a cross-theme cascade) — not just bigger numbers. Specifics deferred until R12 design work.

#### Rarity Weighting — REMOVED

Rarity is no longer a property of cards. All cards are equal — differentiated by theme, archetype, evolution partner, and path served. Card unlock timing (which cards are in your pool) is the only pacing axis at the card level. The "Common-skewed early, smoothing to 20/20/20/20/20" curve from v4 is cut.

#### Meridians (Slot Progression)

Meridians are a **separate progression axis** from cultivation stages.

- Start with **4 technique slots + 4 passive slots** = 8 total cards in play
- Cap at **8 + 8** = 16 total cards in play
- Lore: every cultivator has 8 meridians anatomically; what changes is how many are **refined** enough to channel sustained technique flow.
- Refinement happens at the **Personal Sanctum**. Costs essence + tier-appropriate material. No boss-gating.
- Different path tiers require different slot counts. The path's manifestation tier matches the player's meridian count — at 6 mer, the player can culminate up to Grove tier.

**Meridian refinement pacing (revised in v5 to align with card-unlock timing):**

| Refinement | Target meridian | Realm Position | Path tier enabled |
|---|---|---|---|
| 5th | Mer 5 | End of R3 | Sprout |
| 6th | Mer 6 | End of R5 | Grove |
| 7th | Mer 7 | End of R7 | Forest |
| 8th | Mer 8 | End of R10 | Worldroot |

Each refinement aligns with sufficient cards having been unlocked across all 12 themes that the player can plausibly build the next tier of any theme they're focused on. R11–R12 become pure mastery realms — paths fully manifested, player tests their build at maximum scale.

---

### 2. Cultivation Progression (Idle / AdCap Spine)

The long power curve. Asymmetric gating with realm progression (see Pillar 3).

#### Stages

- **12 stages total.** Names TBD, generic xianxia/wuxia (no IP infringement).
- Each stage has **3 cycling milestones** (functional "tiers").
- The 3 cycles per stage are about **purifying and condensing qi** — expanding the pool, refining the essence each time.

#### Eras (Visual / Power Brackets)

| Era | Stages | Status | Geographic Scope |
|---|---|---|---|
| Mortal | 1–3 | Still human | Provinces of a country |
| Transcendent | 4–7 | Beyond human, can still die | Countries of a continent |
| Immortal | 8–10 | True immortal | Continents of a world |
| Divine | 11 | Demi-god | Worlds of a galaxy |
| Eternal | 12 | God / beyond | Galaxies / existence |

Era names are placeholders.

#### Cycling Mechanics

**Cycling is the shape of qi circulation through the body's meridians.** Mechanically: a % bonus to the head's qi gathering rate (idle + run-derived).

- **8 cycling techniques total in the entire game.** Each is a distinct circulation pattern through some number of meridians.
- **Only one cycle active at a time.** Switching is free and instant.
- **Meridian count gates access.** More refined meridians = more shapes accessible.
- **Each cycle has a cap.** Forge upgrades climb a cycle toward its cap.
- **Head-only mechanically.** Disciples do not run cycles in any way that affects the game.

##### The 8 Cycles

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

**Cycle upgrades happen at the Library** (not Soul Forge). A newly-learned cycle starts at ~30% of its cap. Library tier upgrades climb each known cycle toward its cap.

#### Qi Pool

- Qi pool fills via idle generation (Sect Power-driven), run-derived input (monster cores + enemy essence), and cycling multiplier
- Pool **caps**; player must "hit the button" to advance a tier
- Qi never decays or is lost
- Each stage requires 3 full cycles to be ready for stage breakthrough

#### Tier Breakthroughs (Within a Stage)

Small ceremonies. Click-to-advance once requirements are met.
- 3 per stage
- Performed at the Personal Sanctum
- No combat

#### Stage Breakthroughs

- **Stages 1–3:** just press the button.
- **Stages 4–12:** require **inspiration** as a prereq.
- Non-combat ceremonial moments at the Personal Sanctum.

#### Inspiration

- Drops only from **bosses** ("strong opponents")
- Specifically map-final and realm-final bosses drop *some* of them
- Cannot be banked ahead (realm gating prevents access to higher-stage inspiration outside cultivation reach)
- Self-regulating progression gate

#### Stage Rewards

- Bigger numbers
- More cards added to the draft pool (~2 per stage)
- Occasional cycle unlocks
- (Future scope: new run mechanics per stage. Not in v1 to keep scope manageable.)

#### The Asymmetric Gating Rule

- **Cultivation gates realm progression.** Stage X required to enter Realm X.
- **Realm progression does NOT gate cultivation.** (Patient player could max cultivation in R1 in theory.)
- **EXCEPT** — once stage 4+ requires inspiration, you must engage with the appropriate realm.

---

### 3. Risk Map (Territorial Conquest)

#### Realms (Renamed in v5: Scope-Based)

12 realms total, 1 per cultivation stage. Map counts and scope names locked:

| Realm | Maps | Scope | Era |
|---|---|---|---|
| R1 | 2 | Province | Mortal |
| R2 | 3 | Region | Mortal |
| R3 | 3 | Kingdom | Mortal |
| R4 | 4 | Empire | Transcendent |
| R5 | 6 | Continent | Transcendent |
| R6 | 8 | Sea | Transcendent |
| R7 | 10 | World | Transcendent |
| R8 | 13 | Sky | Immortal |
| R9 | 15 | Heavens | Immortal |
| R10 | 17 | Star | Immortal |
| R11 | 18 | Galaxy | Divine |
| R12 | 20 | Universe | Eternal |

**Total: 119 map regions** + 12 realm-finals (overlap with map bosses) = 119 named map-boss disciples sourced from territorial play.

Realm names are placeholders — the structural lock is scope-based progression, not theme-based.

**Themes are NOT realm-locked.** Every realm contributes cards to every theme through map-boss signatures and region objectives. The player can build any of the 12 paths from R1 onward and grow them across the full game.

**R12 is the capstone realm.** Not a "do it again" realm. R12 is where every system tops out at once: the final Smith recruit, the final Library tier upgrade, the final special-event recruits, the final boss, the final cycle (Cycle 8 at Stage 12 breakthrough). Everything getting the bow on top. R12 is the culmination of power, not a stretch of variety content.

- **5 visual identities total** (one per era), with shared identity within each era to control art budget
- Each realm visually represents the geographic scope of its era

#### Map Structure

- Each map is a region with the 6 universal objectives + a final boss
- Conquering a map = banking all 6 of its objectives
- Final bosses are **named, unique, recruitable cultivators** — see the Boss Roster section

#### Adjacency

- Player starts at one edge of a realm
- Conquering a map unlocks adjacent maps
- Player chooses the path
- **Boss fights are not gated by completion.** Only **recruitment** is gated, and even then only for specific exotic-gate bosses.

**Adjacency patterns by realm size:**
- **R1 (2 maps):** Linear. M1 = start, M2 unlocks after M1
- **R2/R3 (3 maps):** Gateway + branch + final. M1 = gateway, M2 unlocks after M1, M3 (realm-final) unlocks after BOTH M1 and M2
- **R4+ (4-20 maps):** Broader graphs; gateway entry, multiple branches, realm-final gated on completing some subset of prerequisites. Specific patterns TBD per realm.

#### Enemy Categories

Each map has 4-6 fodder types + 2-3 elite types (visual/biome variation; mechanically baseline).

| Category | HP | Damage | Speed | Spawn rate | Drops |
|---|---|---|---|---|---|
| **Fodder** | 0.05× boss baseline | 0.4 (contact only) | 0.5-0.9× player | High continuous | Raw qi, occasional spirit stones |
| **Elite** | 0.5× | 0.8 (telegraphed) | 0.4× | One every ~90 sec | Chest (3-5 cards) + tier-appropriate materials |
| **Mini-boss** | 1.2× | 1.0 | 0.5× | One per minute past 10-min mark | Larger chest (5 cards) + better materials + sometimes inspiration fragment |

**Per-realm scaling:** R1 = 1×, R2 = 1.5×, R3 = 2×. Both HP and damage scale; speed/behavior constant.

**Generic boss on replay:** the named realm-final doesn't respawn. Generic boss with mini-boss stats × ~2 appears at 5- or 10-min mark instead.

**Within-run enemy HP scaling:** `HP(t) = base × 1.10^minute`. By minute 25, ~10× initial HP. Spawn density grows from ~1.5 fodder/sec at 0:00 to ~30+/sec at 25:00.

#### Realm Transition

- **Both required to advance:** defeat the realm's final boss AND reach the cultivation stage that gates the next realm
- Player clicks the new realm to enter — triggers the **ascension cinematic / ceremony**
- After ceremony, player drops into the first region of the new realm
- Player controls *when* to ascend

#### Bosses as Recruits

- **All defeated bosses can be recruited** into the player's sect
- Recruitment is **automatic on defeat** when requirements are met
- **Default requirement is just defeat.**
- **Exotic gates are a per-boss flavor feature**, sparingly used:
  - "Defeat with 100% region completion"
  - "Defeat with a specific build/path active"
  - "Defeat within X minutes"
  - "Defeat after recruiting their rival"
- Critical-path bosses (building-unlockers, realm-finals) are never exotic-gated.
- Defeated boss → joins your sect as a named disciple with name, fighting style, signature technique. Some also bring **building unlocks**.
- **No boss is ever locked out.** Late-completed exotic requirements still unlock the recruit.

#### Boss Replacement on Replay

- Defeated named realm-final bosses do **not** respawn during region replays
- Replaced by a **generic boss** at 5- or 10-minute mark

#### Map Surfacing of Incomplete Work

The Risk map UI clearly indicates regions, realms, and bosses with incomplete objectives or uncollected recruits. Subtle markers, realm-level summaries showing completion %. Lap-back legible but not pressuring.

#### Idle Output from Conquered Regions

Conquered regions passively generate, even when player is offline. All flow into a unified **inbox** screen.

**Per-region output (per hour, R1 baseline; scales 2.4× per realm):**

1. **Essence** — universal upgrade currency (~30/hr R1)
2. **Raw Qi** — feeds qi pool toward tier breakthroughs (~20/hr R1)
3. **Spirit Stones** — higher-tier currency; rare drops + special-event arrivals carry small bundles
4. **Materials** — themed, tier-graded; plateaus at 3-5/hr (scarcity by tier, not quantity)
5. **Inspiration** — drops only from realm-final boss kills, never idle; required for Stage 4+ breakthroughs
6. Random rare drops (loot inbox)
7. Disciple XP (assigned named disciples grow)
8. Reputation / Influence
9. Lore / Codex fragments
10. Event triggers (rare boss spawns, treasure runs, hidden region unlocks, special-event recruit arrivals)
11. Recruitment leads (passive wandering cultivator events)

**Currency Model (4 currencies + Materials):**

| Currency | Tier | Earned from | Spent on |
|---|---|---|---|
| **Qi** | Personal pool | Enemy kills, idle, cycling multiplier | Tier breakthroughs only |
| **Essence** | Common currency | VS-style run drops + idle from regions | Most upgrades (buildings, forge, leaves, meridians, cycle climb base) |
| **Spirit Stones** | Higher currency (gold→platinum, NOT premium MTX) | Boss defeats, rare idle, special-event arrivals | High-impact sinks: generic recruitment, cycle climb stones component, top-tier building upgrades (T7+), high-meridian refinement, reroll/reset operations |
| **Inspiration** | Gating resource | Realm-final bosses (first-time) | Stage 4+ breakthroughs only |

**Qi vs Essence — the conceptual split:**
- **Qi** = personal cultivation energy. INTERNAL to the head. The cultivator getting stronger.
- **Essence** = condensed value extracted from the world. EXTERNAL infrastructure. The sect's operation growing.
- Both must flow for progression. Lots of essence + low qi = stuck at current stage. High qi + no essence = no upgrades.

**Spirit Stones rough tuning intuition:** 1 stone ≈ 1,000 essence value. Not interchangeable; just for tuning sense.

**Cuts from earlier doc versions:**
- Monster Cores — removed; kills drop raw qi directly
- "Spirit Stones as universal currency" — replaced; essence is the universal, stones are tier-up
- Cycling boosters / time crystals — these ARE spirit stones; same mechanic, new name

**Sect Power Multiplier (sub-linear, anchored to AdCap/CC/NGU case studies):**

`multiplier = 1 + sqrt(Sect_Power / 100)`

Late-game still huge but not absurd. Permanent multipliers from any future NG+ would layer on top.

**Material Model:**

- All materials themed; no generic/universal category
- 12 themes × 6 material tiers = 72 materials total
- Material tier ≠ realm. Realm pairs share tier: R1-R2=T1, R3-R4=T2, R5-R6=T3, R7-R8=T4, R9-R10=T5, R11-R12=T6
- Building upgrades + meridian refinement accept any theme at the required tier
- Forge theme-card upgrades require matching theme
- All 12 themes have materials at every tier (Lightning T1 exists even though Lightning isn't an R1-R2 boss theme)

#### Disciple Assignment

- **Manual mode:** player assigns specific named disciples to specific regions/buildings for optimized output. Every named disciple has a **best-in-slot role**.
- **Auto mode:** "ass in a chair" — fills slots based on raw stats. **Deliberately suboptimal, permanently.**
- Auto-mode ignores **Training Hall student slots entirely** (manual-only optimization).

#### Output Rate Scaling

Output rate increases with:
- Sect Power
- Sect buildings and their levels (including specialist count and Master rating)
- Named disciple count, tier, specialty-match per region, and Specialty Rating
- Macro progression unlocks

Output rate does **NOT** scale with cultivation stage directly or time held.

#### Rival Sects

- Exist on the map as **targets to conquer**
- Conquered = conquered, permanently
- Rival sect leaders are recruitable bosses

#### Tactical Routing

Building upgrades require **specialists** (recruited named bosses of the matching specialty) at rating ≥ tier + materials. Players plan routes through realm content to find what they need. Upgrade panels display sourcing info via building-runner's flavor dialogue.

---

### 4. Sect Management

The sect is the engine that makes everything else move faster.

#### Core Principle

**Manual play wins through optimization. Auto play is the mercy button.**

#### Decision Cadences

- **Per-run** (every 10–30 min): claim inbox, glance at sect status. ~30 seconds.
- **Per-session** (couple times an hour): start Forge upgrades, queue Teahouse brews, reassign disciples, spend currency. 2–5 minutes.
- **Per-milestone** (after realm conquest, stage breakthrough, big recruit): restructure. 10–20 minutes.

#### Maintainability Rules (Hard Constraints)

- Progressive disclosure
- One inbox, one screen
- Notifications rare and obvious
- No upkeep, no decay
- Default behavior always reasonable
- One decision at a time
- No FOMO

#### Disciples — Two Tiers

**Named disciples** (~140 across the game):
- ~12 realm-final bosses
- ~119 map bosses
- ~20 special-event recruits

Note: realm-finals are also map bosses; total named ≈ 139.

**Generics** (millions at endgame):
- Aggregate population, not individuals
- Capped by territory
- Tier-trained passively via Training Hall

#### Named Disciple Attributes (7)

1. **Name + portrait**
2. **Realm + position**
3. **Tier** — Stage 1 through Stage 12. Trainable up to Stage 12.
4. **Specialty** — one tag, one family.
5. **Specialty Rating (1–10)** — mastery. Trainable to 10.
6. **Meridian count (4–8)** — fixed at recruitment.
7. **Signature technique** — unique run-pool addition on first defeat.

Plus: Recruitment gate (property of how the player got them, not a stat).

#### Specialty Rating Mechanics

- Drives BIS contribution
- Visible on card as 1–10 integer
- Trainable via Training Hall student slots
- Monotonic per-specialty starting-rating arcs (each new recruit of a specialty has starting rating ≥ all previous of that specialty)
- Building specialists start ≤5 (Heaven-Reader exception, starts at 7)
- Theme specialists scale across realms but theme assignment is no longer realm-locked
- Realm-finals climb 5→10 across the 12 realms

#### Building Specialist Master System

- All specialists default-home to their specialty's building
- One Master per building; player designates; free and instant to swap
- **Building Tier Unlock Rule (v6):** Master's starting rating IS the tier ceiling the building can reach with that specialist. Pao at rating 5 → Teahouse purchasable up to T5. Lin (Heaven-Reader exception) at rating 7 → Pavilion up to T7. Recruiting a higher-rated specialist of the same family extends the ceiling.
- **Tier count per building:** = max rating achievable in that specialty's arc. For most building specialties (6-member arc, ratings 5→10), buildings reach T1-T10. For Heaven-Reader's short arc (3-4 members), Pavilion likely reaches T1-T9 to T1-T10 depending on arc length decision.
- **Specialist count drives visual building growth** independent of tier. Pao alone = tiny tea hut. 6 Brewers = full tea complex. T1 + 6 specialists = sparse-but-populated; T6 + 1 specialist = expanded-but-empty.
- **Master amplification model:**
  - **Compounding buildings** (Recruitment, Storehouse, Library, Training, Outer Court, Pavilion): all specialists at the building amplify all unlocked surfaces collectively. Formula: `compound rate = base × (1 + Σ(specialist ratings) × coefficient)`. Master = narrative.
  - **Flat-cap buildings** (Teahouse, Soul Forge): each upgrade track can have ONE specialist assigned. Per-level output = `base × max(rating_assigned, 1)`. Master picks lead track first.
- Apprentices contribute supplementary effect on Master's terms
- Buildings grow visually with specialist count and tier

#### What Named Disciples Do (3 Roles)

1. **Region duty** — contribute to region's idle output. Specialty match boosts yield.
2. **Building duty** — Master designation or apprentice support.
3. **Training Hall duty** — either **trainer** (lifts generic tier) or **student** (own tier + rating climb).

#### Training Math

**Rule 1 — Ceiling Cascade.** Stage caps trainer assignments at (stage − 1).

**Rule 2 — Dynamic Sect Cap.** Sect Cap = min(highest stage in Training Hall, stage − 1).

**Rule 3 — Cumulative Throughput.** Total training points (exponential stage curve) = rate generics + students climb.

**Student Slots:** named disciples can be placed in student slots. Tier and Specialty Rating both climb toward 10. Slow but unbounded. Manual-only.

#### Sect Power

- Composition-weighted
- Single number visible on Main Hall hub
- Clicking widget deep-links to Management screen
- Affected by: generic distribution, building levels + Master ratings + apprentice counts, named disciple BIS placements (including Specialty Rating), macro progression unlocks

#### Buildings — The Macro Tree

**Building Upgrade Requirements: Specialist with rating ≥ tier + Materials + Essence (+ Spirit Stones at T5+).**

**Tier visibility is realm-gated.** Entering Realm N reveals tiers gated to Realm N across unlocked buildings.

##### Building Tier Curves

Two templates govern how buildings scale with tier.

**Compounding template** (Recruitment, Storehouse, Library, Training, Outer Court, Pavilion):
- Three surfaces unlock at T1, T4, T8
- Each surface holds multiple tracks with their own caps (cap-10 / cap-5 / cap-3 / cap-2)
- All specialists at the building amplify all unlocked surfaces collectively
- Each new tier adds levels to existing tracks AND unlocks new caps on those tracks
- Visual: building grows in scope, density, complexity with tier

**Flat-cap-by-tier template** (Teahouse, Soul Forge):
- A many-knob upgrade economy where each track caps individually
- Building tier determines the ceiling of each track
- Each upgrade track can have ONE specialist assigned; per-level output = `base × max(rating_assigned, 1)`
- Visual: building grows in capacity, equipment, refinement with tier

**Per-building tier surfaces:**

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

**Building tier cost table:**

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

##### The 10 Buildings

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

##### Soul Forge — Three Upgrade Tracks

1. **Techniques** — individual run technique upgrades
2. **Passives** — individual passive upgrades
3. **Paths** — discovered path-tier strengthening (Sapling → Worldroot effects per theme)

Path upgrades work per-discovered-tier. Upgrading the Wood Path lifts ALL discovered Wood tiers proportionally.

Forge purchases fire Minor unlocks like all other building purchases — silent "new" indicator on the building screen, no popup.

(Cycle upgrades formerly lived here in v5 but moved to the Library in v5.1 — see Buildings table above.)

##### Library — Cycle Upgrades (New in v5.1)

The Library hosts cycle upgrades. A newly-learned cycle starts at ~30% of its cap; Library tier upgrades climb each unlocked cycle toward its full cap. The Library's other two jobs (head cultivation speed, path Codex) remain.

##### Teahouse — Foundational Food Building

(Unchanged from v3/v4 — R1 foundational. Sect-wide + run buffs. "In service" tea = permanent buff while brewed.)

#### How the Pillars Connect Through the Sect

- **Territory** → **Population cap** → **Sect size**
- **Trainers** → **Sect Cap** → **Generic tier**
- **Sect size + Sect tier** → **Sect Power**
- **Sect Power** → head's cultivation speed, passive qi flow, idle output rates
- **Buildings + Master ratings** → run buffs, charges, chest size, paint radius
- **Named disciple BIS placements** → bonus output on specific regions/buildings
- **Student slots** → long-term investment in favorite named disciples
- **Central trade-offs:** Local bonus vs. Building Master/apprentice vs. Sect-wide lift vs. Long-term investment. Four viable strategies.

---

## Boss Roster

The named disciple roster is a designed system. Total: **~139 named disciples.**

### Specialty Taxonomy (Locked)

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

### Boss Schema (7 Attributes + Combat Profile)

(As listed in Sect Management above.)

**Clarification on themes:** Building specialists (Brewer, Trainer, Smith, Charisma, Organizer, Administrator, Scholar, Heaven-Reader) carry NO theme tag. A Brewer is just a Brewer — brewing is a skill, not a theme. Their signature technique has a theme (since all cards are themed), but the disciple themselves is theme-less.

Theme specialists (Wood, Earth, Fire, etc.) carry their theme tag as their specialty. They have no building affinity.

Every named disciple has exactly one specialty, from one family (building or theme). Their signature technique is always themed (it has to be — themes are the path-membership mechanic).

**Boss Combat Profile (additional schema for in-fight design):**

- HP scaling (relative to R1 M1 baseline)
- Contact damage
- Ability damage
- Armor %
- Movement speed vs. player
- Phase structure (count + HP thresholds)
- Attack set (each: type, telegraph time, damage, cooldown, foreshadowing note)
- Telegraph generosity (relative scale)
- Arena interaction (none / static hazard / dynamic hazard / boss-becomes-arena)

**Escalation principle:** R12 finals should have ~5 attacks across 3-4 phases. Escalation through tighter telegraphs, higher damage, attack overlap, arena interaction — NOT more moves. R1-R3 prototype curve documented in prototype-spec.md leaves headroom.

### R1-R3 Prototype Boss Roster + Partner Passives

See **prototype-spec.md** for full details on the 8 R1-R3 building-trigger bosses (themes, archetypes, body-parts, signatures, partner passives, combat profiles, and per-map objective values).

Partner passive distribution across the 8 prototype maps uses **forward-shift derangement**: each map's Resources objective drops the NEXT map's boss partner. R3 M3 wraps to R1 M1. No map drops its own boss's partner.

**Uniform reward type per objective (R1-R3 prototype):**

| Objective | Always drops (first-time only) |
|---|---|
| Survival | Essence bundle |
| Kills | Raw qi cache |
| Targets | Tier-appropriate materials, mixed-theme bundle |
| Territory | Region's themed material cache (single theme) |
| Resources | Designated partner passive (per forward-shift table) |
| Boss | Signature technique + sect recruit + spirit stones + (realm-finals only) inspiration shard |

### Starting Rating Rules

- Monotonic per-specialty (each new chain recruit starts at rating ≥ all previous of that specialty)
- Building specialists start ≤5 (Heaven-Reader exception starts at 7)
- Theme specialists distributed across all realms; rating arcs follow specialty membership, not realm placement
- Realm-finals climb 5→10 across realms
- A specialist's starting rating IS the tier their building can be purchased up to (so the 1st Brewer at rating 5 unlocks Teahouse T1-T5; the 2nd Brewer at rating 6 extends to T6; etc.)

### The 12 Realm-Final Headliners (Themes Unmoored in v5)

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

### The 8 R1–R3 Building-Trigger Bosses

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

### The 20 Special-Event Recruits

Deterministic triggers; never RNG. Always-join (decline not offered).

(Roster structure carried forward from v4: 4 reputation thresholds, 4 achievement-driven, 3 region-specific, 4 Grand Master, 3 Relationship, 2 composite. Specific triggers TBD.)

### Theme Distribution Principle

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

---

## Cross-Pillar Systems

### The Unlock Web

The dependency graph across all four pillars.

#### Surfacing Model — Three Weight Tiers

| Weight | What it covers | Surfacing | Count |
|---|---|---|---|
| **Major** | New building, realm, era, stage, meridian, realm-final recruit, Grand Master recruit, Relationship recruit, **first-time path tier discovery (each of 60: 12 themes × 5 tiers)** | Full-screen moment | ~110 |
| **Medium** | New upgrade tier purchasable, new path tier discovered subsequent times, new card in pool, +1 chest cap, +1 charge, map boss recruit, region adjacency, new cycle unlocked, **first-time evolution pairing discovered (~48)**, special-event recruit arrival | Toast/banner + post-run summary + persistent "new" indicator | Hundreds |
| **Minor** | A specific purchase available within a building, stat tier purchasable, qi pool cap, cycle cap-climb increments | Silent "new" indicator only | Thousands |

**Minor unlock principle:** "the option to purchase a thing," not "the thing itself." Power still costs.

#### Three-Layer Notification Model

1. Platform-native toasts (Steam, console)
2. Post-run summary screen bundling all Medium-and-above unlocks
3. Persistent hub indicators with "new" state until visited

No badges, no red dots.

#### Source Inventory

(Carried forward from v4. Notable v5 additions:)

**From VS runs:**
- Evolution pairings discovered (each first-time event = Medium)
- Path tier first-time discoveries (each = Major)
- Path tier subsequent discoveries on other themes = Medium

#### Target Inventory

**Run loadout pool:**
- New techniques added (Medium each)
- New passives added (Medium each)
- **Rarity tier access** — fully cut
- **Universal/non-evolvable cards** — fully cut

**Cultivation:**
- Tier breakthroughs (Medium, 36)
- Stage breakthroughs (Major, 12)
- Era transitions (Major, 5)
- New cycle learnable (Medium, 8)
- Qi pool cap +tier (Minor)
- Inspiration drop rate +tier (Minor)
- Cycle cap-climb tiers (Minor)

**Risk map:**
- New region accessible (Medium)
- New realm accessible (Major)

**Sect management:**
- New building unlocked (Major, 8 events — all R1–R3)
- Building tier upgrade purchasable (Medium)
- Specific upgrade within building (Minor)
- Pop cap +tier (Minor)
- Special-event recruit arrives (Medium for most; Major for Grand Master + Relationship)
- Boss recruit joins (Medium map boss, Major realm boss)
- Disciple Specialty Rating milestones (Medium / Minor)

**Path system (new):**
- First-ever evolution discovered (Medium)
- First time discovering a specific evolution pairing (Medium each, ~48 total)
- First time culminating a path tier (Major each, 60 total)
- Path tier strengthened at Forge (Minor)

#### Load-Bearing Edges

1. **Cycling milestone → tier breakthrough → stage breakthrough → realm access.** Cultivation spine.
2. **Boss defeat → recruit → specialist available → building tier unlocked.**
3. **Inspiration drop → Stage 4+ breakthrough.**
4. **Territory conquered → generic population cap → Sect Power.**
5. **Region conquest + objectives → cards added to pool → evolution + path discovery opportunities.** (Updated: region objectives now load-bearing for passive unlocks.)
6. **Specialty Rating training (student slots) → Master rating → next building tier purchasable.**
7. **Recruit all of a specialty → Grand Master arrives.**
8. **Meridian refinement → path tier accessible → 5-card culmination recipe achievable.** (New in v5.)

#### Archetype Coverage

- **Speedrunner** — served. Default defeat-only recruit rule. Path discovery is optional dopamine, not gating.
- **Completionist** — best-served. Discovery cascades and path tier collection give a deep completion track.
- **Idle-leaner** — served if they accept some active play.
- **Build-tinkerer** — best-served in v5. With rarity cut and paths being recipe-discovery puzzles, the build-tinkerer has 12 path arcs × 5 tiers = 60 discovery moments to chase.
- **Relationship-seeker** — served via Relationship recruit category.

---

### Story / Framing

Minor but present. Lives in era transitions, boss dialogues, codex drops, milestone narrative beats, building-runner flavor text. Designed after core systems are locked. One protagonist: the sect head.

### Art Direction

- Indie-scope. Heavy reliance on AI-generated art or friend artist
- 5 era visual identities to control budget
- Boss portraits highest priority (~139 named identities)
- Generic visualization is an open creative question
- Buildings grow visually with tier and population

### Pricing & Release

Premium $5–$10. No microtransactions. Steam-first. Consoles + Steam Deck first-class. Mobile thoughtful port later.

### Endgame

Possible infinite mode + leaderboards. Locked after core game is complete.

---

## Deferred for Later

- **Stage-tied new run mechanics**
- **Teahouse recipe specifics** — variety, exact buff slot counts, brewing UX
- **Forge upgrade curves** — per-card / per-path tuning beyond Forge T1
- **Generic visualization** — open creative question
- **Material naming** — 8 prototype materials named (bamboo shoots, alchemy reagents, iron ore, sealed scrolls, sealed writs, ancient manuscripts, tribulation feathers, frost-iron ingots); remaining 64 deferred
- **Total path count beyond Sapling** — 12 themes × 4 additional tiers (Sprout through Worldroot) = 48 layered effects to design
- **Per-specialty rating arc tables** — Smith was sketched in v4; Brewer / Trainer / Organizer / Charisma / Administrator / Scholar all need full arcs spec'd
- **Theme assignment for the post-prototype boss roster** — 8 R1-R3 prototype themes locked (see prototype-spec.md); R4-R12 roster theme distribution open
- **The mid-game Heaven-Reader** — specific realm and signature technique
- **Specific region-objective passive unlocks for R4+** — each evolvable pair's partner sourced from a defined region objective
- **Specific R5 and R9 region identities** for special-event recruit triggers
- **Exotic gate distribution** — how many bosses, which kinds
- **Signature technique mechanics for the 9 non-trigger realm-finals**
- **Building visual-growth art rubric**
- **R12 realm-final identity** — Universe-scope mastery boss; theme and specialty open
- **The 12 path Sprout effects** — first layered manifestation beyond Sapling
- **48 evolution effects** (each evolvable pair has a unique evolved technique form)
- **Card-level scaling curves locked for archetype baselines** (Strike/Projectile/Orbital/Zone); per-card variance within archetypes still open
- **Naming pass on all 96 day-1 cards** — current names are placeholders
- **R11 and R12 design** — beyond "mastery realms," what specifically are they?
- **NG+ ("Cultivation Rebirth")** — outlined as concept, not designed. Endgame consideration only.

---

## Open Questions Still Worth Resolving

- **Re-fight vs. auto-unlock for late-completed boss recruits.** Leaning re-fight.
- **Skip / reroll / banish housed in Storehouse vs. Library.** Storehouse currently.
- **Meridian refinement material identities** — what specific materials gate each refinement
- **Per-boss exotic gate distribution**
- **Apprentice contribution coefficient** (specialist amplification math placeholder: `1 + rating × 0.1` for flat-cap; compounding formula coefficient TBD)
- **Cycle cap values** — placeholder %s in doc
- **Whether Heaven-Reader arc is truly 3 members or should be 4** (affects Pavilion's max tier: T1-T9 vs T1-T10)
- **Trigger values for special-event recruits** — placeholders only
- **Path Sprout/Grove/Forest/Worldroot effect designs** — 48 effects to design eventually; pacing during development TBD
- **Whether the pairing convention (Strike↔Vitality etc.) is truly consistent across all 12 themes** or whether some themes should deliberately break for variety
- **Spirit stone exchange rate / sink list** — rough 1 stone ≈ 1,000 essence locked, specific sinks TBD beyond locked ones
- **Soul Forge T1 leaves** — designed as a flat-cap track only, no separate leaf list (intentional but flag for review)

---

## Prototype Critical Path

The prototype proves the four-pillar loop end-to-end. Scope:

**Active surface:** R1 (2 maps) + R2 (3 maps) + R3 (3 maps) = 8 maps + 3 realm-finals. Ascension to R4 not in prototype.

**Sect surface:** All 8 unlockable buildings online (Recruitment Hall, Teahouse, Training Hall, Storehouse, Outer Court, Library, Ascension Pavilion, Soul Forge) by end of R3. Main Hall and Personal Sanctum present from start.

**Prototype tier state (locked):**
- 7 buildings (Recruitment / Teahouse / Training / Storehouse / Outer Court / Library / Forge): T1-T5 purchasable (each Master at rating 5)
- Ascension Pavilion: T1-T7 purchasable (Lin's Heaven-Reader exception at rating 7)

**Cultivation surface:** Stages 1, 2, 3 complete (no inspiration required). 5th meridian refined at end of R3.

**Path surface:** Day-1 pool of 96 cards + R1-R3 unlock additions (~28 new cards). Sapling tier path discovery for any theme the player commits to. Some players may discover Sprout if they refine 5th meridian and have the right unlock progress.

**Cycle surface:** Cycle 1 from start. Cycle 2 unlocked on Stage 2 breakthrough (early R1-R2). Cycle 3 unlocked on Stage 4 breakthrough (post-prototype). Library cycle upgrades available from R3 onward.

**Build-blocking work remaining for the prototype:**

1. **T2-T5 leaf content** for 6 buildings (Recruitment / Training / Storehouse / Outer Court / Library / Forge). T1 designed; tiers 2-5 still need leaf specification. (Teahouse and Pavilion T1-T7 are fully spec'd in building-tier-curves; Soul Forge T1 is flat-cap on Technique track only.)
2. **Wave composition per map** — 4-6 fodder types + 2-3 elite types per map, spawn timing
3. **Per-card content for 96 day-1 cards** — individual effects and per-level values (archetype baselines locked, per-card variance open)
4. **Library cycle climb economy** — specific essence costs to climb each cycle toward cap
5. **Naming pass** — cards, bosses, regions, signatures, partner passives, materials

Items 2-5 are large content-authoring efforts better suited to spreadsheet work than chat-based design sessions.
