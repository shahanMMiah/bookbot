""" Book bot program that print stat of book files. """
import argparse
import os


def word_count(words):
    """Return how many words in str

    Args:
        words (int): Number of wors
    """

    splt_words = words.split()
    return len(splt_words)


def letter_count(words):
    """Creates  dict how times a char is found in str

    Args:
        words (str): input string
    """
    ltr_count = {}

    for letter in words.lower():

        if not letter in ltr_count:
            ltr_count[letter] = 1
            continue

        ltr_count[letter] += 1

    return ltr_count


def char_count_report(title, book_str):
    """Creates report of found character and how many times its found

    Args:
        title (str): title of book
        book_str (_type_): book content as string
    """
    # get word count
    book_count = word_count(book_str)

    # get letter dictionary
    ltr_count = letter_count(book_str)

    # pirnt report
    print(f"--- Begin report of {title} ---")
    print(
        f"""{book_count} words found in the document
    """
    )

    # sort most to least found
    dict_ls = list(ltr_count.keys())
    dict_ls.sort(reverse=True, key=lambda c: ltr_count[c])

    # found char amount count
    for char in dict_ls:
        if char != " ":

            print(f"The '{char}' character was found {ltr_count[char]} times")


def set_args():
    """create arguement parser

    return (ArgumentParser) - argument parser instance
    """
    parser = argparse.ArgumentParser(prog="bookbot", description="print stats of books")

    parser.add_argument("-f", "--file_path", type=str, help="file path of book")

    return parser


def main():
    """ Main funtion to run on call

    Raises:
        RuntimeError: if file cannot be read as string
    """
    # get args
    parser = set_args()
    args = parser.parse_args()

    file_path = args.file_path

    # load file as string
    content = None
    with open(file_path, 'r', encoding="utf-8") as file_obj:
        content = file_obj.read()

    if not content:
        raise RuntimeError(f"could not find file {file_path}")

    # print report
    book_name = os.path.basename(file_path)
    char_count_report(book_name, content)


if __name__ == "__main__":
    main()
