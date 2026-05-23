# CLAUDE.md — Cultivation Game

Project-specific addendum. **Read `claude-rules.md` first, then this.** Project rules override universal defaults where stated.

---

## What This Project Is

A premium ($5–10) idle-survivor cultivation game. Vampire Survivors as the core active loop, with Adventure Capitalist (idle), Risk (territorial conquest), and sect management layered on top. Currently in design phase, transitioning to prototype build (R1–R3 scope). Engine: Godot 4 (GDScript).

One playable character throughout: the sect head.

---

## Repo State

- **GitHub:** `cultivation-game` (public, owned by user)
- Structural split from monolithic v6 doc complete. Design corpus lives under `docs/` organized by domain.

---

## Tools In Use

- **Claude.ai chat** — design conversation, exploratory work, branching decisions
- **Claude Code** — code authoring, file ops, structural changes (coding phase begins next session)
- Both share the same subscription budget; tool choice is workflow, not cost
- When invoked from the repo directory, Claude Code reads this `CLAUDE.md` automatically

---

## Repo Structure

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
│   │   ├── design-pass.md
│   │   ├── asset-inventory.md
│   │   ├── bosses.md
│   │   └── rewards.md
│   ├── data/
│   │   └── schema.md
│   └── open-questions.md
│
├── tools/                   # reusable scripts
│   ├── key_out_checkerboard.py    # strip Ludo's baked checkerboard, see drift #23
│   └── extract_cloud_pieces.py    # split cloud-band PNG into individual cloud sprites via scipy connected components
├── assets/                  # locked art assets, pre-Godot import
│   ├── buildings/
│   │   ├── main_hall.png             # current lock = v3 painterly (2026-05-23 session 4)
│   │   ├── main_hall_v1_navy_roof.png # preserved (locked s3, retired s4)
│   │   └── main_hall_v2_warm_olive.png # preserved (interim s4, retired same session)
│   └── hub/
│       ├── mountains.png    # locked s2
│       ├── clouds.png       # keyed s4 (currently unused in hub_test)
│       ├── clouds/          # 8 extracted cloud forms (cloud_01..08.png), currently unused
│       └── crowd/           # 9 keyed silhouettes (s4), 18-figure scatter in hub_test
├── game/                    # Godot project — created 2026-05-23 session 4
│   ├── project.godot        # viewport 1920×1080, GL Compatibility renderer
│   ├── scenes/hub_test.tscn # 6-layer skyline composite, reference scene
│   ├── scripts/             # drift.gd, crowd_bob.gd, screenshot_and_quit.gd
│   └── assets/              # res:// mirrors of locked hub assets
├── screenshots/             # dev render outputs (gitignored)
└── _archive/                # obsolete docs, exhaust
```

When referencing files in conversation, use this layout. The structure is designed so most sessions touch 2–5 files, not the whole thing.

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
9. **Tier-state interpretation (drifted three times in one session):** Master's starting rating IS the tier ceiling. Pao at rating 5 → Teahouse T1–T5. Don't confuse "tier" with "realm" — prototype is R1–R3 by realm, T1–T5/T1–T7 by tier.
10. **Boss spawn rule.** Spawns when all 5 other objectives complete OR at 25-min mark, whichever first. NOT 30-min. NOT player-triggered.
11. **Search past convos before inventing.** If something feels designed but isn't in visible docs, search first. **Audits especially must search past chats for prior locks** — the 2026-05-21 audit missed the "What's next today?" session's player-baseline and boss-anchor work because it didn't sweep past chats; gap-closing tranche 1 (2026-05-22) found them via the standard search-first pass. Audit protocol now includes a past-chat sweep on every gap item before marking it "open."
12. **When math interpretation changes, flag prior calculations as needing redo.** Don't silently update conclusions while leaving stale numbers in earlier turns.
13. **Map completion requires boss defeat.** Boss is objective #6 of 6. You cannot advance past a map without defeating its boss. Adjacency unlocks via conquest, conquest requires all 6 objectives banked. The only "late-completed boss" scenario is exotic recruit gates (see risk-map.md).
14. **Compounding building functions = three tier surfaces.** For any compounding building (Recruitment, Storehouse, Library, Training, Outer Court, Pavilion), the three functions listed in sect-management.md must match the three tier surfaces (T1/T4/T8) in building-tier-curves.md. UI features that live at a building — Codex at Library, Sect Power widget at Main Hall, Mission Select wherever — are noted separately and don't count as functions. Drift here is what caused the Library three-surface confusion.
15. **Title-ladder consistency across chains.** Chain-entry specialists (rating 5, first to unlock a building) sit on the low title rung. Mid-chain titles climb. R12 chain capstones get the highest rung — the master-of-masters who taught everyone in the chain. Chain-entry names must leave headroom for that climb. Polished examples: *Smith Tian* (R3 entry, room for Forge-Lord / Anvil-Sage at R12), *Warden Bao* (R2 entry, room for Grand Marshal / Warlord at R12). Existing names at mid-rung at rating 5 (*Master Pao*, *Magistrate Hong*) have narrative cover but the constraint is real and must be respected when designing their R12 capstones.

16. **Hub holds 10 buildings, not 8.** Main Hall + Personal Sanctum are head-only buildings present from first launch — never unlock through the specialty chain. The "8 buildings unlock through R1–R3" framing in scope.md refers to the 8 specialty buildings only. When describing the hub UI / building grid / asset count / visual progression, count all 10. sect-management.md has the canonical 10-row building table; design-pass.md and asset-inventory.md count 10. Drift here is what caused the first-launch hub spec to assume an empty starting grid before it was corrected.

17. **Exploratory framings drift into locked status during long brainstorm sessions.** Three-function lists, tier-surface framings, and "what does this scale" propositions floated during exploratory work get carried into master docs without going through a deliberate lock check. The "reputation generation" Outer Court function, "inspiration drop rate" Pavilion function, "realm transition ceremonies" Pavilion function, "4 reputation thresholds" for special-event recruits, and **Recruitment Hall T8 "qi yield"** (cleaned tranche 2) were all this — brainstorm content from v4-era roster work that became "locked" without verification against the economy / schema / building-tier-curves model. Mitigation: anything in a "three functions" or "tier surfaces" list must correspond to a concrete tuneable knob that exists elsewhere in the model (economy.md / schema.md / building-tier-curves.md). If it doesn't, it's brainstorm content, not a decision. Audit-pass approach: cross-reference sect-management.md three-functions against building-tier-curves.md tier surfaces (drift pattern #14 enforces match) and against economy.md / schema.md (any "currency" or "generator" mentioned must have a sink and a definition).

18. **Don't propose workflows that conflict with locked architecture axes.** During the 2026-05-23 hub-art session, suggested a chained-canvas Ludo workflow (Edit Image to add each building onto the same canvas one at a time, replacing the locked image with each iteration). The user caught it: this conflicts with the locked Population overlay axis in sect-management.md, which requires per-building overlay anchor points and click hotspots that a baked composite cannot provide. Mitigation: before proposing any workflow involving art / data / system architecture, cross-reference against the canonical axes (sect-management.md Visual Growth, scope.md hub interaction model, design-pass.md surface specs). Same cross-reference move drift pattern #14 enforces — applied to workflow proposals, not just three-function lists.

19. **Design-doc voice contaminates tool prompts.** When asked to write a Ludo prompt during the 2026-05-23 session, the first draft was design-doc prose (subject + spec + composition + style + avoid list — what works in this file, but not in a tool prompt). Subsequent iterations kept regressing back into verbose form even after the prompt-craft lessons were locked. Mitigation: tool prompts are not design specs. For image gen, follow the locked Prompt-Craft Lessons in design-pass.md — 20 words or less for most cases, painter's mental sketch register (subject, view, era, medium), no quantity callouts, no inverse-described elements, no avoid lists. When writing for a generative tool, switch out of design-doc voice deliberately.

20. **Single-tone silhouette prompts can't carry color qualifiers on features.** During the 2026-05-23 hub-art session 2, drafted an elder silhouette prompt with "Pure black figure" AND "long grey beard." Direct contradiction — Ludo either picks one and ignores the other, or compromises into something neither wanted. User caught it. Mitigation: when a silhouette is locked to a single tone (pure black, pure white), drop all color qualifiers from feature descriptions. The silhouette IS the color descriptor. Beard length, beard volume, beard shape are valid descriptors; beard color is fixed by the silhouette rule.

21. **Environment Reference 1 dominates over figure subject in Generate New.** When generating silhouette figures with the TLA env Reference 1 anchor, five of six gens treated "robed cultivator" as a scene element to place into a landscape rather than as the subject of the frame. Only prompts with a strong concrete pose anchor ("hands clasped behind back") broke through. Mitigation: when generating figure assets, switch Reference 1 to the character lineup family — that's what the two-Reference-1 model anchors are for. Environment Reference 1 is for scenes; Character Reference 1 is for figures. Sticking with the env reference when generating figures because "we've been using it all session" is the failure mode.

22. **Generate New does not honor "transparent background" in the prompt.** Despite the Edit-Image-honors-transparency lesson locked 2026-05-23 session 1, Generate New returned opaque backgrounds in every attempt during session 2, regardless of prompt phrasing ("transparent background", "pure black figure on transparent background", etc.). Some gens returned a rendered checkerboard pattern that visually mimics transparency but is actually baked pixels — distinguishable by the pattern being slightly off-color or having a faint gradient. Mitigation: drop "transparent background" from Generate New prompts entirely. Use "Pure black figure" or "white background" instead, then follow up with Edit Image (see drift pattern #23 for the next step).

23. **Edit Image background removal also returns baked checkerboard, not true RGBA.** Confirmed 2026-05-23 session 3 on Main Hall. The Ludo Edit Image "Remove the background, keep only the figure" operation visually appears to produce a transparent PNG — the checkerboard pattern is visible — but the output file is RGB with the checkerboard baked as actual pixels. No alpha channel. Drift pattern #22 documented the Generate New failure; this session confirmed the failure mode extends to Edit Image as well. The session 2 lock "Edit Image honors transparency reliably" was wrong; it was visually plausible but not file-true. Mitigation: third pipeline step required — programmatic key-out of the baked checkerboard. The keying script lives at `tools/key_out_checkerboard.py`. Pattern is robust: Ludo's checkerboard uses desaturated grays in 200–255 brightness range; saturated building / character art (red columns, navy roofs, pure-black silhouettes) keys cleanly with gray-detection + brightness threshold + 1px alpha erosion for edge cleanup. The Generate-then-Edit pattern (session 2 lock) is now Generate-then-Edit-then-key, a three-step pipeline. See [Locked Decisions > Generate-then-Edit pattern](#locked-decisions--memorize-these) for the canonical pipeline.

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
- **Apprentice coefficient (compounding buildings):** 0.10. Formula: `compound rate = base × (1 + Σ(specialist ratings) × 0.10)`. Per-building tuning may diverge during playtest. **Exception: Storehouse draft charges (tranche 3)** are leaf-driven only and do NOT scale with apprentice ratings — apprentice compounding on Storehouse feeds the offline-cap surface (T1) instead. Compounding-template exception explicit in [building-tier-curves.md](docs/systems/building-tier-curves.md).
- **Day-1 pool:** 96 cards (12 themes × 8). Endgame ~444
- **Card max level:** 8
- **Meridian range:** 4–8. Refinement pacing: 5th end-R3, 6th end-R5, 7th end-R7, 8th end-R10
- **Meridian refinement materials:** any-theme at the realm's material tier; spirit stones gate 7th+
- **Building tier ceiling = Master's starting rating** (see drift pattern #9)
- **Heaven-Reader arc:** 4 members, ratings 7→8→9→10, Pavilion T1–T10
- **Cycle upgrades live at Pavilion T8** (flat-cap surface), NOT Library
- **6 universal objectives per map:** Survival / Kills / Targets / Territory / Resources / Boss
- **Uniform reward type per objective:** Survival=Essence, Kills=Raw qi, Targets=mixed materials, Territory=themed material cache, Resources=designated partner passive, Boss=signature + recruit + stones + (realm-finals)inspiration shard
- **Exotic recruit gates:** Visible up-front in mission select. If gate not met when boss defeated, "draw" outcome — boss runs away, objective doesn't bank, map incomplete, re-fight required after gate satisfied. Bosses who **first unlock** a building, or who are **realm-finals**, are never exotic-gated. R12 building-chain capstones may be exotic-gated *in addition to* the chain prerequisite.
- **Chain prerequisite (separate from exotic gates):** Nth specialist in any building chain requires recruiting all 1..N-1 prior. Natural recruitment gate, player adapts intuitively. Not a form of exotic gating.
- **Evolution model:** VS-style. Technique transforms into evolved form, occupying the same technique slot. Paired passive persists unchanged in its passive slot — its effect keeps running. Not "consumed or fused." This is the VS / Brotato / Halls of Torment convention.
- **Forge upgrade semantics:**
  - **Techniques (T1):** one Forge track per card-family, base→evolved chained. Base 1–10 (+10% each, max +100%) unlocks first. Once base is at +10, evolved 1–10 unlocks — inherits the base +100% as floor, climbs to +200% on the evolved form.
  - **Passives (T4):** one track per passive card. 1–10, +10% per level, max +100%. Independent tracks.
  - **Paths (T8):** one track per *discovered path tier* (Wood Sapling, Wood Sprout, etc. are each their own track). 1–10, +10% per level, max +100%. No inter-tier unlock gating. What +10% scales is a designer call per effect.
  - All three surfaces populate dynamically as content is discovered.
- **Scaling math pass — damage stack closed (2026-05-22).** Multiplicative composition: `base_atk × card_intrinsic_dmg × card_level_mult × forge_mult × teahouse_atk_stack × path_bundle × sect_power × crit`. Locks summarized below; details in respective system docs. Economy-side cost curves (cycle caps, leaf cost curves) remain open but not damage-stack.
- **Card level scaling (2026-05-22):** Even multiplicative, L8 = 2.0× per card (~+10.4%/level). Per-card content (which level adds pierce vs area vs damage) = per-card design pass. [run-loop.md](docs/pillars/run-loop.md) Card Damage Envelope.
- **Per-archetype L1 DPS (2026-05-22):** Strike 6 / Projectile 5 / Orbital 4 / Zone 3 single-target DPS at baseline (Atk=10). Multi-target effectiveness varies by archetype (Zone 3-4×, Orbital 1.5×, others 1.0×). [run-loop.md](docs/pillars/run-loop.md).
- **Teahouse 16-track inventory (2026-05-22):** 5 cap-10 / 6 cap-5 / 3 cap-3 / 2 cap-2. Within-stat additive, cross-stat multiplicative. Per-leaf base 0.5% / 1% / 2% / 4% scaled by `max(rating, 1)`. T4/T8 cap growth flagged for leaf-content design pass. [building-tier-curves.md](docs/systems/building-tier-curves.md) Teahouse Sixteen Tracks.
- **Path bundle envelope (2026-05-22):** Per-tier damage-equivalent contribution Sapling +20% → Sprout +40% → Grove +60% → Forest +100% → Worldroot +200%. Bundle = `1 + Σ(tier × forge_track)`. Wind Sapling exception routes to AS axis (additive with Teahouse AS). Per-effect content = 48-effect design pass. [path-system.md](docs/systems/path-system.md) Path Bundle Math Envelope.
- **Sect Power per-realm envelope (2026-05-22):** R1=25 (×1.50) / R2=75 (×1.87) / R3=200 (×2.41) / R6=1,500 (×4.87) / R12=10K (×11). Sub-linear sqrt formula extends past R12 for NG+. [economy.md](docs/systems/economy.md) Sect Power Multiplier.
- **Prototype TTK envelope (2026-05-22):** R1 M1 Yun ~30 sec fresh run at avg L5 (deliberate teaching pace, current archetype DPS — bump if playtest wants tighter VS feel). R3 M3 Tian ~22 sec with full R3 macro stack. **Soul Forge is unbuilt for the Tian fight** — Tian's defeat unlocks it. Player power growth R1 M1 → R3 M3 ≈ ×4.87 vs boss HP growth ×3.0 = earned-growth shape pulled forward (dopamine-explosion arrives earlier than R10-R12 envelope predicted).
- **NG+ architecture deferred (2026-05-22).** Three patterns compatible: Angels separate-multiplier (AdCap), Realm Grinder extended-SP, Cookie Clicker prestige-reset. R12 = ×11 stays meaningful regardless of pattern. Dedicated NG+ design session post-prototype.
- **Library three functions = three tier surfaces** (per drift pattern #14): (a) head's cultivation speed (T1), (b) region material drop rate (T4), (c) generic disciple qi rate sect-wide (T8). Codex is UI at Library, not a function.
- **Prototype scope** is *not* mechanics-only. R1–R3 mechanics + shippable opening flow (splash → title → character select → menu → map → run → hub loop) + per-surface art and audio assets. Surface and asset inventory tracked in `docs/prototype/design-pass.md`. Production state tracked in `docs/prototype/asset-inventory.md`.
- **Opening flow** = 9 surfaces + Dialog/Cutscene system. Splash / Title / Character Select / First-launch Hub / Hub Returning / Map-Level Select / In-Run HUD / Pause-Settings / Post-Run + Dialog/Cutscene cross-surface. Full specs in `docs/prototype/design-pass.md`.
- **Visual growth — two axes.** Tier drives base art (3 stages T1/T4/T8, prototype shows T1+T4 only). Specialist count drives dynamic Godot overlay layer (NPC silhouettes, lit windows, particles). Both independent and simultaneous. Locked in `docs/pillars/sect-management.md` Visual Growth section.
- **Art style — backdrop locked flat vector; architecture re-opened session 4.** Camera/perspective: front-facing 2D skyline (not 3/4 angled top-down). Backdrop landscape layers (mountains, mist) are flat vector with hard shape gradients, deep blue palette — LOCKED. Architecture register was locked flat vector in session 3 based on v1 Main Hall coming back flat, RETIRED in session 4 when user chose v3 painterly Main Hall (Studio Ghibli–register, includes baked bonsai tree + stone shrine). Current hub_test composites both styles. Style coexistence decision deferred until 2–3 more buildings exist for a fuller cross-style read. See [open-questions.md](docs/open-questions.md) and [asset-inventory.md > Style Locks](docs/prototype/asset-inventory.md).
- **Hub asset architecture (Locked 2026-05-23, redesigned 2026-05-23 session 2):** Front-facing skyline composition with separable parallax layers, composited at runtime in Godot. Layer stack: (1) sky — solid color or gradient in Godot, no Ludo asset; (2) mountains — Ludo-generated back layer, static or slow parallax; (3) clouds — Ludo-generated, horizontal drift; (4) mist — Godot-native hand-authored sprites, additive blend, slow drift; (5) buildings — 10 individual sprites with ground edges baked into base, foreground focus; (6) crowd FG — silhouette layer of disciples facing the sect, sparse bob/shuffle motion, scales with sect population. Mist and sky require no Ludo gens. Buildings sit on a horizontal platform line drawn across the canvas (above the foreground mountain peaks) — mountains read as true parallax background, platform is the building's floor, crowd FG occludes the platform from below. The original iso compound architecture (background plate + 10 iso building sprites) was abandoned 2026-05-23 session 2 after the perspective mismatch open question and Ludo style-consistency failures on iso compound work. Drift pattern #18 (Population overlay axis) still respected — buildings remain separable sprites with anchor points; population is now an aggregate FG crowd density rather than per-building NPCs. Detail in [design-pass.md > Hub asset architecture](docs/prototype/design-pass.md).
- **Backdrop layers locked (2026-05-23 session 2):** Mountains layer locked (flat vector, deep blues, hard shape gradients). Clouds layer locked (transparent PNG, white cloud forms with light blue underlining). Mist layer to be hand-authored in Godot. Sky is a Godot solid/gradient. The original `stone_floor.png` plate is INVALIDATED by the architecture pivot — no longer in the layer stack.
- **Main Hall — three locked versions across sessions 3 and 4.** Current canonical: `assets/buildings/main_hall.png` = **v3 painterly** (1327×613, true RGBA, locked 2026-05-23 session 4). Painterly Studio Ghibli–register, includes baked bonsai tree (left) and stone shrine (right). Replaces v1 navy roof (locked session 3, retired session 4 for blue-on-blue collision with mountains) and v2 warm olive (interim session 4, retired same session for the v3 painterly choice). Both prior versions preserved as `main_hall_v1_navy_roof.png` and `main_hall_v2_warm_olive.png`. Building base includes baked platform / stairs / balustrade per drift pattern #18. The session 3 lock that flat-vector was the building style register is RETIRED — see Art style entry above and the open style-coexistence question.
- **Crowd FG silhouette pool locked (2026-05-23 session 2):** 9 unique silhouettes, all waist-up, back-facing (facing the sect), hands clasped behind back, pure black on transparent background. Pool: upright topknot, bowed topknot, ceremonial hat, long-hair tied (low ponytail), long flowing hair female, high-bun female, broad heavyset, pointed hood, cowl hood. Crowd in Godot is composed by selecting from pool, scaling per population, distributing across the FG band, and applying sparse bob/shuffle tween (1-2 figures shifting weight every few seconds). Variety adequate for 10-12 simultaneous figure target. Pool expandable later if needed. Note: silhouettes are stored with baked checkerboard like other Ludo outputs — they need running through `tools/key_out_checkerboard.py` before Godot import.
- **Generate-then-Edit-then-key pipeline locked (2026-05-23 session 2, extended session 3 per drift #23):** For any Ludo asset requiring a transparent background, use a three-step pipeline:
  1. **Generate New** with subject on "white background" or "Pure black figure" (drop "transparent background" from prompt — Generate New doesn't honor it, drift #22).
  2. **Edit Image** with "Remove the background, keep only the figure" — returns visually-transparent but checkerboard-baked output (drift #23).
  3. **Programmatic key-out** via `tools/key_out_checkerboard.py` — strips the baked checkerboard, returns true RGBA, crops to bbox.

  Three-step adds ~10 sec per asset but produces Godot-ready transparent PNGs. Script is reproducible across all asset families (buildings, characters, cards, UI). The session 2 lock "Edit Image honors transparency reliably" is retired and replaced by this three-step.
- **Compositing previews don't happen in Claude.** Mechanical compositing (load PNGs, key, scale, paste) is faster in any image editor (Photoshop / Affinity / Krita / Figma) with direct visual feedback, and the canonical preview is the Godot scene itself once the project exists. Claude is genuinely useful for prompt iteration with Ludo and design reasoning, marginal for pixel-pushing previews. The session 3 composite preview (Main Hall + mountains) was a one-off to validate style cohesion before locking — subsequent compositing happens in Godot.
- **Two-Reference-1 model for Ludo (Locked 2026-05-23):** One Reference 1 anchor per macro family — Avatar TLA character lineup for Characters family, Avatar TLA environment screenshot (Air Temple establishing shot) for Environments + buildings family. Cards / UI / VFX may get their own Reference 1 anchors when reached. First-piece-in-family exception to the both-references rule: first piece uses Reference 1 only; once locked, becomes Reference 2 for everything downstream in that family. **Buildings family Reference 2 now locked = Main Hall (session 3).**
- **Ludo Pipeline (Verified 2026-05-23):** 6 generation modes (Generate New / Edit Image / Generate from References / Generate with Style / Edit with Mask / Erase with Mask), 9 image types (Background / Asset / Sprite / Sprite VFX / Icon / UI Asset / Texture / Art / Gameplay), 2-image batches per call. Filter dropdowns (esp. Perspective) don't reliably apply — bake critical filter values as literal prompt prefixes. Asset type enforces default isometric perspective regardless of Reference 1 angle or prompt. Full mechanics + Prompt-Craft Lessons in [design-pass.md > Asset Pipeline](docs/prototype/design-pass.md).
- **Music architecture.** 9 Suno tracks for prototype (3 realm-ambient + 3 boss + 3 realm-final) + user's own title track + R12 apex callback (deferred). Instrumental, anime-cinematic, no vocals except possibly the R12 apex callback. R1 M2 counts as realm-final for music despite shallow R1 difficulty curve.
- **"They Escaped" (renamed from "Draw")** — exotic-gate-not-met outcome. Boss objective shows defeated check, then animates to un-checked with gate-not-met message. Other banked objectives still bank. Amber/neutral banner color. No R1–R3 prototype boss triggers this in normal play; system architected for R4+.
- **Dialog/cutscene system in prototype.** 19 beats: 8 first-time boss intros (in-run at boss spawn) + 8 first-time recruits (post-run) + 3 stage breakthroughs (in-hub). Technique evolution does NOT use dialog (would break VS pacing) — transient banner only. Tone: xianxia cheese is correct.
- **Character creator = preset carousel for prototype.** 8 presets (locked MC + 7 V1–V5 concepts), MC default. Real parts-swap creator deferred post-prototype.
- **Cross-surface controller focus state** is a global UX requirement — every interactive element (hub buildings, modals, carousel, mission select, draft cards, map regions) gets a focus/selected state for controller, mobile, and accessibility play. Warm gold glow + pulse, layered on top of any game-state visual.
- **Engine:** Godot 4 (4.6.3 stable), GDScript
- **Godot project exists at `game/`** as of 2026-05-23 session 4 (Claude Code kickoff). `project.godot` configured for 1920×1080 viewport, GL Compatibility renderer, linear texture filter. Standard directory structure per [tech-stack.md](docs/tech-stack.md). Godot binary lives at `C:\Users\tobes\Desktop\Godot.exe` on the dev machine (not on PATH; reference by full path in commands).
- **hub_test scene** (`game/scenes/hub_test.tscn`) validates the 6-layer skyline composite at 1920×1080 and serves as the reference scene for hub-architecture decisions. Working: gradient sky / mountains / mist (programmatic radial gradient, normal blend, drift via `drift.gd` at 4/6/9 px/sec) / grey ground / black horizon platform / Main Hall v3 / 18-figure crowd FG with bob/shuffle tween (`crowd_bob.gd`, asymmetric 1.2s/1.0s SINE, one-at-a-time on 1.5–5s interval). Clouds keyed but dropped pending better individual-cloud asset variety.
- **Cook-before-code rule** — project-specific working-style rule established 2026-05-23 session 4. Propose plan and wait for explicit approval before any Edit/Write/Bash that mutates state. Pure investigation (Read/Grep/Glob) is fine without preapproval. Re-render of an already-built scene is fine. Saved as memory at `~/.claude/projects/C--dev-cultivation-game/memory/feedback_cook_before_code.md`.
- **Python toolchain** — Python 3.12.10 at `C:\Users\tobes\AppData\Local\Programs\Python\Python312\python.exe` (winget install, not on PATH for the bash subprocess; reference by full path). `Pillow`, `numpy`, `scipy` installed. Used by `tools/key_out_checkerboard.py` (drift #23) and `tools/extract_cloud_pieces.py` (new s4).

### Player Baselines (Locked 2026-05-22)

R1 M1, minute 0, fresh run. Full table in [run-loop.md](docs/pillars/run-loop.md).

- Atk 10, HP 100
- Move speed 100 units/sec (1.0× baseline)
- Pickup radius 50, paint radius 30, hitbox radius 16
- Defense 0 (Teahouse-only), regen 0 (Vitality L4+ only)
- iframes 0.5 sec after taking damage
- Crit chance 0%, crit damage 1.5× (Offense L4+ / Metal Sapling add)
- Attack speed: no global stat, per-technique cooldowns only. Wind Sapling = global atk speed buff
- Qi pool cap (Stage 1) = 1,000; qi accumulation 5/sec passive
- Starter loadout: 1 player-chosen tech at L1, 3 empty tech + 4 empty passive slots

### XP and Leveling (Locked 2026-05-22)

- Gem values: Fodder 1, Elite 5, Mini-boss 20, Boss 100
- Gem persistence: 30 sec on ground
- Curve placeholder: `XP_to_next(n) = floor(5 × 1.12^(n-1))`
- No hard level cap. Levels past all-slots-L8 grant +1 Atk each (flex bonus)
- **XP gem and raw qi collapse into single pickup orb** (tranche 2). One orb per kill, walking over grants both.

### Boss Anchor + Enemy Baselines (Locked 2026-05-22)

R1 M1 minute 0, absolute values. Full table in [scope.md](docs/prototype/scope.md).

- **Lady Yun = 800 HP, 8 contact dmg.** Boss-relative anchor; all 8 prototype bosses back-solve from this.
- Fodder 8 HP / 3 dmg; Elite 100 HP / 6 dmg; Mini-boss 400 HP / 10 dmg
- Damage relatives vs Yun's 8: Fodder 0.4×, Elite 0.8×, Mini-boss 1.2×, Boss 1.0×
- **Within-run HP scaling (`HP(t) = base × 1.10^minute`) applies to fodder/elite/mini-boss only.** Boss HP is absolute at encounter — does NOT scale with spawn minute. Skill signal: speedrunner who pops boss at min 10 fights same Yun as slow player at min 25, but with less card growth.

### Qi Pool Cap Home (Locked 2026-05-22)

Cap is inherent to current cultivation stage. NOT a tunable building surface. Within a stage, cap stays fixed — fill three times via cycling cadence to be stage-ready. Cap rises at stage breakthroughs only.

- Curve: `cap(stage) = 1,000 × 2^(stage-1)`. Stage 1 = 1,000. Stage 12 = ~2M.
- Doubling matches AdCap idle output growth (~2.4× per realm per risk-map.md), preserving the "fill three times" cadence at every era.
- Confirmed by prior user statement (2026-05-11): *"If you hit your cap you cycle. If you cycle three times you progress. Why would you want the cap bigger?"*

### Currency Ambient Drops (Locked 2026-05-22)

Per-kill ambient drops during runs, R1 M1 minute 0 baseline. Full table in [economy.md](docs/systems/economy.md).

- **Fodder:** XP gem 1, raw qi 1, 0.1% chance × 1 spirit stone. No essence, no materials.
- **Elite:** XP gem 5, raw qi 5, 3 essence, 1 region-themed material. No stones.
- **Mini-boss:** XP gem 20, raw qi 20, 15 essence, 1 spirit stone, 3 region-themed materials.
- **Boss (replay generic):** XP gem 100, raw qi 100, 50 essence, 3 stones, 5 region-themed materials. No inspiration (first-time only).
- **Boss (first-time named):** Ambient stacks on top of rewards.md first-time bundle.
- **Essence is VS-gold-style** — no fodder drop. Genre-correct.
- **Materials are 100% region-themed for ambient.** Off-theme variety stays exclusive to Targets first-time.
- **Per-realm ambient scaling:** R1=1×, R2=1.5×, R3=2×, R4+=2.4×/realm. Applies to all four resource streams 1:1.
- **Within-run ambient scaling:** none. Drop values fixed per kill regardless of minute. Locked pending playtest confirmation.
- **Cycling multiplier:** additive across learned cycles. `qi_gain_rate = base × (1 + Σ cycle_climb_%)`. Cap percentages per cycle still open.

### Per-Building Idle Base Rates (Locked 2026-05-22)

T1/T4/T8 unlock values for all 8 buildings with no leaves purchased. Full table in [building-tier-curves.md](docs/systems/building-tier-curves.md).

- **Library:** T1 +10% head qi accum / T4 +10% region material drop / T8 each generic disciple +0.5 qi/hr to sect pool
- **Recruitment Hall:** T1 1 recruit per 4hrs / T4 1 recruit per tick / T8 −10% recruitment cost (leaves to −40%). **"Qi yield" dropped from T8** — drift pattern #17 cleanup.
- **Storehouse:** T1 offline cap 12h→24h / T4 3 reroll + 3 skip + 3 banish charges per run (climbs to 13/13/13) / T8 chest size 5 cards (to 7 at L10)
- **Teahouse:** 0% base; 16 tracks activate via paid leaves. **Track upgrades INSTANT. Specialist assignment INSTANT. Buffs are persistent passive modifiers — no brew time, no expiration.**
- **Soul Forge:** 0% base; tracks activate via paid leaves
- **Training Hall:** T1 +5% disciple training speed / T4 named-disciple training unlocked / T8 generics start +1 stage above sect average
- **Outer Court:** T1 −5% building costs / T4 +5% disciple effectiveness / T8 pop cap +5 slots
- **Ascension Pavilion:** T1 +5% head qi accum (stacks with Library) / T4 +10% tier breakthrough speed / T8 cycle climb tracks unlock

### Idle Composition Rule (Locked 2026-05-22)

```
inbox_per_hour_R = ((region_R_base × Π(amplifier_multipliers)) + Σ(generator_outputs_R)) × (1 + sqrt(SP/100))
```

- **Amplifier buildings** multiply region idle streams: Library T1/T4/T8, Outer Court T4, Pavilion T1.
- **Generator buildings** add new streams: Recruitment Hall T1, Library T8.
- **Run-only surfaces** apply during runs only: Storehouse T4, Teahouse, Pavilion T4, Soul Forge.
- **Cap-extenders** modify caps: Storehouse T1, Outer Court T8.
- **Cost-reducers** modify upgrade costs: Outer Court T1, Recruitment Hall T8.

### Storehouse Offline Idle Cap Progression (Locked 2026-05-22)

| State | Offline cap |
|---|---|
| Not built | 12h |
| T1 unlock | 24h |
| T1 maxed | 48h |
| T4 unlock | 72h |
| T4 maxed | 5d |
| T8 unlock | 7d |
| T8 maxed | 14d |

### Pavilion T8 Cycle Climb Economy (Locked 2026-05-22)

10 leaf levels per cycle. Cycle 1 cost curve: 1K / 2.5K / 5K / 10K / 20K / 40K / 80K / 160K / 320K / 640K essence. Total Cycle 1 max climb ≈ 1.3M essence. Per-cycle escalation: Cycle N L1 = Cycle 1 L1 × 1.5^(N−1). Total endgame cycle climb sink ≈ 40M essence. Specific values flagged for scaling math pass; formula structure locked.

### Card Draft Mechanics (Locked 2026-05-22)

Tranche 3 close. Full mechanics in [run-loop.md Level-Up Draft section](docs/pillars/run-loop.md). Schema in [schema.md](docs/data/schema.md) (CardDraft + Storehouse_DraftChargeState + LeafTrack entities).

- **Charge source:** Storehouse T4. Three independent tracks (reroll / skip / banish), 10 leaves each. T4 unlock = 3/3/3 charges per run. Each leaf = +1 charge to that track. T4 maxed = 13/13/13.
- **Apprentices do NOT scale charges.** Apprentice compounding on Storehouse feeds offline cap only. Charges are leaf-driven discrete values. Exception explicit in building-tier-curves.md compounding template.
- **Reroll = re-spin entire offer.** 1 charge = new full draft. Pick-1-reroll explicitly cut.
- **Banish = this-run scope only.** Card removed from this run's draft pool. Returns on next run. Global banish considered and rejected.
- **Skip = small essence cache.** 10 essence for level-up draft, `5 × chest_size` essence for chests. Charge cap prevents skip-everything farming.
- **L8 cards filtered from draft offers.** Once a card maxes, it stops appearing in drafts. Once entire 16-slot loadout is at L8, level-ups silently grant +1 Atk each.
- **Tech-vs-passive weighting:** `weight_tech = (empty_tech + 1) / (empty_tech + empty_passive + 2)`. Floor of 1 prevents zero-weight starvation. Early game skews toward empty slots; late game settles to 50/50.
- **Card behavior on pick = VS convention.** Card not in loadout enters slot at L1. Card already at LN goes to L(N+1). Same UX regardless of new vs existing.
- **Evolution + path culmination can coexist in same chest.** Path takes 1 slot, evolution takes 1 slot, remaining slots fill random. The "one evo slot per draft" rule still holds — path is a different conditional category.
- **Path culmination occupies 1 chest slot.** Not a bonus +1. Same visual treatment as evolution, distinct "PATH" frame tag.
- **Run-start screen UI:** requirements locked, layout deferred. Theme tabs (primary) + archetype sub-filter + favorites pin + search + card preview pane. Browse-to-pick target <30 sec at endgame. Full requirements in [rewards.md](docs/prototype/rewards.md).

### Wave System (Locked 2026-05-22)

Tranche 4 close. Full spec in [run-loop.md Wave Composition section](docs/pillars/run-loop.md). Per-realm rosters and per-map slot-fire table in [scope.md](docs/prototype/scope.md).

- **Wave-based spawning, one wave per in-game minute, authored per map.** VS / HoT convention. Each wave specs `min_alive`, `spawn_interval`, active enemy types, and any slot enemy (elite / mini-boss) that arrives that minute.
- **Global alive cap: 300.** Engine ceiling and frame-rate driver. New spawns suppressed at the cap.
- **Default wave template locked** — 26 minutes (0–25), non-monotonic, peaks at 300/0.1s late game. Grounded in VS Mad Forest wave data. Same template used by all 8 prototype maps; per-map authoring overrides which slots fire and which enemies fill the active-types list.
- **Per-realm density modifier:** R1 ×1.0 / R2 ×1.5 / R3 ×2.0 applied to `min_alive` (capped at 300). Same factors as the locked HP/dmg per-realm scaling.
- **8 elite slots + 4 mini-boss slots in the template.** Per-map slot-fire counts ramp R1 M1 (4 elites, 1 mini-boss) → R3 M3 (8 elites, 4 mini-bosses). Slot enemies drop chests on death.
- **Boss-fight spawn behavior: ALL slots fire during boss fight.** Fodder waves continue, scheduled elite/mini-boss slots fire as scheduled. Boss is a target inside the ongoing wave, not a 1v1 isolation. Layered tension is the design intent.
- **Aggro: pure pursuit + off-screen despawn (>1000u, both conditions).** Bosses arena-locked, do not despawn. Per-enemy behavior quirks (ranged, charge, pack, summon) explicitly deferred to a later behavior pass.

### Realm Roster Structure (Locked 2026-05-22)

Tranche 4 close. Full spec in [scope.md Realm Enemy Rosters](docs/prototype/scope.md).

- **Rosters authored per realm, not per map.** Genre convention (VS ships ~138 normal + 58 boss enemies across 54 stages with heavy cross-stage reuse). Maps within a realm share a roster with light biome-specific swaps.
- **Bosses stay 1-per-map** (119 across full game, 8 in prototype). Fodder, elites, and mini-bosses are realm-pool.
- **R1 roster:** 5 fodder + 3 elites + 2 mini-bosses (covers M1 + M2).
- **R2 roster:** 7 fodder + 4 elites + 3 mini-bosses (covers M1 + M2 + M3).
- **R3 roster:** 8+1 fodder + 4 elites + 3 mini-bosses (covers M1 + M2 + M3).
- **Prototype total:** 48 unique enemy designs across 8 maps + 8 bosses.
- **Universal climbing-fodder convention:** humanoid / ghost / beast trio reskins per realm. R1 = Footpath Bandit / Stray Spirit / Wandering Mongrel; R2 = Hill Bandit / Frontier Shade / Plains Stalker; R3 = Rogue Apprentice / Wandering Shade / Beast-Spirit. Pattern continues R4–R12.
- **R12 void-aspected elite reuse** (deferred idea, 2026-05-22): R12 could field elite mobs from R1–R11 as void-aspected variants (purple-glow shader treatment) — saves massive asset production at top tier, threads "Void corrupts everything before" cosmology. Filed in [open-questions.md](docs/open-questions.md) Deferred section.

### Per-Enemy Variance (Locked 2026-05-22)

- **XP per enemy: flat per category** for prototype. Fodder 1 / Elite 5 / Mini-boss 20 / Boss 100. Per-enemy-type variance desired long-term, deferred.
- **Damage per enemy: flat per category** for prototype. Fodder 3 / Elite 6 / Mini-boss 10 / Boss 8 (R1 M1 baseline). Per-enemy-type variance desired long-term, deferred.

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
- **Bundle all touched files in a zip mirroring the repo structure**, so the user can unzip at the repo root and overwrite cleanly. The zip should NOT contain a top-level project folder — its contents should be relative to the repo root (e.g. `CLAUDE.md`, `STATE.md`, `docs/pillars/cultivation.md`). One zip per wrap.
- `STATE.md` updated LAST, reflecting what was touched and what's next
- **No standalone session-handoff docs.** Wrap updates the persistent docs. The handoff IS the diff in git.

---

## When Coding Phase Begins (Godot)

**Pre-code sequencing (in order before Claude Code session 1):**

1. **Design pass** — ✅ COMPLETE 2026-05-21. See `docs/prototype/design-pass.md` (filled inventory) + `docs/prototype/asset-inventory.md` (production tracker).
2. **Audit pass** — ✅ COMPLETE 2026-05-21. Findings in `docs/open-questions.md` under High-Priority. Five gap categories surfaced: player baselines, fodder/elite specs, card draft Storehouse-charge values, currency ambient drops, per-building idle base rates.
3. **Gap-closing session(s)** — close holes the audit found.
   - **Tranche 1 — ✅ COMPLETE 2026-05-22.** Player baselines, boss baseline anchor, qi pool cap home all locked. Past-chat sweep surfaced prior work from "What's next today?" (2026-05-21) that the audit had missed; values reconciled and locked into docs.
   - **Tranche 2 — ✅ COMPLETE 2026-05-22.** Currency ambient drops + per-building idle base rates + composition rule + Storehouse offline cap + Pavilion T8 cycle climb economy + Teahouse brew lock + Recruitment Hall T8 "qi yield" cleanup all done in one session. Schema housekeeping from tranche 1 + open-questions.md restructure also rolled in.
   - **Tranche 3 — ✅ COMPLETE 2026-05-22 (locks + housekeeping).** Card draft Storehouse-charge values (3/3/3 → 13/13/13) + reroll-all + per-run banish + skip-essence rewards + L8-filter + tech/passive weighting + VS-convention card behavior + evo/path coexistence + path slot occupancy + run-start UI requirements all locked. Same-session housekeeping fold-in resolved building-tier-curves.md (Storehouse T4 charge tracks subsection), schema.md (CardDraft + Storehouse_DraftChargeState + LeafTrack entities, 5 new invariants, 3 CUT additions), open-questions.md (tranche 3 moved to Resolved).
   - **Tranche 4 — ✅ COMPLETE 2026-05-22 (locks).** Wave system locked (one wave per minute, 300 alive cap, default wave template grounded in VS Mad Forest data, per-realm density ×1/×1.5/×2 on min_alive capped at 300). Elite/mini-boss slot system locked (8+4 slots, per-map fire counts). Aggro/pursuit locked (pure pursuit + off-screen despawn). Boss-fight spawn behavior locked (all slots fire during boss). Realm rosters locked R1+R2+R3 (48 enemy designs total). Per-enemy XP and damage variance locked flat-per-category for prototype. R12 void-aspected elite reuse idea filed. HP-scaling genre-divergence flagged for post-playtest revisit. **Schema.md housekeeping deferred to next session opening** — Wave / EnemyRoster / EnemySlotConfig entities + invariants + CUT additions needed; schema.md was not in context this session.
4. **Scaling math pass damage-stack — ✅ COMPLETE 2026-05-22.** Card level scaling, per-archetype L1 DPS, Teahouse 16-track inventory, path bundle envelope, SP per-realm envelope, prototype TTK envelope, NG+ architecture flag all locked. R1 M1 and R3 M3 checkpoints walked. Damage stack closed for prototype build purposes. **Economy-side cost curves still open** (per-cycle climb cap %s, Cycle 1 L1 cost confirmation, per-cycle ×1.5 escalation factor, Storehouse T4 reroll/skip/banish per-leaf costs, Pavilion T8 per-cycle L1 cost confirmation, per-map wave content overrides, tech/passive weighting floor specifics, skip-essence amounts) — these are economy-flow work, not damage-stack, and not gating prototype build.
5. **Prototype production focus — ✅ MAIN HALL LOCKED, GODOT IMPORT NEXT.** Session 1 (2026-05-23) closed the Ludo workflow discovery: 6 modes / 9 image types / 2-image batches / Two-Reference-1 model / first-piece-in-family exception / 13 prompt-craft lessons. Original iso compound architecture locked, first plate locked v1, Main Hall multiple attempts. **Session 2 (2026-05-23) pivoted the hub architecture** from iso compound to front-facing skyline after the perspective mismatch open question and continued Ludo style-consistency failures on iso architecture work. Pivot rationale: Ludo holds painted style reliably on architecture pieces but drifts to flat vector on landscape-only work; iso compound puts both burdens on every gen. Front-facing skyline separates them cleanly via parallax layers. Session 2 locks: art style updated (front-facing 2D, painted architecture + flat-vector backdrops, both accepted as tool-reality split — note: superseded session 3), hub asset architecture redesigned (6 layers: sky / mountains / clouds / mist / buildings / crowd FG), backdrop layers locked (mountains + clouds Ludo-generated, mist + sky Godot-native), crowd FG silhouette pool locked (9 figures), Generate-then-Edit pattern locked (Generate New + Edit Image two-step for transparent backgrounds — note: superseded session 3 by drift #23, now three-step), 4 new prompt-craft lessons. **Session 3 (2026-05-23)** locked first building: Main Hall generation came back flat vector, harmonizes with locked flat-vector backdrop (style register open question resolved — flat vector all the way), composite preview validated layer cohesion. Drift pattern #23 discovered (Edit Image background removal also bakes checkerboard); three-step pipeline locked with `tools/key_out_checkerboard.py` as canonical step 3. Main Hall locked as Reference 2 anchor for the buildings family. Compositing-in-Claude retired as inefficient — Godot scene is the canonical preview going forward.
6. **Claude Code kick-off — ✅ COMPLETE 2026-05-23 session 4.** Godot 4.6.3 project created at `game/`. hub_test.tscn assembles the 6-layer skyline at 1920×1080. Mountains + Main Hall + grey ground + black horizon line + mist (programmatic, animated) + 18-figure crowd FG (keyed + animated bob/shuffle) all working in motion. Main Hall iterated three locks within the session (v1 navy retired → v2 warm olive interim → v3 painterly final). Cloud layer keyed but dropped from current scene pending better individual-cloud variety; extraction tool ready at `tools/extract_cloud_pieces.py`. Python 3.12 toolchain installed. Cook-before-code rule established mid-session. Full session-4 summary in [open-questions.md > Resolved 2026-05-23 Session 4](docs/open-questions.md).

**Engine + workflow:**
- Engine: Godot 4 with GDScript (C# only if perf demands it later)
- Code lives in `game/` subdirectory of the repo
- Run from terminal: `cd cultivation-game/` then `claude` to invoke Claude Code with context
- First milestone: R1–R3 prototype with all 8 buildings unlockable + shippable opening flow; full scope in `docs/prototype/scope.md` and `docs/prototype/design-pass.md`

---

## What's Open — Brief Reference

Authoritative list lives in `docs/open-questions.md`. Currently:

- **Scaling math pass damage-stack — ✅ CLOSED 2026-05-22.** All damage-stack components locked (see Locked Decisions). Cross-refs: [run-loop.md](docs/pillars/run-loop.md), [building-tier-curves.md](docs/systems/building-tier-curves.md), [path-system.md](docs/systems/path-system.md), [economy.md](docs/systems/economy.md).

- **Economy-side cost curves — OPEN, deferred to dedicated economy session.** Not damage-stack, not gating prototype build. Items: per-cycle climb cap %s (8 cycles, currently placeholder 10/20/35/50/75/110/160/250%), Cycle 1 L1 cost confirmation (1K placeholder), per-cycle ×1.5 escalation factor confirmation, Storehouse T4 reroll/skip/banish per-leaf cost curves, Pavilion T8 per-cycle L1 cost confirmation, tech/passive weighting +1/+2 floor playtest specifics, skip-essence amounts (10 / 5×chest_size playtest confirmation), per-map wave content overrides.

- **NG+ architecture (2026-05-22) — DEFERRED.** Three patterns compatible (Angels separate-multiplier / Realm Grinder extended-SP / Cookie Clicker prestige-reset). Dedicated session post-prototype; doesn't gate current work.

- **Per-card content design pass** — what each card level grants (more damage / pierce / area / projectile count / etc.). Per-card variance around archetype DPS envelope. Per-effect "damage-equivalent translation" for non-damage path effects. Wind Sapling AS-axis confirmation. Deferred.

- **Within-run HP scaling genre divergence (tranche 4)** — `HP(t) = base × 1.10^minute` locked tranche 1 is divergent from VS Normal mode (which derives in-run difficulty entirely from wave content). User noted "we have a different game shape, but in this slice it's very adjacent — might need to revisit." Flagged for **post-playtest revisit**. First lever to pull if the multiplicative stack overshoots.

- **Boss-HP-doesn't-scale-within-run** — locked unilaterally tranche 1, flag for user confirmation.

- **Within-run ambient scaling = none** — locked pending playtest confirmation. Tranche 2.

- **R12 chain capstone "evolution" effect** per chain (8 building + 12 theme).

- **R12 void-aspected elite reuse idea** — filed tranche 4. Saves R12 asset production by reusing R1–R11 elites with purple-glow shader. Decision deferred to R12 design.

- **Full title-ladder pass** across all 20 chains.

- **Evolution-eligibility rules per card** — affects evolved card art count and Forge track structure.

- **R12 apex callback track** (vocal language, instrumentation).

- **Hub building layout — ✅ RESOLVED 2026-05-23.** Per the locked hub asset architecture, layout emerges per-building when each sprite is dropped into the Godot scene. No pre-planned layout needed.

- **Building isometric vs plate perspective — ✅ RESOLVED 2026-05-23 session 2 by architecture pivot.** Front-facing skyline composition supersedes the iso compound architecture. Perspective mismatch question no longer applies — buildings and backdrop are now separate parallax layers at the same camera orientation.

- **Building visual style register — ⚠️ RE-OPENED 2026-05-23 session 4.** Session 3 resolved as flat vector based on v1 navy Main Hall. Session 4 user replaced with v3 painterly (Studio Ghibli–register) — flat-vector-architecture lock retired. Painterly building now sits on flat-vector backdrop in hub_test. Three paths open: (a) regen backdrop in painterly to match, (b) regen buildings in flat vector to match, (c) accept cross-style as intentional. Deferred until 2–3 more buildings exist for fuller cross-style read.

- **Head-only building tier states (PRE-EXISTING DISCREPANCY surfaced 2026-05-23) — OPEN.** Original framing: design-pass.md Surface 5 specs "10 buildings × 2 visual stages = 20" but Art Inventory lists Main Hall + Personal Sanctum as "single state each" (= 18 total). Skyline architecture pivot doesn't resolve this — Main Hall and Personal Sanctum still need to be defined as either tier-progressing (3 stages each = +2 per building) or static (single state each). Decision pending. Lower priority than active production work.

- Per-boss exotic gate distribution.

- 48 path effects (each also needs +10% Forge scaling target).

- Pairing convention universality.

- Spirit stone exchange rate / specific sinks beyond locked ones.

- Trigger values for special-event recruits (constraint locked: not reputation, not building-tier-tunable, never RNG).

---

*This file is itself subject to the universal rules. If it grows past ~2k tokens, split it. Prune stale sections. Treat as working document.*
