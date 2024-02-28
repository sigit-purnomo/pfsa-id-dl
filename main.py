# This script is refer to nerindo Github Repository - https://github.com/yoseflaw/nerindo/tree/master 

import torch
from torch.optim import Adam
from corpus import Corpus
from models import NERModel
from tester import Tester
from pprint import pprint
import os
import pandas as pd

from ast import literal_eval
from tqdm import tqdm

if __name__ == "__main__":
    available_gpu = torch.cuda.is_available()
    if available_gpu:
        print(f"GPU is available: {torch.cuda.get_device_name(0)}")
        use_device = torch.device("cuda")
    else:
        use_device = torch.device("cpu")
    corpus = Corpus(
        input_folder="corpus/pfsa-id-test",
        min_word_freq=3,
        batch_size=64,
        wv_file="corpus/pretrained-embeddings/id.bin"
    )
    print(f"Train set: {len(corpus.train_dataset)} sentences")
    print(f"Val set: {len(corpus.val_dataset)} sentences")
    print(f"Test set: {len(corpus.test_dataset)} sentences")
    # configurations building block
    base = {
        "word_input_dim": len(corpus.word_field.vocab),
        "char_pad_idx": corpus.char_pad_idx,
        "word_pad_idx": corpus.word_pad_idx,
        "tag_names": corpus.tag_field.vocab.itos,
        "device": use_device
    }
    w2v = {
        "word_emb_pretrained": corpus.word_field.vocab.vectors if corpus.wv_model else None
    }
    cnn = {
        "use_char_emb": True,
        "char_input_dim": len(corpus.char_field.vocab),
        "char_emb_dim": 37,
        "char_emb_dropout": 0.25,
        "char_cnn_filter_num": 4,
        "char_cnn_kernel_size": 3,
        "char_cnn_dropout": 0.25
    }
    attn = {
        "attn_heads": 16,
        "attn_dropout": 0.25
    }
    transformer = {
        "model_arch": "transformer",
        "trf_layers": 1,
        "fc_hidden": 256,
    }
    configs = {
        #"PFSA-ID-BL": base,
        "PFSA-ID-BLW": {**base, **w2v}
        #"PFSA-ID-BLWC": {**base, **w2v, **cnn},
        #"PFSA-ID-BLWCA": {**base, **w2v, **cnn, **attn},
        #"PFSA-ID-TWCA": {**base, **transformer, **w2v, **cnn, **attn}
    }
    
    data_test = pd.read_csv(f"corpus/pfsa-id-test/data_paragraph.csv",converters={'tags': literal_eval})
    data_sample = data_test.sample(n=5, random_state=1)
    
    for model_name in configs:
        checkpoint_path = f"model/PFSA-ID Corpus/{model_name}.pt"
        print(f"Start Training: {model_name}")
        model = NERModel(**configs[model_name])
        tester = Tester(
            model=model,
            data=corpus,
            device=use_device,
            model_name=model_name
        )
        
        if os.path.exists(checkpoint_path):
            tester.model.load_state(checkpoint_path)
        else:
            print("No checkpoint found. Use model's last state for inference.")
        
        for index, row in tqdm(data_sample.iterrows(),total=data_sample.shape[0]):
            words, infer_tags, unknown_tokens = tester.infer(docs=row["paragraph"], index=index, true_tags=row["tags"])
    
    print()
