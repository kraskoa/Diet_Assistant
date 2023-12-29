# from meals import Meal


class Day:
    """
    Class that represents a day of dieting, contains all of the day's meals
    """
    none_dict = {
        "Breakfast": None,
        "Snack": None,
        "Lunch": None,
        "Teatime": None,
        "Dinner": None
    }

    def __init__(self, number_of_meals: int = 3, meals: dict = none_dict):
        self._meals = meals
        self._number_of_meals = number_of_meals

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
        for meal in self._meals:
            daily_calories += meal.calculate_calories("portion")
        return daily_calories

    def calculate_total_nutrients(self) -> dict:
        """
        Function that calculates the total nutritional values for the day

        Returns:
            dict: dictionary with total nutritional values for the day
                  {"label": "quantity"}
        """
        daily_nutrients = {}
        for meal in self._meals:
            for nutrient in meal.nutrients:
                daily_nutrients[nutrient["label"]] += nutrient["quantity"]
        return daily_nutrients
