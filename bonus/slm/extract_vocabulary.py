import csv


PUNCT = ".,!?;:'"
TRANSL = str.maketrans('', '', PUNCT)

def read_csv(path):
    with open(path, "r", encoding="utf-8", newline="") as csvfile, \
         open("vocab.txt", "w", encoding="utf-8", newline="\n") as f:
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            if not row:
                continue
            words = " ".join(row).split()
            if not words:
                continue
            if len(words) > 0:
                words = words[1:]
            for word in words:
                for p in PUNCT:
                    cnt = word.count(p)
                    if cnt:
                        f.write((p + "\n") * cnt)
                clean = word.translate(TRANSL)
                if clean:
                    f.write(clean + "\n")

 