from pytest_bdd import given, when, then, scenario


# region Scenarios
@scenario('../features/01.feature', 'Nombre scenario')
def test_nombre_scenario(context):
    pass
# endregion


# region Givens
@given('Ejemplo given step')
def step_given(context):
    pass
# endregion


# region Whens
@when('Ejemplo when step')
def step_when(context):
    pass
# endregion


# region Thens
@then('Ejemplo then step')
def step_then(context):
    assert True
