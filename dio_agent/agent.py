from google.adk.agents import LlmAgent

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

import os

# MODEL = "gemini-2.5-flash"
MODEL = "gemini-3-flash-preview"

# Caso tenha feito o deploy de seu MCP em um servidor
# with ToolboxSyncClient("http://127.0.0.1:5000") as toolbox_client:
    # tools_full = toolbox_client.load_toolset()

import logging

logger = logging.getLogger('agent_neo4j_cypher')
logger.info("Initializing Database for tools")

import logging

logging.getLogger("neo4j").setLevel(logging.ERROR)
logging.getLogger("google_genai").setLevel(logging.ERROR)

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="google_genai.types")

data_analyst_agent = LlmAgent(
    model=MODEL,
    name='data_analyst_agent',
    description="""
    Este agente de análise de dados tem acesso a um grafo de conhecimento contendo informações sobre fraudes financeiras.
    """,
    instruction="""
    Você é um agente especializado em dados.
        
    Para cada pergunta do usuário, acesse a tool `get_schema` para entender o schema da base de grafos Neo4j.
    Para executar uma query no banco de grafos, utilize a tool `query_neo4j`.
    
    Use a tabela abaixo como referencia de termos em ingles e portugues.
    Termo Original,Tradução Técnica (Formal),Tradução de Mercado (BR)
    FirstPartyFraudster,Fraudador de Primeira Parte,Autor de Auto-fraude
    SecondPartyFraud,Fraude de Segunda Parte,Fraude por Conluio
    SecondPartyFraudSuspect,Suspeito de Fraude de 2ª Parte,Suspeito de Conluio
    """,
    
    tools=[
      MCPToolset(
            connection_params=StdioConnectionParams(
                server_params = StdioServerParameters(
                    command='./toolbox/toolbox',
                    args=["--tools-file","./toolbox/tools.yaml","--stdio"],
                ),
                timeout=60
            ),
        )
    ]
)

root_agent = LlmAgent(
    model=MODEL,
    name='dio_agent',
    global_instruction = "",
    description="""
    Agente principal (interface humana) para análise de dados.
    Ele agrega, correlaciona e apresenta informações de forma compreensível, a partir dos dados obtidos pelo analista de dados e pelo grafo de conhecimento.
    """,
    instruction="""
    Você é o agente responsável por coordenar os demais agente e gerar as respostas aos usuários.
    
    Quando o usuário fizer uma solicitação, você:
    - Coordena agentes especializados (ex: o data_analyst_agent) para coletar informações.
    - Integra e correlaciona os resultados.
    
    Priorize os agentes de pesquisa de dados sobre agentes diretos de banco de dados quando precisar de insights investigativos.
    """,

    sub_agents=[data_analyst_agent]
)