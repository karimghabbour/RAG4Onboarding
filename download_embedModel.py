# To download the model files locally from HuggingFace & Save it 

from transformers import AutoTokenizer, AutoModel

def download_model():
    model_name = "Salesforce/SFR-Embedding-2_R"
    model_path = "models/sfr"

    # Download and save the model and tokenizer locally
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.save_pretrained(f"{model_path}/tokenizer/{model_name}")

    model = AutoModel.from_pretrained(model_name)
    model.save_pretrained(f"{model_path}/model/{model_name}")

    print("Model and tokenizer saved locally.")

if __name__ == "__main__":
    download_model()