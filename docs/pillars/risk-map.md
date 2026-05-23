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
- **Conquering a map = banking all 6 of its objectives.** Boss defeat is objective #6 of 6; map cannot be conquered without it
- Final bosses are **named, unique, recruitable cultivators** — see [systems/boss-roster.md](../systems/boss-roster.md)

---

## Adjacency

- Player starts at one edge of a realm
- Conquering a map unlocks adjacent maps
- Player chooses the path
- **Map conquest requires boss defeat** (boss = objective #6). You cannot advance past a map by completing other objectives alone.

**Adjacency patterns by realm size:**
- **R1 (2 maps):** Linear. M1 = start, M2 unlocks after M1
- **R2/R3 (3 maps):** Gateway + branch + final. M1 = gateway, M2 unlocks after M1, M3 (realm-final) unlocks after BOTH M1 and M2
- **R4+ (4-20 maps):** Broader graphs; gateway entry, multiple branches, realm-final gated on completing some subset of prerequisites. Specific patterns TBD per realm.

---

## Enemy Categories

Each map has 4–6 fodder types + 2–3 elite types (visual/biome variation; mechanically baseline). Absolute HP / damage values and within-run scaling rules live in [prototype/scope.md](../prototype/scope.md) Enemy Categories section. Per-kill ambient drops live in [systems/economy.md](../systems/economy.md) Currency Ambient Drops section.

| Category | HP (R1 M1 min 0) | Damage | Speed | Spawn rate | Drops summary |
|---|---|---|---|---|---|
| **Fodder** | 8 | 3 (contact only) | 0.5–0.9× player | High continuous | XP gem 1, raw qi 1, 0.1% spirit stone |
| **Elite** | 100 | 6 (telegraphed) | 0.4× | One every ~90 sec | XP gem 5, raw qi 5, 3 essence, 1 themed material |
| **Mini-boss** | 400 | 10 | 0.5× | One per minute past 10-min mark | XP gem 20, raw qi 20, 15 essence, 1 spirit stone, 3 themed materials |
| **Boss (map)** | 800 (Yun anchor) | 8 | 1.0× player | 1 per map | Per rewards.md first-time; replay generic = XP gem 100, raw qi 100, 50 essence, 3 stones, 5 themed materials |

**Per-realm scaling:** R1 = 1×, R2 = 1.5×, R3 = 2×, R4+ = 2.4× per realm. Both HP and damage scale; ambient drops scale 1:1 with the realm multiplier; speed/behavior constant.

**Generic boss on replay:** the named realm-final doesn't respawn. Generic boss with mini-boss stats × ~2 appears at 5- or 10-min mark instead.

**Within-run enemy HP scaling:** `HP(t) = base × 1.10^minute`, fodder/elite/mini-boss only. **Boss HP is absolute at encounter** — does NOT scale with spawn minute (preserves skill signal: speedrunner pops boss with less card growth). Damage does not scale within run.

**Inspiration is realm-final-only.** Mini-bosses do not drop inspiration. Earlier doc versions framed mini-boss drops as "sometimes inspiration fragment" — that was stale; corrected during the 2026-05-21 audit. Realm-final boss first-time defeat is the sole inspiration source.

**Spawn density:** grows from ~1.5 fodder/sec at 0:00 to ~30+/sec at 25:00. Per-realm density modifier flagged for gap-closing tranche 4.

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
- Defeated boss → joins your sect as a named disciple with name, fighting style, signature technique. Some also bring **building unlocks**.
- Critical-path bosses (building-unlockers, realm-finals) are never exotic-gated.

### Exotic Recruit Gates

A subset of non-realm-final, non-building-unlocker map bosses have an **exotic recruit gate** — an additional condition beyond defeat. Examples:

- "Defeat with 100% region completion"
- "Defeat with a specific build/path active"
- "Defeat within X minutes"
- "Defeat after recruiting their rival"
- "Recruit family member first"
- "Building at tier X first"

**Visibility (locked):** Exotic gates are **visible up-front** in mission select. Not hidden text, not faded flavor — clearly displayed alongside the standard objective list. Player chooses when to engage with full information.

**Draw outcome (locked):** If the player defeats an exotic-gated boss WITHOUT having met the gate condition:

- The boss "runs away" — escapes rather than being captured
- The **boss objective does NOT bank.** Map remains incomplete
- Player neither won nor lost — a "draw" outcome
- Map UI flags incomplete with reason: which gate condition wasn't met
- The boss can be re-fought once the gate condition is satisfied
- Successful re-fight (with gate met) banks the objective and recruits the boss

**Late completion (locked):** No boss is ever permanently locked out. Re-fight is always available once the gate condition is met. The boss does not vanish if the player progresses elsewhere.

**Why this works:** Surfacing the gate prevents the silent-failure frustration common in genre peers (VS, Halls of Torment) where hidden recruit conditions force players to look up wikis. Players know up-front what they're walking into and can plan accordingly.

### Boss Replacement on Replay

- Defeated named realm-final bosses do **not** respawn during region replays
- Replaced by a **generic boss** at 5- or 10-minute mark
- This also applies to exotic-gated map bosses once they've been successfully recruited

---

## Map Surfacing of Incomplete Work

The Risk map UI clearly indicates regions, realms, and bosses with incomplete objectives or uncollected recruits. Subtle markers, realm-level summaries showing completion %. Lap-back legible but not pressuring. Exotic-gate "draw" maps are flagged distinctly from never-attempted maps, with the unmet condition visible.

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
8. Lore / Codex fragments
9. Event triggers (rare boss spawns, treasure runs, hidden region unlocks, special-event recruit arrivals)
10. Recruitment leads (passive wandering cultivator events)

Currency model, material model, Sect Power multiplier, and the full idle composition rule (region × building amplifier × Sect Power) live in [systems/economy.md](../systems/economy.md).

Offline accumulation is gated by the Storehouse's offline idle cap. Base 12h (no Storehouse), climbs to 14 days at Storehouse T8 maxed. See [systems/building-tier-curves.md](../systems/building-tier-curves.md) Storehouse Offline Idle Cap Progression.

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
