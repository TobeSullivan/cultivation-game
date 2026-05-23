# Design Pass — Prototype Surfaces, Art, Audio

Inventory of everything the prototype needs *besides* R1–R3 mechanics. Companion to [scope.md](scope.md). This doc exists because "prototype" means a player can boot the game, see screens, hear sound, play a run, beat a boss, see the hub, repeat — not just mechanics on a flat background.

Filled out 2026-05-21 design pass session. Asset production tracking lives in [asset-inventory.md](asset-inventory.md).

---

## Status Legend

- **LOCKED** — design decision settled
- **DEFERRED** — design call pushed to a later milestone (with reason)
- **OPEN** — needs design call before implementation

---

## Opening Flow

```
[Splash] → [Title] → [Character Select (new game)] → [First-launch Hub] → [Map] → [Run] → [Post-run] → [Hub (returning)]
                  ↘ [Continue] → [Hub (returning)] → [Map] → [Run] → [Post-run] → [Hub] (loop)
```

Status: **LOCKED**. 9 surfaces + 1 cross-surface system (Dialog/Cutscene). Cross-surface principle: every interactive element needs a focus/selected state for controller, mobile, and accessibility play.

---

## Per-Surface Specs

### Surface 1 — Splash

- **Purpose:** Studio brand mark. First frame the player sees.
- **Status:** LOCKED.
- **Contents:** Single static studio mark, ~2 seconds, skippable on any input.
- **Rationale:** No engine logo (Godot is FOSS — not required). No cinematic intro (over-invested budget for $5–10 price-point). No multi-mark sequence (player boots often for short check-ins; long splash punishes that loop).
- **Asset ask:** 1 studio mark image.
- **Audio:** Optional 1-second sting.

### Surface 2 — Title Screen

- **Purpose:** Brand the game, route to game start / settings / quit.
- **Status:** LOCKED.
- **Contents:**
  - Game logo treatment (typography)
  - Parallax key art background (3 layers: foreground MC silhouette / mid-ground sect / sky background)
  - Subtle ambient motion (drifting petals, qi wisps, slow cloud movement) via Godot particles + tweens
  - Menu (3 buttons): **Primary** (contextual — "Continue" if save exists, "New Game" if not), **Settings**, **Quit**
- **Save model:** Single save slot. No multi-slot UI. Wipe Save lives in Settings (title-entry only, not in-run pause).
- **Audio:** Your own Suno title track. Lyric language deferred. R12 apex callback hook flagged.
- **Asset ask:** 1 layered key art piece (3 separable layers), 1 logo treatment.

### Surface 3 — Character Select

- **Purpose:** Player picks their sect head before committing to a new run.
- **Status:** LOCKED.
- **Contents:**
  - Carousel UI (8 presets, MC default-highlighted)
  - Each preset: full-body portrait + brief flavor name (workshop later)
  - Confirm button + Back button
- **Presets:** The locked MC (V2 Image 1 from the 2026-05-20 Ludo session) + the 7 other concepts from the same session (V1 male, V3 androgynous mystic ×2, V4 older master ×2, V5).
- **Real parts-swap creator:** DEFERRED post-prototype. Reason: hand-painted style doesn't compose cleanly across arbitrary swaps; Ludo workflow relies on reference compounding. 8-preset carousel delivers agency without combinatorial asset explosion.
- **Asset ask:** 8 character portrait thumbnails + 8 full sprite-sheets × 4 animations (idle/walk/hit/defeat) = 32 animations.

### Surface 4 — First-Launch Hub

- **Purpose:** Player's first hub view after committing to a new run.
- **Status:** LOCKED.
- **Contents:**
  - Sect compound background (Mortal-era walled mountain plateau)
  - Main Hall + Personal Sanctum visible (head-only buildings, present from start)
  - 0 of 8 specialty buildings visible (progressive reveal as conquered)
  - Currency HUD top (4 currencies + materials)
  - Mission Select button corner
  - Light contextual tooltips on first hover/tap of each element. No forced tutorial.
- **Onboarding philosophy:** First run IS the tutorial. R1 M1 with Yun teaches the run loop. Hub teaches itself when player returns with currency to spend.
- **Asset ask:** Shared with Surface 5 (same background + UI chrome).

### Surface 5 — Hub (Returning)

- **Purpose:** Between-runs home. Building grid, disciple roster, currencies, paths, mission select entry.
- **Status:** LOCKED. Architecture redesigned 2026-05-23 session 2 from iso compound to front-facing skyline.
- **Visual treatment:** 2D front-facing skyline composition (not iso/top-down — perspective revised session 2). Hand-painted register on architecture pieces, flat vector with hard shape gradients on backdrop landscape layers. The two styles coexist because they sit at different depth layers and the eye reads them as distinct planes. Mortal-era visual identity for prototype.
- **Building interaction:** Each building = clickable hotspot (TextureButton or Sprite2D + Area2D in Godot). Click → modal Control opens with tier state / master / disciples / upgrade preview / purchase button. Close returns to hub.
- **Building art axes** (per [pillars/sect-management.md](../pillars/sect-management.md) Visual Growth section):
  - **Tier axis:** 3 base-art stages per building (T1 / T4 / T8). Prototype shows T1 + T4 only (cap is T5, T7 for Pavilion). Larger tier stages naturally read as more impressive in the skyline composition — taller/wider sprites break the horizon line higher and overlap into the cloud and mountain layers behind them.
  - **Population axis:** Aggregate foreground crowd silhouette layer (not per-building NPCs — redesigned session 2). Density / count / scale of crowd figures grows with sect population. Reads at-a-glance as sect size; subtle bob/shuffle motion on 1-2 figures every few seconds keeps it alive without competing with cloud and mist motion for attention.
- **HUD persistent elements:** 4 currency icons + count (top), materials button (opens 24-cell modal for prototype, 72-cell full game), Mission Select button (corner).
- **Asset ask:** Backdrop layer stack — mountains layer Ludo-generated (LOCKED s2), clouds layer Ludo-generated (KEYED s4, dropped from current hub_test pending better individual-cloud variety), mist hand-authored in Godot (IN GAME s4), sky Godot-native gradient (IN GAME s4); 10 individual building sprites × 2 visual stages = 20 base building images (Main Hall v3 painterly LOCKED + IN GAME s4 — `assets/buildings/main_hall.png` 1327×613 — see open questions for style coexistence with flat-vector backdrop; head-only single-state status separately unresolved); crowd FG silhouette pool (9 figures keyed + IN GAME s4 as 18-figure scatter with bob/shuffle tween in hub_test); modal UI chrome.
- **Hub asset architecture:** Front-facing skyline with 6 separable parallax layers. Architecture detail and rationale in [Asset Pipeline > Hub asset architecture](#hub-asset-architecture-redesigned-2026-05-23-session-2). The previously open "Hub building layout — specific positions on the compound" question is resolved via emergent per-building placement in Godot, not pre-planned.

### Surface 6 — Map / Level Select

- **Purpose:** Risk-overlay world map for region selection and conquest tracking.
- **Status:** LOCKED.
- **Visual treatment:** Stylized hand-painted parchment/scroll world map. Soft visual zones for realm boundaries (no hard lines). Prototype shows R1–R3 in a single contiguous Mortal-realm view.
- **Region game-states (4):**
  - **Locked** — gray / fog, non-interactable, no boss preview
  - **Adjacent / unlockable** — full color, pulsing or glowing edge, click to inspect
  - **Available** — full color, clear region art
  - **Conquered** — full color + completion crest (sect banner) planted, subtle ambient glow
- **Interactive states (2, overlaid on game-states):**
  - **Hover** — PC mouse only, subtle outline brighten (warm gold tint)
  - **Focused / selected** — cross-platform, strong gold glow + gentle pulse. On console this IS the cursor (joystick moves focus region-to-region). On PC, click sets focus. On mobile, tap sets focus.
- **Conquest animation:** On map return after victorious run, camera pans to just-conquered region, banner plants with sound cue, adjacent regions reveal from fog.
- **Mission Select modal:** Region name + biome thumbnail, boss portrait + theme/archetype tags, 6 objective list (with completion state if previously played), reward preview, exotic gate requirements (with met/unmet state visible up-front per locked decision), recommended cultivation stage/tier (soft warning, never gating), Start Run button.
- **Asset ask:** 1 world map (parchment), 8 region biome thumbnails, region state overlays (fog / pulse / banner / focus ring), modal UI chrome.

### Surface 7 — In-Run HUD

- **Purpose:** Core VS-loop UI during a run.
- **Status:** LOCKED.
- **Persistent HUD elements:**
  - **Top center:** Timer (big, counts up from 0:00), kill counter (small, below timer)
  - **Top left:** 4–5 currency icons accumulating this run (raw qi, essence, materials, stones)
  - **Top right:** Pause button (PC: Esc / Controller: Start / Mobile: tap icon)
  - **Bottom:** Full-width XP bar with embedded level number, card slot icon row above it
  - **On-character:** Health bar directly under player sprite (modern feel, less screen clutter)
- **NOT persistent (deliberately):** No on-screen objective tracker. Objectives live in the pre-mission modal (going in) and the pause screen (live progress during run).
- **Transient elements:**
  - **Bank notification** — fades in/out (~2 sec) when an objective completes. "Kills complete!" / "Territory complete!" Same family as VS level-up flash.
  - **Level-up draft modal** — 3-choice with Storehouse-charged reroll / skip / banish charges. Modal pauses the action.
  - **Boss spawn warning** — ~5 sec before boss arrival (at 5-of-6 objectives banked or 25-min mark, whichever first per CLAUDE.md drift pattern #10).
- **Asset ask:** HUD chrome elements (~10), level-up draft modal chrome, transient notification typography/box.

### Surface 8 — Pause / Settings

- **Purpose:** In-run pause + settings access (both in-run and from title).
- **Status:** LOCKED.
- **Pause behavior:** Hard freeze (no soft-pause damage risk in an active-dodging VS game).
- **Pause overlay contents:**
  - Big "PAUSED" header
  - **Live objective progress** — 6 objectives with current/target values (the persistent reference per Surface 7 design)
  - **Active cards loadout** — what's been drafted this run, levels each card is at
  - **Active passives loadout** — same
  - Resume button (default focus)
  - Settings button (opens Settings sub-modal)
  - Quit to Hub button (confirm dialog → ends run, banks completed objectives, applies "They Escaped" logic to any boss with unmet exotic gate)
- **Settings sub-modal (context-aware):**
  - **From both entry points:**
    - **Audio:** Master / Music / SFX / Ambient sliders
    - **Video:** Resolution dropdown, fullscreen toggle, vsync toggle (PC only — hidden on console/mobile)
    - **Controls:** Key rebind (PC), controller rebind (console), virtual button positioning (mobile, VS-style fixed-position auto-fade)
    - **Accessibility (minimum viable):** Text size (small / med / large), screen shake toggle, flash reduction toggle
  - **Title-screen entry only:** Save Management section with Wipe Save (confirmation required)
- **Asset ask:** Pause overlay chrome, settings modal chrome, slider/toggle/dropdown UI elements.

### Surface 9 — Post-Run

- **Purpose:** Banking reveal — the dopamine moment after a run ends.
- **Status:** LOCKED.
- **Sequence:**
  1. Run ends → screen fades to dark
  2. **Outcome banner** appears: Victory (green) / Defeat (red) / "They Escaped" (amber/neutral), with appropriate music sting
  3. **Objectives panel slides in** — 6 objective rows animate one at a time, check-mark sound on each banked objective
  4. **Reward panel builds** — banked rewards count up from 0 to final with currency-pickup-sound per increment
  5. **First-time-only rewards** flagged distinctly (gold border / sparkle effect / "FIRST CLEAR!" tag)
  6. **Continue button** (default focus) → returns to map screen (with conquest animation if victory)
- **"They Escaped" outcome** (exotic-gate-not-met):
  - Banner says "THEY ESCAPED" in amber/neutral color (workshop exact wording)
  - Boss objective row shows defeated check-mark → animates to un-checked with "gate not met" message
  - All other banked objectives bank normally — only boss conquest is rejected
  - Prototype: no R1–R3 boss can trigger this in normal play (all are first-time building unlockers, never exotic-gated). System architected for R4+.
- **Defeat outcome:** Partially-banked objectives still bank. Friendlier than VS-genre default; fits "your sect's territorial conquest" framing — even failed runs push something forward.
- **Implementation note:** Run loop must bank objectives at threshold-crossing moments (mid-run), not only at run-end. Flag for audit pass on run-loop.md.
- **Asset ask:** Outcome banner art (3 variants: Victory / Defeat / They Escaped), reward iconography (per currency / material type), conquest animation overlay.

### Cross-Surface System — Dialog / Cutscene

- **Purpose:** Narrative beats at moments that already pause the action.
- **Status:** LOCKED. Added to prototype scope.
- **Visual treatment:** Scroll/banner overlay + portrait display + typed text + continue/skip button.
- **Trigger points (19 prototype beats):**
  - **8 first-time boss intros** (in-run, at boss spawn — action already pauses for boss arrival)
  - **8 first-time recruit moments** (post-run, after victory — action already over)
  - **3 stage breakthroughs** (in-hub at Personal Sanctum — Stage 1→2, 2→3, 3→4)
- **NOT used for technique evolution** — would break VS pacing. Evolutions use a transient banner instead (Brotato-style level-up celebration).
- **Tone:** Cliché xianxia/cultivation cheese is correct here. Audience expects it. 1–2 lines per beat.
- **Writing:** 19 beats, yours to write (cheese encouraged).
- **Asset ask:** 1 dialog UI chrome (scroll/banner + typography). Portraits reused from boss and MC sprite asks.

---

## Art Inventory

### Character art

| Asset | Count | Notes |
|---|---|---|
| Sect Head presets (full sprites) | 8 | One is locked MC; other 7 from V1–V5 Ludo session |
| Sect Head animations | 32 | 8 presets × idle/walk/hit/defeat |
| Sect Head portraits | 8 | Carousel UI + breakthrough dialog cutscenes |
| Boss full sprites | 8 | All R1–R3 bosses |
| Boss animations | 32 | 8 bosses × idle/walk/attack/aura (Tier 1 animated per tech-stack.md) |
| Boss portraits | 8 | Reused for dialog/cutscene system |
| Fodder enemies | ~24–32 | 8 regions × 3–4 fodder each, static only |
| Elite enemies | ~8–16 | 8 regions × 1–2 each, static only |

**Sprite-sheet animations subtotal:** ~64. Pro budget = 12,000 credits/year, ~10 credits per animation = ~640 credits used. Massive headroom.

### Building art

| Asset | Count | Notes |
|---|---|---|
| Backdrop: mountains layer | 1 | LOCKED 2026-05-23 session 2. Flat vector, deep blues. |
| Backdrop: clouds layer | 1 | LOCKED 2026-05-23 session 2. Transparent PNG. |
| Backdrop: mist layer | 0 | Godot-native, hand-authored sprites, no Ludo asset. |
| Backdrop: sky | 0 | Godot-native gradient/color, no Ludo asset. |
| Specialty building art | 16 | 8 buildings × 2 tier states (T1 + T4); T8 deferred post-prototype |
| Head-only building art | 2 | Main Hall + Personal Sanctum, single state each (status open — see Open Questions) |
| Crowd FG silhouettes | 9 | LOCKED 2026-05-23 session 2. Pool of unique waist-up back-facing silhouettes; in-Godot composition handles scaling/count/distribution per population. |
| Atmosphere overlays | ~6 | Lit windows, qi wisps (Godot particles + small textures) |

### Environment / world

| Asset | Count | Notes |
|---|---|---|
| Region biome assets | ~32 | 8 regions × ~4 each (ground tile + 2–3 props per region) |
| World map | 1 | Hand-painted parchment, Mortal-realm scope |
| Region state overlays | ~4 | Fog, pulse, banner, gold focus ring |

### Card art

| Asset | Count | Notes |
|---|---|---|
| Day-1 card pool | 96 | 12 themes × 8 cards |
| Boss drop cards | 16 | 8 signature + 8 partner, R1–R3 only |
| Evolved card variants | TBD | Each evolvable technique needs evolved-form art; count depends on evolution-eligibility rules (deferred) |

**Approach:** Item visual + bordered card frame composed via Ludo reference workflow. Path-discovered state = visual modifier (border swap + particles), not separate generated card art.

### VFX

| Asset | Count | Notes |
|---|---|---|
| Technique VFX | ~30–50 | Per archetype × theme variants; heavy Godot tween/shader work reduces naive count |
| Pickup VFX | ~6 | Raw qi, essence, materials, stones, level-up, health |
| Damage / hit / crit sparks | ~5 | Reused universally |

### UI / iconography

| Asset | Count | Notes |
|---|---|---|
| Currency icons | 4 | Raw qi, essence, spirit stones, inspiration |
| Material icons | 24 | 12 themes × 2 tiers (T1–T2 for R1–R3 prototype) |
| Path icons | 12 | Theme markers, Sapling tier |
| Objective icons | 6 | Survival / Kills / Targets / Territory / Resources / Boss |
| Building state icons | ~12 | Locked / available / tier badges |
| HUD chrome | ~10 | Timer, XP bar, card slots, health bar, pause button |
| Modal chrome | ~5 | Hub modal, mission select, draft, pause, dialog scroll |
| Misc UI icons | ~10 | Settings, audio, controls, back, confirm |

### Splash / title / key art

| Asset | Count | Notes |
|---|---|---|
| Studio mark | 1 | Splash screen |
| Title key art layered | 3 layers | Parallax: foreground MC silhouette / mid-ground sect / sky |
| Title typography | 1 | Game logo treatment |

### Headline prototype total

Roughly **350–400 distinct art assets** of varying complexity, **~64 sprite-sheet animations**. Card art is the biggest single category. Within Ludo Pro's 12k credit/year budget.

---

## Audio Inventory

### Music — LOCKED

All tracks instrumental, anime-cinematic register, no vocals (with one possible exception flagged below).

| Track | Surface | Source | Prototype count |
|---|---|---|---|
| Title theme | Title screen | Your own (Suno) | 1 |
| Realm ambient | In-run | Suno | 3 (R1 / R2 / R3) |
| Realm boss (non-final) | Boss spawn | Suno | 3 (one per realm: R1 M1, R2 M1 + M2, R3 M1 + M2 — shared per realm) |
| Realm-final boss | Realm-final boss spawn | Suno | 3 (R1 M2, R2 M3, R3 M3) |
| Victory sting | Post-run win | Suno | 1 |
| Defeat sting | Post-run loss | Suno | 1 |
| They-Escaped sting | Post-run gate-fail | Suno | 1 (deferred — no R1–R3 boss triggers this) |

**Prototype Suno tracks: 9** + your title track = **10 tracks total.**

**R12 apex callback track (deferred design hook):** title-track-as-R12-final-boss-music callback. May be the only track with vocals if it lands. Language deferred (constructed cultivation tongue vs Mandarin vs other — likely not English to keep it mythic vs literal).

**Note on R1 M2:** Counts as realm-final for music purposes (gets unique track) despite shallow R1 difficulty curve. Keeps the music architecture consistent across all 12 realms with no R1 special-casing.

### SFX — LOCKED

**Approach:** Archetype-shared base SFX + theme color modifier layers. License a base library (Soundly / GameDev Market / Humble Bundle audio packs) + layer/modify in Audacity or Reaper.

| Category | Count | Notes |
|---|---|---|
| Combat | ~50 | 4 archetypes × 12 themes + hit/crit/dodge. Base archetype SFX with theme modifier layers. |
| Pickups | 6 | Raw qi / essence / material / stones / level-up / health |
| UI | 6 | Navigate / select / back / modal open / modal close / hover |
| Run flow | 5 | Objective bank / boss warning / boss arrival / run start / run end |
| Sect hub | 5 | Tier purchase / recruit / breakthrough / path advance / dialog typing |
| Ambient loops | 8 | 8 region biomes |
| Special | ~3 | Evolution / cycle activation / R12 capstone (deferred) |

**Prototype SFX total: ~80–85.** Mostly library + modification, not original commissioning.

### Audio pipeline tools

- **SFX layering:** Audacity (free) or Reaper ($60)
- **Sound libraries:** Soundly subscription or one-time pack purchase
- **Music:** Suno Premium (in hand)

---

## Asset Pipeline

### Ludo.ai mechanics (verified 2026-05-23)

Authoritative basics learned during the first hub-art session. Use these — earlier hand-wavy framings were wrong.

**Six generation modes:**

| Mode | Inputs | Use for |
|---|---|---|
| Generate New | text prompt + filters only | Pure ideation, no references |
| Edit Image | base image + text + optional Ref 2 | Modify an existing image globally |
| Generate from References | Ref 1 + optional Ref 2 + prompt | Use *elements* from references in a new image |
| Generate with Style | Ref 1 + optional Ref 2 + prompt | Adopt *artistic style* of references — primary mode for our pipeline |
| Edit with Mask | base + drawn mask + prompt + optional Ref 2 | Surgical replacement of a specific region |
| Erase with Mask | base image + mask | Remove object, AI fills in (no prompt) |

**Nine image types:** Background, Asset, Sprite, Sprite VFX, Icon, UI Asset, Texture, Art, Gameplay. Each shapes the output framing. Asset and Sprite are isolated subjects (no background); Sprite has flat lighting for animation; Background is full-scene atmosphere with no characters/UI; Icon is fixed 1:1; Texture is seamless tileable.

**Output batch:** Ludo returns 2 images per call (not 4 as previously assumed).

**Filters available:** Image Type, Genre, Color, Art Style (preset list), Perspective (incl. Top-Down), Aspect Ratio. Image Strength slider in edit modes.

**Filter reliability:** The Perspective dropdown does not reliably apply, at least for Asset and Art types. Bake critical filter values as a literal prompt prefix (e.g. `Top-Down View.` even when the dropdown is set). Treat other dropdowns the same way until verified by testing.

**Style filter availability:** No Art Style dropdown is shown in Generate with Style mode. Style is carried by Reference 1.

**Prompt structure (per Ludo's own guidance):** Subject / Action / Setting / Style, one paragraph, natural language, no special syntax. Their detailed example is ~30 words. Our experience: shorter prompts consistently outperform longer ones (see Prompt-Craft Lessons below).

### Two-Reference-1 model

The earlier "single canonical Reference 1 (Avatar TLA lineup) never changes" framing breaks the moment we leave character work — a character lineup leaks character elements into a building/environment generation. Use two Reference 1 anchors, one per macro family:

- **Characters family** → Avatar TLA character lineup (locked MC + boss + enemy sprites all reference this).
- **Environments + buildings family** → an Avatar TLA environment screenshot (Air Temple establishing shot or equivalent). Painterly aesthetic, architecture/landscape as subject.

Cards, UI, VFX may need their own Reference 1 anchors as we get to them; decide per-family when reached.

### First-piece-in-family exception

The previous "never generate without both references attached" rule cannot apply to the **first piece in any family**, since there's no Reference 2 yet. The corrected rule:

> First piece in a family uses Reference 1 only (or a one-time anchor). The locked first piece then becomes Reference 2 for everything downstream in that family.

For hub family specifically, the first locked piece (compound background plate, locked 2026-05-23) becomes Reference 2 for all 10 individual building generations + any future hub-canvas changes.

### Hub asset architecture (redesigned 2026-05-23 session 2)

Original iso compound architecture (background plate + 10 iso building sprites) was abandoned 2026-05-23 session 2 after the building-isometric-vs-plate-perspective open question and continued Ludo style-consistency failures on iso compound work. Two compounding problems forced the pivot: (a) Asset-type generations enforce a default isometric angle that didn't match the locked plate, so every building gen fought the plate's perspective; (b) Ludo holds painted style reliably on architecture pieces but drifts to flat vector on landscape-only work, so the iso compound put both burdens on every gen at once.

Front-facing skyline composition separates the two problems via parallax depth layers. Architecture pieces still render painterly; landscape pieces render flat vector; both coexist because they sit at different depth layers.

**Architecture (6-layer parallax stack, composited at runtime in Godot):**

1. **Sky** — solid color or gradient drawn in Godot. No Ludo asset. Allows time-of-day tinting via shader/color swap.
2. **Mountains** — Ludo-generated back layer. Static or slow parallax. Locked 2026-05-23 session 2.
3. **Clouds** — Ludo-generated, transparent PNG. Horizontal drift animation in Godot. Locked 2026-05-23 session 2.
4. **Mist** — hand-authored in Godot (soft sprites, low-opacity, additive blend, slow drift). Not a Ludo asset — Ludo's mist output didn't match the painted source and Godot-native is both better-fitting and cheaper.
5. **Buildings** — 10 individual sprites. Ground edges baked into each sprite's base. Front-facing perspective, consistent register. Drift pattern #18 (Population overlay) still respected — buildings stay separable sprites with anchor points and click hotspots.
6. **Crowd FG** — silhouette layer of disciples facing the sect (away from camera), hands clasped behind back, sparse bob/shuffle motion. Pool of 9 unique silhouettes locked 2026-05-23 session 2.

The plateau / ground band the buildings sit on is structural-line-only — not a separate art asset. Each building sprite has its ground edge baked into its base, and the crowd FG covers anything below the horizon line as population scales up.

**Visual growth axes redesigned to fit the skyline:**

- **Tier axis** unchanged in principle (T1/T4/T8 base art per building). Larger tier stages naturally read as more impressive in front-facing — taller/wider sprites break the horizon line higher and overlap with the cloud/mountain layers behind.
- **Population axis** redesigned from per-building NPC overlays to aggregate FG crowd density. Implementation lives in [pillars/sect-management.md](../pillars/sect-management.md) Visual Growth section. Drift pattern #18 not violated — population is still a runtime overlay independent of tier; only the visual representation changed.

**Per-building work per the Tier axis:** each of the 10 buildings needs T1 + T4 sprites for prototype (head-only Main Hall and Personal Sanctum single-state status unresolved — see Open Questions).

**Hub building layout (was open question):** RESOLVED via emergent per-building placement in Godot, not pre-planned. Layout decisions happen when each building sprite is dropped into the scene. Front-facing pivot doesn't change this — it actually makes per-building placement simpler, since buildings just need horizontal position + depth-layer assignment rather than iso-grid coordination.

**Backdrop layers locked status:**

| Layer | Status | Notes |
|---|---|---|
| Sky | Godot-native | Solid/gradient color in scene, no Ludo asset |
| Mountains | LOCKED | Ludo flat-vector, deep blue palette, hard shape gradients |
| Clouds | LOCKED | Transparent PNG, white forms with light-blue underlining |
| Mist | Godot-native | Hand-authored sprite set, additive blend, no Ludo asset |
| Buildings | TODO | First gen (Main Hall) pending, uses compound-scene-then-edit pattern |
| Crowd FG | LOCKED (pool of 9) | See sect-management.md Visual Growth |

The original `stone_floor.png` plate is INVALIDATED by the architecture pivot — no longer in the layer stack.

### Prompt-Craft Lessons (running list)

Learned via direct Ludo session iteration. Apply to every generation.

1. **Describe only visible elements.** Never name what shouldn't appear, even with "no" or "not." Models manifest nouns regardless of qualifying language. "No buildings" tends to produce buildings.
2. **Quantity callouts leak.** "Space for ten buildings" produced ten buildings in an open-courtyard prompt. Don't reference numbers of things you don't want drawn.
3. **Edit Image for global/scene-wide changes** (color shifts, structural removals, mood adjustments). Regenerates the whole image with consistent visual logic.
4. **Edit with Mask for genuinely local single-element changes** (swap one specific element, recolor one spot). Mask region treats prompt nouns as isolated patches.
5. **Mask prompts inflate nouns to mask scale.** Be ruthlessly minimal — 1–2 words ideally. `stone floor` outperformed `packed-earth ground with subtle moss patches`. Let surrounding pixels inform the fill at the edges.
6. **Minimal Edit Image prompts outperform verbose ones.** `stone floor` produced cleaner results than detailed multi-clause prompts.
7. **Filter dropdowns don't reliably apply.** Confirmed for Perspective on Asset and Art types. Bake critical filter values as literal prompt prefixes (`Top-Down View.`). Assume the same of other dropdowns until verified.
8. **Asset type enforces its own default isometric perspective** regardless of Reference 1's angle or prompt directives. "Same angle as reference" doesn't translate. Asset is a centered hero shot. Plan composition workflow around this constraint, not against it.
9. **Asset outputs frequently include a base/platform/foundation.** Need to suppress it explicitly when composite-integrating with a ground plate.
10. **Asset outputs need explicit shadow direction** to ground them visually on a target background. `casting a soft shadow on the ground` works.
11. **Generate with Style inherits linework, painterly register, and palette family loosely.** Specific color choices (e.g. coral/red on pagoda trim) revert to training biases each gen. Color overrides require explicit prompt language or post-gen Edit Image cleanup.
12. **Color edits don't persist across descendant generations.** An Edit Image color fix only modifies the edited image. To propagate a color change downstream, the edited image must itself become Reference 2 — not just the source for new generations.
13. **The design-doc voice contaminates prompts.** Anything reading like a spec ("comfortably hold X buildings", "with Y and Z details") is too verbose and leaks unwanted nouns. Prompts should read like a painter's mental sketch: subject, view, era, medium. Twenty words is plenty for most cases.
14. **Reference 1 dominates over subject in Generate New for landscape/figure prompts.** During session 2, env Reference 1 absorbed "robed cultivator" as a scene element to place into a landscape rather than the frame's subject — five of six gens did this. Mitigation: switch Reference 1 to the character lineup family when generating figures. Sticking with the env reference because "we've been using it all session" is the failure mode. The two-Reference-1 model has families for a reason — use them.
15. **Generate New does not honor "transparent background" in the prompt.** Multiple session 2 attempts confirmed Generate New returns opaque backgrounds regardless of prompt phrasing. Some gens returned a rendered checkerboard pattern that visually mimics transparency but is baked pixels — distinguishable by slightly off-color or faint gradient. Mitigation: drop "transparent background" from Generate New prompts entirely; use "Pure black figure" or "white background" instead.
16. **Two-step Generate-then-Edit pattern for transparency.** Generate New produces the subject on opaque background. Edit Image then strips the background ("Remove the background, keep only the figure"). Edit Image honors transparency reliably and returns clean transparent PNG. Adds one gen per asset but eliminates the fake-checkerboard failure mode. Pattern works for both figures and isolated objects (clouds layer locked session 2 used this).
17. **Single-tone silhouette prompts can't carry color qualifiers on features.** "Pure black figure" + "long grey beard" is a direct contradiction — Ludo either picks one and ignores the other, or compromises into something neither wanted. When a silhouette is locked to a single tone, drop all color qualifiers from feature descriptions. The silhouette IS the color descriptor. Beard length, beard volume, beard shape are valid; beard color is fixed by the silhouette rule.
18. **Abstract body-type descriptors fail without a concrete posture/feature anchor.** "Tall thin xianxia cultivator" came back as a scene, not a figure. "Broad heavyset xianxia cultivator with hands clasped behind back" came back correctly. The posture anchor ("hands clasped behind back") gives Ludo a concrete pose to render, which forces it to treat the descriptor as figure attributes rather than scene mood. Pattern: every figure prompt needs at least one concrete pose/feature word to break Reference 1 dominance.
19. **Compound-scene-then-peel-layers pattern for multi-layer assets.** When a scene needs multiple separable layers (mountains + clouds + mist), generate a styled compound scene first (Generate New with style reference locked), then peel each layer out via Edit Image ("Remove X, keep Y"). This uses Ludo's strongest mode (Edit Image, proven consistent) and avoids the consistency lottery of generating each layer independently from references. Pattern validated session 2 on hub backdrop (3 layers extracted from a single compound source, all style-consistent because they share the source).

### Asset tracking

Production state lives in [asset-inventory.md](asset-inventory.md). Status (TODO / Briefed / Generated / Locked / In Repo), date, prompt snippet where useful.

### Reference asset location

Reference 1 images and locked Reference 2 pieces currently live in **Ludo Favorites** plus local working files. The previously documented `res://assets/_references/` path does not exist yet — the Godot project has not been created. Once the Godot project is initialized (code-phase kickoff per CLAUDE.md), references will be copied into `res://assets/_references/` for permanent dev-only storage.

### Folder structure / naming / resolution / animation handoff

Per [tech-stack.md](../tech-stack.md). Unchanged from prior locks. Validate `res://` paths exist after Godot project creation.

---

## In-Scope vs Out-of-Scope (Final Cut)

### In prototype

- All 9 surfaces (Splash through Post-Run) + Dialog/Cutscene system
- Cross-surface controller focus state (global UX requirement)
- 9 Suno tracks + your title track + ~80 SFX
- ~350–400 art assets across categories
- 8 character presets, 8 R1–R3 bosses, R1–R3 region biomes
- Mortal-era visual identity for all assets

### Out of prototype (deferred)

| Item | Reason |
|---|---|
| Engine logo / multi-mark splash | Cut from splash spec |
| Multiple save slots | Single save covers needs |
| Parts-swap character creator | Presets sufficient; build if game earns out |
| Per-tier-unique building art (T1–T10 each) | 3-stage tier visuals sufficient; prototype uses T1 + T4 only |
| T8 building visual state | Beyond prototype tier cap (T5 / T7 Pavilion) |
| Era-evolution art passes (Transcendent / Immortal / Divine / Eternal) | All prototype assets Mortal-era |
| R4+ region biome assets | Beyond prototype map scope |
| Animated story cinematics with motion | Static dialog/banner sufficient |
| Full accessibility suite | Minimum viable only |
| Real exotic-gate-triggered "They Escaped" encounters | No R1–R3 boss is exotic-gated; system architected but untriggered in prototype |
| Mobile platform polish beyond layout | PC-first per tech-stack.md |
| Console export configurations | PC-first per tech-stack.md |
| Save versioning / migration | Post-launch concern |
| Mod support | Out of v1 scope |
| R12 apex callback track | Deferred design hook (track + lyric question) |

### Open questions (post-design-pass)

Surfaced during this session or follow-up work, not blockers but flagged:

- Evolution-eligibility rules per card (affects evolved card art count)
- R12 apex callback track specifics (vocal language, instrumentation)
- ~~Hub building layout — specific positions on the compound (lands when first building art arrives)~~ **RESOLVED 2026-05-23** — emergent per-building placement in Godot per the locked hub asset architecture.
- Mobile virtual button specific placements / sizes / fade behavior (deferred until mobile is active scope)
- ~~**Building isometric vs plate perspective (NEW 2026-05-23):** Asset-type Generate with Style enforces its own default isometric angle that doesn't match the locked plate's flatter perspective.~~ **RESOLVED 2026-05-23 session 2 by architecture pivot.** Front-facing skyline composition supersedes the iso compound architecture. Perspective mismatch no longer applies — buildings and backdrop are now separate parallax layers at the same camera orientation.
- **Building visual style register under front-facing skyline — RE-OPENED 2026-05-23 session 4.** Brief history: session 2 raised the question; session 3 resolved as flat vector (Main Hall v1 navy came back flat, composite preview validated cohesion with locked flat-vector backdrop); session 4 user replaced v1 with v2 warm olive (still flat vector, color shift only for silhouette read against mountains) → then user replaced v2 with **v3 painterly** (Studio Ghibli–register, bonsai + stone shrine baked in). v3 is the current lock and explicitly retires the flat-vector-architecture lock. New open question: how does painterly architecture coexist with flat-vector backdrop layers? Three possible paths — (a) regenerate backdrop layers in painterly register to match, (b) regenerate buildings in flat vector to match backdrop, (c) accept the cross-style composition as intentional (different visual planes read differently by design). Decision deferred until more buildings are generated and the cross-style read can be evaluated across the full hub composition. Currently 1 of 10 buildings; need at least 2–3 more to judge cohesion vs jarring at the full scene scale.
- **Head-only building tier states (PRE-EXISTING DISCREPANCY surfaced 2026-05-23, still open after architecture pivot):** Surface 5 specs "10 buildings × 2 visual stages = 20". Art Inventory > Building art lists Main Hall + Personal Sanctum as "single state each" (= 18 total). Skyline architecture pivot doesn't resolve this — Main Hall and Personal Sanctum still need to be defined as either tier-progressing (3 stages each = +2 per building) or static (single state each). Decision pending. Lower priority than building style register since both head-only buildings still exist in the skyline.

All landed in [open-questions.md](../open-questions.md) under Deferred for Later.
