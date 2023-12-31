from ..meals import Meal

import requests
import random


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
    defaults = {"diet": "", "cuisineType": "", "calories": ""}
    # A list of all sensible dish types, without it the API returns many
    # drinks/cocktails recipes which are unsuitable for the project
    dish_types = ["Main course", "Sandwiches"]
    exclusions = ""
    list_of_meals_objects = []
    for arg in kwargs.items():
        if arg[0] == "excluded":
            for ingredient in arg[1]:
                exclusions += f"excluded={ingredient}&"
        else:
            defaults[arg[0]] = f"{arg[0]}={arg[1]}"

    chosen_dish_type = random.choice(dish_types)
    data = requests.get(secrets["url"].format(
        app_id=secrets["app_id"],
        app_key=secrets["app_key"],
        diet=defaults['diet'],
        cuisineType=defaults['cuisineType'],
        calories=defaults['calories'],
        mealType=meal_type,
        dishType=chosen_dish_type,
        excluded=exclusions
    )).json()["hits"]

    for hit in data:
        list_of_meals_objects.append(Meal(hit["recipe"]))

    return list_of_meals_objects
