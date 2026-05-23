# State — Cultivation Game
Last updated: 2026-05-23 (session 3)

## Current focus

**Main Hall locked. Three-step asset pipeline locked. Next session = Claude Code, Godot project creation.**

Session 3 closed the first building generation, surfaced drift pattern #23 (Edit Image background removal also bakes checkerboard), and locked the canonical three-step Generate-then-Edit-then-key pipeline with a reusable script. Composite preview confirmed style cohesion. Hub art production unblocked on the remaining 9 buildings, and the engine work that's been gated by "first building must land before Godot setup" can now begin.

## Last session

Hub art session 3, 2026-05-23.

**First building generation:**

- **Three Main Hall attempts** with the cloud-line ground-dodge prompt: "Mortal-era xianxia main hall above the cloud line. Front view, tiled roof, red columns. Painterly hand-painted illustration with visible brushwork."
- **Style returned flat vector**, not painterly. The "painterly hand-painted illustration with visible brushwork" prompt elements were ignored. User read: this is fine — flat vector harmonizes with the locked flat-vector backdrop layers. The painterly aspiration is retired.
- Three outputs: (1) Generate New result with clouds, (2) Edit Image "remove clouds" result with blue sky, (3) Edit Image "remove background" result — visually transparent (checkerboard pattern) but file is RGB with checkerboard baked. This was the drift #23 discovery moment.

**Composite preview (one-off, validated then retired as a Claude workflow):**

- Stripped checkerboard from image 1 via PIL (gray-detection + brightness threshold + 1px alpha erosion + bbox crop).
- Composited keyed Main Hall onto locked mountains backdrop.
- First attempt: building too big (filled frame, dwarfed mountains, edge halos visible). Rejected.
- Second attempt: building scaled to 40% canvas width, centered, base near bottom. Halos cleaned up by lower brightness threshold + erosion. Composition read as intended: mountains as true parallax background, building as foreground element, sky breathing room above.
- **User read on the preview:** style cohesion confirmed (both layers flat vector with deep-blue palette — they belong together), the painterly-vs-vector worry was wasted breath. Building scale and platform-line treatment are decisions to make in Godot, not in Claude. Compositing in Claude retired as inefficient — image editors and the Godot scene itself are the right surfaces.

**Pipeline lock:**

- Drift pattern #23 confirmed: Ludo Edit Image "Remove background" returns RGB with checkerboard baked as pixels, not RGBA. The session 2 lock "Edit Image honors transparency reliably" was visually plausible but file-incorrect.
- The Generate-then-Edit two-step (session 2 lock) is replaced by **Generate-then-Edit-then-key three-step**:
  1. Generate New on "white background" or "Pure black figure"
  2. Edit Image "Remove the background, keep only the figure"
  3. Programmatic key-out via `tools/key_out_checkerboard.py`
- Script is reproducible. Sample run on Main Hall image 1 produced canonical asset at `assets/buildings/main_hall.png` (1160×572, true RGBA, cropped to bbox).
- All 9 remaining buildings will follow the same three-step. All 9 locked crowd silhouettes will need to run through the script too — they were locked session 2 before drift #23 was understood, so they're currently checkerboard-baked, not true RGBA.

**Main Hall locked:**

- Canonical asset: `assets/buildings/main_hall.png`
- Style register: flat vector, deep-blue + red palette, harmonizes with locked backdrop
- Building base includes baked platform / stairs / balustrade per drift pattern #18
- Reference 2 anchor for the buildings family — all 9 remaining buildings use locked Main Hall as Reference 2

**Drift patterns added (CLAUDE.md):**

- **#23** — Edit Image background removal also returns baked checkerboard, not true RGBA. Mitigation: third pipeline step with `tools/key_out_checkerboard.py`.

**Open questions resolved:**

- **Building visual style register under front-facing skyline** — RESOLVED. Flat vector across the board, validated by composite preview.

**Workflow lesson surfaced:**

- Mechanical compositing (load PNGs, key, scale, paste) is faster in image editors or directly in the target engine. Claude's value is in prompt iteration with Ludo and design reasoning; pixel-pushing previews are the wrong use of the tool. Captured in CLAUDE.md Locked Decisions ("Compositing previews don't happen in Claude").

**Files modified this session (in this wrap):**

- `CLAUDE.md` — Drift pattern #23 added. Three-step Generate-then-Edit-then-key pipeline locked (replaces session 2 two-step). Main Hall locked. Style register resolved (flat vector across all layers). Compositing-previews-not-in-Claude lock added. Pre-code sequencing step 5 updated with session 3 progress. What's Open: building visual style register moved to RESOLVED. Repo structure section updated with `tools/` and `assets/` directories.
- `tools/key_out_checkerboard.py` — NEW. Reusable script for stripping Ludo's baked checkerboard from Edit Image output.
- `assets/buildings/main_hall.png` — NEW. Canonical Main Hall asset, true RGBA, ready for Godot import.
- `STATE.md` — full rewrite (this file).

**Files NOT modified this wrap, pending Claude Code session opening:**

Two docs that need session 3 updates but weren't in context this session. Spec'd below so the Claude Code session can do them as part of orientation:

- `docs/prototype/design-pass.md`:
  - Asset Pipeline section: update Generate-then-Edit pattern to Generate-then-Edit-then-key three-step. Reference `tools/key_out_checkerboard.py` as the step 3 tool. Cross-reference drift #23.
  - Prompt-Craft Lessons: add a new lesson on "design-doc voice contaminates tool prompts" if not already there from session 2; add a lesson on three-step pipeline. Style-register-painterly-vs-vector entry: mark resolved (flat vector locked).
  - Hub asset architecture / Surface 5: Main Hall locked notation, reference to `assets/buildings/main_hall.png`.

- `docs/prototype/asset-inventory.md`:
  - Style Locks table: art style entry updated (painterly aspiration retired, flat vector across all layers).
  - Buildings table: Main Hall row marked locked with asset path and dimensions.
  - Reference 2 anchors table: buildings family Reference 2 = locked Main Hall (`assets/buildings/main_hall.png`).
  - Production state for crowd silhouette pool: note that the locked 9 figures need to run through `tools/key_out_checkerboard.py` before Godot import (currently checkerboard-baked from session 2 work).

Open-questions.md housekeeping from previous wraps (still deferred): see "Open-questions.md housekeeping" section below.

## Next step

**Launch Claude Code from the repo for Godot project setup.**

Workflow:
1. Unzip this wrap into the repo root.
2. Commit ("Session 3: Main Hall locked, three-step pipeline, drift #23").
3. `cd cultivation-game/`
4. `claude` to launch Claude Code with full context. CLAUDE.md, claude-rules.md, and STATE.md auto-load.

**Session opening tasks for Claude Code:**

1. **Two doc cleanups** (spec'd in "Files NOT modified this wrap" above): update `docs/prototype/design-pass.md` and `docs/prototype/asset-inventory.md` with session 3 locks. Same-session housekeeping before engine work begins.
2. **Open-questions.md cleanup** (deferred from session 2 wrap, see below).
3. **Create Godot project** in `game/`. Godot 4 with GDScript. Standard project structure (scenes, scripts, assets folders within game/).
4. **First scene: hub composite test.** Drop the layer stack at real resolution:
   - Sky: Godot ColorRect or gradient
   - Mountains: import `mountains.png` from session 2 (assuming it's in the repo — check `assets/backdrop/` or wherever it was placed; if not, user needs to drop it in)
   - Clouds: import locked clouds asset (same check)
   - Mist: hand-author in Godot — start with 2-3 sprites, additive blend, slow horizontal drift
   - Buildings: import `assets/buildings/main_hall.png` (locked this session, true RGBA)
   - Crowd FG: keying-pending. Run the 9 silhouettes through `tools/key_out_checkerboard.py` first, then import.
5. **Author platform / horizon line** that the building sits on. This is a Godot-native decision — color, thickness, exact y-position. The line goes above the foreground mountain peaks so mountains read as parallax background, building sits on platform.
6. **Sample crowd composition.** Drop 1-2 silhouette figures in the FG band at varying scales to validate the three-layer-with-depth read. Sparse bob/shuffle tween authoring deferred until composition reads right.
7. **Parallax setup.** Mountains slow scroll, clouds horizontal drift, mist slow drift, buildings + crowd static (or very slight parallax). Numbers to iterate.

**Production parallel track:** While engine work is happening, the other 9 buildings can continue being generated in Ludo using the locked three-step pipeline with Main Hall as Reference 2. This is user-side work, doesn't block Claude Code.

## Open questions / blocked on

Full list in `docs/open-questions.md` (cleanup deferred again, see below). Highest leverage for current production:

- **Head-only building tier states** — Surface 5 vs Art Inventory discrepancy (10 × 2 = 20 vs 18 with two head-only single-state). Carried forward. Not blocking — both Main Hall and Personal Sanctum will get a single locked sprite for now; tier-progression decision can be deferred to a later art pass.

Other open items (not gating Godot session):
- Economy-side cost curves (own session, post-prototype-art)
- NG+ design session (post-prototype)
- 48 path effects (per content design pass)
- Per-card design pass (96 day-1 cards × per-level content)
- Full title-ladder pass across all 20 chains

## Open-questions.md housekeeping (deferred again to next session opening)

Not in context this session. Cleanup needed when next loaded — to be folded into the doc cleanups in the Claude Code session opening:

**Move to Resolved:**
- Building isometric vs plate perspective (resolved 2026-05-23 session 2 by architecture pivot)
- Building visual style register under front-facing skyline (resolved 2026-05-23 session 3, composite preview validated)
- Hub building layout (resolved session 1, still resolved under skyline)

**Add or update:**
- Head-only building tier states (carried forward, still open, demoted priority — non-blocking)

**Keep as currently flagged:**
- All economy-side cost curve items
- NG+ architecture
- All previously-flagged content design passes
- Within-run HP scaling genre divergence (post-playtest revisit)
- R12 void-aspected elite reuse idea
