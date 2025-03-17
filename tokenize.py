import os
import re

class Tokenizer:
    def __init__(self):
        self.token_id_map = {}
        self.id_token_map = {}
        self.tokens       = set()

    def tokenize(self, text_data):
        new_tokens = re.split(r"([,.:;?_!\"()\']|--|\s)", text_data)
        new_tokens = [item for item in new_tokens if item.strip()]
        self.tokens.update(new_tokens)
        return new_tokens 

    def update_dictionary(self):
        all_tokens = list(self.tokens)
        for idx, token in enumerate(sorted(all_tokens)):
            self.token_id_map[token] = idx
            self.id_token_map[idx]   = token

    def prepocess(self, file_path):
        with open(file_path, "r") as f:
            text_data = f.read()

        self.tokenize(text_data)
        self.update_dictionary()

    def encode(self, text):
        tokens = self.tokenize(text)
        ids = [self.token_id_map[token] for token in tokens]
        return ids


    def decode(self, ids):
        words = [self.id_token_map[id_] for id_ in ids]
        text = " ".join(words)
        # Replace space before puncuations
        text = re.sub(r'\s+([,.?!"()\'])', r"\1", text)
        return text

if __name__ == "__main__":
    file_name = "the-verdict.txt"
    tokenizer = Tokenizer() 
    tokenizer.prepocess(file_name)
    
    for item in tokenizer.token_id_map:
        print(f"{item}:{tokenizer.token_id_map[item]}")



