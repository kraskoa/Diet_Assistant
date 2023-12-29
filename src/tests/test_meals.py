import pytest
from ..meals import Meal

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
        "cuisineType": "sports",
        "ingredients": {
            0: {
                "food": "chicken",
            }
        }
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
    assert meal.ingredients == ["chicken"]


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
    assert nutrients["Fat"] == 2.5
    assert nutrients["Protein"] == 30
    assert nutrients["Sugars"] == 0


def test_calculate_nutrients_100g():
    meal = Meal(mock_meals_list[0])
    nutrients = meal.calculate_nutrients("100g")
    assert nutrients["Fat"] == 0.91
    assert nutrients["Protein"] == 10.91
    assert nutrients["Sugars"] == 0


def test_meal_str():
    meal = Meal(mock_meals_list[0])
    result = "The Chicken breast meal weighs 550 grams total"
    result += " and has 252.5 calories per portion"
    assert str(meal) == result
