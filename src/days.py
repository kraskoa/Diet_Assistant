from meals import Meal


class Day:
    """
    Class that represents a day of dieting, contains all of the day's meals
    """
    def __init__(self, meals: list[Meal] = None):
        self._meals = meals

    @property
    def meals(self):
        return self._meals

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
