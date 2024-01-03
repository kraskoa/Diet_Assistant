from .days import Day


class MealPlan():
    """
    Class that represents an entire meal plan. Created mainly for the
    sake of efficiently formatting data to write in the final output file
    """
    def __init__(
                self, number_of_days: int,
                number_of_meals_per_day: int,
                days: list[Day] = []
                ):
        if 1 <= number_of_days <= 14:
            self._number_of_days = number_of_days
        else:
            msg = "Can only generate a meal plan for maximum of two weeks"
            raise ValueError(msg)
        self._number_of_meals_per_day = number_of_meals_per_day
        self._days_of_eating = days

    @property
    def number_of_days(self):
        return self._number_of_days

    @property
    def number_of_meals_per_day(self):
        return self._number_of_meals_per_day

    @property
    def days_of_eating(self):
        return self._days_of_eating

    def generate_meal_plan(self, secrets: dict, **kwargs):
        """
        Function that generates a meal plan for each day

        Args:
            secrets (dict): a dictionary with credentials for the API
        """
        for _ in range(self._number_of_days):
            self._days_of_eating.append(Day(self._number_of_meals_per_day))
        for day in self._days_of_eating:
            day.create_menu(secrets, **kwargs)

    def calculate_average_calories(self) -> float:
        """
        Function that calculates average daily caloric intake

        Returns:
            float: average daily caloric intake
        """
        total_calories = 0
        for day in self._days_of_eating:
            total_calories += day.calculate_total_calories()
        return round(total_calories / self._number_of_days, 2)

    def calculate_average_nutrients(self) -> dict:
        """
        Function that calculates the average nutritional values for
        the entire diet (meal plan duration)

        Returns:
            dict: dictionary with average nutritional values for the
                  meal plan - {"label": "quantity"}
        """
        average_nutrients = {
            "Fat": 0,
            "Carbs": 0,
            "Protein": 0,
            "Fiber": 0,
            "Sugars": 0
        }
        for day in self._days_of_eating:
            for nutrition_dicts in day.calculate_total_nutrients().items():
                average_nutrients[nutrition_dicts[0]] += nutrition_dicts[1]
        average_nutrients = {
            key: round(value / self._number_of_days, 2)
            for key, value in average_nutrients.items()
            }
        return average_nutrients

    def __str__(self):
        res = "Diet summary: \n"
        cals = self.calculate_average_calories()
        res += f"\tAverage daily caloric intake for the whole diet: {cals}kcal"
        res += "\n\tAverage daily nutritional values for the whole diet: \n"
        for label, quantity in self.calculate_average_nutrients().items():
            res += f"\t\t{label}: {quantity}g\n"
        res += "\n\n"
        for number, day in enumerate(self._days_of_eating):
            res += f"Day {number + 1}\n"
            res += f"{day}\n\n\n"
        return res
