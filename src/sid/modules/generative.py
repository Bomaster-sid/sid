
import google.generativeai as genai
from src.sid.core.logger import setup_logger
logger = setup_logger('SID_Generative')

def configurar_api(api_key):
    try:
        if not api_key or 'SUA_API_KEY' in api_key:
            logger.error('API Key inválida ou não configurada.')
            return False
        genai.configure(api_key=api_key)
        return True
    except Exception: return False

# --- CORREÇÃO GARANTIDA AQUI ---
# O nome do parâmetro deve ser 'instrucao_sistema'
def gerar_texto(prompt, instrucao_sistema='Você é um assistente prestativo.'):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=instrucao_sistema)
        return model.generate_content(prompt).text.strip()
    except Exception as e: return f'Erro: {e}'

def gerar_codigo(pedido):
    instrucao = 'Gere APENAS código Python.'
    # A chamada deve usar o nome de parâmetro correto: instrucao_sistema
    return gerar_texto(pedido, instrucao_sistema=instrucao)
