#Test the ability for a state to be received in multiple two digit formats and return the UPPER CASE response.

def test_state():

    assert state.upper(oH) == "OH"
    result = state.upper (oh)
    assert result == 'OH'