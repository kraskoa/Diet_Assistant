from ..utils.get_meals import get_meals
from ..utils.load_secrets import load_secrets


secrets = load_secrets("secrets.json")


def test_load_secrets():
    secrets = load_secrets("secrets.json")
    assert ["url", "app_id", "app_key"] == list(secrets.keys())


def test_get_meals():
    list_of_meals_objects = get_meals(secrets, "Lunch", cuisineType="Asian")
    assert len(list_of_meals_objects) == 20
    assert "Lunch".lower() in list_of_meals_objects[0].meal_type[0].split('/')
    assert "Asian".lower() in list_of_meals_objects[0].cuisine_type


def test_get_meals_excluded():
    list_of_meals_objects = get_meals(secrets, "Lunch", excluded="chicken")
    all_ingredients = []
    for meal in list_of_meals_objects:
        all_ingredients.append(meal.ingredients)
    assert "chicken" not in all_ingredients


def test_get_meals_excluded_multiple():
    list_of_meals_objects = get_meals(
        secrets, "Lunch", excluded=["chicken", "butter"]
        )
    all_ingredients = []
    for meal in list_of_meals_objects:
        all_ingredients.append(meal.ingredients)
    assert "chicken" not in all_ingredients
    assert "butter" not in all_ingredients


def test_get_meals_calories():
    list_of_meals_objects = get_meals(secrets, "Lunch", calories=500)
    all_meals_calories = []
    for meal in list_of_meals_objects:
        all_meals_calories.append(meal.calculate_calories("portion"))
    assert max(all_meals_calories) <= 500
