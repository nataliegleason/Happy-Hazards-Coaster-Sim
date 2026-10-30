from dataclasses import dataclass

@dataclass(frozen=True)
class BlockSpec:
    name: str
    t_nominal: float
    t_min: float
    t_max: float

BLOCKS = [
    BlockSpec("station",  45, 35, 90),
    BlockSpec("lift",     25, 22, 30),
    BlockSpec("midcourse",20, 17, 35),
    BlockSpec("final",    15, 13, 30),
]
SCAN_PERIOD_S = 0.05
SENSOR_LATENCY_S = 0.02
BRAKE_DELAY_S = 0.3