from behave import *
from src.pokemon_service import Pokemon
@given(u'el "pokemon" fue elegido')
def step_impl(context):
    context.service = Pokemon()

@when(u'elijo el modo {hablar}')
def step_impl(context, hablar):
    context.result = context.service.hablar("ditto","limber")

@then(u'el sistema me dice su nombre y habilidad')
def step_impl(context):
    assert context.result == [{"name":"ditto","abiliti":"limber"}]
