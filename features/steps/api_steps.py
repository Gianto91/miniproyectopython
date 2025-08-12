from behave import given, when, then
from features.steps.common import session
import allure

@given('la API base es "{base_url}"')
def step_set_base(context, base_url):
    context.base_url = base_url

@when('hago una solicitud GET a "{endpoint}"')
def step_get(context, endpoint):
    context.response = session.get(context.base_url + endpoint)

@then('el código de respuesta debe ser {status_code:d}')
def step_status(context, status_code):
    allure.attach(str(context.response.text), name="response_body", attachment_type=allure.attachment_type.JSON)
    assert context.response.status_code == status_code

@then('el campo "{campo}" debe ser "{valor}"')
def step_json_field(context, campo, valor):
    keys = campo.split(".")
    data = context.response.json()
    for k in keys:
        data = data[k]
    assert str(data) == valor
