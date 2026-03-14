# builder.py

"""
Builder Agent
Responsável por processar os dados coletados pelo Research Agent
e criar o produto inicial para o pipeline.
"""

import json
from datetime import datetime

def run_builder(input_file="research_output.json"):
    input_path = "../../data_pipeline/research_output.json"
    output_path = "../../data_pipeline/product.json"

    try:
        # Ler dados do Research Agent
        with open(input_file, "r") as f:
            research_data = json.load(f)

        products = []
        for intem in research_data:
            products.append({
                "agent": "builder",
                "input_topic": item["nicho"],
                "timestamp": datetime.utcnow().isoformat(),
                "product_summary": f"{item['problema']} de {item['nicho']} para {item['publico']}",
                "sources_used": []
            })


        # Salvar produto para QA Agent
        with open(output_path, "w") as f:
            json.dump(products, f, indent=4)

        print("Builder Agent finalizado. Produto salvo em data_pipeline/product.json")

    except FileNotFoundError:
        print(f"Arquivo {input_file} não encontrado. Execute o Research Agent primeiro.")

if __name__ == "__main__":
    run_builder()

