import pytest
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
        "totalNutrients": {
            "FAT": {
                "label": "Fat",
                "quantity": 5,
            },
            "CHOCDF": {
                "label": "Carbs",
                "quantity": 10,
            },
            "PROCNT": {
                "label": "Protein",
                "quantity": 60,
            },
            "FIBTG": {
                "label": "Fiber",
                "quantity": 3,
            },
            "SUGAR": {
                "label": "Sugars",
                "quantity": 0
            }
        },
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


def test_calculate_calories_per_portion():
    meal = Meal(mock_meals_list[0])
    assert meal.calculate_calories("portion") == 252.5


def test_calculate_calories_per_100g():
    meal = Meal(mock_meals_list[0])
    assert meal.calculate_calories("100g") == 91.82


def test_calculate_calories_invalid():
    meal = Meal(mock_meals_list[0])
    with pytest.raises(ValueError):
        meal.calculate_calories("whatever")


def test_calculate_nutrients_portion():
    meal = Meal(mock_meals_list[0])
    nutrients = meal.calculate_nutrients("portion")
    assert nutrients["Fat"] == 5
    assert nutrients["Protein"] == 60
