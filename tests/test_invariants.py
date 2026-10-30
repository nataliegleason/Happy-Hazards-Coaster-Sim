from src.controller import scan, Inputs, State

#dispatch overrides for testing
def good_inputs(**overrides):
    """All conditions met for dispatch, with optional changes."""
    base = dict(estop_ok=True, restraints_verified=True, dispatch_request=True)
    base.update(overrides)
    return Inputs(**base)


#dispatch permissive test when all conditions are met
def test_dispatch_allowed_when_all_conditions_met():
    outputs, _ = scan(good_inputs(), State())
    assert outputs.dispatch_permissive is True

#dispatch permissive tests when any condition is not met (restraints, b2, etc.)
def test_h2_no_dispatch_without_restraints():
    outputs, _ = scan(good_inputs(restraints_verified=False), State())
    assert outputs.dispatch_permissive is False

def test_h2_no_dispatch_when_b2_occupied():
    outputs, _ = scan(good_inputs(), State(occupied_b2=True))
    assert outputs.dispatch_permissive is False

def test_h2_no_dispatch_after_train_enters_b2():
    state = State()
    _, state = scan(Inputs(s2_e=True), state)           # train enters B2
    outputs, state = scan(good_inputs(s2_e=True), state)
    assert outputs.dispatch_permissive is False


#clearing tests for each block when the train reaches the next block
def test_b1_clears_when_train_reaches_b2():
    outputs, state = scan(Inputs(s2_e=True), State(occupied_b1=True)) # train enters B2
    assert state.occupied_b1 is False
    assert state.occupied_b2 is True #A bug where B2 never becomes occupied would slip through, so we check that B2 is occupied as well.

def test_b2_clears_when_train_reaches_b3():
    outputs, state = scan(Inputs(s3_e=True), State(occupied_b2=True)) # train enters B3
    assert state.occupied_b2 is False
    assert state.occupied_b3 is True

def test_b3_clears_when_train_reaches_b4():
    outputs, state = scan(Inputs(s4_e=True), State(occupied_b3=True)) # train enters B4
    assert state.occupied_b3 is False
    assert state.occupied_b4 is True

def test_b4_clears_when_train_reaches_b1():
    outputs, state = scan(Inputs(s1_e=True), State(occupied_b4=True)) # train enters B1
    assert state.occupied_b4 is False
    assert state.occupied_b1 is True