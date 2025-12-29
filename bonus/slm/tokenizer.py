def tokenizer():
    import re
    tokens = []
    seen = set()
    with open("vocab.txt", "r") as file:
        vocab = file.read().splitlines()
        for word in vocab:
            w = word.strip()
            if not w:
                continue
            if not re.search(r"[A-Za-z]", w):
                continue
            if w not in seen:
                seen.add(w)
                tokens.append(w)
    with open("tokens.txt", "w") as file:
        for token in tokens:
            file.write(token + "\n")
    return tokens


def list_tokens():
    with open("tokens.txt", "r") as file:
        tokens = file.read().splitlines()
        list_of_tokens = []
        with open("tokens.py", "w") as file:
            for token in tokens:
                list_of_tokens.append(token)
            file.write(f"list_of_tokens = {str(list_of_tokens)}")
    return tokens

def numberize_tokens(token_sequence):
    with open("tokens.txt", "r") as file:
        tokens = file.read().splitlines()
        token_to_index = {token: index for index, token in enumerate(tokens)}
        with open("numbered_tokens.py", "w") as f:
            f.write(f"token_to_index = {str(token_to_index)}\n")
            indexed_sequence = [token_to_index[token] for token in token_sequence if token in token_to_index]
    return indexed_sequence

