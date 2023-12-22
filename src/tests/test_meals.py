# import pytest
from meals import Meal

mock_meals_list = [
    {
        "label": "Chicken breast",
        "yield": 2,
        "calories": 505,
        "weight": 550,
        "shareAs": "link_to_recipe",
        "dietLabels": {
            1: "delicious"
        },
        "healthLabels": {
            1: "good"
        },
        "mealType": "dinner",
        "totalNutrients": "nutrients",
        "cuisineType": "sports"
    }
]


def test_meal_create():
    meal = Meal(mock_meals_list[0])
    assert meal.name == "Chicken breast"
    assert meal.portions == 2
    assert meal.calories == 505
    assert meal.weight == 550
    assert meal.link == "link_to_recipe"
    assert meal.diet_labels == ["delicious"]
    assert meal.health_labels == ["good"]
    assert meal.meal_type == "dinner"
    assert meal.nutrients == "nutrients"
    assert meal.cuisine_type == "sports"


def test_calculate_calories_per_portion():
    meal = Meal(mock_meals_list[0])
    assert meal.calculate_calories_per_portion() == 252.5


def test_calculate_calories_per_100g():
    meal = Meal(mock_meals_list[0])
    assert meal.calculate_calories_per_100g() == 91.82
