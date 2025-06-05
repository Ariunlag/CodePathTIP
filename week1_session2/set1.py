def reverse_sentence(sentence):
    return " ".join(reversed(sentence.split(" ")))



if __name__ == '__main__':
    sentence = "tubby little cubby all stuffed with fluff"
    print(reverse_sentence(sentence))

    sentence = "Pooh"
    print(reverse_sentence(sentence))