# Session Handoff — 2026-05-20

Long session covering: pre-code lock pass → Sprout effects → tech stack + art pipeline → first asset generation pass. Ended at "ready to set up Godot project."

---

## Part 1 — Pre-Code Lock Pass

### 1. Prototype scope reduction
**6 buildings ship at T1 only** for prototype (Recruitment / Training / Storehouse / Outer Court / Library / Forge). Building tier ceiling rule unchanged in design — prototype just ships less content for these buildings. Teahouse keeps T1-T5, Pavilion keeps T1-T7.

### 2. Specialist amplification coefficient
`compound rate = base × (1 + Σ(specialist ratings) × 0.05)`. Endgame 6 specialists avg rating 7.5 → 3.25× (hits 2-4× target band). Prototype 1 specialist rating 5 → 1.25×.

### 3. Cycle 1 / Cycle 2 caps
+10% / +20% — final, not placeholders.

### 4. Skip / reroll / banish housing
**Storehouse**. Locked.

### 5. Items confirmed as already-locked (not actually open)
- Meridian refinement materials — any tier-appropriate, unified pool
- Teahouse mechanics — 16 flat-cap tracks, no in-service juggling
- Soul Forge T1 — flat-cap Technique track only, no leaves

### 6. Items confirmed deferred
- Heaven-Reader arc length (3 vs 4 members)
- Pairing convention consistency across all 12 themes

---

## Part 2 — 12 Sprout Effects + Tier-2 Theme Names

Pattern: Sprout = amp Sapling identity. Grove introduces new mechanics. Tier names per theme distinct.

| Theme | Sprout Name | Effect |
|---|---|---|
| Wood | Sprout | Evolved Wood techs +damage |
| Earth | Stone | Evolved Earth: knockback + shockwave AoE up |
| Fire | Flame | Evolved Fire: kills chain-explode (reduced dmg) |
| Water | Stream | Evolved Water: pierce no damage falloff |
| Metal | Edge | Evolved Metal: crits inflict armor break |
| Wind | Gust | Evolved Wind: stacking atk speed on hit |
| Ice | Snow | Evolved Ice: slowed enemies take +dmg from all |
| Lightning | Arc | Evolved Lightning: bigger chains, overcharge |
| Shadow | Umbra | Evolved Shadow: proximity stacks dmg reduction |
| Spirit | Apparition | Evolved Spirit: spirit allies stack dmg buff |
| Star | Shimmer | Evolved Star: meter fills faster, starfall up |
| Void | Hollow | Evolved Void: erasures leave damaging rifts |

---

## Part 3 — Tech Stack & Production Pipeline

### Engine
**Godot 4** with **GDScript**. Already installed by user.

### Art Generation
**Ludo.ai Pro** ($35/mo annual). Confirmed:
- Unlimited image generation
- 12,000 credits/year for animation (metered)
- No free tier exists despite some outdated reviews suggesting otherwise
- Animation costs 4-16 credits each — reserve for player + bosses only

### Art Style — Locked
**Cel-shaded hand-drawn inspired by Avatar: The Last Airbender.** Ludo's actual output leans manhua/xianxia anime, which is a better commercial fit for the cultivation genre target audience. Don't fight back toward pure Avatar.

**Reference strategy:** Avatar TLA character lineup as Reference 1 (style). Locked MC as Reference 2 (subject) for downstream generations. Mode: "Generate with Style" in Image Generator.

### Protagonist — Locked
**V2 Image 1 from 2026-05-20 generation pass.** Female cultivation sect head, late teens, low braid with cloth wrap, teal/grey layered robes. Other 7 character concepts retained for future character creator presets + NPC roster (~140 named disciples).

### Animation Strategy — Two-Tier
- **Tier 1 (real animations):** Player + bosses. ~4 animations each. Total budget ~32-160 credits for prototype.
- **Tier 2 (static + tween):** Fodder, elites, VFX, props, pickups. Godot tweens fake the motion. Modulate shaders for damage flash. Effectively unlimited.

### Save System
**Godot 4 Resource-based to `user://`.** SaveManager autoload singleton. Save data as Resource subclasses serialized via `ResourceSaver.save()` / `ResourceLoader.load()`. Matches our existing data-schema architecture (type-safe, subresources, editor-inspectable).

### Project Directory Structure
Locked. See `tech-stack-and-pipeline.md` for full tree.

Key separation:
- `assets/` = art
- `scenes/` = .tscn
- `scripts/` = .gd code
- `resources/` = Resource class definitions
- `data/` = .tres content instances (matches data-schema)
- `autoloads/` = singletons

---

## Part 4 — Assets Generated This Session

8 character concepts produced via Ludo's "Generate with Style" mode using the Avatar TLA reference:

| ID | Description | Status |
|---|---|---|
| V1 Image 1 | Young male, topknot, teal/grey robes (variant A) | Future character creator preset |
| V1 Image 2 | Young male, topknot, layered teal/grey robes (variant B) | Future preset |
| V2 Image 1 | **Young female, braid, teal/grey robes** | **LOCKED PROTAGONIST** |
| V2 Image 2 | Same prompt, accidentally male variant | Future preset |
| V3 Image 1 | Long-haired androgynous mystic, white/indigo robes | Future preset (late-game look) |
| V3 Image 2 | Long-haired androgynous mystic, white/purple robes | Future preset (late-game look) |
| V4 Image 1 | Older male, Fire Nation-coded, brown/gold robes | Future preset (late-game look) |
| V4 Image 2 | Same prompt, more austere variant | Future preset (late-game look) |

V3 and V4 concepts read as later-cultivation-arc aesthetics — useful as templates for player visual evolution across Stage 4-12.

---

## State at Session End

**Design:** Effectively complete for prototype. 7 open questions remain but none prototype-blocking.

**Build-blocking work:** 4 items, all content-authoring (wave composition, per-card content, library cycle climb, naming pass). Can run parallel to engineering.

**Production:**
- Godot 4 installed
- Ludo Pro to subscribe (user committed)
- Style locked
- Protagonist locked
- Directory structure designed
- Save approach decided
- Build order outlined

---

## Next Session

**Start writing code.** User will drop in code and test.

Immediate sequence:
1. Set up the Godot project structure (folders, project.godot, autoload registrations)
2. Write Resource class definitions matching data-schema.md
3. Write SaveManager skeleton
4. Write Player scene + script (movement, camera, placeholder sprite)
5. Write Enemy scene + script (basic chase + damage)
6. Write the first technique (Vine Whip)
7. Iterate from there

User will need to provide locked MC image at step 4 (or earlier) and place in `res://assets/characters/player/`. Other assets needed in later steps:
- Step 5: at least one enemy sprite in `res://assets/characters/enemies/`
- Step 9: ground tile + bamboo prop in `res://assets/environments/r1_m1/`
- Step 10: Lady Yun sprite in `res://assets/characters/bosses/`

---

## Remaining Open Questions

Down to 7, none prototype-blocking:

- Re-fight vs. auto-unlock for late-completed boss recruits (leaning re-fight)
- Per-boss exotic gate distribution
- Heaven-Reader arc length — deferred
- Trigger values for special-event recruits
- Path Grove/Forest/Worldroot effect designs (36 effects; 12 Sprout done)
- Pairing convention consistency — deferred
- Spirit stone exchange rate / sink list

---

## Docs Updated This Session

1. `v6-merge-and-open-questions.md` — open questions trimmed, Recently Locked section expanded
2. `cultivation_game_design_doc_v6.md` — open questions trimmed, coefficient + cycle caps + Storehouse lock + prototype critical path updated, Sprout effects table added
3. `prototype-spec.md` — tier state updated to T1-only for 6 buildings
4. `data-schema.md` — coefficient lock noted, Sprout field marked locked
5. `tech-stack-and-pipeline.md` — **NEW** — engine, art tooling, style lock, save system, directory structure, build order
6. `session-handoff-2026-05-20.md` — this doc

---

## Process Notes from This Session

Three drifts caught and corrected mid-session:

1. **Teahouse mechanics** — invented "in-service tea juggling" and "brewing time" that were already explicitly rejected in earlier sessions. Caught via past-conversation search. Removed.

2. **Meridian refinement materials** — almost re-invented as "per-meridian identity" before searching past convos and finding unified-materials lock.

3. **Generation count assumption** — assumed user generated 1 image per Ludo prompt when Ludo returns 2 per generation. Misread the female + male V2 result as "two prompts ran." User corrected.

Pattern recognized: the open-questions doc framing made already-locked items look open. Search before proposing on any item that *feels* designed but is listed as open. Applied this mid-session and it caught additional drift.
