#!/usr/bin/env python3

import sys

from collections import defaultdict


def parse_dice_and_category(input_str: str)-> tuple[list[int], str]:
    try:
        dice, category = input_str.split()
    except ValueError as e:
        raise ValueError("Input should contain a space\
                          separating dice and category")
    return parse_dice(dice), _validate_category(category)


def _validate_category(category_str: str) -> str:
    if not category_str.strip() in CATEGORIES.keys():
        raise ValueError(f"Unknown category: {category_str}")
    return category_str


def valid_categories() -> list[str]:
    return sorted(CATEGORIES.keys())


def parse_dice(dice_str: str) -> list[int]:
    dice = [int(d) for d in dice_str.strip().split(',')]
    if len(dice) != 5:
        raise ValueError(f"Wrong number of dice. Expected 5, got {dice}")
    outside_range = filter(lambda x: x < 1 or x > 6, dice)
    if len(outside_range) > 0:
        raise ValueError(f"Illegal dice values: {outside_range}")
    return dice


def score(dice: list[int], category: str | None) -> int:
    score_function = CATEGORIES[category]
    return score_function(dice)


def _frequencies(dice: list[int]) -> dict:
    frequencies = defaultdict(int)
    for die in dice:
        frequencies[die] += 1
    return frequencies


def chance(dice: list[int]) -> int:
    return sum(dice)


def yatzy(dice: list[int]) -> int:
    if 5 in _frequencies(dice).values():
        return 50
    else:
        return 0


def _number_frequency(dice: list[int], number):
    return _frequencies(dice)[number]*number


def ones(dice: list[int]) -> int:
    return _number_frequency(dice, 1)


def twos(dice: list[int]) -> int:
    return _number_frequency(dice, 2)


def threes(dice: list[int]) -> int:
    return _number_frequency(dice, 3)


def fours(dice: list[int]) -> int:
    return _number_frequency(dice, 4)


def fives(dice: list[int]) -> int:
    return _number_frequency(dice, 5)


def sixes(dice: list[int]) -> int:
    return _number_frequency(dice, 6)


def _n_of_a_kind(dice: list[int], n: int) -> int:
    frequencies = _frequencies(dice)
    for i in [6,5,4,3,2,1]:
        if frequencies[i] >= n:
            return i*n
    return 0


def pair(dice: list[int]) -> int:
    return _n_of_a_kind(dice, 2)


def three_of_a_kind(dice: list[int]) -> int:
    return _n_of_a_kind(dice, 3)


def four_of_a_kind(dice: list[int]) -> int:
    return _n_of_a_kind(dice, 4)


def _is_straight(frequencies: list[int]) -> bool:
    return len(filter(lambda x: x == 1, frequencies.values())) == 5


def small_straight(dice: list[int]) -> int:
    frequencies = _frequencies(dice)
    if _is_straight(frequencies) and frequencies[6] == 0:
        return sum(dice)
    else:
        return 0


def large_straight(dice: list[int]) -> int:
    frequencies = _frequencies(dice)
    if _is_straight(frequencies) and frequencies[1] == 0:
        return sum(dice)
    else:
        return 0


def two_pairs(dice: list[int]) -> int:
    frequencies = _frequencies(dice)
    score = 0
    if len(filter(lambda x: x >=2, frequencies.values())) == 2:
        for i in [6,5,4,3,2,1]:
            if frequencies[i] >= 2:
                score += i*2
    return score


def full_house(dice: list[int]) -> int:
    frequencies = _frequencies(dice)
    if 3 in frequencies.values() and 2 in frequencies.values():
        return sum(dice)
    return 0


CATEGORIES = {"chance": chance,
              "yatzy": yatzy,
              "ones": ones, "twos": twos, "threes": threes,
              "fours": fours, "fives": fives, "sixes": sixes,
              "pair": pair, "threeofakind": three_of_a_kind, "fourofakind": four_of_a_kind,
              "smallstraight": small_straight, "largestraight": large_straight,
              "twopairs": two_pairs, "fullhouse": full_house
              }


if __name__ == "__main__":
    category = None
    if len(sys.argv) > 1:
        if "--help" in sys.argv:
            print(f"""\
                  Yatzy calculator program. Usage:\n\
                  yatzy.py <category>\n\
                  where <category> is the category to score.\
                  This should be one of:\n\
                  {sorted(CATEGORIES.keys())}\n\
                    You should pass dice rolls to standard input, \
                        formatted as one roll of five dice per line of input:\n\
                        1,2,3,4,5\n\
                            1,2,2,3,3
                            """)
            sys.exit(0)
        category = sys.argv[1]
    if not category in CATEGORIES.keys():
        print(f"unknown category: {category}")
        sys.exit(-1)

    for dice_input in sys.stdin.readlines():
        dice_str = dice_input.strip()
        try:
            dice = parse_dice(dice_str)
            points = score(dice, category)
        except ValueError as e:
            sys.stderr.write(f"ERROR in input '{dice_str}': {e}\n")
            points = "BAD_INPUT"
        print(f"""[{dice_str}] "{category}": {points}""")
