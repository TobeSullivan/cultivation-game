# Vision

A premium idle-survivor cultivation game. Vampire Survivors as the core active loop, with Adventure Capitalist (idle), Risk (territorial conquest), and sect management layered on top. No compromise on depth in any of the four pillars; everything funnels through the VS run loop because that's the only thing the player actually plays.

---

## High-Level Vision

- **Genre:** idle-survivor / cultivation power fantasy
- **Inspiration:** Vampire Survivors + Adventure Capitalist + Risk + sect-management games. Saplings borrow from VS, Brotato, Halls of Torment, ARPGs.
- **Cultivation flavor:** Cradle (Will Wight) for progression-ladder shape; Infinite Realm (Ivan Kal) for cultivation-specific mechanics (qi, cycling, tiers, paths). Generic xianxia/wuxia naming throughout — no IP infringement.
- **Tone:** never hard. Power fantasy. Defeat (not death) is part of the cycle. Players are never punished, always accommodated.
- **Scope:** hundreds of hours of content. Achievement-web depth.
- **Pricing:** premium. $5–$10. Pay once, get everything. No microtransactions, no ads, no F2P dark patterns.
- **Platforms:** PC first, with Steam Deck and consoles as first-class citizens (not afterthoughts). Mobile considered later as a thoughtful port, not the source.
- **Story:** minor but present. Frame and flavor. Designed after core systems are locked.
- **Endgame:** infinite/leaderboard mode is on the roadmap, TBD.
- **Player character:** one. The sect head. Singular protagonist throughout the entire game.

---

## Core Design Principles

1. **VS run is the only verb.** Every other system feeds into or out of the run loop.
2. **Every run unlocks something new.** Achievement-web philosophy — kills, survival, drops, milestones all feed the unlock web.
3. **Defeat is part of the cycle.** No game-over screens. Failed runs still bank progress.
4. **Player agency over grind.** If a player replays a region, it's their choice; the game doesn't second-guess them.
5. **Conquered territory is permanent.** The game never pulls players back to maintain what they've earned.
6. **Selection-based UI, not hover.** Steam Deck and console first. Persistent detail panels.
7. **Pause-friendly everywhere.** The game waits for the player.
8. **Premium respect.** No engagement traps, no FOMO timers, no daily login anxiety.
9. **Maintainability.** The game must never feel overwhelming. Progressive disclosure throughout. Notifications are rare and obvious, never spammy. No notification badges. No upkeep, no decay. New systems unlock when the player is ready.
10. **One decision at a time.** When the player engages manually with a system, the screen presents one thing to think about, not a wall of sliders.
11. **All unlocks visible, surfacing weighted to scope.** Every unlock the player earns is visible somewhere. *How* it's surfaced depends on how much it opens up — see [systems/unlock-web.md](systems/unlock-web.md).
12. **Front-loaded systems, deepening content.** Every major game system comes online during R1–R3 (the Mortal era). R4–R12 is content depth within revealed infrastructure, not new mechanical surface area.
13. **Builds, not cards, do the work.** Individual cards are tools. The expressive depth lives in evolutions and path culminations, not in card-level differentiation. No rarity tiers, no chase cards, no "this Common version is worse than the Rare version" framing.

---

## Version Notes (v6)

v6 consolidates v3/v4/v5/v5.1 into a single source of truth. Specific v6 locks added on top of v5:

1. **Body parts as variant axis.** Cards have a body-part variant tag (Head/Arms/Legs/Body + advanced). Pairing convention extends — pairs share body part. Day-1 pool architecture: 8 cards per theme = 4 archetype-paired cards × 4 core body-part variants, with each theme weighted toward 2 variants out of the 4.
2. **Building tier mechanic clarified.** Master's starting rating IS the tier ceiling for that building. Recruiting a higher-rated specialist extends the ceiling. Tier count per building = max rating achievable in that specialty's arc (typically T1–T10; Heaven-Reader short-arc = T1–T7 to T1–T10 depending on arc length). Specialist count drives visual building growth independent of tier.
3. **Unified materials economy.** Single tier-graded pool, optionally theme-tagged. 12 themes × 6 material tiers = 72 materials total. Realm pairs share material tier (R1-R2=T1, R3-R4=T2, …, R11-R12=T6). No separate building vs card material pools.
4. **Righteous Path = 13th path.** Capstone path combining all 12. Recipe: 8 specific evolution pairs sourced from R4-R11 realm-final signatures + their evo-partner passives. Discoverable only in infinite/endgame mode after R12 conquered. R12 realm-final = the capstone fight; final boss tier resolved.
5. **Currency model (4 + materials).** Qi (personal cultivation pool, tier breakthroughs), Essence (universal upgrade currency), Spirit Stones (higher-tier currency — gold→platinum, not premium MTX — for high-impact sinks), Inspiration (Stage 4+ gating). Plus Materials. Monster Cores cut.
6. **Building Tier Curves locked.** Two templates: Compounding (3 surfaces unlock at T1/T4/T8) and Flat-cap-by-tier. See [systems/building-tier-curves.md](systems/building-tier-curves.md).
7. **Boss combat profile schema** added: HP scaling, contact dmg, ability dmg, armor%, speed vs player, phase structure, attack set, telegraph generosity, arena interaction.
8. **Map adjacency pattern.** R1 linear (2 maps), R2/R3 gateway + branch + final (3 maps each).
9. **Enemy categories.** Fodder (HP 0.05, dmg 0.4, speed 0.5-0.9× player), Elite (HP 0.5, dmg 0.8, every ~90s), Mini-boss (HP 1.2, dmg 1.0, past 10min). Per-realm: R2=1.5×, R3=2×.
10. **Partner passive distribution locked** for 8 prototype maps (forward-shift derangement — see [prototype/rewards.md](prototype/rewards.md)).
11. **Per-map reward quantities locked** for 8 prototype maps (formulas + per-map values — see [prototype/rewards.md](prototype/rewards.md)).
12. **Uniform reward type per objective.** Survival=Essence, Kills=Raw qi, Targets=mixed materials bundle, Territory=themed material cache, Resources=designated partner passive, Boss=signature + recruit + spirit stones + (realm-finals only) inspiration shard.
13. **Sect Power multiplier formula** locked at sub-linear sqrt: `multiplier = 1 + sqrt(Sect_Power / 100)`. Matches AdCap/Cookie Clicker/NGU Idle case study patterns; tames late-game runaway.

---

## Story / Framing

Minor but present. Lives in era transitions, boss dialogues, codex drops, milestone narrative beats, building-runner flavor text. Designed after core systems are locked. One protagonist: the sect head.

## Art Direction

- Indie-scope. Heavy reliance on AI-generated art or friend artist
- 5 era visual identities to control budget
- Boss portraits highest priority (~139 named identities)
- Generic visualization is an open creative question
- Buildings grow visually with tier and population

See [tech-stack.md](tech-stack.md) for the locked art pipeline (Ludo.ai Pro, style anchor, protagonist).

## Pricing & Release

Premium $5–$10. No microtransactions. Steam-first. Consoles + Steam Deck first-class. Mobile thoughtful port later.

## Endgame

Possible infinite mode + leaderboards. Locked after core game is complete.
