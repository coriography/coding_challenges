
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
    >>> t.content_url
    'corilint.url'

    """

    def __init__(self, content_url, common_words_url, n):
        self.content_url = content_url
        self.common_words_url = common_words_url
        self.n = n

    def file_to_str(file_path):
        """Takes in file path, opens file, and turns the file's contents into a string."""

        file_contents = open(file_path).read()

        return file_contents

    def print_top_n_words():
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()


