# Prototype Scope — R1–R3

Build-ready details for the 8-map prototype. Scope: R1 (2 maps) + R2 (3 maps) + R3 (3 maps) = 8 maps + 3 realm-finals. All 8 building unlocks compressed into this range. Stages 1–3 complete (no inspiration required). 5th meridian refined at end of R3.

**Prototype scope explicitly includes shippable opening flow + per-surface art + audio assets, not just R1–R3 mechanics.** Surface and asset inventory tracked in [design-pass.md](design-pass.md).

Companion files:
- [design-pass.md](design-pass.md) — surface, art, audio, pipeline inventory
- [bosses.md](bosses.md) — full per-map boss profile, combat data, region objectives
- [rewards.md](rewards.md) — per-objective rewards, partner-passive distribution, per-map quantities

---

## The 8 Maps — Master Table

| # | Map | Boss | Specialty | Building | Theme | Archetype | Body-Part | Starting Rating | Meridian Count |
|---|---|---|---|---|---|---|---|---|---|
| 1 | R1 M1 | Lady Yun | Charisma | Recruitment Hall | Wood | Zone | Legs | 5 | 5 |
| 2 | R1 M2 | Master Pao | Brewer | Teahouse | Water | Projectile | Arms | 5 | 6 |
| 3 | R2 M1 | Warden Bao | Trainer | Training Hall | Earth | Strike | Legs | 5 | 5 |
| 4 | R2 M2 | Steward Mei | Organizer | Storehouse | Metal | Orbital | Body | 5 | 5 |
| 5 | R2 M3 | Magistrate Hong | Administrator | Outer Court | Fire | Zone | Head | 5 | 6 |
| 6 | R3 M1 | Archivist Wen | Scholar | Library | Lightning | Projectile | Head | 5 | 6 |
| 7 | R3 M2 | Augur Lin | Heaven-Reader | Ascension Pavilion | Wind | Orbital | Body | **7** | **7** |
| 8 | R3 M3 | Smith Tian | Smith | Soul Forge | Ice | Strike | Arms | 5 | 7 |

Coverage check:
- Themes: 8 of 8 elementals used, all unique. Shadow/Spirit/Star/Void reserved for Transcendent+.
- Archetypes: Strike ×2, Projectile ×2, Orbital ×2, Zone ×2.
- Body parts: Head ×2, Arms ×2, Legs ×2, Body ×2.
- R1–R3 boss names locked via polish pass (2026-05-21); 96 day-1 card names still placeholders.

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

## Sect Hub Starting State

Two head-only buildings exist in the sect hub from first launch — they do not unlock through map conquest:

- **Main Hall** — hub, head's seat, Sect Power widget. Run by the head.
- **Personal Sanctum** — meridian refinement, cycling assignment, tier and stage breakthroughs. Run by the head.

Neither has a Master designation or specialty chain. The hub holds **10 buildings total in prototype**: these 2 head-only + the 8 specialty buildings below.

See [pillars/sect-management.md](../pillars/sect-management.md) for the full 10-building table and [prototype/design-pass.md](design-pass.md) for hub UI specifications.

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

## Prototype Tier State (LOCKED)

| Building | Master | Starting Rating | Tiers Purchasable in Prototype |
|---|---|---|---|
| Recruitment Hall | Yun | 5 | T1–T5 |
| Teahouse | Pao | 5 | T1–T5 |
| Training Hall | Bao | 5 | T1–T5 |
| Storehouse | Mei | 5 | T1–T5 |
| Outer Court | Hong | 5 | T1–T5 |
| Library | Wen | 5 | T1–T5 |
| Ascension Pavilion | Lin | **7** (Heaven-Reader exception) | **T1–T7** |
| Soul Forge | Tian | 5 | T1–T5 |

Tier ceiling = Master's starting rating. Purchasing tiers costs essence + materials (+ spirit stones at T5+) per the [building tier cost table](../systems/building-tier-curves.md).

---

## Enemy Categories

Each map has 4–6 fodder types + 2–3 elite types (visual/biome variation; mechanically baseline).

### Boss Anchor

**Lady Yun (R1 M1 boss) = 800 HP, 8 contact damage.** All other prototype boss numbers in [bosses.md](bosses.md) are stated as relatives to Yun = 1.0× and back-solve from this anchor.

### R1 M1 Minute-0 Absolute Values

| Category | HP | Contact dmg | Speed |
|---|---|---|---|
| Fodder | 8 | 3 | 0.5–0.9× player |
| Elite | 100 | 6 | 0.4× |
| Mini-boss | 400 | 10 | 0.5× |
| Boss (Yun) | 800 | 8 | varies |

Damage relatives (vs Yun's 8): Fodder 0.4×, Elite 0.8×, Mini-boss 1.2×, Boss 1.0×.

Spawn cadence, slot timing, and aggro behavior live in [run-loop.md](../pillars/run-loop.md) Wave Composition section.

### Drops

- **Fodder:** raw qi (~1 per kill ambient), occasional spirit stones
- **Elite:** chest (3–5 cards) + tier-appropriate materials
- **Mini-boss:** larger chest (5 cards) + better materials
- **Boss:** see [rewards.md](rewards.md) for the full per-objective table

### Scaling Rules

**Per-realm scaling:** R1 = 1×, R2 = 1.5×, R3 = 2×. Both HP and damage scale; speed/behavior constant. Applies to all categories including bosses. Same factors also apply to wave `min_alive` (capped at 300) per [run-loop.md](../pillars/run-loop.md) Wave Composition.

**Within-run HP scaling (fodder / elite / mini-boss only):** `HP(t) = base × 1.10^minute`. By minute 25, ~10× initial HP.

**Bosses are exempt from within-run scaling.** Boss HP is absolute at encounter time. A speedrunner who pops the boss at minute 10 fights the same HP as a slow player at minute 25 — but with less card growth available, so the encounter is meaningfully harder. Skill signal preserved without making boss HP "feel" inflated.

**Generic boss on replay:** the named realm-final doesn't respawn. Generic boss with mini-boss stats × ~2 appears at 5- or 10-min mark instead.

### Per-Map Slot-Fire Counts (Locked 2026-05-22)

Each map decides which of the wave template's 8 elite slots and 4 mini-boss slots actually fire. Difficulty ramp:

| Map | Elite slots fire | Mini-boss slots fire |
|---|---|---|
| R1 M1 | 4 of 8 | 1 of 4 |
| R1 M2 | 5 of 8 | 2 of 4 |
| R2 M1 | 5 of 8 | 2 of 4 |
| R2 M2 | 6 of 8 | 2 of 4 |
| R2 M3 | 7 of 8 | 3 of 4 |
| R3 M1 | 6 of 8 | 3 of 4 |
| R3 M2 | 7 of 8 | 3 of 4 |
| R3 M3 | 8 of 8 | 4 of 4 |

Slot-fire counts cleanly satisfy Targets-objective elite requirements at natural pacing (e.g. R1 M1 wants 3 elites, fires 4 slots — first 3 bank the objective, 4th is bonus chest). The named enemy per fired slot draws from the realm roster below.

---

## Realm Enemy Rosters (Locked 2026-05-22)

Rosters authored **per realm**, not per map. Genre convention — VS ships ~138 normal + 58 boss enemies across 54 stages with heavy cross-stage reuse; HoT pools by hall biome. Maps within a realm share a roster with light biome-specific swaps.

Bosses stay per-map unique (119 across the full game, 8 in prototype). Fodder, elites, and mini-bosses are realm-pool.

### R1 Roster

5 fodder + 3 elites + 2 mini-bosses = 10 designs for 2 maps.

**Fodder pool** (8 HP / 3 dmg base):

| Name | Speed | Fields on |
|---|---|---|
| Footpath Bandit | 0.6× | both maps |
| Stray Spirit | 0.7× | both maps |
| Wandering Mongrel | 0.7× | both maps |
| Bamboo Sprite | 0.8× | M1 only (Bamboo Hollow / Wood biome) |
| Hot-Spring Boar | 0.6× | M2 only (Cauldron Springs / Water biome) |

Each map fields 4 fodder: 3 universal + 1 biome.

**Elite pool** (100 HP / 6 dmg base):

| Name | Fields on |
|---|---|
| Bandit Captain | both maps |
| Ancient Grove Spirit | M1 only |
| Cauldron Construct | M2 only |

Each map fields 2 elites (1 universal + 1 biome), rotated across the fired elite slots.

**Mini-boss pool** (400 HP / 10 dmg base):

| Name | Fields on |
|---|---|
| Mountain Bandit Chief | both maps |
| Drunken Brewmaster | M2 only (foreshadows Pao's Bottle Lob) |

R1 M1 fires 1 mini-boss slot (Mountain Bandit Chief). R1 M2 fires 2 (Mountain Bandit Chief + Drunken Brewmaster).

### R2 Roster

7 fodder + 4 elites + 3 mini-bosses = 14 designs for 3 maps. R2 ×1.5 modifier applies to HP/dmg/density per locks above.

**Fodder pool** (8 HP / 3 dmg base → R2 effective 12 HP / 4.5 dmg):

| Name | Speed | Fields on |
|---|---|---|
| Hill Bandit | 0.6× | all 3 maps |
| Frontier Shade | 0.7× | all 3 maps |
| Plains Stalker | 0.7× | all 3 maps |
| Stone Wolf | 0.7× | M1 only (Iron Ridge) |
| Rockslide Spirit | 0.5× | M1 only (Iron Ridge) |
| Rogue Clerk | 0.6× | M2 only (Brassgate) |
| Rogue Tax-Collector | 0.6× | M3 only (Stone Keep) |

M1 fields 5 (3 universal + 2 biome); M2 and M3 field 4 (3 universal + 1 biome) and rely on density and slot count for intensity.

**Elite pool** (100 HP / 6 dmg base → R2 effective 150 HP / 9 dmg):

| Name | Fields on |
|---|---|
| Captain (regional bandit lord) | all 3 maps |
| Training-Dummy Construct | M1 only |
| Paperwork Golem | M2 only |
| Sigil-Bound Enforcer | M3 only |

Each map fields 2 elites: 1 universal + 1 biome.

**Mini-boss pool** (400 HP / 10 dmg base → R2 effective 600 HP / 15 dmg):

| Name | Fields on |
|---|---|
| Garrison Drill-Master | M1 (foreshadows Bao's Drill Stomp) |
| Records-Hall Sealkeeper | M2 (foreshadows Mei's Brass Ledger orbital) |
| Court Inquisitor | M3 (foreshadows Hong's Sovereign's Gaze cone) |

Each map uses its own mini-boss across all its fired mini-boss slots — repetition reinforces the boss's signature mechanic before encounter.

### R3 Roster

8 fodder + 1 reskin + 4 elites + 3 mini-bosses = 16 designs for 3 maps. R3 ×2.0 modifier applies.

**Fodder pool** (8 HP / 3 dmg base → R3 effective 16 HP / 6 dmg):

| Name | Speed | Fields on |
|---|---|---|
| Rogue Apprentice | 0.6× | all 3 maps |
| Wandering Shade | 0.7× | all 3 maps |
| Beast-Spirit | 0.7× | all 3 maps |
| Dust-Spirit | 0.8× | M1 only (Ash Archives) |
| Text-Golem | 0.5× | M1 only (Ash Archives) |
| Cloud-Wraith | 0.7× | M2 only (Skygate) |
| Wind-Riding Shade | 0.9× | M2 only (Skygate) |
| Frost-Iron Lesser Golem | 0.5× | M3 only (Frostforge) |
| Hammer-Broken Apprentice (Rogue Apprentice reskin) | 0.6× | M3 only (Frostforge) |

Each map fields 5: 3 universal + 2 biome. M3's second biome slot is a Forge-flavored reskin of Rogue Apprentice (specifically broken-by-Tian — narrative payoff).

**Elite pool** (100 HP / 6 dmg base → R3 effective 200 HP / 12 dmg):

| Name | Fields on |
|---|---|
| Inner Disciple | all 3 maps |
| Knowledge-Hungry Shade | M1 only |
| Tribulation-Marked Apprentice | M2 only |
| Forge-Bound Spirit | M3 only |

Each map fields 2 elites: 1 universal + 1 biome.

**Mini-boss pool** (400 HP / 10 dmg base → R3 effective 800 HP / 20 dmg):

| Name | Fields on |
|---|---|
| Senior Archivist | M1 (foreshadows Wen's Verse Flurry + branding) |
| Augur-Apprentice | M2 (foreshadows Lin's Augury Wheel) |
| Anvil-Spirit | M3 (foreshadows Tian's Hammer Slam + Cold Forging) |

R3 M3 fires all 4 mini-boss slots with Anvil-Spirit — repetition reinforces the Cold-Forging-stack mechanic ahead of the Tian fight.

### Prototype Total Roster

| Realm | Fodder | Elites | Mini-bosses | Bosses |
|---|---|---|---|---|
| R1 | 5 | 3 | 2 | 2 |
| R2 | 7 | 4 | 3 | 3 |
| R3 | 8 (+1 reskin) | 4 | 3 | 3 |
| **Total** | **21 (+1)** | **11** | **8** | **8** |

**48 unique enemy designs across the 8-map prototype.** Genre-feasible — VS Mad Forest alone uses ~17 unique types per stage. We average ~6 unique per map plus boss, with strong cross-map reuse within each realm.

### Universal Climbing Fodder Convention

Three universal fodder archetypes (humanoid / ghost / beast) reskin per realm to reflect the realm's tier:

| Archetype | R1 | R2 | R3 |
|---|---|---|---|
| Humanoid | Footpath Bandit | Hill Bandit | Rogue Apprentice |
| Ghost | Stray Spirit | Frontier Shade | Wandering Shade |
| Beast | Wandering Mongrel | Plains Stalker | Beast-Spirit |

R1 = mortal-tier bandits and spirits. R2 = frontier-tier regional opponents. R3 = kingdom-tier cultivator-types. Pattern continues into R4–R12 (Transcendent → Immortal → Divine → Eternal eras), with archetype names climbing accordingly.

---

## Difficulty Curve Check

| Map | HP | Phases | Attacks | Telegraph |
|---|---|---|---|---|
| R1 M1 | 1.0 | 1 | 2 | Maximum |
| R1 M2 | 1.3 | 1 | 2 | Very generous |
| R2 M1 | 1.5 | 1 | 2 | Generous |
| R2 M2 | 1.6 | 1 | 2–3 | Generous |
| R2 M3 | 2.2 | 2 | 3 | Generous→Tight |
| R3 M1 | 2.0 | 1 | 3 | Tight on basics |
| R3 M2 | 2.3 | 1 | 3 | Reasonable |
| R3 M3 | 3.0 | 2 | 4 | Generous→Tight |

Curve holds. Each realm-final is the toughest in its realm. Each new realm's gateway boss is slightly tougher than the previous realm's final. No spikes.

Headroom preserved for R4–R12 escalation: attack count grows slowly to ~5 by R12, phases reach 3–4 at most. Escalation is primarily through tighter telegraphs, attack overlap, and arena interaction, not more moves.

---

## What's Deferred for the Tuning Pass

- **Per-enemy-type behavior quirks** (does brew-imp lob bottles, does stone-wolf charge in packs, do golems summon, do shades phase) — deferred to post-tuning behavior pass
- **Damage variance within a category** (flat per category locked tranche 4 for prototype; per-enemy-type damage flavor desired long-term)
- **XP variance within a category** (flat per category locked tranche 4 for prototype; per-enemy-type variation desired long-term)
- **Per-card per-level variance within archetypes** (archetype baselines locked in v6 master doc)
- **Drop rate %** within categories (spirit stone drop rate from fodder, etc.)
- **Forge upgrade cost curves beyond Forge T1**
- **T2–T5 leaf content for 6 buildings** (Recruitment / Training / Storehouse / Outer Court / Library / Forge); Teahouse + Pavilion fully spec'd in [building-tier-curves](../systems/building-tier-curves.md)
- **Per-map wave authoring** — default wave template locked tranche 4 ([run-loop.md](../pillars/run-loop.md)); per-map wave content overrides (which specific enemies fill each minute's active enemies field) deferred to per-map content pass
- **Library cycle climb economy**
- **Naming pass** — R1–R3 boss names + 16 signature/partner cards LOCKED (2026-05-21). 96 day-1 card names still placeholders; full title-ladder pass across all 20 chains deferred (see [open-questions.md](../open-questions.md))
