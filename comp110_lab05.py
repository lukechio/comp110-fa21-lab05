"""
Module: comp110_lab05

Exercises from lab 05, dealing with strings and file reading.
"""

def max_wind_speed(hurricane_dorain):

  
    f = open(hurricane_dorain,'r')
    biggest = 0
    for line in f:
        vals = line.split(',')
        diff = int(vals[-2]) 
        if diff > biggest:
            biggest = diff
    return biggest



def contains_word(word, review):
    lowerword=word.lower()
    reviewlowered=review.lower()
    my_str_words = reviewlowered.split()
    test = lowerword in my_str_words
    return test

    pass # replace this line with your implementation of this function


def test_max_wind_speed():
    if max_wind_speed("irma.csv") == 185:
        print("irma PASSESD")
    else:
        print("irma FAILED")

    if max_wind_speed("florence.csv") == 140:
        print("florence PASSED")
    else:
        print("florence FAILED")

    if max_wind_speed("dorian.csv") == 185:
        print("dorian PASSESD")
    else:
        print("dorian FAILED")

    
    print("Starting test of max_wind_speed")

    # To Do: Call your max_wind_speed function on the irma.csv file, using an if
    # statement to indicate whether the result was correct or not.
    # Then repeat the process for the florence.csv and dorian.csv files to check
    # whether your function works for those files.

    print("FAILED: Not implemented yet.") # remove this line when you finish the to do

    print("Done testing max_wind_speed")


def test_contains_word():
    """ Function that tests the contains_word function. """

    print("\nStarting test of contains word")

    if contains_word('ok', 'ok') != True:
        print("FAILED: contains_word('ok', 'ok')")
    elif contains_word('ok', 'OK') != True:
        print("FAILED: contains_word('ok', 'OK')")
    elif contains_word('ok', 'bad') != False:
        print("FAILED: contains_word('ok', 'bad')")
    elif contains_word('ok', 'movie ok') != True:
        print("FAILED: contains_word('ok', 'movie ok')")
    # To Do: update the chained conditional to test all of your new test cases.
    else:
        print("All contains_word test cases passed!")


    print("Done testing contains word")


def main():
    """ Calls the tester functions in the code. """
    test_max_wind_speed()
    test_contains_word()

# Do not modify anything after this point.
if __name__ == "__main__":
    main()
