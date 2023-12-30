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
