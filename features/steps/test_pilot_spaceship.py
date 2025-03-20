from behave import given, when, then
from spaceship_model import Spaceship
from pilot_model import Pilot
from assertpy import assert_that

@given('un vaisseau spatial "{vaisseau}" avec une capacité de "{capacite}" pilotes')
def step_given_vaisseau(context, vaisseau, capacite):
    context.spaceship = Spaceship(vaisseau, int(capacite))

@when('un pilote "{pilote}" est assigné à ce vaisseau')
def step_when_assign_pilot(context, pilote):
    context.pilot = Pilot(pilote)
    context.spaceship.add_pilot(context.pilot)

@then('le pilote doit apparaître dans la liste des pilotes du vaisseau')
def step_then_pilot_in_spaceship(context):
    assert_that(context.pilot).is_in(context.spaceship.pilots)

@given('un vaisseau spatial "{vaisseau}" avec un niveau de carburant de "{carburant}" unités')
def step_given_carburant(context, vaisseau, carburant):
    context.spaceship = Spaceship(vaisseau, int(carburant))

@when('il tente de voyager en consommant "{consommation}" unités')
def step_when_travel(context, consommation):
    context.result = context.spaceship.travel(int(consommation))

@then('il doit afficher le message "{resultat}"')
def step_then_travel_result(context, resultat):
    assert_that(context.result).is_equal_to(resultat)

@given('un pilote "{pilote}" déjà assigné au vaisseau "{vaisseau1}"')
def step_given_pilot_assigned(context, pilote, vaisseau1):
    context.spaceship1 = Spaceship(vaisseau1, 2)
    context.pilot = Pilot(pilote)
    context.spaceship1.add_pilot(context.pilot)

@when('on tente de l\'assigner à un autre vaisseau "{vaisseau2}"')
def step_when_assign_to_another_ship(context, vaisseau2):
    context.spaceship2 = Spaceship(vaisseau2, 2)
    context.error_message = ""
    try:
        context.spaceship2.add_pilot(context.pilot)
    except Exception as e:
        context.error_message = str(e)

@then('le système refuse avec le message "{messageErreur}"')
def step_then_refuse_pilot_transfer(context, messageErreur):
    assert_that(context.error_message).is_equal_to(messageErreur)
