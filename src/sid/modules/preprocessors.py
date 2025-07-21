
import pandas as pd
# Assuming logger is in core
from src.sid.core.logger import setup_logger

logger = setup_logger('SID_Preprocessors_Module')

def limpar_nomes_colunas(df):
    '''
    Limpa os nomes das colunas de um DataFrame pandas, removendo espaços em branco
    do início e fim e convertendo para minúsculas.

    Args:
        df (pd.DataFrame): O DataFrame com as colunas a serem limpas.

    Returns:
        pd.DataFrame: Um novo DataFrame com os nomes das colunas limpos.
    '''
    logger.info("Limpando nomes de colunas do DataFrame.")
    if not isinstance(df, pd.DataFrame):
        logger.error("Input para limpar_nomes_colunas não é um DataFrame.")
        return df

    df_limpo = df.copy()
    df_limpo.columns = df_limpo.columns.str.strip().str.lower()
    logger.info("Nomes de colunas limpos com sucesso.")
    return df_limpo
