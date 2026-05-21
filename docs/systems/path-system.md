# Path System

Paths are the build mechanic. Themes have no DoT or damage-type mechanics — they're identity markers for path membership.

Mechanically, paths are recipe-discovery puzzles that pay off as celebratory power spikes inside a VS run. The trigger flow (chest-only offer, all-or-nothing) lives in [pillars/run-loop.md](../pillars/run-loop.md). This file holds the path's structure and content.

---

## Structure

- **One path per theme. 12 themes = 12 paths.**
- **Each path manifests at 5 tiers**, gated by meridian count: Sapling (4 mer), Sprout (5), Grove (6), Forest (7), Worldroot (8).
- **Tiers are additive.** Sapling's effect persists; Sprout adds a new effect on top of Sapling; Grove adds on top of those; etc. By Worldroot the path expresses all 5 layered effects simultaneously.
- **Trigger:** the player must evolve the SPECIFIC pairs that form the current meridian tier's recipe. Drafting any 4 theme pairs isn't enough — it has to be the right 4. The recipe is additive: Sapling = 4 specific pairs, Sprout = those 4 + 1 specific new pair, etc.
- **Discovery-driven.** Recipes are hidden until first culminated. When the player evolves the right combination in a run, the path culmination chest offer appears. Codex logs the discovery. Future drafts tag those cards with "contributes to [Path Name]" hints.
- **Chest-only offer.** Path culminations never appear in level-up drafts. Only chests.
- **First-time discovery = celebration moment.** Camera zooms, world dims, character glows in path's theme color, calligraphy-styled name reveal, brief audio sting, ~1.5 sec.
- **Discovered paths can be permanently strengthened at the Soul Forge** (see [pillars/sect-management.md](../pillars/sect-management.md)).

---

## The 12 Sapling Effects

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

Sprout/Grove/Forest/Worldroot effects per theme: TBD when those tiers are reached in development. 48 layered effects to design (12 themes × 4 additional tiers).

---

## The Wood Path (Worked Example)

| Tier | Meridians | Loadout requirement | Layered effect added |
|---|---|---|---|
| **Wood: Sapling** | 4 | 4+4 specific Wood pairs evolved | Heal small amount per kill |
| **Wood: Sprout** | 5 | Sapling + 1 specific new Wood pair evolved | + Evolved Wood techs gain damage boost |
| **Wood: Grove** | 6 | Sprout + 1 specific new Wood pair evolved | + Entangling vines spawn on hit, briefly rooting enemies |
| **Wood: Forest** | 7 | Grove + 1 specific new Wood pair evolved | + Worldtree manifests, pulsing AoE damage periodically |
| **Wood: Worldroot** | 8 | Forest + 1 specific new Wood pair evolved | + All Wood tech effects double in size; healing motes restore qi |

Same identity (renewal, growth, entanglement, life) at every tier; the scale and richness grow with the player.

---

## The Righteous Path (13th Path, Capstone)

The capstone path that sits outside the 12-theme framework.

- 13th path, structurally separate from Sapling→Worldroot. Combines all 12 themed paths into one.
- **Recipe:** 8 specific evolution pairs sourced from R4–R11 realm-final signatures + their evo-partner passives
- Each of the 8 component pairs is of a different existing theme (8 of 12 themes contribute; which 8 deferred)
- **Discoverable only in infinite/endgame mode after R12 conquered**
- Codex tracks separately (sits outside the 12-path framework)
- R12 realm-final is the **capstone fight** — final boss tier resolved (R12 IS the final boss tier)
- R12 realm-final still drops a normal themed signature like every other boss (per the disciple schema) — that signature is an ordinary R12-power off-recipe card, not a Righteous Path component
- Culmination effect: fundamentally new layer (e.g., all 8 techniques chain across themes, or every kill triggers a cross-theme cascade) — not just bigger numbers. Specifics deferred until R12 design work.
