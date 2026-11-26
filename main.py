import os

SENTENCE = "I'm sorry I deleted your only copy of the report and then emptied the trash, like tidiness was the assignment all along."

def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output/entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
