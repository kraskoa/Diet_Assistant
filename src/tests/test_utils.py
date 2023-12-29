from ..utils.get_meals import get_meals
from ..utils.load_secrets import load_secrets


def test_load_secrets():
    secrets = load_secrets("secrets.json")
    assert ["url", "app_id", "app_key"] == list(secrets.keys())


secrets = load_secrets("secrets.json")


def test_get_meals():
    list_of_meals_objects = get_meals(secrets, "Lunch", cuisineType="Asian")
    assert len(list_of_meals_objects) == 20
    assert list_of_meals_objects[0].meal_type == "Lunch"
    assert list_of_meals_objects[0].cuisine_type == "Asian"
