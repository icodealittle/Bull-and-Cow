from bulls_n_cows import *
TEST_GUESSES = [[1, 2, 3, 4], [5, 2, 3, 4], [7, 6, 5, 4], [0, 9, 8, 5],
                [2, 4, 6, 8], [1, 3, 5, 7], [1, 2, 0, 9]]

TEST_SECRET = [[1, 9, 8, 7],[2, 4, 6, 7], [1, 2, 0, 9],[7, 6, 5, 4]]

def create_guessbook(guesses = 7):
    guess_book = {}
    for i in range(guesses):
        entry = {}
        entry['GUESS'] = []
        entry['COWS'] = 0
        entry['BULLS'] = 0
        guess_book['GUESS ' + str(i)] = entry
    return guess_book


def test_count_bulls_and_cows():
    ''' Function test_count_bulls_and_cows
        Input: None.
        Returns: Number of failing test conditions for cow/bull sequences
        Do: Test various cow/bull sequences to ensure those counters
            are working as expected. Key cases: 0 cows, 0 bulls;
            4 cows, 0 bulls; 4 bulls, 0 cows, 2 cows, 2 bulls
    '''
    failed = 0
    success = 0

    #Need inpput player_guess – the digits cannot the same or in the same position
    #Test 1: 0 cows and 0 bulls
    auto_digits = [5, 8, 9, 2]
    player_digits = [3, 4, 1, 6]
    fake_bulls = 0
    fake_cows = 0
    print('Secret code:  ', auto_digits, ' and User input:  ', player_digits,
          'should have 0 bulls and 0 cows   ')
    #Calling funtion form bulls_n_cows
    #Storing the value that would be return
    bulls, cows = counts_bulls_and_cows(auto_digits, player_digits)
    if bulls == fake_bulls and cows == fake_cows:
        print('SUCCESS')
        success += 1
    else:
        print('FAIL')
        failed += 1

    #Need inpput player_guess – the digits cannot the same or in the same position
    #Test 1: 4 cows and 0 bulls
    auto_digits = [5, 8, 9, 2]
    player_digits = [2, 9, 8, 5]
    fake_bulls = 0
    fake_cows = 4
    print('Secret code:  ', auto_digits, ' and User input:  ', player_digits,
          'should have 0 bulls and 4 cows   ')
    #Calling funtion form bulls_n_cows
    #Storing the value that would be return
    bulls, cows = counts_bulls_and_cows(auto_digits, player_digits)
    if bulls == fake_bulls and cows == fake_cows:
        print('SUCCESS')
        success += 1
    else:
        print('FAIL')
        failed += 1

    #Need inpput player_guess – the digits cannot the same or in the same position
    #Test 1: 0 cows and 0 bulls
    auto_digits = [5, 8, 9, 2]
    player_digits = [5, 8, 9, 2]
    fake_bulls = 4
    fake_cows = 0
    print('Secret code:  ', auto_digits, ' and User input:  ', player_digits,
          'should have 4 bulls and 0 cows   ')
    #Calling funtion form bulls_n_cows
    #Storing the value that would be return
    bulls, cows = counts_bulls_and_cows(auto_digits, player_digits)
    if bulls == fake_bulls and cows == fake_cows:
        print('SUCCESS')
        success += 1
    else:
        print('FAIL')
        failed += 1

    #Need inpput player_guess – the digits cannot the same or in the same position
    #Test 1: 0 cows and 0 bulls
    auto_digits = [5, 8, 9, 2]
    player_digits = [5, 8, 2, 9]
    fake_bulls = 2
    fake_cows = 2
    print('Secret code:  ', auto_digits, ' and User input:  ', player_digits,
          'should have 2 bulls and 2 cows   ')
    #Calling funtion form bulls_n_cows
    #Storing the value that would be return
    bulls, cows = counts_bulls_and_cows(auto_digits, player_digits)
    if bulls == fake_bulls and cows == fake_cows:
        print('SUCCESS')
        success += 1
    else:
        print('FAIL')
        failed += 1

    return failed

def auto_play_game(secret_code, guess_book):
    ''' Function auto_play_game
        Input:  secret_code (list of digits),
                guess_book (dictionary of guess history)
        Returns: True if auto-player a winner; False otherwise
        Do: Automate the playing of Bulls and Cows for regression
        testing. Instead of using interactive input from stdin, this
        function uses test data fed directly to the function to simulate
        an entire "systems test" and complete game flow
        Concept: instead of guess = input(...), now using
        guess = TEST_GUESSES[i]
    '''

    fake_digits = secret_code
    guess_previous = ""
    
    for i in range(len(TEST_GUESSES)):
        guess_digits = TEST_GUESSES[i]
        score_bulls_cows = counts_bulls_and_cows(fake_digits, guess_digits)
        guess_book['GUESS ' + str(i)]['GUESS'] = guess_digits
        guess_book['GUESS ' + str(i)]['BULLS'] = score_bulls_cows[0]
        guess_book['GUESS ' + str(i)]['COWS'] = score_bulls_cows[1]

        guess_history = "".join([str(guess_digits), ' Bulls: ', str(score_bulls_cows[0]),' Cows: ', str(score_bulls_cows[1])])

        if guess_digits == 0:
            guess_previous = guess_previous + guess_history
        else:
            guess_previous = guess_previous + '\n' + guess_history

        print('\nYour guess history was: \n' + str(guess_previous))

        if score_bulls_cows[0] == 4:
            print('You win!', secret_code)
            return True
    print('You lost!!!!!!', secret_code, 'BOOOO!!!')
    return False

def test_regression_bull_cow(secret_code):
    ''' Function test_regression_bull_cow
        Input: secret_code: secret to test with (the one we're "cracking").
        Returns: None
        Do: Automatically exercise and test the entire bulls n cows system
        by calling auto_play_game() multiple times with both "winning" and
        "losing" data. Printed output can then be "diff'd" and examined either
        manually or automatically via tool support

        Example: code is our test data, and autoplay instead of interactive
        secret_code = TEST_SECRET[0]
        guess_book = create_guessbook(7)
        result = auto_play_game(secret_code, guess_book)
    '''
    guess_book = create_guessbook(7)
    result = auto_play_game(secret_code, guess_book)

def main():
    print('Beginning test suite. Testing count bulls and cows...')
    fails = test_count_bulls_and_cows()
    if fails > 0:
        print('Something went wrong. Pls go back and fix errors')
    else:
        print('Counting Bulls and Cows Passed All Tests')
    print('Beginning Auto Play Regression Tests')
    print('TEST LOSING COMBINATION')
    test_regression_bull_cow(TEST_SECRET[0])
    test_regression_bull_cow(TEST_SECRET[1])
    print('TEST WINNING COMBINATION')
    test_regression_bull_cow(TEST_SECRET[2])
    test_regression_bull_cow(TEST_SECRET[3])

main()
