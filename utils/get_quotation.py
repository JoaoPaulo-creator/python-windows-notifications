from httpx import get


def get_currency_quotation(link_consulta):

    USD = 'USD'
    BRL = 'BRL'
    PAIRS = f'{USD}-{BRL}'
    JSON_PAIRS = f'{USD}{BRL}'

    request = get(f'{link_consulta}/{PAIRS}', timeout=None)

    request_json_output = request.json()[f'{JSON_PAIRS}']
    quoted_value = request_json_output['ask']

    output = f'\n COTAÇÃO DO DÓLAR AMERICANO \n' \
             f'\nUSD 1 = R$ {quoted_value}\n' \


    return output
