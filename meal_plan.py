class MealPlan:
    def __init__(self):
        self.meal_plan_id = None
        self.breakfast_recipes = []
        self.lunch_recipes =[]
        self.dinner_recipes = []

    def set_meal_plan_id(self, meal_plan_id):
        self.meal_plan_id = meal_plan_id

    def fill_breakfast_recipes(self, breakfast_recipes):
        self.breakfast_recipes = breakfast_recipes

    def fill_lunch_recipes(self, lunch_recipes):
        self.lunch_recipes = lunch_recipes

    def fill_dinner_recipes(self, dinner_recipes):
        self.dinner_recipes = dinner_recipes