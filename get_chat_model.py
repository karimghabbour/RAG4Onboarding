import torch
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModelForCausalLM

def get_chat_model():
    model_name = "meta-llama/Meta-Llama-3-8B"
    cache_dir = "models/llama3"
    access_token = "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" #Needed since this is a gated model 

    # Load model and tokenizer from the local cache
    tokenizer = AutoTokenizer.from_pretrained(f"{cache_dir}/tokenizer/{model_name}")
    model = AutoModelForCausalLM.from_pretrained(f"{cache_dir}/model/{model_name}")
    
    return tokenizer, model

    
    
    
