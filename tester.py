import time

import numpy as np
import pandas as pd
import torch
from spacy.lang.id import Indonesian

class Tester(object):

    def __init__(self, model, device, data, model_name):
        self.device = device
        self.model = model.to(self.device)
        self.data = data
        self.model_name = model_name

    def infer(self,docs, index=None, true_tags=None):        
        data_infer = {
            "models": [],
            "tokens": [],
            "unks": [],
            "predicted_tags": [],
            "true_tags": [], 
        }
        data_seqeval = {
            "sentences": [],
            "tokens_length": [],
            "tokens": [],
            "predicted_tags": [],
            "true_tags": [],
        }
        df_infer = None
        df_seqeval = None
        model_name = self.model_name
        self.model.eval()
        # tokenize sentence
        nlp = Indonesian()
        #nlp.max_length = 2000000
        nlp.add_pipe('sentencizer')
        doc = nlp(docs)
        tokens_len = 0
        for sent in doc.sents:
            data_seqeval["sentences"].append(sent.text)
            tokens = [token.text for token in nlp(sent.text)]
            data_seqeval["tokens"].append(tokens)
            max_word_len = max([len(token) for token in tokens])
            # transform to indices based on corpus vocab
            numericalized_tokens = [self.data.word_field.vocab.stoi[token.lower()] for token in tokens]
            numericalized_chars = []
            char_pad_id = self.data.char_pad_idx
            for token in tokens:
                numericalized_chars.append(
                    [self.data.char_field.vocab.stoi[char] for char in token]
                    + [char_pad_id for _ in range(max_word_len - len(token))]
                )
            # find unknown words
            unk_idx = self.data.word_field.vocab.stoi[self.data.word_field.unk_token]
            unks = [t for t, n in zip(tokens, numericalized_tokens) if n == unk_idx]
            # begin prediction
            token_tensor = torch.as_tensor(numericalized_tokens)

            token_tensor = token_tensor.unsqueeze(-1).to(self.device)
            char_tensor = torch.as_tensor(numericalized_chars)
            char_tensor = char_tensor.unsqueeze(0).to(self.device)
            predictions, _ = self.model(token_tensor, char_tensor)
            # convert results to tags
            predicted_tags = [self.data.tag_field.vocab.itos[t] for t in predictions[0]]
            # print inferred tags
            max_len_token = max([len(token) for token in tokens] + [len('word')])
            max_len_tag = max([len(tag) for tag in predicted_tags] + [len('pred')])           
            #print(
            #    f"{'word'.ljust(max_len_token)}\t{'unk'.ljust(max_len_token)}\t{'pred tag'.ljust(max_len_tag)}"
            #    + ("\ttrue tag" if true_tags else "")
            #)
            endpos = tokens_len+len(tokens)
            t_tags = true_tags[tokens_len:endpos]
            p_tags = []
            for i, token in enumerate(tokens):
                is_unk = "unk" if token in unks else "-"
                data_infer["models"].append(str(self.model_name))
                data_infer["tokens"].append(str(token))
                data_infer["unks"].append(str(is_unk))
                data_infer["predicted_tags"].append(str(predicted_tags[i]))
                data_infer["true_tags"].append(str(t_tags[i]))
                #t_tags.append(str(true_tags[i+tokens_len]).strip())
                p_tags.append(str(predicted_tags[i]).strip())     
                #print(
                #    f"{token.ljust(max_len_token)}\t{is_unk.ljust(max_len_token)}\t{predicted_tags[i].ljust(max_len_tag)}"
                #    + (f"\t{true_tags[i]}" if true_tags else "-")
                #)
           
            
            data_seqeval["true_tags"].append(str(t_tags))
            data_seqeval["predicted_tags"].append(str(p_tags))
            tokens_len = tokens_len + len(tokens)
            data_seqeval["tokens_length"].append(str(len(tokens)))   
 
        df_infer = pd.DataFrame(data_infer)
        #wandb.log({f"dataframe_infer_{self.model_name}": wandb.Table(dataframe=df_infer)})  
        df_infer.to_csv(f"testing-result/df_infer_{model_name}_{index}.csv")

        df_seqeval = pd.DataFrame(data_seqeval)
        #wandb.log({f"dataframe_seqeval_{self.model_name}": wandb.Table(dataframe=df_seqeval)})
        df_seqeval.to_csv(f"testing-result/df_seqeval_{model_name}_{index}.csv")
        return tokens, predicted_tags, unks
        #eturn tokens, predicted_tags, unks, df_infer, df_seqeval