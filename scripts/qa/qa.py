import json

def run_qa():
    input_path = "../../data_pipeline/product.json"
    output_path = "../../data_pipeline/approved_product.json"

    try:
        with open(input_path, "r") as f:
            products = json.load(f)

        for p in products:
            p["qa_passed"] = True   #placeholder

        with open(output_path, "w") as f:
            json.dump(products, f, indent=4)

        print("QA Agent finalizado, produtos aprovados em data_pipeline/approved_product.json")

    except FileNotFoundError:
        print("product.json não encontrado. Execute o Builder Agent primeiro.")

f __name__ == "__main__":
    run_qa()

