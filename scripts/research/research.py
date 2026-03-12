# research.py

"""
Research Agent
Responsável por coletar dados iniciais para o pipeline.
"""

import json
from datetime import datetime

def run_research(topic):

    # Estrutura de dados produzida pelo agente
    research_data = {
        "agent": "research",
        "topic": topic,
        "timestamp": datetime.utcnow().isoformat(),
        "sources": [
            "example_source_1",
            "example_source_2"
        ],
        "notes": "Dados iniciais coletados pelo agente de pesquisa."
    }

    # salvar arquivo de saída
    with open("research_output.json", "w") as file:
        json.dump(research_data, file, indent=4)

    print("Research Agent executado com sucesso.")
    print("Arquivo research_output.json criado.")

if __name__ == "__main__":

    topic = input("Digite o tópico de pesquisa: ")

    run_research(topic)
