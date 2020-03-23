from bulls_n_cows import generator, dup_digits, counts_bulls_and_cows, user_player
max_guess = 7

def main():
    secret = generator()
    player_guess_history = ""

    for i in range(max_guess):
        player_guess = user_player()
        score_bulls_cows = counts_bulls_and_cows(secret, player_guess)
        round_guesses = "".join([str(player_guess), ' Bulls:  ', str(score_bulls_cows[0]), ' Cows:  ', str(score_bulls_cows[1])])

        if i == 0:
            player_guess_history = player_guess_history + round_guesses
        else:
            player_guess_history = player_guess_history + '\n' + round_guesses

        print(str(player_guess_history))

        if score_bulls_cows[0] == 4:
            print('You win!', secret)
            break

    print('You lost!!!!!!', secret, '\nBOOOO!!!')
    


main()
