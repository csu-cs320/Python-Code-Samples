import re

def lines_from_file(filename):
    '''Try writing a good doc string for this'''
    with open(filename) as f:
        return f.readlines()

def first_empty_string_index(strings):
    '''What would you want a user of this function to know about its behaviour?
    Edge cases?'''
    for index, string in enumerate(strings):
        if not string.strip():
            return index
    return -1

def syllables(s):
    '''Rough calculation of syllables, will miscount sometimes.
    i.e. dodge, wake, etc'''
    only_vowels = re.sub(r'[^aeiouy]', ' ', s.lower())
    # what does the intermediat result, only_vowels, look like?
    return len(only_vowels.split())

# how could you split this function up better so it's not mixing fileIO and program logic?
# It currently requires a file in order to test its functionality.
# Wouldn't it be nice to just be able to pass it data during an interactive session?
def poem_syllables_per_line(filename):
    lines = lines_from_file(filename)
    empty_line = first_empty_string_index(lines)
    for line in lines[empty_line + 1:]:
        line = line.strip()
        print('"{}" has {} syllables (roughly!)'.format(line, syllables(line)))

if __name__ == "__main__":
    import sys
    poem_filename = sys.argv[1]
    poem_syllables_per_line(poem_filename)
