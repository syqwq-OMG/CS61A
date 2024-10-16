"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls > 0, "Must roll at least once."
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    dice_sum, is_sow_sad = 0, False

    for _ in range(num_rolls):
        dice_points = dice()
        if dice_points == 1:
            is_sow_sad = True
        dice_sum += dice_points

    return 1 if is_sow_sad else dice_sum
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    ones, tens = player_score % 10, opponent_score // 10 % 10
    return max(1, 3 * abs(ones - tens))
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls >= 0, "Cannot roll a negative number of dice in take_turn."
    assert num_rolls <= 10, "Cannot roll more than 10 dice."
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        return boar_brawl(player_score, opponent_score)
    return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score


def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    factor_cnt = 0
    for factor in range(1, n + 1):
        if n % factor == 0:
            factor_cnt += 1
    return factor_cnt
    # END PROBLEM 4


def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    score_factors_num = num_factors(score)
    if score_factors_num == 3 or score_factors_num == 4:
        while not is_prime(score):
            score += 1
    return score
    # END PROBLEM 4


def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return sus_points(simple_update(num_rolls, player_score, opponent_score, dice))
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update, score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        score0 = update(strategy0(score0, score1), score0, score1, dice)
        if score0 >= goal:
            break
        score1 = update(strategy1(score1, score0), score1, score0, dice)
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"

    def always_roll_strategy(player_score, opponent_score):
        return n

    return always_roll_strategy
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    first = strategy(0, 0)
    for pl in range(goal):
        for op in range(goal):
            if strategy(pl, op) != first:
                return False
    return True
    # END PROBLEM 7


def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"

    def average_dice(*args):
        tot = 0
        for _ in range(times_called):
            tot += original_function(*args)
        return tot / times_called

    return average_dice

    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, times_called=1000, return_point=False):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    max_point, max_idx = -1, 0
    for num_rolls in range(1, 11):
        current_point = make_averaged(roll_dice, times_called)(num_rolls, dice)
        if current_point > max_point:
            max_point, max_idx = current_point, num_rolls
    if return_point:
        return max_idx, max_point
    else:
        return max_idx

    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print("Max scoring num rolls for six-sided dice:", six_sided_max)

    print("always_roll(6) win rate:", average_win_rate(always_roll(6)))  # near 0.5
    print("catch_up win rate:", average_win_rate(catch_up))
    print("always_roll(3) win rate:", average_win_rate(always_roll(3)))
    print("always_roll(8) win rate:", average_win_rate(always_roll(8)))

    print("boar_strategy win rate:", average_win_rate(boar_strategy))
    print("sus_strategy win rate:", average_win_rate(sus_strategy))
    print("final_strategy win rate:", average_win_rate(final_strategy))
    # print("ChatGPT_strategy win rate:", average_win_rate(gpt_strategy))
    "*** You may add additional experiments as you wish ***"


def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    if boar_brawl(score, opponent_score) >= threshold:
        return 0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    if sus_update(0, score, opponent_score) - score >= threshold:
        return 0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(
    score,
    opponent_score,
    dice=six_sided,
    simulation_times=100,
    goal=GOAL,
    conservative_threshold=20,
):
    """
    when player score is close to goal enough to reach the threshold
    we'll use conservative stragy when tend to use boar_brawl. otherwise,
    we'll do some simulation and then compare the 1-10 roll with boar brawl
    and choose the better

    score: player's score
    oppenent_score: opponent's score
    dice: dice type, default six-sided
    simulation_times: times to calculate average possible points that will get from the supposed roll time, default 1000
    goal: the winning score
    conservative_threshold: when(the diverge between score and goal) to reduce dicing and tend more to boar_brawl rule, default 10
    """
    # BEGIN PROBLEM 12
    if score >= goal - conservative_threshold:
        if (
            sus_update(0, score, opponent_score, dice) - score
            >= (score_to_win := goal - score) / 2
            # >= (score_to_win := 2) / 2
        ):
            best_roll = 0
        else:
            best_roll = score_to_win // 2
    else:
        # best_roll, expect_point = max_scoring_num_rolls(
        #     dice=dice, times_called=simulation_times, return_point=True
        # )
        best_roll, expect_point = 6, 18
        if sus_update(0, score, opponent_score, dice) - score >= expect_point:
            best_roll = 0

    return best_roll  # Remove this line once implemented.
    # END PROBLEM 12


def gpt_strategy(score, opponent_score, dice=six_sided, goal=GOAL):
    """
    A strategy that balances aggressive and conservative approaches based on the player's score.
    """
    conservative_threshold = 10  # When the player's score is within 10 points of winning, play conservatively.
    large_deficit_threshold = 20  # When trailing by 20 or more points, take more risks.

    # If you're within 10 points of winning, play conservatively
    if score >= goal - conservative_threshold:
        if sus_update(0, score, opponent_score, dice) >= goal - score:
            return 0  # Use boar brawl if it can get you closer to the goal safely
        else:
            return 1  # Roll just 1 die to avoid risk

    # If you're trailing by 20 points or more, take more risks
    if score < opponent_score - large_deficit_threshold:
        return max_scoring_num_rolls(
            dice, times_called=100
        )  # Aggressive play, more dice rolls

    # Otherwise, calculate the optimal number of dice to roll based on simulations
    best_roll, expect_point = max_scoring_num_rolls(
        dice=dice, times_called=100, return_point=True
    )

    # If boar brawl yields more points than expected rolls, use it
    if sus_update(0, score, opponent_score, dice) > expect_point:
        return 0

    return best_roll  # Return the best number of rolls based on simulation


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument(
        "--run_experiments", "-r", action="store_true", help="Runs strategy experiments"
    )

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
