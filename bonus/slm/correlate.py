import numbered_tokens
import json 
def correlations():
    correlations_dict = {}
    with open("vocab.txt", "r") as file:
        tokens = file.read().splitlines()
        for i, token in enumerate(tokens):
            next_token = tokens[i + 1] if i + 1 < len(tokens) else None

            if not token or next_token is None:
                continue

            if token in correlations_dict:
                correlations_dict[token].add(next_token)
            else:
                correlations_dict[token] = {next_token}
    with open("correlations.py", "w") as f:
        f.write("correlations = {\n")
        for key, value in correlations_dict.items():
            if "'" in key or "'" in value:
                f.write(f'"{key}": {list(value)},\n')
            else:
                f.write(f"'{key}': {list(value)},\n")
        f.write("},\n")
    print(correlations_dict)

def alt_correlations():
    correlations_dict = {}
    with open("vocab.txt", "r") as file:
        prev = None
        for line in file:
            token = line.strip()
            if not token:
                continue
            if prev is not None:
                correlations_dict.setdefault(prev, []).append(token)
            prev = token

    with open("alt_correlations.py", "w") as f:
        f.write("correlations = ")
        f.write(json.dumps(correlations_dict, ensure_ascii=False, indent=2))
        f.write("\n")
    print(correlations_dict)
