
import logging

# Importa todos os módulos que o orquestrador pode chamar
from .modules import matematica, generative, escrita_algoritmos, memoria, teoria_mente, autoconsciencia
from .core.logger import setup_logger

logger = setup_logger("SID_Orchestrator")

# --- O CÉREBRO ORQUESTRADOR ---
def delegar_tarefa_sid(prompt, historico_conversa=None):
    prompt_lower = prompt.lower()
    logger.info(f"Orquestrador recebeu o prompt: '{prompt}'")

    # Palavras-chave para detecção de intenção
    keywords_matematica = ['calcule', 'quanto é', 'resolva uma expressão']
    keywords_algoritmos_codigo = ['crie um código', 'escreva um script', 'faça uma função', 'gere código']
    keywords_algoritmos_texto = ['descreva um algoritmo', 'explique a lógica', 'passos para']
    keywords_memoria = ['lembre-se de', 'salve isto', 'qual foi', 'histórico']
    keywords_teoria_mente = ['o que você achou', 'qual a intenção', 'como me sinto']
    keywords_autoconsciencia = ['sobre você', 'como você funciona', 'seus limites']


    # --- Lógica de Orquestração ---
    # A ordem dos 'if/elif' pode influenciar qual módulo é chamado primeiro se houver sobreposição de palavras-chave.
    # Ajuste conforme a prioridade desejada.

    if any(keyword in prompt_lower for keyword in keywords_matematica):
        expressao = prompt_lower.replace('calcule','').replace('quanto é','').replace('resolva uma expressão','').strip()
        # Chama o módulo de matemática. Ele retorna um dicionário {status, result/message}
        return matematica.resolver_expressao_matematica(expressao)

    elif any(keyword in prompt_lower for keyword in keywords_algoritmos_codigo):
        # Chama o módulo gerativo para gerar código. Ele retorna um dicionário {status, result/message}
        resposta_codigo = generative.gerar_codigo(prompt)
        # Formata a resposta para o endpoint da API
        if resposta_codigo.get("status") == "success":
             return {
                 "tipo": "codigo",
                 "resposta": "Claro! Aqui está o código Python que você pediu:",
                 "codigo": resposta_codigo['result']
             }
        else:
             return {
                 "tipo": "codigo_erro",
                 "resposta": "Não consegui gerar o código Python.",
                 "erro": resposta_codigo.get('message', 'Erro desconhecido na geração de código.')
             }

    elif any(keyword in prompt_lower for keyword in keywords_algoritmos_texto):
        # Chama o novo módulo de escrita_algoritmos. Ele retorna um dicionário {status, result/message}
        resposta_algoritmo = escrita_algoritmos.escrever_algoritmo(prompt)
        # Formata a resposta
        if resposta_algoritmo.get("status") == "success":
            return {
                "tipo": "algoritmo_texto",
                "resposta": resposta_algoritmo['result']
            }
        else:
             return {
                 "tipo": "algoritmo_erro",
                 "resposta": "Não consegui descrever o algoritmo.",
                 "erro": resposta_algoritmo.get('message', 'Erro desconhecido na descrição do algoritmo.')
             }

    # Exemplo de como integrar módulos de Memória, Teoria da Mente e Autoconsciência:
    # Note que a integração real pode ser mais complexa, passando contexto, histórico, etc.
    elif any(keyword in prompt_lower for keyword in keywords_memoria):
         resposta_memoria = memoria.gerenciar_memoria(prompt, historico_conversa)
         return {"tipo": "memoria", "resultado": resposta_memoria.get('result', resposta_memoria.get('message', 'Erro no módulo de memória.'))}

    elif any(keyword in prompt_lower for keyword in keywords_teoria_mente):
         resposta_teoria_mente = teoria_mente.analisar_intencao(prompt, historico_conversa)
         return {"tipo": "teoria_mente", "resultado": resposta_teoria_mente.get('result', resposta_teoria_mente.get('message', 'Erro no módulo de teoria da mente.'))}

    elif any(keyword in prompt_lower for keyword in keywords_autoconsciencia):
         # Para autoconsciência, talvez a SID "reflita" sobre sua última resposta ou um tópico
         # Aqui estamos apenas chamando o módulo com o prompt para simular
         resposta_autoconsciencia = autoconsciencia.refletir_sobre_resposta(prompt, "Simulando resposta anterior da SID...") # Substituir "Simulando..." pela resposta real se disponível
         return {"tipo": "autoconsciencia", "resultado": resposta_autoconsciencia.get('result', resposta_autoconsciencia.get('message', 'Erro no módulo de autoconsciência.'))}


    else:
        # Para todas as outras tarefas que não se encaixam em palavras-chave específicas,
        # usa o Módulo Gerativo padrão para texto livre.
        resposta_geral = generative.gerar_texto(prompt)
        # Formata a resposta geral
        if resposta_geral.get("status") == "success":
             return {"tipo": "geral", "resultado": resposta_geral['result']}
        else:
             return {"tipo": "geral_erro", "resultado": f"Não consegui responder. {resposta_geral.get('message', 'Erro desconhecido.')}"}

