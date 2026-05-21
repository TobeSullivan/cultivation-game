# CLAUDE.md — Cultivation Game

Project-specific addendum. **Read `claude-rules.md` first, then this.** Project rules override universal defaults where stated.

---

## What This Project Is

A premium ($5–10) idle-survivor cultivation game. Vampire Survivors as the core active loop, with Adventure Capitalist (idle), Risk (territorial conquest), and sect management layered on top. Currently in design phase, transitioning to prototype build (R1–R3 scope). Engine: Godot 4 (GDScript).

One playable character throughout: the sect head.

---

## Repo State — Read This Carefully

- **GitHub:** `cultivation-game` (public, owned by user)
- **Status as of 2026-05-21:** repo exists but is **completely empty**. No files committed. **Not cloned locally yet.**
- **Storage layer:** this repo is where ALL project content lives. The Claude.ai Project folder contains ONLY `claude-rules.md` and this file (`CLAUDE.md`). Per universal rules.

---

## First Session Priority (Heavy Operation)

The very first task in the next session is the structural setup. **This is strongly recommended to be done with Claude Code, not Claude.ai chat.** Claude Code can read the filesystem directly, split files in place, and move files between directories without producing 10+ separate artifacts the user has to save manually.

Sequence:

1. User has already cloned the repo and unzipped the initial file dump (see Current Repo State below)
2. Claude Code reads `CLAUDE.md` to orient
3. Triggers heavy-op checkpoint, confirms with user
4. Creates the planned folder structure (`docs/pillars/`, `docs/systems/`, `docs/prototype/`, `docs/data/`, `game/`)
5. Splits `cultivation_game_design_doc_v6.md` into ~10 focused files across `docs/`
6. Moves `prototype-spec.md` → split into `docs/prototype/` files
7. Moves `data-schema.md` → `docs/data/schema.md`
8. Moves `v6-merge-and-open-questions.md` → `docs/open-questions.md`
9. After split, moves `cultivation_game_design_doc_v6.md` to `_archive/`
10. Authors `STATE.md` and `PROJECT.md`
11. Initial commit + push

If using Claude.ai instead: same sequence but produces artifacts the user manually saves to the correct paths. Slower and error-prone.

---

## Current Repo State (Post-Zip-Unzip, Pre-First-Session)

After user unzips the initial file dump into the cloned repo, this is what exists:

```
cultivation-game/
├── README.md                              # one-paragraph project description
├── claude-rules.md                        # universal rules
├── CLAUDE.md                              # this file
├── cultivation_game_design_doc_v6.md      # CURRENT canonical design — to split next session
├── prototype-spec.md                      # CURRENT prototype detail — to split next session
├── data-schema.md                         # CURRENT data schema — to relocate next session
├── v6-merge-and-open-questions.md         # CURRENT open questions — to relocate next session
├── tech-stack-and-pipeline.md             # CURRENT production decisions — to relocate next session
└── _archive/
    ├── building-tier-curves.md            # content folded into v6
    └── session-handoff-2026-05-20.md      # one-off doc, no longer needed
```

**Active files at root that need handling next session:**

| File | What next session does with it |
|---|---|
| `cultivation_game_design_doc_v6.md` | Split into ~10 focused files under `docs/`, then move original to `_archive/` |
| `prototype-spec.md` | Split into `docs/prototype/scope.md`, `docs/prototype/bosses.md`, `docs/prototype/rewards.md` |
| `data-schema.md` | Move to `docs/data/schema.md` |
| `v6-merge-and-open-questions.md` | Move to `docs/open-questions.md` |
| `tech-stack-and-pipeline.md` | Move to `docs/tech-stack.md` (production decisions: engine, art pipeline, save system, Godot subdirectory structure, build order — already locked) |

**Files already in `_archive/`:** leave alone. Reference only if explicitly needed for "what did we used to think about X." Note: v3/v4/v5 of the design doc were already cleared from the Claude.ai Project folder by the user prior to this zip — they don't need to be archived again.

**Important production note from `tech-stack-and-pipeline.md`:** the Godot subdirectory layout (what goes in `game/assets/`, `game/scenes/`, `game/scripts/`, etc.) is already locked. When code phase begins, follow that structure — do not re-design.

---

## Planned Structure (Does Not Exist Yet)

```
cultivation-game/
├── README.md                # one paragraph: what this is
├── claude-rules.md          # universal rules
├── CLAUDE.md                # this file (project addendum)
├── STATE.md                 # current focus / last session / next step
├── PROJECT.md               # map of what exists, one line each
│
├── docs/
│   ├── README.md            # design index
│   ├── vision.md            # high-level vision + core principles
│   ├── tech-stack.md        # engine, art pipeline, save system, build order (production)
│   ├── pillars/
│   │   ├── run-loop.md
│   │   ├── cultivation.md
│   │   ├── risk-map.md
│   │   └── sect-management.md
│   ├── systems/
│   │   ├── path-system.md
│   │   ├── economy.md
│   │   ├── building-tier-curves.md
│   │   ├── boss-roster.md
│   │   └── unlock-web.md
│   ├── prototype/
│   │   ├── scope.md
│   │   ├── bosses.md
│   │   └── rewards.md
│   ├── data/
│   │   └── schema.md
│   └── open-questions.md
│
├── game/                    # Godot project (empty until coding phase)
└── _archive/                # obsolete docs, exhaust
```

When referencing files in conversation, use this layout. The structure is designed so most sessions touch 2–5 files, not the whole thing.

---

## Tools In Use

- **Claude.ai chat** — design conversation, exploratory work, branching decisions
- **Claude Code** — code authoring, file ops, structural changes (when coding phase begins)
- Both share the same subscription budget; tool choice is workflow, not cost
- When invoked from the repo directory, Claude Code reads this `CLAUDE.md` automatically

---

## Terminology — Project-Specific, Often Confused

| Term | Meaning |
|---|---|
| **Cards** | Run-loadout pool entries. NOT "scrolls" (deferred flavor rename) |
| **Themes** | Identity markers for path membership. 12 of them (Wood/Earth/Fire/Water/Metal/Wind/Ice/Lightning/Shadow/Spirit/Star/Void). NOT damage types, NOT DoT types |
| **Specialties** | Who-runs-the-building tags. 8 building specialties + 12 theme specialties |
| **Tier** | Used in MULTIPLE contexts: card level (1–8), cultivation tier-within-stage (3 per stage), material tier (1–6), building tier (varies). Specify which when ambiguous |
| **Stage** | Cultivation stage (1–12), 1 per realm. NOT a tier synonym |
| **Realm** | Geographic scope (R1 Province → R12 Universe). NOT a stage or tier synonym |
| **Era** | Visual identity bracket. 5 eras (Mortal/Transcendent/Immortal/Divine/Eternal) |
| **Path** | One per theme (12 paths) + Righteous Path (13th capstone). 5 manifestation tiers per path (Sapling → Sprout → Grove → Forest → Worldroot) |

---

## Drift Patterns User Has Corrected — Do Not Repeat

1. **Don't fish for validation.** Answer the question. One lock-and-move per turn.
2. **Don't drift from docs.** Follow what's locked. Flag changes as changes explicitly.
3. **Recruit unlocks PURCHASE POTENTIAL, not auto-tier.** Recruiting Nth specialist makes Nth tier purchasable. The tier still costs materials + essence.
4. **Bosses don't need many attacks.** R12 finals = ~5 attacks across 3–4 phases. Escalation through tighter telegraphs, attack overlap, arena interaction — NOT more moves.
5. **6 universal objectives per map.** Not 3, not 4. Variable is numbers, not which objectives.
6. **Resources are unified.** Tier-gated, optionally theme-tagged. No separate building vs card material pools.
7. **First-time-only rewards.** Ambient drops only on replay. No double-dipping.
8. **Path-recipe-membership and card-power are orthogonal.** Specialist rating and tier-unlock-via-recruit are separate axes.
9. **Tier-state interpretation (drifted three times in one session):** Master's starting rating IS the tier ceiling. Pao at rating 5 → Teahouse T1–T5. Lin at rating 7 (Heaven-Reader exception) → Pavilion T1–T7. Don't confuse "tier" with "realm" — prototype is R1–R3 by realm, T1–T5/T1–T7 by tier.
10. **Boss spawn rule.** Spawns when all 5 other objectives complete OR at 25-min mark, whichever first. NOT 30-min. NOT player-triggered.
11. **Search past convos before inventing.** If something feels designed but isn't in visible docs, search first.
12. **When math interpretation changes, flag prior calculations as needing redo.** Don't silently update conclusions while leaving stale numbers in earlier turns.

---

## Locked Decisions — Memorize These

These come up constantly and are easy to misremember.

- **Currency model:** 4 currencies + Materials.
  - Qi (personal pool, tier breakthroughs only)
  - Essence (universal upgrade currency)
  - Spirit Stones (higher-tier, not premium MTX — gold→platinum)
  - Inspiration (Stage 4+ breakthroughs only)
  - Monster Cores CUT — kills drop raw qi directly
- **Materials:** 12 themes × 6 tiers = 72. Realm pairs share tier (R1–R2=T1, R3–R4=T2, etc.)
- **Sect Power multiplier:** `1 + sqrt(Sect_Power / 100)` — sub-linear, NOT linear
- **Day-1 pool:** 96 cards (12 themes × 8). Endgame ~444
- **Card max level:** 8
- **Meridian range:** 4–8. Refinement pacing: 5th end-R3, 6th end-R5, 7th end-R7, 8th end-R10
- **Building tier ceiling = Master's starting rating** (see drift pattern #9)
- **6 universal objectives per map:** Survival / Kills / Targets / Territory / Resources / Boss
- **Uniform reward type per objective:** Survival=Essence, Kills=Raw qi, Targets=mixed materials, Territory=themed material cache, Resources=designated partner passive, Boss=signature + recruit + stones + (realm-finals)inspiration shard
- **Engine:** Godot 4, GDScript

---

## Working Style — This Project Specifically

- **Mobile interface.** User often replies from phone. Tables and short lists scan well. Avoid walls of prose.
- **Propose-with-recommendation.** When asking user to pick between options, give your lean and reasoning. Don't present pure menus.
- **Search-first triggers.** Always search docs before:
  - Filling in any numeric value
  - Restating a rule from memory
  - Proposing a system change ("I think we should...")
  - Describing how something works
- **Direct on mistakes.** Restate cleanly, integrate the correction, move on. No excessive apology.
- **No emojis.** User doesn't use them.

---

## End-of-Session Protocol — This Project

Universal rules cover the wrap protocol. Project specifics:

- Files touched live in the repo, NOT the Claude.ai Project folder
- Artifacts go to the path in the repo where they belong (e.g., `docs/systems/economy.md`, not just `economy.md`)
- `STATE.md` updated LAST, reflecting what was touched and what's next
- **No standalone session-handoff docs.** Wrap updates the persistent docs. The handoff IS the diff in git.

---

## When Coding Phase Begins (Godot)

- Engine: Godot 4 with GDScript (C# only if perf demands it later)
- Code lives in `game/` subdirectory of the repo
- Run from terminal: `cd cultivation-game/` then `claude` to invoke Claude Code with context
- First milestone: R1–R3 prototype with all 8 buildings unlockable; full scope in `docs/prototype/scope.md` (post-split)

---

## What's Open — Brief Reference

Authoritative list lives in `docs/open-questions.md` once structure exists. Currently:

- Re-fight vs. auto-unlock for late-completed boss recruits (leaning re-fight)
- Apprentice contribution coefficient
- Heaven-Reader arc length (3 vs 4 members)
- Path Sprout/Grove/Forest/Worldroot effect designs (48 still to design)
- Pairing convention universality across all 12 themes
- T2–T5 leaf content for 6 buildings (Recruitment/Training/Storehouse/Outer Court/Library/Forge)
- Spirit stone exchange rate / specific sinks
- Soul Forge T1 leaves design

---

*This file is itself subject to the universal rules. If it grows past ~2k tokens, split it. Prune stale sections. Treat as working document.*
