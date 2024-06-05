# Convert English text to IPA using: eng_to_ipa
# @pnry - version 0.0.3
# Last modified: 12 Dec 2020
# Last modified: 05 Jun 2024


# Usage:
# toIPA(filename, mode="para") # insert IPA paragraphs follows English paragraphs
# toIPA(filename, mode="word") # insert IPA transcription next to each word
# In Terminal:
# python3 to-ipa.py input.txt para
# python3 to-ipa.py input.txt word

import os
import sys
import time
import eng_to_ipa as ipa

NEWLINE_PLACEHOLDER = " p15081553y "


def toIPA(filename, mode="word"):
    print(filename, mode)

    start_time = time.time()
    transcript = ""

    print(f"Transcribing {filename} to IPA...")
    print("This may take a while, please wait...\n")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().strip().split("\n")
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return

    num_paragraphs = len(text)

    print(f"Total: {num_paragraphs} paragraphs")

    if mode == "para":
        print("Inserting IPA paragraphs following English paragraphs")
        for i in range(num_paragraphs):
            print(f"Processing paragraph number: {i+1}")
            ipa_text = ipa.convert(text[i])
            transcript += f"[{i+1}] {text[i]}\n\n[{i+1}] {ipa_text}\n\n"
    else:
        print("Inserting IPA next to each word")
        for i in range(num_paragraphs):
            print(f"Processing paragraph number: {i+1}")
            english_words = text[i].split(" ")
            ipa_words = [ipa.convert(word) for word in english_words]
            for word, ipa_word in zip(english_words, ipa_words):
                transcript += f"{word}[{ipa_word}]  "
            transcript += "\n\n"

    base_dir = os.path.dirname(filename)
    base_filename = os.path.basename(filename)
    ipa_filename = os.path.join(base_dir, "_ipa_done_" + base_filename)

    with open(ipa_filename, "w", encoding="utf-8") as file:
        file.write(transcript)

    print("\n#-----------------------")
    print("Done!")
    print(f"Took: {time.time() - start_time} seconds")
    print("#-----------------------")


if __name__ == "__main__":
    if len(sys.argv[1:]) > 0:
        print("Using CLI mode")
        toIPA(*sys.argv[1:])
    else:
        print("Using function call")
        toIPA("input.txt", "para")
