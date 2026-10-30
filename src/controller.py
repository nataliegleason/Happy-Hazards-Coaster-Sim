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
    occupied_b1: bool = False
    occupied_b2: bool = False
    occupied_b3: bool = False
    occupied_b4: bool = False
    prev_inputs: Inputs = field(default_factory=Inputs)
    # , timers, fault flags get added here later

def rising(prev: bool, now: bool) -> bool:
    return now and not prev

def scan(inputs: Inputs, state: State) -> tuple[Outputs, State]: #recieves inputs
    """One controller cycle. Defaults to the safe state."""
    prev = state.prev_inputs

    #rising edge detection: if the previous value was False and the current value is True, then a rising edge has occurred.
    if rising(prev.s2_e, inputs.s2_e):
        state.occupied_b2 = True      # train entered B2

    if rising(prev.s3_e, inputs.s3_e):
        state.occupied_b2 = False     # train reached B3, so B2 is clear

    if rising(prev.s3_e, inputs.s3_e):
        state.occupied_b3 = True      # train entered B3

    if rising(prev.s4_e, inputs.s4_e):
        state.occupied_b3 = False     # train reached B4, so B3 is clear

    if rising(prev.s4_e, inputs.s4_e):
        state.occupied_b4 = True      # train entered B4

    if rising(prev.s1_e, inputs.s1_e):
        state.occupied_b4 = False      # train reached B1, so B4 is clear

    if rising(prev.s1_e, inputs.s1_e):
        state.occupied_b1 = True      # train entered B1

    if rising(prev.s2_e, inputs.s2_e):
        state.occupied_b1 = False      # train reached B2, so B1 is clear

    permissive = ( #when can train leave the station? when all of these are true:
        inputs.estop_ok #estop circuit healthy
        and inputs.restraints_verified #restraints confirmed
        and inputs.dispatch_request #dispatch requested
        and not state.occupied_b2 #b2 not occupied
    )

    state.prev_inputs = inputs #save for next scan edge detection

    state.time_s += 0.05 #time increases with each scan by 50ms

    return Outputs(dispatch_permissive=permissive), state
