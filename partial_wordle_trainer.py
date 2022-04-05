def count_sort_letters(array, column):
    """ Auxiliary subroutine for performing count sort based upon column of interest
    :input parameters: array; array of equal length a-z strings.  column;  integer digit column position of interest.
    :return:  array sorted lexicographically according to the digit column position of interest
    :worst-case time complexity: O(NM)
    :auxiliary space complexity: O(n+b) where b is the base (27)
    :precondition: input array is a non-empty array containing strings of equal length, input column
    is a valid integer digit column position within the string length
    :postcondition: returned array is sorted lexicographically according to the digit column position
    of interest - returned array is to contain the same elements as the input array
    """
    #  initialise output and count array
    output = [0] * len(array)
    count = [0] * 27  # cell for each letter and one additional for dummy character
    minimum = ord('a') - 1  # subtract one to allow for dummy character

    # iterate over every word in the input array
    for word in array:
        # obtain column letter if within string length and generate position counts, else use dummy position of 0
        letter = ord(word[column]) - minimum if column < len(word) else 0
        count[letter] += 1

    # store accumulative counts
    for i in range(len(count) - 1):
        count[i + 1] += count[i]

    for word in reversed(array):
        # obtain index of current letter of item at index col in count array
        letter = ord(word[column]) - minimum if column < len(word) else 0
        output[count[letter] - 1] = word
        count[letter] -= 1

    return output


def radix_sort_letters(array):
    """ Radix sort string implementation lexicographically orders strings considering each positional digit character
    :input parameters: array; array of equal length a-z strings
    :return: array; sorted lexicographically
    :worst-case time complexity: O(NM)
    :auxiliary space complexity: O(n+b) where b is the base (27)
    :precondition: array of equal length a-z strings with no duplicates
    :postcondition: lexicographically sorted array containing the same elements as the input array
    """
    # elements contain the same char length; iterate through all digit positions
    for column in range(len(array[0]) - 1, -1, -1):
        array = count_sort_letters(array, column)  # and sort each digit column position within its own set

    return array


def trainer(wordlist, word, marker):
    """
    :input parameters: wordlist; array of equal length a-z strings.  word; string of equal length a-z.
    marker; array containing elements in the range {0,1} of equal length to word and wordlist elements
    :return: array of possible correct strings that lie within the wordlist
    :worst-case time complexity: O(NM)
    :auxiliary space complexity: O(n+b) where b is the base (27)
    :precondition: all of word, marker and wordlist elements are of equal length.  word and wordlist
    elements contain a-z strings.  wordlist contains no duplicates.  marker contains elements in range {0,1}.
    marker and word align such that should marker contain only elements {1}; that word is the correctly guessed
    word itself and present in the original search wordlist.
    :postcondition: returned array contains elements that are potential correct answers sourced from
    the original input wordlist - returned array cannot contain elements that are not in wordlist.
    """
    #  initialise containers and sorted wordlist using radix sort
    sorted_lst = radix_sort_letters(wordlist)
    guess = word
    output = []
    corr_pos = []
    incorrect_pos = []
    incorrect_pos_letters = []

    #  consider all positional information given by marker; group like terms
    for position in range(len(marker)):

        #  correct character and position
        if marker[position] == 1:
            corr_pos.append(position)

        #  correct character, incorrect position
        elif marker[position] == 0:

            #  group the indexes of incorrect positions and those letters
            incorrect_pos.append(position)
            incorrect_pos_letters.append(guess[position])

    #  for the case where marker contains all 1's
    if len(corr_pos) == len(marker):
        return guess

    #  sort the correct letters belonging to the incorrect position
    incorrect_pos_letters = radix_sort_letters(incorrect_pos_letters)

    #  container for filtered unique correct letters at incorrect positions
    unique_incorrect_pos_letters = []

    #  iterate over the unique sorted letters that are at incorrect positions
    for letter in incorrect_pos_letters:

        #  remove duplicates from correct letters belonging to the incorrect position
        if len(unique_incorrect_pos_letters) == 0 or unique_incorrect_pos_letters[-1] != letter:
            unique_incorrect_pos_letters.append(letter)

    #  assess every query from sorted wordlist
    for query in sorted_lst:
        val = True

        for position in corr_pos:  # for every correct position in the marker

            #  check query against correct characters; if the char in query does not equate to guess'; invalid query
            if query[position] != guess[position]:
                val = False
                break

        for position in incorrect_pos:  # for every incorrect position in the marker
            if query[position] == guess[position]:  # if known incorrect char position is equal to guess'; invalid query
                val = False
                break

        #  container for incorrect letters in every query
        incorrect_query_letters = []

        #  for every incorrect position in the marker
        for position in incorrect_pos:
            #  append all the incorrect letters present in the current iteration query
            incorrect_query_letters.append(query[position])

        #  sort the incorrect query letters
        incorrect_query_letters = radix_sort_letters(incorrect_query_letters)

        #  container for filtered unique incorrect letters in query
        unique_incorrect_query_letters = []

        #  iterate over the unique sorted letters that are incorrect in the query
        for letter in incorrect_query_letters:

            #  remove duplicates from correct letters belonging to the incorrect position
            if len(unique_incorrect_query_letters) == 0 or unique_incorrect_query_letters[-1] != letter:
                unique_incorrect_query_letters.append(letter)

        #  compare the lengths of correct letters in incorrect positions between query and info from guess and marker
        if len(unique_incorrect_pos_letters) != len(unique_incorrect_query_letters):

            #  if unequal; invalid query
            val = False
        else:

            #  if not compare lists of incorrect letters in the query and that of the guess
            for i in range(len(unique_incorrect_query_letters)):

                #  assess sorted lists; if ever unequal - query does not contain valid permutation of correct letters
                if unique_incorrect_pos_letters[i] != unique_incorrect_query_letters[i]:
                    val = False
                    break

        if val:  # if query satisfies marker positions and conditional permutations of correct letters from guess
            output.append(query)  # add to output as valid

    return output
