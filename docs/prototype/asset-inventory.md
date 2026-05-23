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

## Style Locks (2026-05-23, updated session 4)

| Lock | Value | Source |
|---|---|---|
| Art style — backdrop landscape layers | Flat vector with hard shape gradients, deep blue palette | Locked 2026-05-23 session 2 |
| Art style — architecture | **OPEN — style coexistence question** | Session 3 locked flat vector after first Main Hall (navy roof) came back flat. Session 4 user-chose v2 warm olive (still flat vector). Session 4 user-chose v3 painterly (Studio Ghibli–register) → flat-vector-architecture lock retired. Now: painterly building on flat-vector backdrop. Decision deferred — see open-questions.md. |
| Camera angle | Front-facing 2D skyline | Revised 2026-05-23 session 2 (was 3/4 angled top-down — abandoned with architecture pivot) |
| Hub architecture | 6-layer parallax stack: sky / mountains / clouds / mist / buildings / crowd FG | Locked 2026-05-23 session 2 |
| Hub composite | hub_test.tscn validated 2026-05-23 session 4. Layer stack composites correctly at 1920×1080. Mountains y=350 / Ground 935–1080 / HorizonPlatform 895–935 black 40px / MainHall 0.45× / 18-figure crowd at y≈1020–1045 / 3-sprite mist with normal-blend pale-cool gradient drifting 4/6/9 px/sec. | New |
| Reference 1 — Characters family | Avatar TLA character lineup | Existing |
| Reference 1 — Environments + buildings family | Avatar TLA environment screenshot (Air Temple establishing shot) | New 2026-05-23 |
| Locked Reference 2 — Mountains layer | Locked 2026-05-23 session 2 | Existing |
| Locked Reference 2 — Buildings family | **OPEN** — was Main Hall (locked session 3) → retired session 4 by v3 painterly replacement. Painterly Main Hall would normally become new Ref 2; pending style coexistence decision. | New |
| Ludo Pipeline | See [design-pass.md > Asset Pipeline](design-pass.md#asset-pipeline) | Verified 2026-05-23 |
| Generate-then-Edit-then-key pipeline | Three-step: Generate New on opaque background → Edit Image to strip → `tools/key_out_checkerboard.py` to convert baked checkerboard to true RGBA | Locked 2026-05-23 session 3 (drift #23 forced step 3) |

**Architecture pivot 2026-05-23 session 2:** Original iso compound architecture (background plate + 10 iso building sprites) abandoned. The building-isometric-vs-plate-perspective open question is resolved by the pivot — front-facing skyline puts buildings and backdrop on the same camera orientation. Original `stone_floor.png` plate INVALIDATED.

**Asset-state surprise 2026-05-23 session 4:** `clouds.png` was discovered to have a SOLID WHITE opaque background, not the baked checkerboard documented in session 2. Session 2 lock "transparent PNG" was incorrect — file was opaque-white-bg until session 4 keying. Key script worked correctly on it anyway (white pixels are desaturated + bright, same selector as checkerboard).

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
| Sky | IN GAME (Godot-native) | 2026-05-23 s4 | TextureRect + GradientTexture2D top-to-bottom (cool blue → pale blue). Allows time-of-day tinting via gradient swap. `game/scenes/hub_test.tscn` Sky node. |
| Mountains | IN GAME (LOCKED) | 2026-05-23 s2 / imported s4 | Flat vector, deep blues. `game/assets/hub/mountains.png` 1344×768, scaled 1.43× at y=350 in hub_test. |
| Clouds | KEYED (currently unused) | 2026-05-23 s4 | True RGBA via session 4 keying. Source `assets/hub/clouds.png` 1344×252 after bbox crop. 8 individual cloud forms extracted to `assets/hub/clouds/cloud_01..08.png` via `tools/extract_cloud_pieces.py`. **Dropped from hub_test in session 4** — single-sprite drift exposed sparse coverage + pixelated edges; user opted to defer clouds until better individual-cloud asset variety lands. |
| Mist | IN GAME (Godot-native) | 2026-05-23 s4 | Three Sprite2D nodes with programmatic radial GradientTexture2D (pale cool grey-blue #b8c4d0 center, fade to transparent edge). Normal alpha blend, opacity 0.55. Each elongated to varied widths/heights (3.125×0.78, 3.9×0.7, 2.7×0.86). Drifts 4/6/9 px/sec via `drift.gd`. Sits in y=750–900 seam band. Not a Ludo asset — Godot-only. |

### Invalidated assets (architecture pivot)

| Asset | Status | Notes |
|---|---|---|
| Sect compound background plate (`stone_floor.png`) | INVALIDATED 2026-05-23 s2 | Original iso compound architecture abandoned. Plate no longer in the layer stack. Kept in Ludo Favorites for archive only. |

### Buildings (10 individual sprites, composited at runtime over backdrop)

| Building | T1 | T4 | Notes |
|---|---|---|---|
| Main Hall (head-only) | **LOCKED v3 painterly** | n/a | `assets/buildings/main_hall.png` 1327×613 keyed RGBA (2026-05-23 s4). Painterly Studio Ghibli–register, includes baked bonsai tree (left) and stone shrine (right). v1 navy-roof + v2 warm-olive preserved as `main_hall_v1_navy_roof.png` / `main_hall_v2_warm_olive.png`. Style coexistence with flat-vector backdrop OPEN. |
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

### Crowd FG silhouette pool (Locked 2026-05-23 session 2, keyed + in game session 4)

Pool of 9 unique silhouettes, all waist-up, back-facing (facing the sect), hands clasped behind back, pure black figures on now-true-RGBA PNG (keyed session 4 via `tools/key_out_checkerboard.py`). Composed in Godot at runtime — selection / scaling / distribution / sparse bob-shuffle tween handle population growth.

| # | Silhouette | File | Status | Notes |
|---|---|---|---|---|
| 1 | Upright topknot (male) | `male_topknot.png` 449×764 | IN GAME | Used twice in hub_test |
| 2 | Bowed-head topknot (male) — older | `old_topknot.png` 526×757 | IN GAME | Used twice in hub_test |
| 3 | Ceremonial hat (court official) | `fancy_hat.png` 429×758 | IN GAME | Used twice in hub_test |
| 4 | Long-hair tied back (female low ponytail) | `female_long_hair.png` 677×747 | IN GAME | Used twice in hub_test (one flipped) |
| 5 | Long flowing hair (female topknot) | `female_topknot.png` 514×768 | IN GAME | Used twice in hub_test |
| 6 | High-bun / hooded female | `hooded_female.png` 563×752 | IN GAME | Used twice in hub_test |
| 7 | Broad heavyset (large monk) | `large_monk.png` 790×716 | IN GAME | Widest silhouette; used twice |
| 8 | Strong monk | `strong_monk.png` 572×732 | IN GAME | Used twice in hub_test |
| 9 | Pointed hood | `hooded.png` 526×747 | IN GAME | Used twice in hub_test |

**In-game composition (hub_test session 4):** 18 figures (each silhouette twice, half horizontally flipped via negative scale.x for variation). Scales 0.08–0.14 (small). Baselines aligned at y=1075. Uneven horizontal spacing (60–150px gaps) with two visible clusters (left x=150–430, right x=1370–1540) and looser middle spread. Bob/shuffle controller (`crowd_bob.gd`) picks one figure at a time on a 1.5–5s random interval, runs an asymmetric down-then-up tween (1.2s sink, 1.0s recover, 5px amplitude, SINE ease-in-out). Pool expandable later if needed.

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

Stored in **Ludo Favorites** + local working files. Godot project exists at `game/` as of 2026-05-23 session 4, but Reference 1/2 assets have not yet been copied into `res://assets/_references/` — currently only locked production assets are mirrored into `game/assets/`. Reference copy is a follow-up task.

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
| First locked building | Specialty building gens | OPEN | Main Hall is in its third locked version (v3 painterly). Would normally become the buildings-family Reference 2 anchor; pending style coexistence decision (see open-questions.md). |
| First locked card frame + item | Card pipeline | TBD | Future |
| ~~Compound background plate (`stone_floor.png`)~~ | ~~Hub buildings + canvas changes~~ | INVALIDATED 2026-05-23 s2 | Original iso compound architecture abandoned; plate no longer in the layer stack |
