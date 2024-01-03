from ..utils.load_secrets import load_secrets
from ..days import Day
from ..errors import NoRecipesFoundError
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


def test_create_menu():
    day = Day(5)
    assert None in day.meals.values()
    day.create_menu(secrets, diet="high-protein", cuisineType="American")
    assert None not in day.meals.values()


def test_calculate_total_calories():
    day = Day(3)
    day.create_menu(secrets, calories=300)
    total = 0
    for meal in day.meals.values():
        total += meal.calculate_calories("portion")
    assert total <= 900


def test_calculate_total_nutrients():
    day = Day(3)
    day.create_menu(secrets, diet="high-protein")
    total = 0
    for meal in day.meals.values():
        total += meal.calculate_nutrients("portion")["Protein"]
    assert total > 50


def test_create_menu_no_recipes():
    day = Day(5)
    with pytest.raises(NoRecipesFoundError):
        day.create_menu(secrets, calories=1)
