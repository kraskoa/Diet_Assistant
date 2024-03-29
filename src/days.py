from .utils.get_meals import get_meals
import random


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
            none_dict.pop("Teatime")
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
        return round(daily_calories, 2)

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
        daily_nutrients = {
            key: round(value, 2) for key, value in daily_nutrients.items()
            }
        return daily_nutrients

    def __str__(self):
        res = ""
        meal_len = 11
        for meal, meal_name in self._meals.items():
            meal_padded = meal.ljust(meal_len) + ": "
            res += f"{meal_padded}{meal_name}\n\n"
        res += "\n"
        for label, quantity in self.calculate_total_nutrients().items():
            res += f"\t{label}: {quantity}g\n"
        res += f"\tCalories: {self.calculate_total_calories()}kcal\n"
        return res

    def create_menu(self, secrets: dict, **kwargs):
        """
        Function that creates a menu for the day using data from API

        Args:
            secrets (dict): a dictionary with credentials for the API
        """
        for meal in self._meals.keys():
            meals_list = get_meals(secrets, meal, **kwargs)
            self._meals[meal] = random.choice(meals_list)
