# Pillar 1 — VS Run Loop (Active)

**The only thing the player plays.** Movement only — autofire combat. Mobile-friendly even though PC-first.

---

## Run Structure

- **Length:** up to 30 minutes, hard cap.
- **End conditions:** complete all 6 universal objectives + defeat the boss = territory conquered.
- **Pacing:** parallel objectives + boss-trigger. Boss spawns when all other objectives are complete OR at the 25-minute mark, whichever comes first. Skilled/powered players can finish in 10 minutes; slower players take the full 30. Both paths win.
- **Pause-friendly:** runs can be paused/resumed cleanly. Generous handling on quit/disconnect — completed objectives bank even if the player drops out mid-run.

---

## Player Baselines (R1 M1, minute 0, fresh run)

These are the canonical anchor. Every other absolute number in the game (enemy HP, technique damage, building output, currency drops) ladders off these. All tunable during prototype playtest.

| Stat | Value | Notes |
|---|---|---|
| Atk | 10 | Base attack; cards multiply |
| HP | 100 | |
| Move speed | 100 units/sec | 1.0× baseline; fodder/elite speeds reference this |
| Pickup radius | 50 units | Grows via Utility passives |
| Paint radius | 30 units | Smaller than pickup; painting needs intent |
| Hitbox radius | 16 units | Player sprite ~32; collision tighter than visual |
| Defense | 0 | Teahouse upgrade track only |
| HP regen | 0/sec | Vitality passives at L4+ add regen |
| iframes | 0.5 sec | Invulnerability window after taking damage |
| Crit chance | 0% | Offense passives L4+ / Metal Sapling add |
| Crit damage | 1.5× | +50% on crit; Metal Sapling boosts further |
| Attack speed | n/a global | Per-technique cooldowns only. Wind Sapling = global +atk speed |
| Qi pool cap (Stage 1) | 1,000 | Inherent to current stage; see [cultivation.md](cultivation.md) |
| Qi accumulation rate | 5/sec | Passive baseline before cycling bonus |
| Starter loadout | 1 tech at L1 (player-chosen theme) | 3 empty tech + 4 empty passive slots (4 meridians refined) |

---

## Six Universal Objectives

Every map has all six. Question is *how much* / *how many*, not *if*:

1. **Survival** — last X minutes
2. **Kills** — defeat X enemies
3. **Targets** — kill X elites/mini-bosses
4. **Territory** — paint X% of the map
5. **Resources** — gather X of a thing
6. **Boss** — defeat the final encounter

### Per-Objective Banking

- Each objective is independently completable
- Complete = banked forever (across all future runs)
- In-progress = resets on run end (win or lose)
- 3/3 elites in one run = done permanently for that region
- 2/3 elites = back to 0/3 next run
- All 6 banked = region conquered
- Speedrun-friendly *and* casual-friendly: chip away over multiple runs, or hammer it all in one efficient run.

### Region Objectives as Card Unlock Source

Region objectives are a primary source of evolution-partner passive unlocks. Map bosses drop techniques (their signature) on first defeat; the evolution partner passive that pairs with that technique unlocks from a region objective on a different map. This decouples technique-from-passive unlocking and prevents bosses from feeling like the only meaningful unlock source.

- The "gather X resources" and "paint X%" objectives are good candidates for evo-partner passive unlocks (least directly tied to combat narrative)
- Every evolvable card in the pool has its partner reachable through normal play — the unlock web ensures no card is stranded as "evolvable in theory, partnerless in practice"
- Cross-checking the roster + region-objective design is required to maintain this invariant

---

## Painting / Territory Mechanic

- Movement paints the map (Splatoon-style territory claim)
- Paint accumulates **persistently across runs** — it doesn't reset between runs
- Paint radius is unlockable (like VS pickup radius); starts small, grows over time
- Pure objective tracker for now (does nothing functional beyond filling the % bar). Functional effects can be added later if they earn it.
- Once a region's paint % objective is met, that objective banks. Other objectives still need completing for full conquest.

---

## Mission Select Screen

Player picks region from the Risk map. Pre-run screen shows:
- Region name, biome
- Full objective list (numbers, types)
- Enemy types / hints
- Boss preview (silhouette until first encounter)
- Rewards on success
- Recommended cultivation tier (soft warning, never a block)

Same objectives are pinned in the in-run HUD.

---

## Wave Composition (Locked 2026-05-22, Gap-Closing Tranche 4)

Wave-based spawning, VS / HoT convention. One wave per in-game minute, authored per-map. Each wave specifies the active enemy types, the minimum alive count to maintain, the spawn interval, and any slot enemy (elite / mini-boss) that appears that minute.

**Global alive cap:** 300 enemies on screen at once. Engine ceiling; new spawns suppressed at the cap. Late-game waves frequently target this cap.

**Per-realm density modifier applied to `min_alive`:** R1 ×1.0 / R2 ×1.5 / R3 ×2.0 / R4+ scales with realm. Modifier multiplies the wave's `min_alive` value; result is capped at 300. HP/dmg per-realm scaling is separate (same factors, applied to enemy stats per [scope.md](../prototype/scope.md)).

**Within-run HP scaling (fodder / elite / mini-boss only):** `HP(t) = base × 1.10^minute`. By minute 25, ~10× initial HP. **Note:** This is a genre divergence from VS Normal mode, which derives in-run difficulty from wave content (enemy types, density) rather than a hidden per-minute HP multiplier. Lock held tranche 1 pending playtest — see [open-questions.md](../open-questions.md).

**Bosses are exempt from within-run scaling.** Boss HP is absolute at encounter time, regardless of spawn minute. Speedrunner who pops the boss at minute 10 fights the same HP as a slow player at minute 25 — but with less card growth available. Skill signal preserved.

### Default Wave Template (R1 M1 baseline, 25-min run)

Numbers grounded in VS Mad Forest wave data. Pattern is intentionally non-monotonic — breather waves punctuate the climb so named enemies get focus when fodder thins, then density peaks before boss.

| Min | min_alive | interval | Slot |
|---|---|---|---|
| 0 | 15 | 1.0s | — |
| 1 | 30 | 1.0s | Elite |
| 2 | 50 | 0.5s | — |
| 3 | 40 | 0.25s | Elite |
| 4 | 30 | 1.0s | — |
| 5 | 10 | 1.0s | Elite |
| 6 | 20 | 0.5s | — |
| 7 | 80 | 0.5s | Elite |
| 8 | 100 | 1.5s | Mini-boss |
| 9 | 50 | 0.5s | — |
| 10 | 10 | 0.5s | Mini-boss |
| 11 | 200 | 0.2s | — |
| 12 | 30 | 0.25s | Elite |
| 13 | 150 | 0.3s | — |
| 14 | 40 | 0.2s | Elite |
| 15 | 150 | 0.2s | Mini-boss |
| 16 | 200 | 0.15s | — |
| 17 | 100 | 0.5s | Elite |
| 18 | 150 | 0.3s | — |
| 19 | 200 | 0.2s | — |
| 20 | 300 | 0.1s | Mini-boss |
| 21 | 300 | 0.1s | — |
| 22 | 250 | 0.1s | — |
| 23 | 300 | 0.1s | — |
| 24 | 300 | 0.1s | — |
| 25 | 100 | 0.1s | **BOSS** |

8 elite slots + 4 mini-boss slots in the template. Per-map authoring picks which slots fire — gentle maps fire few, realm-finals fire most. Per-map slot-fire counts table in [scope.md](../prototype/scope.md).

### Elite / Mini-boss Slot Behavior

- Slot enemies arrive **as part of the wave**, alongside fodder. Not paused, not gated.
- Slot enemies drop chests on death (3–5 cards default elite, 5 cards default mini-boss; Storehouse T8 unlocks larger chests).
- Slot rotations are per-map authoring: each slot in the firing set names which enemy from the realm's elite or mini-boss pool to spawn that minute.
- L8-filtered, weighted draft rules apply to chest contents identically (see Level-Up Draft section).

### Boss-Fight Spawn Behavior (Locked 2026-05-22)

**All wave activity continues during the boss fight.** Fodder waves, scheduled elite slots, and scheduled mini-boss slots all fire as the wave template dictates while the boss is alive. The boss is a target inside the ongoing wave, not a clean 1v1 isolation.

Design intent: layered tension. If the player can't kill an elite or mini-boss before the next one spawns, they *feel* that pressure stacking. The speedrunner who pops the boss at minute 10 trades chest loot (skipped slots fired in minutes 11–25) for time; the slow player at minute 25 fights through every slot they didn't bank. Both paths win, both paths feel earned.

### Aggro / Pursuit (Locked 2026-05-22)

- **Pure pursuit.** All enemies path directly toward the player at their assigned speed. No wander, no aggro range, no biome-specific behavior — that's the deferred per-enemy-quirks pass.
- **Off-screen despawn.** Enemies despawn when both off-screen AND >1000 units from player. Mirrors VS.
- **Bosses do not despawn.** Arena-locked once spawned; despawn rule doesn't apply.
- **Per-enemy behavior quirks** (ranged attacks, charges, pack tactics, summons) explicitly deferred to a later behavior pass.

---

## Replays of Conquered Regions

- Same map, same enemies, same boss, same drops
- Banked objectives stay banked (no FOMO on missing unlocks)
- Resources, XP, materials still flow normally
- The named realm-final boss does **not** respawn after defeat. A generic boss appears at the 5- or 10-minute mark instead.
- Replays are 100% player choice — they grind because they want to (XP, materials, flexing, nostalgia). The game doesn't push or pull them.

---

## Leveling and XP

- XP drops as gems on kill; player picks up via pickup radius
- **Gem values:** Fodder 1, Elite 5, Mini-boss 20, Boss 100
- **Gem persistence:** 30 seconds on the ground, then despawn (prevents ground-clutter at high spawn density)
- **XP curve:** `XP_to_next(n) = floor(5 × 1.12^(n-1))` — placeholder shape, tuned during prototype
- **No hard level cap.** Once all unlocked slots are at L8, further levels grant +1 Atk each (flex bonus — keeps late-game levels meaningful, doesn't reroll the build)

---

## Level-Up Draft

The mid-run decision-making layer.

- **Triggers:** level-up (always 3 cards) AND chests (3–7 cards, variable, dopamine moment).
- **Chest sources:** elites, mini-bosses, objective completions.
- **Chest cap:** 5 cards default; 7 unlockable through macro progression. Never higher than 7.
- **Card types (two pool types only):**
  1. Techniques (auto-firing weapons / damage-dealing abilities)
  2. Passives (stat / rule modifiers)
- **Evolution is a conditional draft slot, not a pool entry.** See below.
- **Path culmination is a conditional chest-only offer.** See [systems/path-system.md](../systems/path-system.md).
- **No consumables, no pets/companions as a separate type.** Pet-like effects exist as cultivation-flavored techniques.
- **Card max level:** 8.
- **Slot layout:** two visible rows (techniques on top, passives on bottom). Both rows scale together with meridian count.
- **Run-start pick:** first card is selected before the run begins via a card selection screen (not via an awkward instant-level-up at run start, which VS handles poorly). The selection pool is the player's full currently-unlocked card pool — day-1 sees 96 cards, endgame sees ~444. The player picks any one card (technique or passive) to start the run with at level 1. UI requirements live in [rewards.md](../prototype/rewards.md) Run-Start Screen UI Requirements.

### Draft Charges — Reroll / Skip / Banish (Locked 2026-05-22)

All three are per-run charges sourced from the Storehouse T4 surface. Three independent tracks, each with 10 leaf levels. T4 unlock starts each track at 3. Each leaf adds +1 to that track. T4 maxed (L10 each) = 13 / 13 / 13 charges per run.

**Charges do NOT scale with apprentice ratings.** Apprentice compounding on Storehouse feeds the offline cap (locked surface, per building-tier-curves.md). Charges are discrete, per-track, leaf-driven only.

**Reroll** — re-spins the entire offer. 1 charge = whole new draft (3 cards for level-up, 3–7 for chest). VS / HoT / Brotato convention. Pick-1-reroll explicitly NOT a thing — surgical rerolling would multiply effective budget by chest size.

**Skip** — closes the draft, no card taken. Awards a small essence cache:

| Skip type | Essence awarded |
|---|---|
| Level-up draft (3 cards) | 10 |
| Chest (3–7 cards) | 5 × chest size |

Flavor: the Storehouse keeper redirects unused resources. Charge cap prevents skip-everything farming.

**Banish** — removes a card from the draft pool **for this run only.** Not global, not permanent. Build-tinkerers wanting persistent curation can re-banish each run cheaply. Global banish considered and rejected for simplicity and regret-prevention.

### Card Filter Rules

- **L8 cards are filtered from draft offers.** Once a card reaches max level, it stops appearing in level-up drafts and chests.
- **All-loadout-L8 case:** once every slot in the loadout is at L8 (8 tech + 8 passive at max meridians = 16 slots), level-ups silently grant +1 Atk each (no draft UI). The flex-bonus rule from XP and Leveling.
- **Filter fallback (rare edge case):** if the filtered pool can't fill the draft (player has very few unlocked cards and most are L8), random empty-slot picks fall back to the full pool.

### Tech-vs-Passive Weighting

Draft offers are weighted toward empty slots, with a floor of 1 to prevent zero-weight starvation:

```
weight_tech = (empty_tech + 1) / (empty_tech + empty_passive + 2)
```

Examples:
- Starter loadout (3 empty tech, 4 empty passive): ~44% tech / ~56% passive
- 1 empty tech, 4 empty passive: ~29% tech / ~71% passive
- All slots filled: 50/50 (level-ups on existing cards)

Prevents the bad-pacing case where 3 passives offer when player has 3 empty tech slots screaming to be filled.

### Card Behavior on Pick — Mirror VS

Cards behave identically whether new pickup or level-up:

- Card not in loadout → take it → enters slot at L1
- Card already at LN → take it → L(N+1)

UI shows current level on the card face. Player doesn't track "is this new or a level-up" — the card simply progresses.

---

## Card Damage Envelope and Level Scaling (Locked 2026-05-22)

The damage envelope each card delivers, and how level-ups scale it. Per-card content variance (which level adds pierce vs area vs damage etc.) deferred to per-card design pass; the envelope below is what the scaling math closes against.

### Per-Archetype DPS Envelope at L1

Reference single-target DPS for a card at L1, no buffs, baseline player (Atk = 10). Per-card variance around the archetype reference is a design-pass concern; envelope numbers anchor the math.

| Archetype | Single-target DPS | Multi-target effectiveness | Per-hit feel (illustrative) |
|---|---|---|---|
| **Strike** | 6 | 1.0× (adjacent only) | 6 dmg × 1.0 hit/sec |
| **Projectile** | 5 | 1.0× (line) | 3.3 dmg × 1.5 hit/sec |
| **Orbital** | 4 | 1.5× (sweeps groups) | 2 dmg × 2.0 hit/sec |
| **Zone** | 3 | 3–4× (DoT across area) | 1.5 dmg × 2.0 hit/sec |

**Role rationale:**
- Strike anchors single-target. High per-hit damage, weak vs hordes.
- Zone weakest single-target but multi-target effectiveness makes it the field-control archetype (VS Garlic profile).
- Projectile and Orbital sit between, differentiated by movement pattern.
- base_atk = 10 acts as the global "Might" multiplier; if base_atk grows (Teahouse Atk track), all archetypes scale 1:1.

### Card Level Scaling — Even Multiplicative, L8 = 2.0× Endpoint

Each card level multiplies damage by ~+10.4% on top of the previous level. L1 = 1.0×, L8 = 2.0×.

| Level | Multiplier |
|---|---|
| L1 | 1.00× |
| L2 | 1.10× |
| L3 | 1.22× |
| L4 | 1.34× |
| L5 | 1.47× |
| L6 | 1.62× |
| L7 | 1.78× |
| L8 | 2.00× |

**Rationale:**
- 2.0× endpoint is intentionally smaller than VS-style ×5-10 per-card scaling — this game has Forge as a separate macro-permanent layer, so in-run leveling is the smaller of the two run-side levers. Forge handles the "permanent and earned" felt growth.
- Even shape (every level worth the same multiplicatively) keeps level-up draft decisions interesting at every level — not front-loaded (low levels matter most, late levels meh) and not back-loaded (early levels feel meh).
- Matches the per-minute enemy HP ramp (`1.10^minute`) almost exactly when players average ~1 level/minute, which the XP curve and wave density roughly support. Card-level scaling tracks enemy HP organically.

### Power-Source Timing — Three Layered Sources

In-run player power has three sources, each with different timing within a run:

| Source | Timing within run | Felt effect | Macro persistence |
|---|---|---|---|
| Slot-filling | Min 0-7 | Front-loaded; handles early ramp | None (rebuilds each run) |
| Card levels | Min 0-25 (even) | Tracks the `1.10^min` curve | None |
| Evolutions + Paths | Min 15-25 | Back-loaded; handles boss + late density | Forge tracks |

The three sources layer correctly without explicit engineering. Linear or back-loaded card scaling would break this layering.

### Per-Card Content (Deferred)

What each specific level grants (more damage / pierce / area / projectile count / duration / etc.) is per-card content — VS-style heterogeneous upgrades are interesting design but require per-card spec work. The envelope above is the math constraint. Per-card content lands in the per-card design pass.

---

## Evolution Slots (Conditional, Not Pool Entries)

Evolutions are not draft cards in the pool. They're a conditional slot that takes over one of the offered card positions when the trigger conditions are met.

- **Trigger condition:** technique X and its paired passive Y both reach level 8 (max).
- **Slot appearance:** on the next level-up draft AND on the next chest draft after the pairing becomes evo-eligible, one of the offered card positions becomes the evolution offer. Persists across every subsequent draft until taken.
- **Player choice:** the player can take the evolution or pick one of the other cards. If skipped, the evolution offer remains and reappears in every future draft until accepted.
- **Multiple evo-eligible pairings:** queue, oldest first. One evo slot per draft, never two simultaneously.
- **Effect of taking it:** the technique transforms into its evolved form, taking over the same technique slot. The paired passive persists unchanged in its passive slot — its effect continues. This follows the VS / Brotato / Halls of Torment convention: evolution replaces the technique but does not consume or fuse the passive.
- **Discovery:** pairings are hidden until first triggered. After the player first evolves Vine Whip + Rooted Stance, all future drafts tag both cards with "evolves with [partner]" hint text. Codex logs the discovery.

---

## Path Culmination Offer (Conditional, Chest-Only)

The full Path system mechanic lives in [systems/path-system.md](../systems/path-system.md). Short version of how it interacts with the run loop:

- **Chest-only offer.** Level-up drafts never offer path culminations. Chests do.
- **All-or-nothing trigger.** Every tech slot must be evolved AND every passive slot must be evolved AND every evolved pair must be a recipe member for the targeted path tier. Got 3 of 4 right, or 4 right with a wrong evolution = no culmination.
- **Recipe matches meridian count.** 4 meridians → only Sapling. 5 → only Sprout. … 8 → only Worldroot.
- **Effect of taking it:** the path activates. All evolved techs in the loadout visually fuse under the path's identity. The tier's effect applies. First-time discovery fires the celebration cinematic. Codex logs the path tier as discovered.
- **Player can skip.** Decline is offered (functional, not punished) — the offer reappears on every subsequent chest until taken or the run ends.
- **Not every evolution leads to a path.** Every card has an evolution partner, but only the specific recipe pairs trigger culmination. Off-recipe pairs still hit hard, they just don't contribute to a path. Build-tinkerers have real space here.

### Path Culmination Slot Occupancy (Locked 2026-05-22)

Path culmination takes **1 chest slot.** Not a bonus +1. Same visual treatment as evolution (distinct frame, "PATH" tag). Player picks culmination or one of the other offers in the chest.

### Conditional-Slot Interaction — Evo + Path in Same Chest (Locked 2026-05-22)

Evolution and path culmination can both appear in the same chest:

- Path culmination occupies 1 chest slot
- Evolution occupies 1 chest slot
- Remaining slots fill random from pool
- Player picks 1

Both are conditional, both are earned, both should be findable. The existing "one evo slot per draft, never two simultaneously" rule prevents two evolutions in one offer — path is a different conditional category and doesn't violate that rule.

---

## Day-1 Pool — 96 Cards

The starter pool is 12 themes × (4 techniques + 4 passives) = 96 cards. Every card is evolvable. Every theme has exactly the 4 evolved pairs that form its Sapling recipe.

### Archetype Taxonomy (Locked, Consistent Across All 12 Themes)

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

### Evolution Pairing Convention

- Strike ↔ Vitality
- Projectile ↔ Offense
- Orbital ↔ Utility
- Zone ↔ Special

The pairing convention is consistent so that once a player learns one theme's pattern they can experiment in others. Pairings still must be DISCOVERED — the player isn't told the convention; they figure it out through play.

### Card Naming (Placeholders — Full Naming Pass Later)

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

---

## Pool Growth Across the Game

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

---

## Rarity Weighting — REMOVED

Rarity is no longer a property of cards. All cards are equal — differentiated by theme, archetype, evolution partner, and path served. Card unlock timing (which cards are in your pool) is the only pacing axis at the card level. The "Common-skewed early, smoothing to 20/20/20/20/20" curve from v4 is cut.

---

## Meridians (Slot Progression)

Meridians are a **separate progression axis** from cultivation stages.

- Start with **4 technique slots + 4 passive slots** = 8 total cards in play
- Cap at **8 + 8** = 16 total cards in play
- Lore: every cultivator has 8 meridians anatomically; what changes is how many are **refined** enough to channel sustained technique flow.
- Refinement happens at the **Personal Sanctum**. Costs essence + tier-appropriate material. No boss-gating.
- Different path tiers require different slot counts. The path's manifestation tier matches the player's meridian count — at 6 mer, the player can culminate up to Grove tier.

### Meridian Refinement Pacing

| Refinement | Target meridian | Realm Position | Path tier enabled |
|---|---|---|---|
| 5th | Mer 5 | End of R3 | Sprout |
| 6th | Mer 6 | End of R5 | Grove |
| 7th | Mer 7 | End of R7 | Forest |
| 8th | Mer 8 | End of R10 | Worldroot |

Each refinement aligns with sufficient cards having been unlocked across all 12 themes that the player can plausibly build the next tier of any theme they're focused on. R11–R12 become pure mastery realms — paths fully manifested, player tests their build at maximum scale.
