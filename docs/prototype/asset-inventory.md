# Asset Inventory — Prototype Production Tracker

Production-state tracking for every prototype asset. Updated as the Ludo pipeline runs.

Companion to [design-pass.md](design-pass.md) (specs) and [../tech-stack.md](../tech-stack.md) (production pipeline).

---

## Status Legend

- **TODO** — not started
- **BRIEFED** — given to Ludo, iterating
- **GENERATED** — first pass complete, evaluating
- **LOCKED** — final asset chosen
- **IN REPO** — placed in `res://assets/` (deferred until Godot project exists)

---

## Style Locks (2026-05-23, updated session 2)

| Lock | Value | Source |
|---|---|---|
| Art style — architecture | Hand-painted illustrated 2D, Avatar TLA aesthetic family (painterly cel-shading, visible brushwork) | User decision 2026-05-23 |
| Art style — backdrop landscape layers | Flat vector with hard shape gradients, deep blue palette | Accepted tool-reality 2026-05-23 session 2 (Ludo holds painted style reliably on architecture, drifts to flat vector on landscape — both styles coexist via parallax depth) |
| Camera angle | Front-facing 2D skyline | Revised 2026-05-23 session 2 (was 3/4 angled top-down — abandoned with architecture pivot) |
| Hub architecture | 6-layer parallax stack: sky / mountains / clouds / mist / buildings / crowd FG | Locked 2026-05-23 session 2 |
| Reference 1 — Characters family | Avatar TLA character lineup | Existing |
| Reference 1 — Environments + buildings family | Avatar TLA environment screenshot (Air Temple establishing shot) | New 2026-05-23 |
| Locked Reference 2 — Backdrop layers | Mountains layer locked 2026-05-23 session 2 | New |
| Ludo Pipeline | See [design-pass.md > Asset Pipeline](design-pass.md#asset-pipeline) | Verified 2026-05-23 |
| Generate-then-Edit pattern | Two-step: Generate New on opaque background → Edit Image to strip background | Locked 2026-05-23 session 2 |

**Architecture pivot 2026-05-23 session 2:** Original iso compound architecture (background plate + 10 iso building sprites) abandoned. The building-isometric-vs-plate-perspective open question is resolved by the pivot — front-facing skyline puts buildings and backdrop on the same camera orientation. Original `stone_floor.png` plate INVALIDATED.

---

## Character Art

### Sect Head presets

| Asset | Status | Date | Repo path | Notes |
|---|---|---|---|---|
| MC preset (V2 Image 1) | LOCKED | 2026-05-20 | `res://assets/characters/player/` (pending) | Reference image for all character generations |
| Preset 2 (V1 male) | LOCKED | 2026-05-20 | (pending) | V1–V5 session |
| Preset 3 (V3 mystic A) | LOCKED | 2026-05-20 | (pending) | |
| Preset 4 (V3 mystic B) | LOCKED | 2026-05-20 | (pending) | |
| Preset 5 (V4 master A) | LOCKED | 2026-05-20 | (pending) | |
| Preset 6 (V4 master B) | LOCKED | 2026-05-20 | (pending) | |
| Preset 7 (V5 variant A) | LOCKED | 2026-05-20 | (pending) | |
| Preset 8 (V5 variant B) | LOCKED | 2026-05-20 | (pending) | |

### Sect Head animations (8 presets × 4 anims = 32)

| Preset | Idle | Walk | Hit | Defeat |
|---|---|---|---|---|
| MC | TODO | TODO | TODO | TODO |
| Preset 2 | TODO | TODO | TODO | TODO |
| Preset 3 | TODO | TODO | TODO | TODO |
| Preset 4 | TODO | TODO | TODO | TODO |
| Preset 5 | TODO | TODO | TODO | TODO |
| Preset 6 | TODO | TODO | TODO | TODO |
| Preset 7 | TODO | TODO | TODO | TODO |
| Preset 8 | TODO | TODO | TODO | TODO |

### Sect Head portraits (carousel + breakthrough cutscenes)

| Preset | Portrait |
|---|---|
| MC | TODO |
| Preset 2 | TODO |
| Preset 3 | TODO |
| Preset 4 | TODO |
| Preset 5 | TODO |
| Preset 6 | TODO |
| Preset 7 | TODO |
| Preset 8 | TODO |

### Bosses (8 sprites + 32 anims + 8 portraits)

| Boss | Sprite | Idle | Walk | Attack | Aura | Portrait |
|---|---|---|---|---|---|---|
| Lady Yun (R1 M1) | TODO | TODO | TODO | TODO | TODO | TODO |
| Master Pao (R1 M2) | TODO | TODO | TODO | TODO | TODO | TODO |
| Warden Bao (R2 M1) | TODO | TODO | TODO | TODO | TODO | TODO |
| Steward Mei (R2 M2) | TODO | TODO | TODO | TODO | TODO | TODO |
| Magistrate Hong (R2 M3) | TODO | TODO | TODO | TODO | TODO | TODO |
| Archivist Wen (R3 M1) | TODO | TODO | TODO | TODO | TODO | TODO |
| Augur Lin (R3 M2) | TODO | TODO | TODO | TODO | TODO | TODO |
| Smith Tian (R3 M3) | TODO | TODO | TODO | TODO | TODO | TODO |

### Enemies (per-region fodder + elite, static only)

| Region | Fodder count | Elite count | Status |
|---|---|---|---|
| R1 M1 (Bamboo Hollow) | 3–4 | 1–2 | TODO |
| R1 M2 (Cauldron Springs) | 3–4 | 1–2 | TODO |
| R2 M1 (Iron Ridge) | 3–4 | 1–2 | TODO |
| R2 M2 (Brassgate) | 3–4 | 1–2 | TODO |
| R2 M3 (Stone Keep) | 3–4 | 1–2 | TODO |
| R3 M1 (Ash Archives) | 3–4 | 1–2 | TODO |
| R3 M2 (Skygate) | 3–4 | 1–2 | TODO |
| R3 M3 (Frostforge) | 3–4 | 1–2 | TODO |

---

## Building Art

### Backdrop layer stack (skyline composition)

| Layer | Status | Date | Notes |
|---|---|---|---|
| Sky | Godot-native | n/a | Solid color or gradient in Godot scene; no Ludo asset. Allows time-of-day tinting via shader/color swap. |
| Mountains | LOCKED | 2026-05-23 s2 | Flat vector, deep blues, hard shape gradients. Back layer, static or slow parallax. Source: Generate New from env Reference 1, kept as 2nd of 2 batch. |
| Clouds | LOCKED | 2026-05-23 s2 | Transparent PNG, white forms with light-blue underlining. Source: Edit Image on the same mountain-scene source, "Remove mountains and mist, keep only clouds." Drifts horizontally in Godot. |
| Mist | Godot-native | n/a | Hand-authored sprites (soft, low-opacity, additive blend, slow drift). Ludo's mist output didn't match painted source; Godot-native fits better and is cheaper. |

### Invalidated assets (architecture pivot)

| Asset | Status | Notes |
|---|---|---|
| Sect compound background plate (`stone_floor.png`) | INVALIDATED 2026-05-23 s2 | Original iso compound architecture abandoned. Plate no longer in the layer stack. Kept in Ludo Favorites for archive only. |

### Buildings (10 individual sprites, composited at runtime over backdrop)

| Building | T1 | T4 | Notes |
|---|---|---|---|
| Main Hall (head-only) | TODO | n/a | Session 1 iso gens INVALIDATED by architecture pivot. Regeneration pending in front-facing skyline register; will be first test of building style register open question. |
| Personal Sanctum (head-only) | TODO | n/a | Single state per existing scope (status open — see Open Questions in design-pass.md) |
| Recruitment Hall | TODO | TODO | |
| Teahouse | TODO | TODO | |
| Training Hall | TODO | TODO | |
| Storehouse | TODO | TODO | |
| Outer Court | TODO | TODO | |
| Library | TODO | TODO | |
| Ascension Pavilion | TODO | TODO | T7-cap building |
| Soul Forge | TODO | TODO | |

*Note: head-only "single state" framing is a pre-existing discrepancy with Surface 5's "10 × 2 = 20" framing — flagged in [design-pass.md open questions](design-pass.md#open-questions-post-design-pass), still open after architecture pivot. Both head-only buildings still exist in the skyline; tier-progression vs static decision pending.*

### Crowd FG silhouette pool (Locked 2026-05-23 session 2)

Pool of 9 unique silhouettes, all waist-up, back-facing (facing the sect), hands clasped behind back, pure black figures on transparent PNG. Composed in Godot at runtime — selection / scaling / distribution / sparse bob-shuffle tween handle population growth.

| # | Silhouette | Status | Notes |
|---|---|---|---|
| 1 | Upright topknot (male) | LOCKED | Original gen, the base pose |
| 2 | Bowed-head topknot (male) | LOCKED | Head slightly bowed, distinct profile from #1 |
| 3 | Ceremonial hat (court official) | LOCKED | Flat-top imperial hat, wider shoulder mantle |
| 4 | Long-hair tied back (male, low ponytail) | LOCKED | Unexpected output from elder prompt — hair-down silhouette variant |
| 5 | Long flowing hair (female) | LOCKED | Wind-blown asymmetric hair, strongest silhouette variant in the pool |
| 6 | High-bun (female) | LOCKED | Bun + side hair-loops, distinct top-of-head from #1 |
| 7 | Broad heavyset (male) | LOCKED | Body mass axis, completely different overall profile |
| 8 | Pointed hood | LOCKED | Monastic / mysterious register, hood reshapes head outline |
| 9 | Cowl hood (draping) | LOCKED | Softer hood variant, traveler / wanderer register |

Pool expandable later if needed (drift pattern: 10-12 was target, stopped at 9 once variety read as crowd). Bald monk attempted but cut (too similar to topknot at silhouette scale). Back-facing elder attempted twice, failed both — Ludo doesn't render back-view beards reliably; if elder is needed later, may need to accept front-facing as an outlier figure or skip entirely.

### Overlays (reused across buildings)

| Asset | Status | Notes |
|---|---|---|
| Lit window glow texture | TODO | Texture |
| Smoke wisp particle | TODO | Particle texture |
| Qi wisp particle | TODO | Particle texture |
| Dust mote particle | TODO | Particle texture |
| Lantern flicker | TODO | Texture + shader |
| Ambient sparkle | TODO | Particle texture |

---

## Environment / World

### Region biome assets (8 regions × ~4 each)

| Region | Ground tile | Prop 1 | Prop 2 | Prop 3 |
|---|---|---|---|---|
| R1 M1 (Bamboo Hollow) | TODO | TODO | TODO | TODO |
| R1 M2 (Cauldron Springs) | TODO | TODO | TODO | TODO |
| R2 M1 (Iron Ridge) | TODO | TODO | TODO | TODO |
| R2 M2 (Brassgate) | TODO | TODO | TODO | TODO |
| R2 M3 (Stone Keep) | TODO | TODO | TODO | TODO |
| R3 M1 (Ash Archives) | TODO | TODO | TODO | TODO |
| R3 M2 (Skygate) | TODO | TODO | TODO | TODO |
| R3 M3 (Frostforge) | TODO | TODO | TODO | TODO |

### World map + region state overlays

| Asset | Status |
|---|---|
| World map (parchment, Mortal-realm scope) | TODO |
| Fog overlay (locked state) | TODO |
| Pulse overlay (adjacent state) | TODO |
| Banner overlay (conquered state) | TODO |
| Focus ring overlay (gold glow + pulse) | TODO |

---

## Card Art

### Day-1 pool (96 cards)

12 themes × 8 cards each. Tracked as 12 theme blocks; populate per-card as names lock.

| Theme | Count | Status |
|---|---|---|
| Wood | 8 | TODO |
| Earth | 8 | TODO |
| Fire | 8 | TODO |
| Water | 8 | TODO |
| Metal | 8 | TODO |
| Wind | 8 | TODO |
| Ice | 8 | TODO |
| Lightning | 8 | TODO |
| Shadow | 8 | TODO |
| Spirit | 8 | TODO |
| Star | 8 | TODO |
| Void | 8 | TODO |

### Boss drop cards (16 — 8 signature + 8 partner)

| Boss | Signature | Partner |
|---|---|---|
| Yun | TODO | TODO |
| Pao | TODO | TODO |
| Bao | TODO | TODO |
| Mei | TODO | TODO |
| Hong | TODO | TODO |
| Wen | TODO | TODO |
| Lin | TODO | TODO |
| Tian | TODO | TODO |

### Evolved card variants

Count and identity deferred — depends on evolution-eligibility rules (see [open-questions.md](../open-questions.md)).

---

## VFX

| Category | Count target | Status |
|---|---|---|
| Strike archetype VFX | 1 base + 12 theme modifiers | TODO |
| Projectile archetype VFX | 1 base + 12 theme modifiers | TODO |
| Orbital archetype VFX | 1 base + 12 theme modifiers | TODO |
| Zone archetype VFX | 1 base + 12 theme modifiers | TODO |
| Pickup VFX (×6) | 6 | TODO |
| Damage/hit/crit sparks | 5 | TODO |

---

## UI / Iconography

| Category | Count | Status |
|---|---|---|
| Currency icons | 4 | TODO |
| Material icons (R1–R3 prototype) | 24 | TODO |
| Path icons (Sapling tier) | 12 | TODO |
| Objective icons | 6 | TODO |
| Building state icons | ~12 | TODO |
| HUD chrome | ~10 | TODO |
| Modal chrome | ~5 | TODO |
| Misc UI icons | ~10 | TODO |

---

## Splash / Title / Key Art

| Asset | Status |
|---|---|
| Studio mark | TODO |
| Title key art — foreground (MC silhouette) | TODO |
| Title key art — mid-ground (sect compound) | TODO |
| Title key art — background (sky) | TODO |
| Game logo typography | TODO |

---

## Audio

### Music (Suno)

| Track | Status |
|---|---|
| Title theme | TODO |
| R1 ambient | TODO |
| R2 ambient | TODO |
| R3 ambient | TODO |
| R1 boss (R1 M1) | TODO |
| R2 boss (shared R2 M1 / M2) | TODO |
| R3 boss (shared R3 M1 / M2) | TODO |
| R1 realm-final (R1 M2) | TODO |
| R2 realm-final (R2 M3) | TODO |
| R3 realm-final (R3 M3) | TODO |
| Victory sting | TODO |
| Defeat sting | TODO |

### SFX (library + modify)

| Category | Count target | Status |
|---|---|---|
| Combat (archetype bases × theme modifiers + hit/crit/dodge) | ~50 | TODO |
| Pickups | 6 | TODO |
| UI | 6 | TODO |
| Run flow | 5 | TODO |
| Sect hub | 5 | TODO |
| Ambient loops (8 regions) | 8 | TODO |
| Special (evolution, cycle, etc.) | ~3 | TODO |

---

## Reference Assets (dev-only)

Stored in **Ludo Favorites** + local working files. The previously documented `res://assets/_references/` path does not exist yet — Godot project hasn't been created. References will be copied into `res://assets/_references/` at code-phase kickoff per [CLAUDE.md](../../CLAUDE.md).

### Reference 1 anchors (per macro family)

| Anchor | Family | Status | Notes |
|---|---|---|---|
| Avatar TLA character lineup | Characters | IN HAND | The original anchor; carries painterly cel-shading + linework + figure aesthetic for character/boss/enemy gens |
| Avatar TLA environment screenshot | Environments + buildings | IN HAND | New 2026-05-23. Air Temple establishing shot or equivalent. Carries the same painterly aesthetic with architecture/landscape as subject |

### Reference 2 anchors (per sub-family, locked piece in each)

| Anchor | Sub-family | Status | Notes |
|---|---|---|---|
| Locked MC (V2 Image 1) | Character pipeline | LOCKED | 2026-05-20 session |
| Mountains backdrop layer | Hub backdrop layers | LOCKED | 2026-05-23 session 2. Anchors style for any future backdrop work (Realm 2+ regional skylines, etc.) |
| Image 1 silhouette (upright topknot) | Crowd FG silhouette pool | LOCKED | 2026-05-23 session 2. First locked figure in the pool; anchors style for any future crowd additions |
| First locked building | Specialty building gens | TBD | Will be the Main Hall once regenerated in the front-facing skyline register and locked. First building also tests the open question on building style register under skyline architecture. |
| First locked card frame + item | Card pipeline | TBD | Future |
| ~~Compound background plate (`stone_floor.png`)~~ | ~~Hub buildings + canvas changes~~ | INVALIDATED 2026-05-23 s2 | Original iso compound architecture abandoned; plate no longer in the layer stack |
