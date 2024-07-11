# To download the chat model files locally from HuggingFace & Save it 

from transformers import AutoTokenizer, AutoModelForCausalLM

def download_chat_model():
    model_name = "meta-llama/Meta-Llama-3-8B"
    model_path = "models/llama3"
    access_token = "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" #Needed since this is a gated model 

    # Download and save the model and tokenizer locally
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=access_token)
    tokenizer.save_pretrained(f"{model_path}/tokenizer/{model_name}")

    model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=access_token)
    model.save_pretrained(f"{model_path}/model/{model_name}")

    print("Chat Model and tokenizer saved locally.")

if __name__ == "__main__":
    download_chat_model()
