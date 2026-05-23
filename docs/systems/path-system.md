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
- **Discovered paths can be permanently strengthened at the Soul Forge** (see [pillars/sect-management.md](../pillars/sect-management.md) and [systems/building-tier-curves.md](building-tier-curves.md)).

---

## Forge Interaction

Each discovered path tier becomes an individual Forge upgrade track. Wood Sapling is one track; Wood Sprout (when discovered) is a separate track; Wood Grove is another; etc. 12 themes × 5 tiers = up to 60 path-tier tracks at endgame.

- **Per-tier independence.** Each track has 10 levels, each +10% to that tier's effect, max +100% per tier.
- **No inter-tier unlock gating.** A 5-meridian player who's culminated Wood Sapling and Wood Sprout can forge both immediately. No "Sapling must be maxed before Sprout unlocks."
- **Discovery is the natural gate.** A path tier must be culminated in a run before its Forge track appears.
- **Tier effects stack and stay forgeable.** Sapling's effect keeps running at Worldroot; forging Wood Sapling at +10 means a +100% heal-per-kill effect still applies even when the player culminates higher tiers in a run.

**What +10% scales is a designer call per effect.** Wood Sapling = heal amount. Metal Sapling = crit chance / crit damage. Fire Sapling = explosion damage or radius. For structural effects like "Worldtree manifests pulsing AoE damage periodically," the designer picks whether +10% applies to damage, radius, frequency, or all three. Flagged for the 48-path-effect design pass — each effect needs its scaling target spelled out when designed.

---

## Path Bundle Math Envelope (Locked 2026-05-22)

The damage-stack multiplier from culminated paths. Per-effect content (the 48 path effects) lands in the design pass; the envelope below is what the scaling math closes against.

### Bundle Composition

Path contributions compose into one multiplier in the broader damage stack:

```
path_bundle = 1 + Σ(tier_contribution × forge_track_mult)
```

- **Across themes:** additive within bundle (Wood Worldroot + Metal Worldroot sum).
- **Across tiers within a theme:** additive (Sapling stays active when Worldroot activates — all five tiers layer simultaneously per the additive-tier rule above).
- **Forge track multiplies each tier's contribution.** Sapling at Forge L10 = +20% × 2 = +40%. No Forge investment = +20% baseline.

### Per-Tier Contribution Envelope

Uniform across themes for math purposes. Per-theme balance is a design-pass concern; envelope sets the math constraint.

| Tier | Damage-equivalent contribution | Cumulative per theme (no Forge) | At Forge maxed (×2) |
|---|---|---|---|
| Sapling | +20% | +20% | +40% |
| Sprout | +40% | +60% | +120% |
| Grove | +60% | +120% | +240% |
| Forest | +100% | +220% | +440% |
| Worldroot | +200% | +420% | +840% |

**Damage-equivalent framing handles non-damage paths cleanly.** Wood healing extends uptime, Ice slow enables more hits, Spirit summons add DPS — all translate to effective DPS at some equivalent rate. Per-effect "damage-equivalent translation" needs explicit definition in the 48-effect design pass.

### Wind Sapling Exception

Wind's Sapling effect (global atk speed) maps to the attack-speed axis rather than direct damage. Should compose **additively with the Teahouse Attack Speed track** ([building-tier-curves.md](building-tier-curves.md) Teahouse Sixteen Tracks) rather than via the path bundle. Wind Sprout/Grove/Forest/Worldroot effects revert to bundle composition unless they too target stat axes. Flagged for design pass.

### Within-Run Timing — Late-Run Back-Loaded Power

Path culminations land mid-to-late run (min 15-25 typically). Loadout has to fill, evolutions land, then the specific recipe completes. This timing puts the path bundle as **late-run back-loaded power** — exactly when the `1.10^minute` enemy HP curve is biting hardest. Layered correctly alongside slot-filling (front-loaded) and card levels (continuous).

### Per-Theme Variance Caveats (for design pass)

- Wood (mostly utility) under-delivers vs Metal (pure damage) at same tier with the uniform envelope assumption. Specific themes can land at ±50% of envelope and rebalance through Forge scaling targets per tier.
- Non-damage Saplings (Wood heal, Ice slow, Spirit summon, Lightning chain) all need explicit damage-equivalent translation defined per-effect.
- Wind Sapling specifically routes to AS axis (above).

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

Sprout/Grove/Forest/Worldroot effects per theme: TBD when those tiers are reached in development. 48 layered effects to design (12 themes × 4 additional tiers). Each effect must also specify what +10% Forge upgrade scales on it.

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
