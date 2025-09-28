import os
import requests
from behave import given, when, then

BASE_URL   = os.getenv("SWAPI_BASE_URL", "https://swapi.dev/api").rstrip("/")
TIMEOUT    = float(os.getenv("SWAPI_TIMEOUT", "5"))                             
VERIFY_SSL = os.getenv("SWAPI_VERIFY_SSL", "true").lower() not in ("0","false","no","off")
HEADERS    = {"User-Agent": "swapi-tests", "Accept": "application/json"}      


@given('que defino o endpoint "{path}"')
def step_defino_endpoint(context, path):
    if not path.startswith("/"):
        path = "/" + path
    context.url = BASE_URL + path  


@when('eu faço uma requisição GET')
def step_faco_get(context):
    context.response = requests.get(
        context.url,
        headers=HEADERS,
        timeout=TIMEOUT,
        verify=VERIFY_SSL,
    )

@then('o status code deve ser {code:d}')
def step_status_code(context, code):
    assert context.response.status_code == code, (
        f"Esperado {code}, mas veio {context.response.status_code} | URL: {context.url}"
    )
    
@then('o campo "{field}" deve ter valor "{value}"')
def step_campo_valor(context, field, value):
    data = context.response.json()          
    atual = data.get(field)               
    assert str(atual) == value, (
        f'Esperado {field}="{value}", mas veio "{atual}" | URL: {context.url}'
    )

@then('o campo "{field}" deve conter "{expected}"')
def step_campo_contem(context, field, expected):
    data = context.response.json()
    exp = expected.lower()

    if isinstance(data, dict) and field in data and data[field] is not None:
        val = str(data[field])
        assert exp in val.lower(), (
            f'Campo "{field}" não contém "{expected}". Valor: "{val}" | URL: {context.url}'
        )
        return

    results = data.get("results")
    if isinstance(results, list):
        achou = False
        for item in results:
            val = item.get(field)
            if val and exp in str(val).lower():
                achou = True
                break
        assert achou, (
            f'Nenhum item em results tem "{field}" contendo "{expected}" | URL: {context.url}'
        )
        return

    assert False, f'Campo "{field}" não encontrado na resposta | URL: {context.url}'
