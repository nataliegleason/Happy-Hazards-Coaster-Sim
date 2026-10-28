# Big title
## Section heading
### Smaller heading
Normal paragraph text.
- Another bullet
**bold text**
`code or a variable name`
| Column A | Column B |
|---|---|
| cell | cell |


## Block Sections
| Block ID | Name | Nominal (s) | Min (s) | Max (s) |
|---|---|---|---|---|
| B1 | Station | 45 | 35 | 90 |
| B2 | Lift hill | 25 | 22 | 30 |
| B3 | Drop, inversion, mid-course brake | 20 | 17 | 35 |
| B4 | Inversion, final brake | 15 | 13 | 30 |

## Sensors
| Sensor ID | Block | Location | Nominal (s) | Min (s) | Max (s) |
|---|---|---|---|---|
| S1_E | B1 | After final brake run | 1 | 2 | 5 |
| S1_X | B1 | Station exit | 35 | 45 | 90 |
| S2_E | B2 | Chain Lift start | 1 | 2 | 5 |
| S2_X | B2 | Chain lift end | 22 | 25 | 30 |
| S3_E | B3 | Chain lift drop | 1 | 2 | 5 |
| S3_M | B3 | Rollback valley apex | 6 | 8 | 12|
| S3_X | B3 | Mid run brake run | 11 | 12 | 23 |
| S4_E | B4 | After mid run brake run | 1 | 2 | 5 |
| S4_X | B4 | Final brake run | 13 | 15 | 30 |

- Scan cycle: 50 ms
- Sensor latency: 20 ms
- Brake actuation delay: 300 ms
- Brake stopping time: 4 s

## Section heading

## Hazard table
| ID | Hazard | Cause | Mitigation | Verifying test |
|---|---|---|---|---|
| H1 | Train collision | Train released into an occupied block | Block-clear interlock | (to be added) |
| H2 | Unsafe dispatch | Restraints unverified, B2 active, or E-stop active | Timeout occurs at 1.5*t_ max which flags a fault and holds previous trains| (to be added) |
| H3| Stalled Train/Rollback | Train stops unexpectedly mid-brake run; rollback possible in B3 | Mid block B3 sensor at valley crest (t_crest) | (to be added) |
| H4 | Sensor failure or Inaccuracy | Hardware Issues | Plausability checks against t_min and t_max; Entry and exit sequence checks | (to be added) |
| H5 | Inconsistent state after fault | Controller restarts, has no indivcation of where trains are | Manual reset and visual clear track verification | (to be added) |

Potential additional hazards: brake failure, weather conditions, etc. 
