# State — Cultivation Game
Last updated: 2026-05-23 (session 2)

## Current focus

**Hub art production, session 2 closed. Architecture pivot landed.** Iso compound abandoned; front-facing skyline locked. Backdrop layers (mountains + clouds) locked. Crowd FG silhouette pool locked at 9 figures. Production now unblocked on building generation — first test is Main Hall in the new front-facing register.

## Last session

Hub art session 2, 2026-05-23. Heaviest session of the project so far on art workflow discovery and architecture pivots.

**Architecture pivot:**

- **Iso compound → front-facing skyline.** Yesterday's locked iso compound architecture was abandoned after the building-isometric-vs-plate-perspective open question hit and continued Ludo style-consistency failures on iso architecture work. Two compounding problems forced the pivot: (a) Asset-type generations enforce a default isometric angle that didn't match the locked plate; (b) Ludo holds painted style reliably on architecture pieces but drifts to flat vector on landscape-only work. Front-facing skyline composition separates the two via parallax depth layers.
- **Layer stack locked (6 layers):** sky (Godot-native gradient) / mountains (Ludo, locked) / clouds (Ludo, locked) / mist (Godot-native hand-authored) / buildings (10 individual sprites, TODO) / crowd FG (silhouette pool of 9, locked).
- **Two style families now coexist** at different depth layers — architecture pieces painterly (TLA family), backdrop landscape flat vector with hard shape gradients. The eye reads them as distinct planes; pivot is the tool-reality split.

**Locks landed:**

1. **Art style updated** — Hand-painted illustrated 2D, Avatar TLA family. Camera revised to front-facing 2D (not 3/4 angled top-down). Architecture painterly, backdrop flat vector, both accepted as tool-reality split.

2. **Hub asset architecture redesigned** — Front-facing skyline 6-layer parallax stack. Buildings still individual sprites (drift pattern #18 respected). Population axis redesigned: aggregate FG crowd density instead of per-building NPCs.

3. **Backdrop layers locked** — Mountains (flat vector, deep blues) + Clouds (transparent PNG, white forms with light-blue underlining) both locked from a single compound-scene-then-peel-layers source. Mist deferred to Godot-native hand-authored sprites. Sky deferred to Godot-native gradient.

4. **Crowd FG silhouette pool locked (9 figures):** upright topknot, bowed topknot, ceremonial hat, long-hair tied (low ponytail), long flowing hair female, high-bun female, broad heavyset, pointed hood, cowl hood. All waist-up, back-facing, hands clasped behind back, pure black on transparent. Composition in Godot at runtime (selection / scaling / distribution / sparse bob-shuffle tween).

5. **Generate-then-Edit pattern locked** — Two-step for any transparent-background asset: Generate New on opaque background, then Edit Image to strip background. Generate New doesn't honor "transparent background" in prompts; Edit Image does, reliably.

6. **6 new prompt-craft lessons (#14-19)** — env Reference 1 dominates over subject on figure work, Generate New doesn't honor transparent background, two-step pattern locked, single-tone silhouette can't carry color qualifiers, abstract body-type descriptors need posture anchor, compound-scene-then-peel-layers pattern for multi-layer assets.

**Drift patterns added (CLAUDE.md):**

- **#20** — Single-tone silhouette prompts can't carry color qualifiers on features ("Pure black figure" + "long grey beard" = contradiction).
- **#21** — Environment Reference 1 dominates over figure subject in Generate New; switch to character Reference 1 for figure work.
- **#22** — Generate New does not honor "transparent background" in the prompt; use Edit Image two-step instead.

**Open questions resolved:**

- **Building isometric vs plate perspective** — RESOLVED by architecture pivot. Front-facing skyline puts buildings and backdrop on the same camera orientation; perspective mismatch no longer applies.
- **Hub building layout** — RESOLVED 2026-05-23 session 1 (emergent per-building in Godot). Still resolved under skyline architecture, in fact simpler now.

**Open questions added or carried forward:**

- **Building visual style register under skyline (NEW session 2)** — Open. Backdrop layers locked flat vector. Open: do front-facing buildings come back painterly (like iso compound did) or flatten toward backdrop style? Resolution: first building gen (Main Hall) tests this.
- **Head-only building tier states** — Still open. Surface 5 vs Art Inventory discrepancy (10 × 2 = 20 vs 18 with two head-only single-state). Skyline pivot doesn't resolve. Lower priority than building style register.

**Generation history this session** (for prompt-craft reference):

- First front-facing test (compound w/ pagodas) — painterly hit, but too many buildings in one image
- Mountain silhouette attempts (3 tries) — all came back flat vector, not painterly. Lesson: empty landscape leaves Ludo too much room; painterly style only holds when architecture anchors it
- Locked mountain backdrop chosen from batch 1 (wide parallax composition)
- Edit Image three-pass to peel mountains / mist / clouds layers — all three returned. Mist quality off (looked like sea fog) — deferred to Godot-native. Mountains + clouds locked.
- Pattern locked: compound-scene-then-peel-layers via Edit Image
- Crowd FG single-figure pivot — original "crowd band" prompt produced a literal mountain scene of cultivators (env reference absorbed subject)
- 6 silhouette attempts across 3 prompts — only "hands clasped behind back" reliably produced figure-as-subject. Pattern: concrete posture anchor breaks env-reference dominance
- Image 1 silhouette locked as base (upright topknot, back-facing)
- Iterative builds to pool of 9 — ceremonial hat, bowed topknot, long-hair tied (unexpected elder result), long flowing hair female, high-bun female, heavyset, two hoods
- Bald monk cut (too similar to topknot at silhouette scale); back-facing elder failed twice and dropped

**Files modified this session:**

- `CLAUDE.md` — Drift patterns #20, #21, #22 added. Locked Decisions: art style updated (front-facing + style split), hub asset architecture redesigned, backdrop layers locked, crowd FG silhouette pool locked, Generate-then-Edit pattern locked. Pre-code sequencing step 5 updated. What's Open updated (building isometric resolved, building style register new open, head-only tier states still open).
- `docs/prototype/design-pass.md` — Surface 5 rewrite (skyline composition). Hub asset architecture section rewrite (6-layer stack, architecture pivot rationale). Building art table rewrite (backdrop layers + crowd FG pool). 6 new prompt-craft lessons (#14-19). Open Questions section update.
- `docs/prototype/asset-inventory.md` — Style Locks table rewrite. Backdrop layer stack new section. Buildings table update (Main Hall regen pending). Crowd FG silhouette pool new section. Invalidated assets section. Reference 2 anchors updated.
- `docs/pillars/sect-management.md` — Visual Growth Axis 2 rewrite (per-building NPC → aggregate FG crowd model; old model retained for context).
- `STATE.md` — full rewrite (this file).

## Next step

**First building generation: Main Hall in front-facing skyline register.** This is the first real test of the open question on building style register under skyline architecture — does Ludo come back painterly on front-facing architecture the way it did on iso compound, or does it flatten toward the backdrop style?

Approach: Generate New with character/env Reference 1 (test both, env probably better given subject is architecture), prompt minimal in painter's sketch register (per Lesson 13). Use the locked mountains backdrop as Reference 2 — first time the new backdrop serves as the style anchor for downstream architecture work.

Suggested first prompt to try (subject to iteration):

```
Front-facing view. Mortal-era xianxia main hall, large tiled roof, weathered red columns. Hand-painted illustration.
```

If painted style holds: lock Main Hall, drop into Godot with locked backdrop layers to validate composite at real resolution. This is also the moment the Godot project gets created.

If painted style drifts to flat vector (matches backdrop): decide whether to accept the unified flat-vector treatment across the whole composition, or fight for painted architecture via Edit Image from a known-painted character/architecture source.

After Main Hall lands and the style register question resolves: proceed to the other 9 buildings using locked Main Hall as the per-building style anchor (Reference 2 for buildings family).

## Open questions / blocked on

Full list in `docs/open-questions.md` (cleanup deferred to next session opening — see below). Highest leverage for current production:

- **Building visual style register under front-facing skyline** — see Next step. First building generation tests this.
- **Head-only building tier states** — Surface 5 vs Art Inventory discrepancy. Pre-existing, surfaced session 1, still open. Lower priority.

Other open items (not gating hub art):
- Economy-side cost curves (own session, post-prototype-art)
- NG+ design session (post-prototype)
- 48 path effects (per content design pass)
- Per-card design pass (96 day-1 cards × per-level content)
- Full title-ladder pass across all 20 chains

## Open-questions.md housekeeping (deferred to next session opening)

Not in context this session. Cleanup needed when next loaded:

**Move to Resolved:**
- Building isometric vs plate perspective (resolved 2026-05-23 session 2 by architecture pivot)

**Add or update:**
- Building visual style register under front-facing skyline (NEW, open)
- Head-only building tier states (carried forward, still open)

**Already-resolved (carry):**
- Hub building layout (resolved session 1, still resolved under skyline)

**Keep as currently flagged:**
- All economy-side cost curve items
- NG+ architecture
- All previously-flagged content design passes
