from ..meals import Meal
import requests


def get_meals(secrets: dict, meal_type: str, **kwargs) -> list:
    defaults = {"diet": "", "cuisineType": ""}
    list_of_meals_objects = []
    for arg in kwargs.items():
        defaults[arg[0]] = arg[1]

    data = requests.get(secrets["url"].format(
        app_id=secrets["app_id"],
        app_key=secrets["app_key"],
        diet=defaults["diet"],
        cuisineType=defaults["cuisineType"],
        mealType=meal_type
    )).json()["hits"]

    for hit in data:
        list_of_meals_objects.append(Meal(hit["recipe"]))

    return list_of_meals_objects
