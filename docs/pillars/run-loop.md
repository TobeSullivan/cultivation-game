# Pillar 1 — VS Run Loop (Active)

**The only thing the player plays.** Movement only — autofire combat. Mobile-friendly even though PC-first.

---

## Run Structure

- **Length:** up to 30 minutes, hard cap.
- **End conditions:** complete all 6 universal objectives + defeat the boss = territory conquered.
- **Pacing:** parallel objectives + boss-trigger. Boss spawns when all other objectives are complete OR at the 25-minute mark, whichever comes first. Skilled/powered players can finish in 10 minutes; slower players take the full 30. Both paths win.
- **Pause-friendly:** runs can be paused/resumed cleanly. Generous handling on quit/disconnect — completed objectives bank even if the player drops out mid-run.

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

## Wave Composition

VS-classic continuous spawn baseline + objective-flavored wave shifts. Difficulty scales with **kill count / progression within the run**, not pure timer (so speedrunners don't fight baby enemies the whole run).

**Within-run enemy HP scaling:** `HP(t) = base × 1.10^minute`. By minute 25, ~10× initial HP. Spawn density grows from ~1.5 fodder/sec at 0:00 to ~30+/sec at 25:00.

---

## Replays of Conquered Regions

- Same map, same enemies, same boss, same drops
- Banked objectives stay banked (no FOMO on missing unlocks)
- Resources, XP, materials still flow normally
- The named realm-final boss does **not** respawn after defeat. A generic boss appears at the 5- or 10-minute mark instead.
- Replays are 100% player choice — they grind because they want to (XP, materials, flexing, nostalgia). The game doesn't push or pull them.

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
- **Run-start pick:** first card is selected before the run begins via a card selection screen (not via an awkward instant-level-up at run start, which VS handles poorly). The selection pool is the player's full currently-unlocked card pool — day-1 sees 96 cards, endgame sees ~444. The player picks any one card (technique or passive) to start the run with at level 1.
- **Skip / Reroll / Banish:** all exist, all start at 0, all earned via macro progression. Per-run charges.

---

## Evolution Slots (Conditional, Not Pool Entries)

Evolutions are not draft cards in the pool. They're a conditional slot that takes over one of the offered card positions when the trigger conditions are met.

- **Trigger condition:** technique X and its paired passive Y both reach level 8 (max).
- **Slot appearance:** on the next level-up draft AND on the next chest draft after the pairing becomes evo-eligible, one of the offered card positions becomes the evolution offer. Persists across every subsequent draft until taken.
- **Player choice:** the player can take the evolution or pick one of the other cards. If skipped, the evolution offer remains and reappears in every future draft until accepted.
- **Multiple evo-eligible pairings:** queue, oldest first. One evo slot per draft, never two simultaneously.
- **Effect of taking it:** the technique transforms into its evolved form, consuming or fusing with the paired passive depending on the pairing's design.
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
