from ..meal_plans import MealPlan


def test_meal_plan_init():
    mp = MealPlan(10)
    assert mp.number_of_days == 10
    assert mp.days_of_eating == []
