# Prototype Scope — R1–R3

Build-ready details for the 8-map prototype. Scope: R1 (2 maps) + R2 (3 maps) + R3 (3 maps) = 8 maps + 3 realm-finals. All 8 building unlocks compressed into this range. Stages 1–3 complete (no inspiration required). 5th meridian refined at end of R3.

Companion files:
- [bosses.md](bosses.md) — full per-map boss profile, combat data, region objectives
- [rewards.md](rewards.md) — per-objective rewards, partner-passive distribution, per-map quantities

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
| R2 M2 | 1.6 | 1 | 2–3 | Generous |
| R2 M3 | 2.2 | 2 | 3 | Generous→Tight |
| R3 M1 | 2.0 | 1 | 3 | Tight on basics |
| R3 M2 | 2.3 | 1 | 3 | Reasonable |
| R3 M3 | 3.0 | 2 | 4 | Generous→Tight |

Curve holds. Each realm-final is the toughest in its realm. Each new realm's gateway boss is slightly tougher than the previous realm's final. No spikes.

Headroom preserved for R4–R12 escalation: attack count grows slowly to ~5 by R12, phases reach 3–4 at most. Escalation is primarily through tighter telegraphs, attack overlap, and arena interaction, not more moves.

---

## What's Deferred for the Tuning Pass

- Exact HP/damage numbers (relative baselines locked; absolute numbers anchored to player baseline Atk 10, HP 100, fodder HP 8 R1 baseline)
- Per-card per-level variance within archetypes (archetype baselines locked in v6 master doc)
- Per-enemy-type behavior quirks (does brew-imp lob bottles, does stone-wolf charge in packs)
- Drop rate % within categories
- Forge upgrade cost curves beyond Forge T1
- T2–T5 leaf content for 6 buildings (Recruitment / Training / Storehouse / Outer Court / Library / Forge); Teahouse + Pavilion fully spec'd in [building-tier-curves](../systems/building-tier-curves.md)
- Wave composition per map (fodder/elite spawn timing)
- Library cycle climb economy
- Naming pass (all current names are placeholders)
