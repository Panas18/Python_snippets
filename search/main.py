import json
import os


def create_hash(sentence_list):
    resedue = [",", ".", "!", ":"]
    word_hash = {}
    for i, sentence in enumerate(sentence_list):
        words = sentence.split(" ")
        words[-1] = words[-1].rstrip()
        for word in words:
            word = word.lower()
            if len(word) == 0:
                break
            if word[-1] in resedue:
                word = word[:-1]
            if word not in word_hash:
                word_hash[word] = [i]
            else:
                if not i in word_hash[word]:
                    word_hash[word].append(i)
    with open(WORD_HASH_DIR, "w") as f:
        json.dump(word_hash, f)


def search(sentence_list, word):
    if not os.path.exists(WORD_HASH_DIR):
        create_hash(sentence_list)

    with open(WORD_HASH_DIR) as f:
        word_hash = json.load(f)

    try:
        word_index = word_hash[word.lower()]
        found_sentence = [sentence_list[index] for index in word_index]
        return found_sentence
    except KeyError:
        print(f" >> [{word}] not found")


if __name__ == "__main__":

    DATASET_DIR = "dataset"
    SENTENCE_LIST = "sentence_list.json"
    WORD_HASH = "word_hash.json"
    SENTENCE_LIST_DIR = os.path.join(DATASET_DIR, SENTENCE_LIST)
    WORD_HASH_DIR = os.path.join(DATASET_DIR, WORD_HASH)

    with open(SENTENCE_LIST_DIR) as f:
        sentence_list = json.load(f)

    found_sentence = search(sentence_list, "snowball")
    if found_sentence:
        for sentence in found_sentence:
            print(sentence)
