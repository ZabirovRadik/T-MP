import os
import pytest

from isb.isb_4_lab import card_selection, algorithm_luhn

SETTINGS = {
    "iins":[510126, 555921, 519747],
    "last_numbers": "0254",
    "hash": "4006234246b4fd2b2833d740927ab20465afad862c74b1a88ec0869bde5c836c",
    "path_to_card": "lab_5//json//card_number.json"
}



def test_get_card_number():
    assert "5559210557390254" == card_selection(SETTINGS["iins"],
                                                SETTINGS["last_numbers"],
                                                SETTINGS["hash"],
                                                SETTINGS["path_to_card"])


@pytest.mark.parametrize(("card_numbers", "result"),
                         [('5559210557390254', False),
                          ('3333333333333333', False),
                          ('4012888888881881', True)])
def test_luhn_algorithm(card_numbers, result):
    assert algorithm_luhn(card_numbers) == result
