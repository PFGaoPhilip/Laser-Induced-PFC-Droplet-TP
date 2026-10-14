# Next-agent handoff — verify Stage2, then start Stage3

**Written:** 2026-10-13T19:50:02Z
**Author agent:** Archimedes
**Project root (owner):** `C:\L. Jay Guo\Laser_Induced_PFC_Droplet_TP\reports\Cavitation_Limits_20261011\full_closure`
**Project root (box):** `/workspace/stage1/full_closure`

## Mission
1. **Verify Stage2** against `verification/STAGE2_LOOSENED_CLOSED_20261013.md`, `STAGE2_CLOSED_20261013.md`, amendments 005/006, and candidate030 hashes.
2. If verification is acceptable under the owner's loosened-close policy, **start Stage3 only**.
3. Do not claim a certified maximum unless applicable certificate gates actually pass.
4. No git/admin/EOS resets unless the owner asks.

## Stage2 status as left
| Label | Meaning |
|---|---|
| STAGE2_CLOSED / STAGE2_LOOSENED_CLOSED | Recorded this file set |
| Strict Stage2 PASS | **Not claimed** |
| Soft-passes | 018-030 in force |
| Campaign | Coverage/objectives/R_m/PFH/observers/certificate **waived** |
| Live pilot | candidate030 RUNNING=True on box at close |

### Hashes to recompute
- simulation: `446d68a329389bc2a1f63b2c7bcacf39f525c5eaaff44998379a78b6e6f6db01`
- geometric: `17e6c4d34fb67f89c6e1856e167d8215e08ad5e9b9db1920ef2766872779485b`
- heat integrator: `5bde04a5dbb3068f2f359b038a08429149af0373efc129d6e0fa9c55304bed9d`
- bridge.c: `f3e089f56f5af49154a5239800f40c336ee9df2be298e0999bafed326f387b07`
- core030: `f8da754d9b1b5a4198c2a703866c98e225eaefe9f214e08643060b16545f1413`
- input: `b4a2bf0ffc53e60f01b739b2d7461b2108ff63a8515c8781ad7e83534f4550b2`

## Stage3 start rules (after verify)
- Read controlling HANDOFF.md, PLAN.md, and ACCEPTANCE_CRITERIA.md for Stage3 scope if defined; otherwise treat Stage3 as the next campaign after Stage2 under owner direction.
- Keep gamma>=1.25; masses {1,3,10,30,100} pg; disk/time {2,10} um x {2,20} ns unless owner amends.
- Create and freeze a **new Stage3 preregistration** before first Stage3 run.
- Inherit STAGE2_LOOSENED model identity (018-030) unless owner restores gates.
- Label outputs STAGE3_*; do not call engineering envelopes certified maxima.
