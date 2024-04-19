
''' This program converts inputed text and outputs the same text
with the first three letters
of each word bolded.
'''
def bold_first_three_letters(text):
    words = text.split()
    bolded_text = []
    for word in words:
        if len(word) >= 3:
            bolded_word = f"\033[1m{word[:3]}\033[0m{word[3:]}"
        else:
            bolded_word = word
        bolded_text.append(bolded_word)
    return ' '.join(bolded_text)


def main():
    user_input = input("Enter text you want the first three letters of every word bolded: ")
    bolded_output = bold_first_three_letters(user_input)
    print("Bolded text: ")
    print(bolded_output)


if __name__ == "__main__":
    main()
