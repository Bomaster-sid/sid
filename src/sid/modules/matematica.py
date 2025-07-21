
from simpleeval import simple_eval
def resolver_expressao_matematica(expressao_str):
    try: return simple_eval(expressao_str)
    except Exception as e: return f'Erro: {e}'
