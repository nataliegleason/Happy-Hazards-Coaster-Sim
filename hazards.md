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

### Assumptions
- The 1-5 s handoff gap between a block’s exit sensor and the next block’s entry sensor
- Stall timeouts only start counting once the next block is clear, so legitimate brake-run holds don’t cause false faults.
- Fault threshold is 1.5 × max for each interval


## Block Sections
| Block ID | Name | Nominal (s) | Min (s) | Max (s) |
|---|---|---|---|---|
| B1 | Station | 45 | 35 | 90 |
| B2 | Lift hill | 25 | 22 | 30 |
| B3 | Drop, inversion, mid-course brake | 20 | 17 | 35 |
| B4 | Inversion, final brake | 15 | 13 | 30 |

Full loop is 113 s nominal.

## Block Occupancy Parameteres
| Block | Becomes occupied on |	Clears on |
|---|---|---|
| B1 | S1_E | S2_E |
| B2 | S2_E | S3_E |
| B3 | S3_E | S4_E |
| B4 | S4_E | S1_E |

This design was chosen because if we chose to clear a block occupancy upon tripping the block exit sensor and not the entry sensor of the next block, then there might be a state that exists where a train has tripped an exit sensor of a block but never an extry sensor of the next block. This means that the train belongs to no blocks, and this breaks our system.

## Sensors
| Sensor ID | Block | Location | Nominal (s) | Min (s) | Max (s) |
|---|---|---|---|---|---|
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

## Hazard table
| ID | Hazard | Cause | Mitigation | Verifying test |
|---|---|---|---|---|
| H1 | Train collision | Train released into an occupied block | Block-clear interlock | (to be added) |
| H2 | Unsafe dispatch | Restraints unverified, B2 occupied, or E-stop active | dispatch permissive (restraints verified, E-stop clear, B2 not occupied) | (to be added) |
| H3| Stalled Train/Rollback | Train stops unexpectedly mid-brake run; rollback possible in B3 | the S3_M timeout flags a fault, the lift stops, dispatch is inhibited, and recovery is manual | (to be added) |
| H4 | Sensor failure or Inaccuracy | Hardware Issues | Plausability checks against t_min and t_max; Entry and exit sequence checks | (to be added) |
| H5 | Inconsistent state after fault | Controller restarts, has no indivcation of where trains are | Manual reset and visual clear track verification | (to be added) |

Potential additional hazards: brake failure, weather conditions, etc. 
