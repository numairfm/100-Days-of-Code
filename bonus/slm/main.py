import correlate
import correlations
import alt_correlations
import extract_vocabulary
import tokenizer
import tokens
import random
import re

csv_files = ["data1.csv", "data3.csv"]

def combine_csv_files(file_list, output_file):
    import pandas as pd

    combined_df = pd.DataFrame()

    for file in file_list:
        df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    combined_df.to_csv(output_file, index=False)


def main():
    #combine_csv_files(csv_files, "combined_data.csv")
    #extract_vocabulary.read_csv("combined_data.csv")
    #tokenizer.tokenizer()
    #tokenizer.list_tokens()
    #tokenizer.numberize_tokens(tokens.list_of_tokens)
    #correlate.alt_correlations()
    #print(len(tokens.list_of_tokens))

       
    token = random.choice(tokens.list_of_tokens)

    def is_valid_token(t):
        s = str(t)
        return bool(re.search(r"[A-Za-z]", s)) or s in {'.', ',', '!', '?'} or s.isdigit()
    

    for i in range(int(input("How many tokens to generate?\n> "))):
        print(token, end=" ", flush=True)
        candidates = []
        try:
            candidates = [t for t in alt_correlations.correlations.get(token, []) if is_valid_token(t)]
        except Exception:
            candidates = []
        if not candidates:
            token = random.choice(tokens.list_of_tokens)
        else:
            token = random.choice(candidates)
    print()
    
if __name__ == "__main__":
    main()
