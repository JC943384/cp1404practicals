def main():
    user_input = input("Please enter your TEXT: ")
    word_count = count_words(user_input)
    longest_word = max(len(word) for word in word_count.keys())
    for word, count in sorted(word_count.items()):
        print(f"{word:{longest_word}} : {count}")


def count_words(user_input):
    words = user_input.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


if __name__ == "__main__":
    main()
