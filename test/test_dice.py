from dice import Die
import pytest

def test_fair():
    die = Die()
    rolls = 100_000

    tally = {i:0 for i in range(1, 7)}
    
    for i in range(rolls):
        tally[die.roll()] += 1

    for i in range(1, 7):
        assert tally[i]/rolls == pytest.approx(1/6, 1e-2)     

def test_average():
    die = Die()
    expect = sum(range(1, 7)) / 6
    
    total = 0
    rolls = 100_000
    for i in range(rolls):
        total += die.roll()
    
    average = total/rolls
    assert average == pytest.approx(expect, rel=1e-2)


@pytest.mark.parametrize('sides, rolls', [(5, 5_000_000), (7, 5_000_000)])
def test_double_roll(sides, rolls):
    die = Die(n=sides)
    
    expect = {i: prob_double_roll(i, sides) for i in range(2, 2 * sides + 1)}
    tally = {i:0 for i in expect}

    for i in range(rolls):
        tally[die.roll()+die.roll()] += 1
    
    for i in range(2, 2 * sides + 1):
        assert tally[i]/rolls == pytest.approx(expect[i], 1e-2)


def prob_double_roll(x, n):
    """
    Expected probabilities for the sum of two dice.
    """
    # For two n-sided dice, the probability of two rolls summing to x is
    # (n − |x−(n+1)|) / n^2, for x = 2 to 2n.

    return (n - abs(x - (n + 1))) / n ** 2


def test_valid_roll():
    """ Test that a die roll is valid. """

    # Intialise a standard, six-sided die.
    die = Die()

    # Roll the die.
    roll = die.roll()

    # Check that the value is valid.
    assert roll > 0 and roll < 7


def test_always_valid_roll():
    """ Test that a die roll is "always" valid. """

    # Intialise a standard, six-sided die.
    die = Die()

    # Roll the die lots of times.
    for i in range(10000):
        roll = die.roll()

        # Check that the value is valid.
        assert roll > 0 and roll < 7

