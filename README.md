# DIO - Google ADK - Neo4j

# Passo a passo

## Pre-Requisitos

## Subir toolbox

[Orientações de instalação do site oficial](https://googleapis.github.io/genai-toolbox/getting-started/introduction/)


Baixe o toolbox e dê permissão de execução
```
export VERSION=0.24.0
curl -L -O https://storage.googleapis.com/genai-toolbox/v$VERSION/linux/amd64/toolbox
chmod +x toolbox
```

Execute o toolbox (arquivo [tools.yaml](toolbox/tools.yaml) utilizado)
```
./toolbox --tools-file "tools.yaml" --ui
```

## MCP Inspector

Execute e abra o MCP Inspector apontando para `http://127.0.0.1:5000/mcp`
```
npx @modelcontextprotocol/inspector
```

## ADK

Instalando o ADK usando pip
```
pip install google-adk
```

Execute o adk web na pasta raiz e abra o navegador
```
adk web
```

# Links 

[Página Oficial do MCP](https://modelcontextprotocol.io/)

[Documentação Google Agent Development Kit](https://google.github.io/adk-docs/)

[ADK Python](https://github.com/google/adk-python)

[MCP Toolbox for Databases](https://github.com/googleapis/genai-toolbox)

[GraphAcademy - Plataforma de cursos gratuitos da Neo4j](https://graphacademy.neo4j.com/pt)

[Ambiente Sandbox Neo4j](https://sandbox.neo4j.com/)

[AI Studio - API Key Google](https://aistudio.google.com/)

[Fraud Detection Repository](https://github.com/neo4j-graph-examples/fraud-detection)

## MCP Servers
[https://mcpservers.org/](https://mcpservers.org/)

[https://hub.docker.com/mcp](https://hub.docker.com/mcp)

[https://mcp.so/](https://mcp.so/)

[https://cursor.directory/](https://cursor.directory/)
