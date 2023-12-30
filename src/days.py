from .utils.get_meals import get_meals
import random
import sys


class Day:
    """
    Class that represents a day of dieting, contains all of the day's meals
    """
    def __init__(self, number_of_meals: int):
        none_dict = {
            "Breakfast": None,
            "Snack": None,
            "Lunch": None,
            "Teatime": None,
            "Dinner": None
        }
        self._number_of_meals = number_of_meals
        if self._number_of_meals == 3:
            none_dict.pop("Snack")
            none_dict.pop("Teatlime")
            self._meals = none_dict
        elif self._number_of_meals == 4:
            none_dict.pop("Teatime")
            self._meals = none_dict
        elif self._number_of_meals == 5:
            self._meals = none_dict
        else:
            raise ValueError("Number of meals has to be between 3 and 5")

    @property
    def meals(self):
        return self._meals

    @property
    def number_of_meals(self):
        return self._number_of_meals

    def calculate_total_calories(self) -> float:
        """
        Function that calculates the total calories for the day

        Returns:
            float: total calories for the day
        """
        daily_calories = 0
        for meal in self._meals.values():
            daily_calories += meal.calculate_calories("portion")
        return daily_calories

    def calculate_total_nutrients(self) -> dict:
        """
        Function that calculates the total nutritional values for the day

        Returns:
            dict: dictionary with total nutritional values for the day
                  {"label": "quantity"}
        """
        daily_nutrients = {
            "Fat": 0,
            "Carbs": 0,
            "Protein": 0,
            "Fiber": 0,
            "Sugars": 0
        }
        for meal in self._meals.values():
            for nutrient in meal.calculate_nutrients("portion").items():
                daily_nutrients[nutrient[0]] += nutrient[1]
        return daily_nutrients

    def create_menu(self, secrets, max_calories: int = sys.maxsize, **kwargs):
        for meal in self._meals.keys():
            meals_list = get_meals(secrets, meal, **kwargs)
            self._meals[meal] = random.choice(meals_list)


if __name__ == "__main__":
    d = Day(5)
    secrets = {
        "url": "https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id}&app_key={app_key}&{diet}&{cuisineType}&mealType={mealType}",
        "app_id": "350da553",
        "app_key": "0e1f552796edd4134e2efadf38def7d1"
    }
    d.create_menu(secrets)
    print(d.calculate_total_calories())
    print(d.calculate_total_nutrients())
    for item in d.meals.items():
        print(f"{item[0]}: {item[1]}")

# dodac pole Excluded, dishType do get_meals i do Meal