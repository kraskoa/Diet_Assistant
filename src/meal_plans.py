from .days import Day


class MealPlan():
    def __init__(self, number_of_days: int, days: list[Day] = []):
        self._number_of_days = number_of_days
        self._days_of_eating = days

    @property
    def number_of_days(self):
        return self._number_of_days

    @property
    def days_of_eating(self):
        return self._days_of_eating

