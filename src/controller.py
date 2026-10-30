from dataclasses import dataclass, field

@dataclass(frozen=True) #frozen=non-writable
class Inputs:

    # Sensors (True = tripped / train present)
    s1_e: bool = False
    s1_x: bool = False
    s2_e: bool = False
    s2_x: bool = False
    s3_e: bool = False
    s3_m: bool = False
    s3_x: bool = False
    s4_e: bool = False
    s4_x: bool = False

    # Operator / safety signals
    estop_ok: bool = False #True = E-stop circuit healthy
    restraints_verified: bool = False
    dispatch_request: bool = False

@dataclass(frozen=True)
class Outputs:
    brake_b1: bool = True # True = brake engaged
    brake_b2: bool = True
    brake_b3: bool = True
    brake_b4: bool = True
    lift_enabled: bool = False
    dispatch_permissive: bool = False

@dataclass
class State: #not frozen, changes every cycle
    time_s: float = 0.0
    # occupancy, timers, fault flags get added here later

def scan(inputs: Inputs, state: State) -> tuple[Outputs, State]: #recieves inputs
    """One controller cycle. Defaults to the safe state."""
    return Outputs(), state