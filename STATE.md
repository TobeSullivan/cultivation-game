# State — Cultivation Game
Last updated: 2026-05-23 (session 4 — Claude Code kickoff)

## Current focus

**Godot project alive. hub_test scene composites the full 6-layer skyline at 1920×1080 with the Main Hall v3 (painterly), 3 animated mist sprites, and an 18-figure crowd FG with bob/shuffle tween. Style coexistence (painterly Main Hall on flat-vector backdrop) is the new live design question, deferred until 2–3 more buildings exist.**

This was the Claude Code kickoff session. Engine work begins. Production parallel track (other 9 buildings in Ludo) can now resume with hub_test as the in-engine validation surface for each new lock.

## Last session

Hub Godot kickoff, 2026-05-23 (session 4). First session in Claude Code.

**Built:**

- `game/` Godot 4.6.3 project — project.godot configured (1920×1080 / GL Compatibility / linear texture filter), directory structure per tech-stack.md
- `game/scenes/hub_test.tscn` — 6-layer skyline composite:
  - Sky: TextureRect + vertical GradientTexture2D (cool blue → pale blue)
  - Mountains: Sprite2D, y=350, scale 1.43×
  - MistLayer: 3 Sprite2Ds with programmatic radial GradientTexture2D (#b8c4d0 pale cool grey-blue, normal alpha blend, opacity 0.55, varied sizes 3.125×0.78 / 3.9×0.7 / 2.7×0.86, y-band 780–850), drift via `drift.gd` at 4/6/9 px/sec
  - Ground: ColorRect dark slate y=935–1080
  - HorizonPlatform: ColorRect black y=895–935 (40px thick)
  - MainHall v3 painterly: centered, scale 0.45×, y=764 (bottom flush with platform top)
  - CrowdFG: 18 silhouettes (9 unique × 2, half horizontally flipped via negative scale.x), baselines y=1075, scales 0.08–0.14, uneven horizontal scatter (left cluster 150–430, mid 580–850, around-building 980–1210, right cluster 1370–1540, far right 1670–1780), bob/shuffle controller attached
- `game/scripts/drift.gd` — horizontal-drift component with wrap (exports speed, wrap_min_x, wrap_max_x)
- `game/scripts/crowd_bob.gd` — sparse one-at-a-time weight-shift controller (1.5–5s random interval, asymmetric 1.2s sink + 1.0s recover, SINE ease-in-out, 5px amplitude)
- `game/scripts/screenshot_and_quit.gd` — dev utility (supports `repo://` path scheme to land outputs in repo root)
- `tools/extract_cloud_pieces.py` — scipy connected-components for splitting cloud-band PNGs into individual cloud sprites

**Asset locks landed this session:**

- **Main Hall v3 painterly** — `assets/buildings/main_hall.png` 1327×613 keyed RGBA. Replaces v1 navy + v2 warm olive (both preserved as `_v1_navy_roof.png` / `_v2_warm_olive.png` for reference). Painterly Studio Ghibli–register includes baked bonsai tree and stone shrine. Style choice retires the session 3 flat-vector-architecture lock — see Open Questions.
- **9 crowd silhouettes keyed** — passed through `tools/key_out_checkerboard.py`. Now true RGBA, in `game/assets/hub/crowd/`. Dimensions 429–790 wide × 716–768 tall.
- **clouds.png keyed** — was discovered to have solid white opaque background (not the checkerboard documented session 2). Key script handled it identically. Plus 8 individual cloud forms extracted via the new `extract_cloud_pieces.py`. Currently unused in scene — single-sprite drift exposed sparse-coverage / pixelated-edges issues; user opted to drop clouds from hub_test until better individual-cloud variety lands.

**Process rule established:**

- **Cook-before-code** — propose plan and wait for explicit approval before any Edit/Write/Bash that mutates state. Established mid-session after a cluster of unilateral iterations on hub_test composition burned through tokens. Saved as memory at `~/.claude/projects/C--dev-cultivation-game/memory/feedback_cook_before_code.md`. Now governs all future engine + doc work in this project.

**Python toolchain set up:**

- Python 3.12.10 via winget (full path `C:\Users\tobes\AppData\Local\Programs\Python\Python312\python.exe` since not on PATH for the bash subprocess)
- `pip install Pillow numpy scipy` complete
- `tools/key_out_checkerboard.py` (existing) + `tools/extract_cloud_pieces.py` (new) both runnable

**Doc updates this wrap:**

- `CLAUDE.md` — repo structure block reflects game/ existence + tools/ contents + assets/ tree; Art Style lock split (backdrop locked flat vector, architecture re-opened); Main Hall entry shows three-version history; Engine entry expanded with Godot project + hub_test + Python toolchain + cook-before-code rule; Pre-code step 6 marked complete; What's Open updated for re-opened style register
- `PROJECT.md` — game/ section populated; new tools/ section; new assets/ section listing the three Main Hall versions + crowd + clouds
- `docs/prototype/asset-inventory.md` — Style Locks table updated (architecture register re-opened, three-step pipeline noted, cloud asset-state surprise noted); Backdrop layer stack reflects IN GAME status with hub_test detail; Buildings table Main Hall row updated (LOCKED v3 painterly); Crowd FG section updated (IN GAME with 18-figure composition + bob controller spec); Reference 2 buildings-family entry re-opened
- `docs/prototype/design-pass.md` — Surface 5 asset ask updated; building visual style register open question re-opened with full session-3-to-session-4 history
- `docs/open-questions.md` — Hub building layout resolved; new painterly-vs-flat-vector style coexistence open question added; head-only building tier states explicit; new "Resolved 2026-05-23 Session 4 (Claude Code Kickoff)" section with full session summary

## Next step

Three reasonable directions, user's call:

1. **Continue hub production parallel track.** Generate 1–2 more buildings in Ludo (e.g., Personal Sanctum + Teahouse — both present in the prototype but not yet briefed). Key + drop into hub_test alongside Main Hall. This gives 3 buildings to evaluate the painterly-vs-flat-vector style coexistence question (currently can't be answered with just 1 building in scene). Decision on style coexistence becomes possible after.

2. **Move to a different surface.** Title screen / Character Select / Splash — these are also in prototype scope per design-pass.md. Could build a second test scene to validate the surface-flow patterns (scene transitions, autoload singletons, UI controls). Doesn't gate hub work; gives engine architecture some breadth before going deep on hub.

3. **Tech-stack build order step 2 — resource class definitions.** Per `docs/tech-stack.md` build order: scaffold the `.gd` files that define Card, Boss, EnemyType, Building, Disciple, SaveData, etc. matching `docs/data/schema.md`. No content yet — just the type definitions. Foundational work that everything else needs eventually.

My lean: **#1** while context is fresh. Need at least 2–3 buildings to make a real call on the style coexistence question, and Personal Sanctum is the natural next pick (other head-only, simple geometry, won't fight the current composition). Then style coexistence question becomes actionable.

## Open questions / blocked on

Full list in `docs/open-questions.md`. Highest leverage for current production:

- **Painterly architecture vs flat-vector backdrop coexistence** (NEW this session) — Main Hall v3 is painterly, mountains + ground + mist + crowd are flat vector. Three resolution paths (regen backdrop / regen buildings / accept cross-style); deferred until 2–3 more buildings let us evaluate at full scene scale.
- **Head-only building tier states** — Main Hall + Personal Sanctum: single state each, or tier-progressing like specialty buildings? Lower priority than the style coexistence question.

Engine architecture items that will surface as scope expands:
- Autoload singletons (GameManager / SaveManager / EventBus / AudioManager) — currently empty placeholders not yet created
- Resource class definitions (per tech-stack.md build order step 2)
- Hub interaction model (click hotspots on buildings → modal — not yet implemented)
- Scene transition patterns (Splash → Title → Character Select → Hub) — not yet wired

Other open items unchanged from session 3 wrap — see `docs/open-questions.md`.

## Commit recommendation

This wrap is a clean commit point. Suggested message:

```
Session 4: Godot kickoff + hub_test + Main Hall v3 painterly

- game/ Godot 4.6.3 project bootstrapped
- hub_test.tscn assembles 6-layer skyline composite (sky/mountains/mist/ground/horizon/building/crowd)
- drift.gd + crowd_bob.gd + screenshot_and_quit.gd
- Main Hall iterated v1 navy -> v2 warm olive -> v3 painterly (current lock)
- 9 crowd silhouettes keyed, 18-figure crowd scatter with bob/shuffle tween
- tools/extract_cloud_pieces.py (scipy connected-components for cloud split)
- Cook-before-code rule established
- Style coexistence (painterly building on flat-vector backdrop) re-opened
```

Files to add: everything under `game/`, new files under `tools/` and `assets/`, plus doc updates listed above. `.gitignore` already covers `screenshots/`.
