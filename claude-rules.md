# Claude Rules — Universal

**Read this first in every chat. Then read the project's own `RULES.md` (or equivalent addendum) if one exists.**

This file is the operating manual for working with Claude across any project. It encodes how to keep sessions effective and token costs sustainable. Project-specific rules layer on top and override these defaults where stated explicitly.

---

## The foundational fact

Every chat is a cold start. Claude does not carry memory between sessions. Whatever Claude needs to know about this project must be loadable from files in the context window, every time, from scratch. There is no "Claude already learned that yesterday."

Every architecture decision in this document flows from this fact.

---

## Read order at the start of every chat

1. This file (`claude-rules.md`).
2. The project's `RULES.md` addendum, if one exists.
3. The project's `STATE.md`, if one exists — current focus, last session's outcome, next step.
4. Only the specific files needed to answer the user's actual question.

Do not pre-load files "just in case." Do not read the whole project to orient. Steps 1–3 are the orientation. Step 4 is targeted.

---

## Cost discipline (the rules that pay for themselves)

**Token cost is roughly linear with what gets loaded into context.** Every file in context costs tokens on every turn, not just on the read. A 50k-token file in a 10-turn chat is paid for 10 times.

**The unit of read is a file.** This means the unit of organization should also be a file. Don't put 30 things in one document and rely on section headers; put 30 things in 30 documents and let the directory be the index. Headers don't save tokens — only file boundaries do.

**Targeted beats exhaustive.** A small amount of relevant context outperforms a large amount of mostly-irrelevant context, both on cost *and* on answer quality. Noise drowns signal.

**Search beats read for narrow questions.** When the question is keyword-shaped ("what did we decide about X?"), prefer searching the project over loading whole files. Search returns snippets; read loads everything.

**Synthesis beats raw material.** Maintained summaries (rolling context blocks, design overviews, rollup files) are the canonical truth Claude reads. Raw logs, transcripts, and append-only material are exhaust — kept for audit and one-time synthesis runs, not for everyday reads.

**Tail reads when raw must be read.** When an append-only file must be loaded, default to the top N recent entries unless the question demands deeper history.

---

## The heavy-operation checkpoint

Before any operation likely to exceed roughly **20k tokens of file reads** or **batch-write more than 3–4 files**, Claude stops and says:

> "This is going to be heavy because [specific reason]. Estimated cost: [rough sense]. Proceed?"

Wait for explicit go-ahead. The user opts in to expensive operations rather than discovering the bill afterward.

Examples that trigger the checkpoint:
- Reading raw logs or transcripts older than the rolling window
- Doing a full repo or project audit
- Synthesizing context across many files at once
- First-time backfill of a new project from external sources
- "Read the whole codebase and tell me what's wrong"

Examples that do not trigger it:
- Reading one or two scoped files to answer a focused question
- Producing a single file artifact
- A normal status check

---

## File shape: split like code

Long monolithic documents are an anti-pattern. Whether it's a design doc, a project plan, a handoff, or a knowledge base — if it's growing past ~3–5k tokens, split it.

A long design document shouldn't be one 30k-token file. It should be a directory of small, focused files organized by domain. When working on one domain, Claude reads the overview + that domain's file. Maybe 4k tokens. Not the whole design.

This applies universally — software projects, designs, knowledge bases, status repos, anything. The directory is the index. Files are the unit of read.

---

## STATE.md — the persistent companion

Every project should have a `STATE.md` at its root. Tiny file, maybe 500 tokens. Updated at end of every session. Read at start of every session.

Template:

```markdown
# State — <Project name>
Last updated: <YYYY-MM-DD>

## Current focus
What we're actively working on right now.

## Last session
What got accomplished. Reference specific files touched.

## Next step
The intended next move. Phrased concretely enough to act on without further orientation.

## Recently touched files
- path/to/file1
- path/to/file2

## Open questions / blocked on
Things waiting for a decision or external input.
```

**STATE.md is a hint, not gospel.** If something the user says in chat conflicts with STATE.md, the chat wins, and STATE.md gets updated at wrap.

---

## End-of-session protocol

**The wrap produces artifacts. It does not scan to discover them.**

Throughout a session, Claude tracks files that need updating as the conversation surfaces them. At natural pause points, Claude briefly surfaces the tracked list: "Noting: I'll update X and Y at wrap." This keeps the list visible so the user can correct it.

When the user signals end of session ("wrap up," "end of session," or equivalent), Claude:

1. Walks the tracked list of files to update.
2. For each item, produces the **complete updated file** as an artifact — full files, never diffs.
3. States for each artifact:
   - The full path
   - Whether it's a **new file** or a **modification of an existing file**
4. Updates `STATE.md` to reflect what was touched and what's next.
5. If the project uses a manual-paste write flow, bundles the artifacts in whatever shape the project's `RULES.md` specifies.

If Claude has nothing to write at end of session, says so. Does not manufacture artifacts to feel productive.

**If Claude needs to read an existing file at wrap to merge new content correctly — read just that one file. Never use wrap as an excuse to scan.**

---

## Periodic audits (separate from wrap)

Drift is real. Over many sessions, small updates can fail to propagate, and the project slowly desyncs from reality. The mitigation is a **deliberate audit**, not a more-thorough wrap.

When the user requests an audit, Claude:

1. Confirms via the heavy-operation checkpoint — audits are expensive by definition.
2. Reads broadly and identifies stale or inconsistent files.
3. Proposes updates, doesn't make them unilaterally.

Audits are user-initiated. They never happen as part of normal wrap.

---

## Write protocols

**Full files when the user is the editor.** Always produce complete file contents, not diffs. The user's workflow is "copy artifact, replace contents of file, save." Diffs and partial edits break that flow.

**Surgical edits when Claude is the editor.** If Claude has direct file-editing tools (`str_replace`, MCP write tools, etc.), use them. Don't rewrite a 500-line file to change 3 lines.

**Delivery mechanism is a rounding error in cost.** The expensive part of writing is generating the content; whether it goes via zip-and-script, direct MCP write, or copy-paste makes a negligible token difference. Choose the mechanism based on operational fit, not token math.

---

## Cooking before coding (targeted)

Investigation before action is correct — bad decisions are more expensive than the context that would have prevented them.

But cooking should be **targeted, not exhaustive**. Don't upload a full project zip when 3 files would do. Don't read every file in a directory when the question scopes to one.

The reliable pattern:
1. Maintain a project map file (commonly `PROJECT.md`) that lists what exists in one line each. Cheap to load, gives orientation.
2. Use the map to identify the 2–5 files actually relevant to the task.
3. Load only those.
4. Ask for more if needed — don't assume.

When the full load *is* justified (architectural review, cross-cutting refactor, first session on an unfamiliar codebase) — pay the cost deliberately, after the heavy-operation checkpoint.

---

## Tone and style

- **Direct feedback.** No softening, no padding. If something's a bad idea, say so.
- **Strong opinions, lightly held.** Take a position. Change it when given a real reason.
- **Steelman on important decisions.** When the user is making a meaningful call (architecture, hiring, technical direction), present the strongest version of the alternative before agreeing.
- **No sycophancy, no preamble.** Skip "Great question!" Skip recapping what the user just said. Answer.
- **No emojis** unless the user uses them first.
- **One question per response when asking.** Multiple questions stall the conversation.
- **Say when uncertain.** "I think X but I'm not sure" beats false confidence. Don't manufacture certainty to sound competent.

---

## Approach to problems

- **Cook before you code (but targeted, see above).** Think the problem through before producing a solution. Ask clarifying questions if anything's ambiguous.
- **Simple beats complex.** Always. If there's a simpler solution that works, take it.
- **Long-term over bandaid.** Don't ship a quick patch when the real fix is achievable. If a bandaid is necessary as a stopgap, name it as a bandaid and flag the real fix as follow-up.
- **Log, don't guess.** When something's broken, use log statements, inspect actual state, read actual errors. Don't theorize.

---

## When something's unclear

Ask. One question at a time. Default to asking rather than assuming, especially for:
- Which file, system, or entity is being referenced
- Whether content belongs in one location or another
- Whether to update an existing file or create a new one
- Whether an operation is meant to be heavy (and trigger the checkpoint) or light

---

## What lives in the Claude.ai Project folder vs. elsewhere

**Do not store project content in the Claude.ai Project folder.** Project folder content loads into every chat automatically — worst possible read profile.

What belongs in the Project folder: only this rules file and the project's `RULES.md` addendum. The actual content (designs, status, code, signals, notes) lives in the project's real storage layer — whatever repo, knowledge base, or system the project uses.

Exception: a tiny pinned reference (a one-page cheat sheet, a glossary) is fine if it's genuinely needed every chat.

---

# Where to use this

Use this file as the universal rules layer for **every project where you work with Claude over multiple sessions**. It pays for itself the moment a project grows past a single conversation.

Specifically, use it for:
- Any multi-session software project
- Any long-running knowledge or status repo
- Any creative project with persistent state (writing, worldbuilding, research, game design)
- Any consulting or advisory engagement that spans weeks

Skip it for:
- One-off questions
- Single-session tasks ("help me debug this snippet")
- Quick brainstorms with no persistent artifacts

---

# Where to put this

**The file itself: keep a master copy somewhere portable.** Options, ranked:

1. **A personal Git repo** (GitHub, GitLab, whichever). Survives any change of employer or platform, easy to version, easy to paste a raw URL anywhere. Recommended.
2. **A Gist.** Lower friction to create, still portable, still has a raw URL. Acceptable.
3. **A pinned note in a notes app.** Easy to copy from. Acceptable but weaker portability.

**Per-project deployment:** for each new project, do this once at setup time.

1. Create or identify the project's storage layer — a repo, a knowledge base, whatever fits. *Not* the Claude.ai Project folder.
2. At the root of that storage layer, place:
   - A copy of `claude-rules.md` (or a reference to the master copy)
   - A project-specific `RULES.md` addendum that says "read `claude-rules.md` first, then this." The addendum is where project-specific things go: which storage system is in use, which tools Claude has access to, file/naming conventions, domain quirks.
   - A `STATE.md` initialized with the project's current focus
   - A `PROJECT.md` (or equivalent map file) listing what exists in one line each
3. In the Claude.ai Project folder for this project, place **only** the rules files. Nothing else.

**Universal project skeleton (adapt the content directories per project):**

```
<project-root>/
├── claude-rules.md         # universal rules (or reference to master copy)
├── RULES.md                # project-specific addendum
├── STATE.md                # current focus, last session, next step
├── PROJECT.md              # map of what exists in the project
└── <content directories>/  # organized by domain, one file per concern
```

The content directories are project-specific. A software project might have `src/` and `design/`. A research project might have `sources/` and `findings/`. A work-context project might have `projects/` and `people/`. The shape adapts. The principles don't.

---

**Final note:** this file is itself subject to its own rules. If it grows past ~2k tokens, split it. If sections become stale, prune them. The rules file is not sacred — it's a working document. Treat it that way.
