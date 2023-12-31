from ..utils.load_secrets import load_secrets
from ..days import Day
import pytest


secrets = load_secrets("secrets.json")


def test_day_create():
    day = Day(4)
    assert day.number_of_meals == 4
    assert len(day.meals) == 4
    assert "Teatime" not in day.meals.keys()


def test_day_wrong_value():
    with pytest.raises(ValueError):
        Day(6)


def test_random_menu():
    day = Day(5)
    assert None in day.meals.values()
    day.create_menu(secrets, diet="high-protein", cuisineType="American")
    assert None not in day.meals.values()
