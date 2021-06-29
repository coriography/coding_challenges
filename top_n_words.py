
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

## Hi! Thanks for the opportunity to complete this challenge. I enjoyed figuring it out and look forward to your feedback. -- Cori Lint

## running instructions: 
# requires Python3. Requires two files in the same directory as this file: “alice_in_wonderland.txt” from https://gist.github.com/phillipj/4944029 (or another content file), and common_words.txt from https://gist.github.com/deekayen/4148741 (or another file of common words, formatted the same way - one word per line). 
# Run doctests with the terminal command '$ python3 top_n_words.py -v'. If tests pass, proceed. If not, investigate errors.
# To execute, run this file in the command line using '$ python3 top_n_words.py' and follow the prompts (use paths of the required files previously mentioned). The class TopNWords will called to create an object based on given parameters, and the method print_top_n_words will be called on the object and print output to the terminal.


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
            word = word.lower().rstrip()
            dict_common_words[word] = 1

        return dict_common_words


    def file_to_str(self):
        """Takes in file path, opens file, and returns file's contents in a string."""

        return open(self.content_path).read()


    def create_dict_of_content(self):
        """Adds all content words to a dictionary."""

        # TODO: deal with non-content file contents (e.g. title, intro, "THE END") - these would be specific to content. For example, you would have to look at the Alice file and see that the content actually starts on line 17, and ends on 3598, and restrict this function to those parameters. I decided this was outside the scope of this exercise but wanted to make a note of it.

        from string import punctuation

        dict_content = {}
        # open and read content file using previously defined function
        content_string = self.file_to_str()
        # replace double-dash ("--") with space #! this is also somewhat specific to content and is a bit of a time and space drain - I might deal with this differently, given more time.
        content_string = content_string.replace("--", " ")
        # split by space => outputs list of words
        list_content = content_string.split()
        # iterate through list
        for word in list_content:
        # convert each word to lowercase and strip punctuation from beginning or end of word
        # ! I'm making an assumption of case-insensitivity - e.g. "Alice" is considered the same word as "alice"
            word = word.lower().strip(punctuation)
            # if punctuation was alone (e.g. "-" surrounded by spaces), it is now an empty string with a length of 0 - don't count that as a word 
            if len(word) > 0:
                # add each word to dict, or increment value by 1 if already in dict
                dict_content[word] = dict_content.get(word, 0) + 1

        return dict_content


    def print_top_n_words(self):

        dict_common_words = self.create_dict_of_common_words()
        dict_content = self.create_dict_of_content()

        # sort dict by descending frequency (values)
        content_sorted_by_frequency = sorted(dict_content.items(), key=lambda x: x[1], reverse=True)

        # print heading as indicated
        print("\nCount / Word\n ===   ===")

        # iterate through the dict until the number of words printed has reached n
        n_count = 0

        for word_key, word_val in content_sorted_by_frequency:
            if n_count < self.n:
            # if word is not in the common words dictionary, increase count and print
                if word_key not in dict_common_words:
                    print(word_key, ": ", word_val)
                    n_count += 1


###** User Input **###

print("Would you like to find the top n uncommon words of a content file? y/n")
user_answer = input()

if user_answer.lower() == "y":
    print("Please enter the content file path: ")
    content_path = input()
    print("Please enter the common words file path: ")
    common_path = input()
    print("Please enter the number of top words you want to see: ")
    num_words = input()

    # Create a TopNWords object from user input and print top words to terminal
    t = TopNWords(content_path, common_path, int(num_words))
    t.print_top_n_words()

elif user_answer.lower() == "n":
    print("OK, bye!")
else:
    print("Please enter 'y' or 'n'.")



if __name__ == "__main__":
    import doctest
    doctest.testmod()


