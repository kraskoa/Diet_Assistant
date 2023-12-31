from ..meals import Meal
from ..errors import NoRecipesFoundError
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
    defaults = {"diet": "", "cuisineType": "", "calories": ""}
    exclusions = ""
    list_of_meals_objects = []
    for arg in kwargs.items():
        if arg[0] == "excluded":
            for ingredient in arg[1]:
                exclusions += f"excluded={ingredient}&"
        else:
            defaults[arg[0]] = f"{arg[0]}={arg[1]}"

    # I've hard-coded the dishType to be Main course, since other
    # dishTypes were pointless to use (drinks, cocktails) or weren't
    # represented by sufficient amount of recipes (sandwiches, desserts)
    data = requests.get(secrets["url"].format(
        app_id=secrets["app_id"],
        app_key=secrets["app_key"],
        diet=defaults['diet'],
        cuisineType=defaults['cuisineType'],
        calories=defaults['calories'],
        mealType=meal_type,
        dishType="Main course",
        excluded=exclusions
    )).json()

    if data["count"] == 0:
        raise NoRecipesFoundError

    for hit in data["hits"]:
        list_of_meals_objects.append(Meal(hit["recipe"]))

    return list_of_meals_objects


# if __name__ == "__main__":
#     secrets = {
#         "url": "https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id}&app_key={app_key}&{diet}&{cuisineType}&mealType={mealType}",
#         "app_id": "350da553",
#         "app_key": "0e1f552796edd4134e2efadf38def7d1"
#     }
#     print(get_meals(secrets, "Lunch", cuisineType="Asian")[0])
