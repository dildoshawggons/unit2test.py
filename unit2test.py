def read_file(file_name):

    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def get_total_words(text):

    return len(text.split())


def get_total_lines(text):

    return text.count('\n') + 1


def get_avg_words_per_line(text):

    total_words = get_total_words(text)
    total_lines = get_total_lines(text)
    return total_words / total_lines


def get_longest_line(text):

    lines = text.split('\n')
    longest_line = max(lines, key=len)
    return longest_line, len(longest_line.split())


def lookup_word(text, word):

    lines = text.split('\n')
    matching_lines = [i + 1 for i, line in enumerate(lines) if word in line]
    if not matching_lines:
        print('Not found')
    else:
        print(f'Found {len(matching_lines)} lines containing the word "{word}":')
        for line_num in matching_lines[:10]:
            print(f'{line_num}: {lines[line_num - 1]}')


if __name__ == '__main__':
    file_name = 'alice.txt'
    text = read_file(file_name)
    total_words = get_total_words(text)
    total_lines = get_total_lines(text)
    avg_words_per_line = get_avg_words_per_line(text)
    longest_line, longest_line_word_count = get_longest_line(text)

    print(f'Total number of words: {total_words}')
    print(f'Average number of words per line: {avg_words_per_line:.2f}')
    print(f'The longest line has {longest_line_word_count} words:\n{longest_line}')

    word = input('Enter a word to look up: ')
    lookup_word(text, word.lower())
