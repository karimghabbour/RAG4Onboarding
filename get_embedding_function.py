import torch
import torch.nn.functional as F
from torch import Tensor
from transformers import AutoTokenizer, AutoModel

def last_token_pool(last_hidden_states: Tensor, attention_mask: Tensor) -> Tensor:
    left_padding = (attention_mask[:, -1].sum() == attention_mask.shape[0])
    if left_padding:
        return last_hidden_states[:, -1]
    else:
        sequence_lengths = attention_mask.sum(dim=1) - 1
        batch_size = last_hidden_states.shape[0]
        return last_hidden_states[torch.arange(batch_size, device=last_hidden_states.device), sequence_lengths]

def get_embedding_function():
    model_name = "Salesforce/SFR-Embedding-2_R"
    cache_dir = "models/sfr"

    # Load model and tokenizer from the local cache
    tokenizer = AutoTokenizer.from_pretrained(f"{cache_dir}/tokenizer/{model_name}")
    model = AutoModel.from_pretrained(f"{cache_dir}/model/{model_name}")

    def embed_texts(texts):
        max_length = 4096
        batch_dict = tokenizer(texts, max_length=max_length, padding=True, truncation=True, return_tensors="pt")
        outputs = model(**batch_dict)
        embeddings = last_token_pool(outputs.last_hidden_state, batch_dict['attention_mask'])
        embeddings = F.normalize(embeddings, p=2, dim=1)
        return embeddings.cpu().detach().numpy()  # Ensure it's a numpy array
    
    
    return embed_texts
    
def embed_query(texts):
        print("run")
      
