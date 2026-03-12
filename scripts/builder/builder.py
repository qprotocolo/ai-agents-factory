# builder.py

"""
Builder Agent
Responsável por processar os dados coletados pelo Research Agent
e criar o produto inicial para o pipeline.
"""

import json
from datetime import datetime

def run_builder(input_file="research_output.json"):
    try:
        # Ler dados do Research Agent
        with open(input_file, "r") as f:
            research_data = json.load(f)

        # Criar produto inicial a partir dos dados
        product_data = {
            "agent": "builder",
            "input_topic": research_data.get("topic", ""),
            "timestamp": datetime.utcnow().isoformat(),
            "product_summary": f"Protótipo baseado no tópico {research_data.get('topic', '')}",
            "sources_used": research_data.get("sources", [])
        }

        # Salvar produto para QA Agent
        with open("product.json", "w") as f:
            json.dump(product_data, f, indent=4)

        print("Builder Agent finalizado. Produto salvo em product.json")

    except FileNotFoundError:
        print(f"Arquivo {input_file} não encontrado. Execute o Research Agent primeiro.")

if __name__ == "__main__":
    run_builder()

