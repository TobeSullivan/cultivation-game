# Tech Stack & Production Pipeline

Locked decisions about how this game gets built. Separated from design docs because production choices have their own concerns. Locked 2026-05-20.

---

## Engine

**Godot 4** (latest stable). Language: **GDScript** (default; switch to C# only if specific performance bottlenecks demand it).

Reasoning: open source, fast iteration, mature VS-like ecosystem, clean exports to Steam Deck + consoles + PC + mobile, indie-friendly tooling, no licensing concerns.

Resources used to learn / reference:
- **GDQuest free 2h Vampire Survivors tutorial** — for genre patterns
- **DarkRewar's SurvivorsStarterKit** (GitHub) — production reference

---

## Art Generation — Ludo.ai Pro

**Subscription:** Ludo Pro at $35/mo annual ($420/year).
- 12,000 credits/year upfront
- Unlimited image generation (the big win for our pipeline)
- Animation credits: 4-16 per sprite animation (Pro doesn't make this unlimited)
- API/MCP access included
- Web app: app.ludo.ai

**Why Pro and not Indie:** Indie's 3,000 credits = ~375 animations/year. With retries, that's tight. Pro removes the image-generation meter entirely so we can iterate freely on the style-locked static images that will dominate our asset volume.

---

## Art Style — Locked

**Style anchor:** Hand-drawn 2D animation, cel-shaded with strong ink outlines and flat color fills, inspired by Avatar: The Last Airbender.

**Honest read on what Ludo actually produces:** The output skews more **manhua / xianxia anime** than pure Avatar TLA (sharper line work, slightly more anime-styled eyes, more rendered shading). This is **acceptable and likely better commercially** — it lands in the cultivation genre's visual vocabulary that the target audience already loves (Mo Dao Zu Shi, Heaven Official's Blessing). Don't fight Ludo back toward pure Avatar — embrace the manhua lean.

**Reference image strategy (used on every generation):**
- **Reference 1:** The Avatar TLA character lineup screenshot (style anchor — does NOT change)
- **Reference 2:** The locked protagonist (subject anchor — set after MC was locked)

Mode in Ludo Image Generator: **Generate with Style**. Both references attached. Style + subject consistency compounds across generations.

**Filter settings:**
- Image Type: **Asset** (for characters, props) or **Background** (for environments) or **Texture** (for tileable ground)
- Art Style filter: Cel-Shaded
- Aspect Ratio: Portrait for characters; Square for icons; Auto for environments

---

## Protagonist — Locked

**The prototype protagonist** is V2 Image 1 from the 2026-05-20 generation pass:
- Young female cultivation sect head
- Late teens
- Long black hair pulled back in a low practical braid with cloth wrap
- Layered dark teal and pale grey silk robes with bound sleeves and wide sash
- Athletic build, steady determined expression
- Full body, slight 3/4 angle, neutral standing pose

**Production note:** Once a character creator is built (post-prototype), this becomes the default preset. The other 7 character concepts from the same session (V1 male, V3 androgynous mystic ×2, V4 older master ×2) become additional creator presets and/or NPC bases for the ~140 named disciple roster. Nothing wasted.

**Visual evolution principle:** The protagonist appearance evolves across cultivation arcs. V2-style practical robes for Stage 1-3 (Mortal). More refined/elevated silhouettes (closer to V3/V4) for Stage 4-12. Reference the existing 8 concepts as templates when designing those evolutions.

---

## Animation Strategy — Two-Tier

**Goal:** stretch Ludo's animation credits (which are metered even on Pro) by reserving them for what the player actually stares at.

### Tier 1 — Real Animated Sprite Sheets (Ludo Animate)

- **Player character** — idle, walk (left/right with sprite flip), hit reaction, defeat. ~4 animations.
- **Bosses** (8 in prototype) — idle, walk, primary attack windup/release, passive aura loop. ~4 animations each.
- **Maybe mini-bosses** — could go either way; defer to playtest.

### Tier 2 — Static Images + Godot Tweens/Shaders

- **All fodder enemies** — single static sprite, tweened position with sine-wave bob to fake walking
- **Elite enemies** — borderline; default static, upgrade to animated if they feel flat
- **VFX** — single image of arc/projectile, rotated via tween, faded with shader
- **Pickups** (XP gems, materials, currency) — static + idle scale-bob tween
- **Environment props** — static, no animation

**Godot tween techniques for fake-animation:**
| Effect | Technique |
|---|---|
| Walking bob | Loop scale.y 0.95 → 1.05 over 0.4s |
| Idle breathing | Loop scale.y 0.98 → 1.02 over 0.8s |
| Damage flash | `modulate = Color(1, 0.3, 0.3)` 100ms then back |
| Crit flash | White modulate burst |
| Attack windup | Scale 1.0 → 1.2 → 1.0 + slight position shift |
| Death | Alpha 1→0 + scale 1→0.5 + Y-rise + particle burst |
| Knockback | Position tween backward with bounce easing |
| Projectile spin | Constant rotation tween, particle trail |
| Telegraph pulse | Modulate yellow→red wind-up |

**Estimated prototype animation budget:** ~32-160 credits across all 8 prototype bosses + player. Pro's 12,000/year is massive headroom.

---

## Save System — Resource-Based to `user://`

Godot 4's idiomatic native save approach.

**Pattern:** Define save data as Resource subclasses. Serialize via `ResourceSaver.save()`. Deserialize via `ResourceLoader.load()`. All to the `user://` path (platform-native: AppData on Windows, Application Support on macOS, .local on Linux).

**Why Resource over FileAccess + JSON:**
- Type-safe — save data IS our schema (matches data-schema.md class structure)
- Subresources work automatically (nested data like disciples within sect)
- Editor inspection of `.tres` save files during dev
- Architecturally consistent — we're already using Resources for content authoring

**Caveat:** Resources can execute code on load. Not a concern for local single-player saves. Would matter only for cloud sync or mods (out of scope).

**Architecture:** `SaveManager` is a singleton (autoload). Single entry point for all save/load operations. Other systems call `SaveManager.save_game()` / `SaveManager.load_game()` — they never touch files directly.

---

## Project Directory Structure

```
res://
├── assets/                  # All art and audio
│   ├── characters/
│   │   ├── player/          # MC sprite + future variants
│   │   ├── bosses/          # Named boss sprites (Yun, Pao, etc.)
│   │   └── enemies/         # Fodder + elite sprites
│   ├── environments/
│   │   └── r1_m1/           # Per-map biome assets
│   ├── cards/               # Card art (96 day-1 + unlock additions)
│   ├── ui/                  # HUD, menus, panels
│   ├── vfx/                 # Attack arcs, hit sparks, particles
│   └── audio/               # SFX, music
│
├── scenes/                  # .tscn scene files
│   ├── main.tscn            # Entry point
│   ├── characters/
│   │   ├── player.tscn
│   │   ├── enemy.tscn       # Base enemy scene
│   │   └── boss.tscn        # Base boss scene
│   ├── maps/
│   │   └── r1_m1.tscn       # Bamboo Hollow scene
│   ├── ui/
│   │   ├── hud.tscn
│   │   ├── level_up_draft.tscn
│   │   └── pause_menu.tscn
│   └── effects/
│       └── damage_number.tscn
│
├── scripts/                 # All .gd files
│   ├── autoloads/           # Singletons (autoloaded in Project Settings)
│   │   ├── game_manager.gd  # Run state, scene transitions
│   │   ├── save_manager.gd  # Load/save to user://
│   │   ├── event_bus.gd     # Global signal hub
│   │   └── audio_manager.gd
│   ├── characters/
│   │   ├── player.gd
│   │   ├── enemy.gd
│   │   └── boss.gd
│   ├── systems/
│   │   ├── combat/          # Damage, hit detection, knockback
│   │   ├── draft/           # Level-up card selection
│   │   ├── cultivation/     # Stages, tiers, qi pool
│   │   ├── territory/       # Paint, objectives, conquest
│   │   ├── sect/            # Buildings, disciples
│   │   └── spawning/        # Enemy spawn director
│   └── ui/
│
├── resources/               # Resource CLASS definitions (.gd extends Resource)
│   ├── card.gd
│   ├── boss.gd
│   ├── enemy_type.gd
│   ├── building.gd
│   ├── disciple.gd
│   ├── save_data.gd         # Top-level save Resource
│   └── ...
│
├── data/                    # Authored content INSTANCES (.tres files)
│   ├── cards/               # 96 day-1 card definitions
│   ├── bosses/              # 8 prototype bosses
│   ├── enemies/             # Per-map enemy definitions
│   ├── maps/                # Map metadata
│   └── buildings/           # Building definitions
│
└── project.godot
```

**Layout principles:**
- `assets/` vs `scripts/` vs `resources/` vs `data/` = clear separation of art, code, schema, content
- `resources/` holds Resource *class definitions* (.gd files that `extend Resource`); `data/` holds *instances* of those classes as `.tres` files
- `autoloads/` holds singletons that everything else routes through
- `systems/` grouped by the four pillars (combat, cultivation, territory, sect) — design maps to code layout
- Maps split into their own folders since each will have ~10 unique assets

---

## Asset Drop Locations (For When Images Are Generated)

When new images come back from Ludo, they go here:

| Asset | Drop In |
|---|---|
| Protagonist sprite (locked MC) | `res://assets/characters/player/` |
| Boss sprites (Yun, Pao, etc.) | `res://assets/characters/bosses/` |
| Fodder enemy sprites | `res://assets/characters/enemies/` |
| Elite enemy sprites | `res://assets/characters/enemies/` |
| Bamboo Hollow ground tile | `res://assets/environments/r1_m1/` |
| Bamboo Hollow props (stalks, rocks) | `res://assets/environments/r1_m1/` |
| Card art | `res://assets/cards/` |
| VFX (Vine Whip arc, etc.) | `res://assets/vfx/` |
| UI elements | `res://assets/ui/` |
| Reference images (Avatar lineup, locked MC) | `res://assets/_references/` (dev-only, excluded from export) |

**Naming convention:**
- snake_case for all asset filenames
- Player: `player_idle.png`, `player_walk.png`, etc.
- Boss: `yun_idle.png`, `yun_walk.png`, etc.
- Enemy: `fodder_bandit.png`, `fodder_spirit.png`, etc.
- Environment: `bamboo_ground_tile.png`, `bamboo_stalk.png`, etc.
- **Tier-state variants on buildings:** `_t1`, `_t4`, `_t8` suffix. Example: `teahouse_t1.png`, `teahouse_t4.png`, `teahouse_t8.png`. Intermediate tiers reuse the most recent milestone base.
- **Sprite sheets (multi-frame animations):** `_sheet` suffix. Example: `player_walk_sheet.png` for the walk-cycle sprite sheet, `player_idle.png` for a single-frame static image.
- **Cards:** `card_<theme>_<name>.png` for base, `card_<theme>_<name>_evolved.png` for evolved variant. Example: `card_wood_vine_whip.png` / `card_wood_vine_whip_evolved.png`.

---

## Ludo Reference Workflow — Locked

Every Ludo generation uses two references attached, in this order:

- **Reference 1: Style anchor** — Avatar TLA character lineup screenshot. **Never changes.** This locks the cel-shaded ink-outline manhua-anime register across the entire production.
- **Reference 2: Subject anchor** — rotates based on what's being generated:
  - Generating a character → locked character of that family (or locked MC for sect head presets)
  - Generating a building → first locked building (preserves style consistency across the hub)
  - Generating a card → locked card frame + the item visual
  - Generating VFX / environment → first locked piece in that category

**Hard rule:** never generate without both references attached. This prevents style drift over long pipelines. The reference set is canonical and version-pinned. Reference images live in `res://assets/_references/` (dev-only, excluded from export builds).

---

## Build Order — Prototype Vertical Slice

Order matters: each step verifies before the next.

1. **Project skeleton.** Create directory structure. Set up project.godot. Configure autoload singletons (GameManager, SaveManager, EventBus, AudioManager — empty shells).
2. **Resource class definitions.** Write the `.gd` files for Card, Boss, EnemyType, SaveData, etc. matching data-schema.md. No content yet — just the class definitions.
3. **SaveManager skeleton.** Empty save_game() / load_game() with `user://` path setup. Test round-trip with a dummy SaveData.
4. **Player scene.** Static sprite (locked MC image as placeholder), 4-direction movement (or 8-direction), camera follow.
5. **One enemy.** Static sprite, walks toward player (with sine-bob tween), takes damage, dies (with death tween).
6. **One technique.** Vine Whip — auto-fires on closest enemy in range, deals damage on hit.
7. **XP + level-up.** Enemy drops XP gem, player picks it up, level-up UI offers 3 cards.
8. **Spawn director.** Wave system that drops enemies at screen edges over time.
9. **R1 M1 map.** Bamboo Hollow scene with tileable ground + scattered props.
10. **Lady Yun boss.** Boss arrival mechanic, two-attack pattern, defeat = run end.

Each step is a tight loop. By step 10 you have a playable R1 M1 with placeholder VFX and animations. Then replace placeholders with real animations and polish.

---

## What's Outside Prototype Scope (Production-Side)

- Character creator (post-prototype; we have 8 concept candidates ready to become presets)
- Animated boss sprite sheets (placeholder static for prototype; animate later)
- Full SFX/music pass (placeholder audio for prototype)
- Console/Steam Deck export configurations (PC-first)
- Save versioning / migration (only matters after launch)
- Mod support (out of scope for v1)

---

## Resolution Conventions — Working Numbers

Locked as working baseline (2026-05-21). Validate after first Ludo→Godot import; revise if asset clarity / file size demands it.

| Asset type | Source resolution | Notes |
|---|---|---|
| Characters (player presets, bosses) | 512×512 | Scaled in scene |
| Enemies (fodder, elite) | 256×256 | Static images, tween-animated |
| Cards (full art including frame) | 512×768 | Portrait orientation |
| Buildings (per tier state) | 512×512 | One source per `_t1` / `_t4` / `_t8` |
| World map | 2048×2048 | Scaled to viewport, may need zoom in later realms |
| Region biome backgrounds | 1920×1080 | Landscape, full run-screen |
| VFX (typical) | 256×256 | Combined with tweens / shaders |
| VFX (screen-spanning) | 512×512 | Boss attack telegraphs, ultimate effects |
| UI icons | 128×128 | Scaled down in HUD |
| Sprite sheets | varies | Use power-of-2 dimensions where possible |

---

## Animation Handoff — Ludo → Godot

Ludo outputs animations as multi-frame sprite sheets (PNG grid). Godot's AnimatedSprite2D node accepts these natively via the SpriteFrames resource. Standard workflow per animation:

1. **Ludo Animate** generates a multi-frame PNG sheet (4–8 frames typical for idle/walk; ≤16 for complex attacks)
2. Save to the appropriate `res://assets/characters/<entity>/` folder with `_sheet` suffix
3. In Godot, create a SpriteFrames resource, import the sheet, define frame grid (rows × columns), set frame durations (typical: 0.1–0.15s per frame for idle, 0.08–0.12s for walk)
4. Attach SpriteFrames to an AnimatedSprite2D node in the entity scene
5. Trigger via `.play("idle")` / `.play("walk")` / etc.

No external format conversion needed. Aseprite / Krita only required for sprite touch-ups.

---

## Open Production Questions

- **GDScript vs C#:** Defaulting GDScript. May revisit if performance bottlenecks emerge in enemy spawning or particle counts.
- **Pixel-perfect filtering vs smooth filtering:** Smooth (Linear), since we're hand-drawn, not pixel art.
- **Aseprite / Krita integration:** Optional cleanup tool for AI sprite touch-ups if needed. Defer.
