# State — Cultivation Game
Last updated: 2026-05-21

## Current focus

Project just completed its structural setup. Design corpus split from monolithic v6 doc into a directory of focused files under `docs/`. Repo is now ready for normal session-scoped work: pick a 2–5 file slice per session.

Transitioning from design phase to prototype build prep. Engine and pipeline already locked (Godot 4 / GDScript, Ludo Pro for art) — see [docs/tech-stack.md](docs/tech-stack.md).

## Last session

Heavy-op structural setup, executed in Claude Code:
- Created `docs/` folder structure (`pillars/`, `systems/`, `prototype/`, `data/`)
- Split [cultivation_game_design_doc_v6.md](_archive/cultivation_game_design_doc_v6.md) into 11 focused files (4 pillars + 5 systems + vision + index)
- Split [prototype-spec.md](_archive/prototype-spec.md) into 3 files under `docs/prototype/`
- Relocated `data-schema.md` → `docs/data/schema.md`, `v6-merge-and-open-questions.md` → `docs/open-questions.md`, `tech-stack-and-pipeline.md` → `docs/tech-stack.md`
- Archived the v6 monolith and removed root-level source files now distributed under `docs/`
- Authored this `STATE.md` and `PROJECT.md`

## Next step

Resolve outstanding open questions or begin prototype Godot scaffolding.

Pick one of:
1. **Prototype build kick-off.** Start at step 1 of the build order in [docs/tech-stack.md](docs/tech-stack.md): create the Godot project skeleton under `game/`, set up autoload singletons (GameManager, SaveManager, EventBus, AudioManager) as empty shells, then write Resource class definitions matching [docs/data/schema.md](docs/data/schema.md).
2. **Knock down open questions.** Highest-leverage items in [docs/open-questions.md](docs/open-questions.md) before coding: meridian refinement material identities, apprentice contribution coefficient, T2–T5 leaf content for the 6 buildings without it.
3. **Naming pass on the prototype.** All boss/card/region names are placeholders. 8 prototype bosses + 16 prototype cards is a tight chunk that would lock visible identity for the build.

## Recently touched files

All files under `docs/` (newly created or relocated this session). Originals archived to `_archive/`.

## Open questions / blocked on

Full list in [docs/open-questions.md](docs/open-questions.md). Highlights:

- Re-fight vs auto-unlock for late-completed boss recruits (leaning re-fight)
- Apprentice contribution coefficient
- Heaven-Reader arc length: 3 vs 4 members (affects Pavilion max tier T1–T9 vs T1–T10)
- 48 path effects (Sprout/Grove/Forest/Worldroot per theme) — pacing during dev TBD
- T2–T5 leaf content for 6 of 8 buildings
