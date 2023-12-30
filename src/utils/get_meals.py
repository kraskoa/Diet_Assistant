from ..meals import Meal
import requests


def get_meals(secrets: dict, meal_type: str, **kwargs) -> list:
    """
    Function that creates a list of Meal objects based on given parameters
    from the API

    Args:
        secrets (dict): a dictionary containing the API's credentials
        meal_type (str): the type of meals to be searched

    Returns:
        list: a list of Meal objects
    """
    defaults = {"diet": "", "cuisineType": ""}
    list_of_meals_objects = []
    for arg in kwargs.items():
        defaults[arg[0]] = f"{arg[0]}={arg[1]}"

    data = requests.get(secrets["url"].format(
        app_id=secrets["app_id"],
        app_key=secrets["app_key"],
        diet=defaults['diet'],
        cuisineType=defaults['cuisineType'],
        mealType=meal_type
    )).json()["hits"]

    for hit in data:
        list_of_meals_objects.append(Meal(hit["recipe"]))

    return list_of_meals_objects
