# Project Map — Cultivation Game

One-line map of what exists in the repo. Updated when files are added/moved/removed. Companion to [STATE.md](STATE.md).

---

## Root

- [README.md](README.md) — one-paragraph project description
- [CLAUDE.md](CLAUDE.md) — project-specific addendum to Claude rules; terminology, locked decisions, drift patterns
- [claude-rules.md](claude-rules.md) — universal Claude operating manual
- [STATE.md](STATE.md) — current focus, last session, next step
- [PROJECT.md](PROJECT.md) — this file

## docs/ — Design Corpus

- [docs/README.md](docs/README.md) — design index
- [docs/vision.md](docs/vision.md) — vision, principles, v6 version notes
- [docs/tech-stack.md](docs/tech-stack.md) — engine, art pipeline, save system, Godot project structure, build order
- [docs/open-questions.md](docs/open-questions.md) — open questions, deferred items, prototype build-blocking work

### docs/pillars/ — The Four Core Systems

- [docs/pillars/run-loop.md](docs/pillars/run-loop.md) — VS run, six universal objectives, level-up draft, evolutions, meridians, 96-card day-1 pool
- [docs/pillars/cultivation.md](docs/pillars/cultivation.md) — 12 stages, 5 eras, 8 cycles, qi pool, breakthroughs, inspiration
- [docs/pillars/risk-map.md](docs/pillars/risk-map.md) — 12 realms, adjacency, enemies, idle output, rival sects
- [docs/pillars/sect-management.md](docs/pillars/sect-management.md) — disciples, training, sect power, 10 buildings

### docs/systems/ — Cross-Pillar Mechanics

- [docs/systems/path-system.md](docs/systems/path-system.md) — 12 paths × 5 tiers, Sapling effects, Righteous Path capstone
- [docs/systems/economy.md](docs/systems/economy.md) — 4 currencies + materials, qi vs essence, sect power multiplier
- [docs/systems/building-tier-curves.md](docs/systems/building-tier-curves.md) — Compounding vs Flat-cap, surfaces, cost table
- [docs/systems/boss-roster.md](docs/systems/boss-roster.md) — specialty taxonomy, schema, ~139 named disciples, special-event recruits
- [docs/systems/unlock-web.md](docs/systems/unlock-web.md) — Major/Medium/Minor surfacing, notification model, load-bearing edges

### docs/prototype/ — R1–R3 Build Target

- [docs/prototype/scope.md](docs/prototype/scope.md) — 8 maps overview, adjacency, building unlock order, difficulty curve
- [docs/prototype/design-pass.md](docs/prototype/design-pass.md) — surface, art, audio, pipeline inventory for shippable prototype
- [docs/prototype/bosses.md](docs/prototype/bosses.md) — full per-map boss detail (identity, biome, signature, combat, objectives)
- [docs/prototype/rewards.md](docs/prototype/rewards.md) — per-objective rewards, forward-shift derangement, per-map quantities

### docs/data/ — Schema

- [docs/data/schema.md](docs/data/schema.md) — entity/relationship model, persistent state, schema invariants

## game/ — Godot Project

Created 2026-05-23 session 4 (Claude Code kickoff). Godot 4.6.3 stable, GDScript.

- `project.godot` — viewport 1920×1080, GL Compatibility renderer
- `scenes/hub_test.tscn` — front-facing skyline composite: sky gradient + mountains + 3 mist sprites (additive blend, slow drift) + grey ground + black horizon line + Main Hall v3 + 18-figure crowd FG silhouette layer with bob/shuffle tween
- `scripts/drift.gd` — generic horizontal-drift component with wrap (used by mist sprites)
- `scripts/crowd_bob.gd` — sparse weight-shift tween controller on CrowdFG (one figure at a time, 1.5–5s random intervals, asymmetric 1.2s/1.0s ease-in-out)
- `scripts/screenshot_and_quit.gd` — dev utility for headless renders (supports `repo://` path scheme to land screenshots in repo root)
- `assets/` — mirrored copies of locked hub assets imported into res://

## tools/ — Reusable Scripts

- [tools/key_out_checkerboard.py](tools/key_out_checkerboard.py) — strip Ludo's baked checkerboard background (drift #23), produce true RGBA. Used on Main Hall, clouds, and 9 crowd silhouettes.
- [tools/extract_cloud_pieces.py](tools/extract_cloud_pieces.py) — connected-components labeling on a keyed cloud PNG, split into individual cloud sprite files. Output unused in current scene (clouds dropped, may revisit).

## assets/ — Locked Pre-Godot Art

- [assets/buildings/main_hall.png](assets/buildings/main_hall.png) — v3 painterly, current lock (2026-05-23 session 4)
- [assets/buildings/main_hall_v1_navy_roof.png](assets/buildings/main_hall_v1_navy_roof.png) — preserved (session 3 lock, retired session 4)
- [assets/buildings/main_hall_v2_warm_olive.png](assets/buildings/main_hall_v2_warm_olive.png) — preserved (session 4 mid-iteration lock, retired same session)
- [assets/hub/mountains.png](assets/hub/mountains.png) — locked session 2
- [assets/hub/clouds.png](assets/hub/clouds.png) — keyed session 4 (was opaque white, not true RGBA — see session 4 notes)
- [assets/hub/clouds/cloud_01..08.png](assets/hub/clouds/) — extracted cloud forms (session 4, currently unused in scene)
- [assets/hub/crowd/*.png](assets/hub/crowd/) — 9 silhouettes, keyed session 4 (true RGBA per drift #23)

## _archive/ — Obsolete / Reference Only

- [_archive/cultivation_game_design_doc_v6.md](_archive/cultivation_game_design_doc_v6.md) — pre-split monolithic design doc; content distributed across `docs/`
- [_archive/prototype-spec.md](_archive/prototype-spec.md) — pre-split prototype spec; content now in `docs/prototype/`
- [_archive/data-schema.md](_archive/data-schema.md) — pre-relocation copy; current version at [docs/data/schema.md](docs/data/schema.md)
- [_archive/v6-merge-and-open-questions.md](_archive/v6-merge-and-open-questions.md) — pre-relocation copy; current version at [docs/open-questions.md](docs/open-questions.md)
- [_archive/tech-stack-and-pipeline.md](_archive/tech-stack-and-pipeline.md) — pre-relocation copy; current version at [docs/tech-stack.md](docs/tech-stack.md)
- [_archive/building-tier-curves.md](_archive/building-tier-curves.md) — content folded into v6 / [docs/systems/building-tier-curves.md](docs/systems/building-tier-curves.md)
- [_archive/session-handoff-2026-05-20.md](_archive/session-handoff-2026-05-20.md) — one-off, superseded by STATE.md
