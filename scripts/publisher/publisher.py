inport json

def run_publisher():
    input_path = "../../data_pipeline_product.json"

    try:
        with open(input_path, "r") as f:
            products = json.load(f)

        for p in products:
            print(f"Publishing: {p['product_summary']}")

        print("Publisher Agent finalizado.")

    except FileNotFoundError:
        print("approved_product.json não encontrado. Execute o QA Agent primeiro.")

if __name__ == "__main__":
    run_publisher()
