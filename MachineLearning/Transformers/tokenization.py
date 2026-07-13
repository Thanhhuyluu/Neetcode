import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        self.word_to_id = {
            self.pad_token: 0,
            self.unk_token: 1,
            self.bos_token: 2,
            self.eos_token: 3,
        }

        unique_words = set()

        for text in texts:
            for word in text.lower().split():
                unique_words.add(word)

        for word in sorted(unique_words):
            self.word_to_id[word] = len(self.word_to_id)

        self.id_to_word = {
            token_id: word
            for word, token_id in self.word_to_id.items()
        }

        self.vocab_size = len(self.word_to_id)

    def encode(self, text: str) -> List[int]:
        tokens = []

        for word in text.lower().split():
            token_id = self.word_to_id.get(
                word,
                self.word_to_id[self.unk_token]
            )
            tokens.append(token_id)

        return tokens        
    def decode(self, ids: List[int]) -> str:
        words = []

        for token_id in ids:
            word = self.id_to_word.get(token_id, self.unk_token)
            words.append(word)

        return " ".join(words)
s = SimpleTokenizer()
s.build_vocab(["i am a hero", "I cant eat"])
print(s.encode("i eat fish"))
print(s.decode([2, 4, 0, 9, 0, 1, 3]))

