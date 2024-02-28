# This script is refer to nerindo Github Repository - https://github.com/yoseflaw/nerindo/tree/master 

import gensim
import torch
from torchtext.data import Field, NestedField, BucketIterator
from torchtext.datasets import SequenceTaggingDataset
from torchtext.vocab import Vocab
from collections import Counter

class Corpus(object):

    def __init__(self, input_folder, min_word_freq, batch_size, wv_file=None):
        # list all the fields
        self.word_field = Field(lower=True)  # [sent len, batch_size]
        self.tag_field = Field(unk_token=None)  # [sent len, batch_size]
        # Character-level input
        self.char_nesting_field = Field(tokenize=list)
        self.char_field = NestedField(self.char_nesting_field)  # [batch_size, sent len, max len char]
        # create dataset using built-in parser from torchtext
        self.train_dataset, self.val_dataset, self.test_dataset = SequenceTaggingDataset.splits(
            path=input_folder,
            train="train.txt",
            validation="dev.txt",
            test="test-data.txt",
            fields=(
                (("word", "char"), (self.word_field, self.char_field)),
                ("tag", self.tag_field)
            )
        )
        # convert fields to vocabulary list
        if wv_file:
            self.wv_model = gensim.models.word2vec.Word2Vec.load(wv_file)
            self.embedding_dim = self.wv_model.vector_size
            word_freq = {word: self.wv_model.wv.vocab[word].count for word in self.wv_model.wv.vocab}
            word_counter = Counter(word_freq)
            self.word_field.vocab = Vocab(word_counter, min_freq=min_word_freq)
            vectors = []
            for word, idx in self.word_field.vocab.stoi.items():
                if word in self.wv_model.wv.vocab.keys():
                    vectors.append(torch.as_tensor(self.wv_model.wv[word].tolist()))
                else:
                    vectors.append(torch.zeros(self.embedding_dim))
            self.word_field.vocab.set_vectors(
                stoi=self.word_field.vocab.stoi,
                vectors=vectors,
                dim=self.embedding_dim
            )
        else:
            self.word_field.build_vocab(self.train_dataset.word, min_freq=min_word_freq)
        # build vocab for tag and characters
        self.char_field.build_vocab(self.train_dataset.char)
        self.tag_field.build_vocab(self.train_dataset.tag)
        # create iterator for batch input
        self.train_iter, self.val_iter, self.test_iter = BucketIterator.splits(
            datasets=(self.train_dataset, self.val_dataset, self.test_dataset),
            batch_size=batch_size
        )
        # prepare padding index to be ignored during model training/evaluation
        self.word_pad_idx = self.word_field.vocab.stoi[self.word_field.pad_token]
        self.char_pad_idx = self.char_field.vocab.stoi[self.char_field.pad_token]
        self.tag_pad_idx = self.tag_field.vocab.stoi[self.tag_field.pad_token]