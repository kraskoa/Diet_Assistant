from ..meal_plans import MealPlan
from ..utils.load_secrets import load_secrets
import pytest


secrets = load_secrets("secrets.json")


def test_meal_plan_init():
    mp = MealPlan(3, 3)
    assert mp.number_of_days == 3
    assert mp.number_of_meals_per_day == 3
    assert mp.days_of_eating == []


def test_meal_plan_init_error():
    with pytest.raises(ValueError):
        MealPlan(20, 3)


def test_generate_meal_plan():
    mp = MealPlan(3, 3)
    mp.generate_meal_plan(secrets, cuisineType="Asian")
    all_meals = []
    for day in mp.days_of_eating:
        for meal in day.meals.values():
            all_meals.append(meal)
            assert "Asian".lower() in meal.cuisine_type
    assert len(all_meals) == 9


def test_calculate_average_calories():
    mp = MealPlan(3, 3)
    mp.generate_meal_plan(secrets, calories=300)
    assert mp.calculate_average_calories() <= 900


def test_calculate_average_nutrients():
    mp = MealPlan(3, 3)
    mp.generate_meal_plan(secrets, diet="high-protein")
    assert mp.calculate_average_nutrients()["Protein"] > 50
