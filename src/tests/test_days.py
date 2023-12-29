from ..days import Day


def test_day_create():
    day = Day(4)
    assert day.meals["Breakfast"] is None
    assert day.number_of_meals == 4
