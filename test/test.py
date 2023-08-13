#Test the ability for a state to be received in multiple two digit formats and return the UPPER CASE response.

def test_state():
    state = "oh"
    assert state.upper() == "OH"
    result = state.upper()
    assert result == 'OH'