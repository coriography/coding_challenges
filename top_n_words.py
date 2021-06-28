
###** TOP N WORDS **###

# Write a small program that takes as input three pieces of information: 

# A text file containing a large amount of English-structured content. 
# ex: “alice_in_wonderland.txt” https://gist.github.com/phillipj/4944029 
# A text file containing “common” words, one word per line. 
# ex: “common.txt” https://gist.github.com/deekayen/4148741) 
# An integer. 

# Assume the text files will be placed in the same directory as your program file. 

# Output the top n words (from the user-given integer input) in descending order that recur in the given text file (alice_in_wonderland.txt), excluding any words that exist in the common words file (common_.txt). 

# The output should be in the following format: 

# Count  Word 
# ===   ==== 
# 37      the 
# 32      and 
# 25      a 
# 18      of 
# 17      that 
# 12      is 
# 10      in 
# 5        with 
# 4        as 
# 1        not 

# Utilize any programming language you want and provide clear instructions on how to run it. 

# Provide a link to a gist on GitHub containing your solution. 

# Plan to spend an hour or less, include the instructions to run it at the top of your gist in the form of comments. 

## TODO: running instructions


class TopNWords:
    """A class for a TopNWords object.

    >>> t = TopNWords("corilint.url", "testing.url", 15)
    >>> t.content_path
    'corilint.url'

    """

    def __init__(self, content_path, common_words_path, n):
        self.content_path = content_path
        self.common_words_path = common_words_path
        self.n = n

        
    def create_dict_of_common_words(self):
        """Adds all common words to a dictionary."""

        common_words = open(self.common_words_path)

        # add common words to their own dict
        dict_common_words = {}
        
        for word in common_words:
            word = word.rstrip()
            # dict_common_words[word] = dict_common_words.get(word, 0) +1
            dict_common_words[word] = 1

        return dict_common_words


    def file_to_str(self):
        """Takes in file path, opens file, and returns file's contents in a string."""

        return open(self.content_path).read()


    def create_dict_of_content(self):
        """Adds all content words to a dictionary."""

        # TODO: deal with non-content file contents (e.g. title, intro)
        # TODO: deal with double-dash ("--") (replace with space)

        from string import punctuation

        dict_content = {}
        # open and read content file (file_to_str)
        content_string = self.file_to_str()
        # split by space => list of words
        list_content = content_string.split()
        # iterate through list
        for word in list_content:
        # word to lowercase, strip punctuation
            word = word.strip(punctuation)
            if word != "I":
                word = word.lower()
            # if punctuation is alone (e.g. "-" surrounded by spaces), don't count it
            if len(word) > 0:
                # add each word to dict or increment val by 1 if already in dict
                dict_content[word] = dict_content.get(word, 0) + 1

        return dict_content


    def print_top_n_words(self):

        dict_common_words = self.create_dict_of_common_words()
        dict_content = self.create_dict_of_content()

        # sort dict by frequency (values)
        content_sorted_by_frequency = sorted(dict_content.items(), key=lambda x: x[1], reverse=True)

        # print heading as indicated
        print("\nCount / Word\n ===   ===")

        # iterate through the dict while count < n
        n_count = 0

        for word_key, word_val in content_sorted_by_frequency:
            if n_count < self.n:
            # if word appears in common words dict, skip it
            # if word is not in the common words dictionary, increase count and print
                if word_key not in dict_common_words:
                    print(word_key, ": ", word_val)
                    n_count += 1
            


t = TopNWords("alice_in_wonderland.txt", "1-1000.txt", 15)
t.print_top_n_words()


if __name__ == "__main__":
    import doctest
    doctest.testmod()


