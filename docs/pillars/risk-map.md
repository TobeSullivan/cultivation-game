# Pillar 3 — Risk Map (Territorial Conquest)

12 realms total, 1 per cultivation stage. The conquest layer that sources cards, recruits, and idle output.

---

## Realms (Scope-Based Names)

| Realm | Maps | Scope | Era |
|---|---|---|---|
| R1 | 2 | Province | Mortal |
| R2 | 3 | Region | Mortal |
| R3 | 3 | Kingdom | Mortal |
| R4 | 4 | Empire | Transcendent |
| R5 | 6 | Continent | Transcendent |
| R6 | 8 | Sea | Transcendent |
| R7 | 10 | World | Transcendent |
| R8 | 13 | Sky | Immortal |
| R9 | 15 | Heavens | Immortal |
| R10 | 17 | Star | Immortal |
| R11 | 18 | Galaxy | Divine |
| R12 | 20 | Universe | Eternal |

**Total: 119 map regions** + 12 realm-finals (overlap with map bosses) = 119 named map-boss disciples sourced from territorial play.

Realm names are placeholders — the structural lock is scope-based progression, not theme-based.

**Themes are NOT realm-locked.** Every realm contributes cards to every theme through map-boss signatures and region objectives. The player can build any of the 12 paths from R1 onward and grow them across the full game.

**R12 is the capstone realm.** Not a "do it again" realm. R12 is where every system tops out at once: the final Smith recruit, the final Library tier upgrade, the final special-event recruits, the final boss, the final cycle (Cycle 8 at Stage 12 breakthrough). Everything getting the bow on top. R12 is the culmination of power, not a stretch of variety content.

- **5 visual identities total** (one per era), with shared identity within each era to control art budget
- Each realm visually represents the geographic scope of its era

---

## Map Structure

- Each map is a region with the 6 universal objectives + a final boss (see [run-loop.md](run-loop.md))
- Conquering a map = banking all 6 of its objectives
- Final bosses are **named, unique, recruitable cultivators** — see [systems/boss-roster.md](../systems/boss-roster.md)

---

## Adjacency

- Player starts at one edge of a realm
- Conquering a map unlocks adjacent maps
- Player chooses the path
- **Boss fights are not gated by completion.** Only **recruitment** is gated, and even then only for specific exotic-gate bosses.

**Adjacency patterns by realm size:**
- **R1 (2 maps):** Linear. M1 = start, M2 unlocks after M1
- **R2/R3 (3 maps):** Gateway + branch + final. M1 = gateway, M2 unlocks after M1, M3 (realm-final) unlocks after BOTH M1 and M2
- **R4+ (4-20 maps):** Broader graphs; gateway entry, multiple branches, realm-final gated on completing some subset of prerequisites. Specific patterns TBD per realm.

---

## Enemy Categories

Each map has 4–6 fodder types + 2–3 elite types (visual/biome variation; mechanically baseline).

| Category | HP | Damage | Speed | Spawn rate | Drops |
|---|---|---|---|---|---|
| **Fodder** | 0.05× boss baseline | 0.4 (contact only) | 0.5–0.9× player | High continuous | Raw qi, occasional spirit stones |
| **Elite** | 0.5× | 0.8 (telegraphed) | 0.4× | One every ~90 sec | Chest (3–5 cards) + tier-appropriate materials |
| **Mini-boss** | 1.2× | 1.0 | 0.5× | One per minute past 10-min mark | Larger chest (5 cards) + better materials + sometimes inspiration fragment |

**Per-realm scaling:** R1 = 1×, R2 = 1.5×, R3 = 2×. Both HP and damage scale; speed/behavior constant.

**Generic boss on replay:** the named realm-final doesn't respawn. Generic boss with mini-boss stats × ~2 appears at 5- or 10-min mark instead.

**Within-run enemy HP scaling:** `HP(t) = base × 1.10^minute`. By minute 25, ~10× initial HP. Spawn density grows from ~1.5 fodder/sec at 0:00 to ~30+/sec at 25:00.

---

## Realm Transition

- **Both required to advance:** defeat the realm's final boss AND reach the cultivation stage that gates the next realm
- Player clicks the new realm to enter — triggers the **ascension cinematic / ceremony**
- After ceremony, player drops into the first region of the new realm
- Player controls *when* to ascend

---

## Bosses as Recruits

- **All defeated bosses can be recruited** into the player's sect
- Recruitment is **automatic on defeat** when requirements are met
- **Default requirement is just defeat.**
- **Exotic gates are a per-boss flavor feature**, sparingly used:
  - "Defeat with 100% region completion"
  - "Defeat with a specific build/path active"
  - "Defeat within X minutes"
  - "Defeat after recruiting their rival"
- Critical-path bosses (building-unlockers, realm-finals) are never exotic-gated.
- Defeated boss → joins your sect as a named disciple with name, fighting style, signature technique. Some also bring **building unlocks**.
- **No boss is ever locked out.** Late-completed exotic requirements still unlock the recruit.

### Boss Replacement on Replay

- Defeated named realm-final bosses do **not** respawn during region replays
- Replaced by a **generic boss** at 5- or 10-minute mark

---

## Map Surfacing of Incomplete Work

The Risk map UI clearly indicates regions, realms, and bosses with incomplete objectives or uncollected recruits. Subtle markers, realm-level summaries showing completion %. Lap-back legible but not pressuring.

---

## Idle Output from Conquered Regions

Conquered regions passively generate, even when player is offline. All flow into a unified **inbox** screen.

**Per-region output (per hour, R1 baseline; scales 2.4× per realm):**

1. **Essence** — universal upgrade currency (~30/hr R1)
2. **Raw Qi** — feeds qi pool toward tier breakthroughs (~20/hr R1)
3. **Spirit Stones** — higher-tier currency; rare drops + special-event arrivals carry small bundles
4. **Materials** — themed, tier-graded; plateaus at 3–5/hr (scarcity by tier, not quantity)
5. **Inspiration** — drops only from realm-final boss kills, never idle; required for Stage 4+ breakthroughs
6. Random rare drops (loot inbox)
7. Disciple XP (assigned named disciples grow)
8. Reputation / Influence
9. Lore / Codex fragments
10. Event triggers (rare boss spawns, treasure runs, hidden region unlocks, special-event recruit arrivals)
11. Recruitment leads (passive wandering cultivator events)

Currency model, material model, and Sect Power multiplier live in [systems/economy.md](../systems/economy.md).

---

## Disciple Assignment

- **Manual mode:** player assigns specific named disciples to specific regions/buildings for optimized output. Every named disciple has a **best-in-slot role**.
- **Auto mode:** "ass in a chair" — fills slots based on raw stats. **Deliberately suboptimal, permanently.**
- Auto-mode ignores **Training Hall student slots entirely** (manual-only optimization).

---

## Output Rate Scaling

Output rate increases with:
- Sect Power
- Sect buildings and their levels (including specialist count and Master rating)
- Named disciple count, tier, specialty-match per region, and Specialty Rating
- Macro progression unlocks

Output rate does **NOT** scale with cultivation stage directly or time held.

---

## Rival Sects

- Exist on the map as **targets to conquer**
- Conquered = conquered, permanently
- Rival sect leaders are recruitable bosses

---

## Tactical Routing

Building upgrades require **specialists** (recruited named bosses of the matching specialty) at rating ≥ tier + materials. Players plan routes through realm content to find what they need. Upgrade panels display sourcing info via building-runner's flavor dialogue.
