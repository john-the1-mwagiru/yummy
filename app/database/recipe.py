from dataclasses import dataclass
from typing import Optional


@dataclass
class Recipe:
    """Class representing a single category"""

    id: Optional[int]
    name: str
    ingredients: list
    directions: dict
    user_id: int


class RecipeModel:
    """Category data class"""

    id_counter = 7
    saved_recipes = [
        Recipe(
            id=1,
            name="Instant Pot Chicken Paprikash",
            ingredients=[
                "2 tablespoons butter",
                "1 tablespoon minced parsley",
                "¼ cup chicken broth",
                "1 cup plain yogurt, divided",
            ],
            directions={
                "step 1": "Fill a large pot with lightly salted water and bring to a rapid boil. Cook egg noodles at a boil until tender yet firm to the bite, 7 to 9 minutes. Drain and toss with butter, parsley, 1/2 teaspoon salt, and 1/2 teaspoon pepper. Keep noodles warm while preparing the chicken.",
                "step 2": "Turn on a multi-functional pressure cooker (such as Instant Pot®) and select z",
            },
            user_id=1,
        ),
        Recipe(
            id=2,
            name="Chicken broth",
            ingredients=[
                "2 tablespoons butter",
                "1 tablespoon minced parsley",
                "¼ cup chicken broth",
                "1 cup plain yogurt, divided",
            ],
            directions={
                "step 1": "Fill a large pot with lightly salted water and bring to a rapid boil. Cook egg noodles at a boil until tender yet firm to the bite, 7 to 9 minutes. Drain and toss with butter, parsley, 1/2 teaspoon salt, and 1/2 teaspoon pepper. Keep noodles warm while preparing the chicken.",
                "step 2": "Turn on a multi-functional pressure cooker (such as Instant Pot®) and select z",
            },
            user_id=1,
        ),
        Recipe(
            id=3,
            name="Savory Snacks",
            ingredients=[
                "2 tablespoons butter",
                "1 tablespoon minced parsley",
                "¼ cup chicken broth",
                "1 cup plain yogurt, divided",
            ],
            directions={
                "step 1": "Fill a large pot with lightly salted water and bring to a rapid boil. Cook egg noodles at a boil until tender yet firm to the bite, 7 to 9 minutes. Drain and toss with butter, parsley, 1/2 teaspoon salt, and 1/2 teaspoon pepper. Keep noodles warm while preparing the chicken.",
                "step 2": "Turn on a multi-functional pressure cooker (such as Instant Pot®) and select z",
            },
            user_id=2,
        ),
        Recipe(
            id=4,
            name="Quick Breakfasts",
            ingredients=[
                "2 tablespoons butter",
                "1 tablespoon minced parsley",
                "¼ cup chicken broth",
                "1 cup plain yogurt, divided",
            ],
            directions={
                "step 1": "Fill a large pot with lightly salted water and bring to a rapid boil. Cook egg noodles at a boil until tender yet firm to the bite, 7 to 9 minutes. Drain and toss with butter, parsley, 1/2 teaspoon salt, and 1/2 teaspoon pepper. Keep noodles warm while preparing the chicken.",
                "step 2": "Turn on a multi-functional pressure cooker (such as Instant Pot®) and select z",
            },
            user_id=2,
        ),
        Recipe(
            id=5,
            name="Quick Snacks",
            ingredients=[
                "2 tablespoons butter",
                "1 tablespoon minced parsley",
                "¼ cup chicken broth",
                "1 cup plain yogurt, divided",
            ],
            directions={
                "step 1": "Fill a large pot with lightly salted water and bring to a rapid boil. Cook egg noodles at a boil until tender yet firm to the bite, 7 to 9 minutes. Drain and toss with butter, parsley, 1/2 teaspoon salt, and 1/2 teaspoon pepper. Keep noodles warm while preparing the chicken.",
                "step 2": "Turn on a multi-functional pressure cooker (such as Instant Pot®) and select z",
            },
            user_id=3,
        ),
        Recipe(
            id=6,
            name="Dinner Snacks",
            ingredients=[
                "2 tablespoons butter",
                "1 tablespoon minced parsley",
                "¼ cup chicken broth",
                "1 cup plain yogurt, divided",
            ],
            directions={
                "step 1": "Fill a large pot with lightly salted water and bring to a rapid boil. Cook egg noodles at a boil until tender yet firm to the bite, 7 to 9 minutes. Drain and toss with butter, parsley, 1/2 teaspoon salt, and 1/2 teaspoon pepper. Keep noodles warm while preparing the chicken.",
                "step 2": "Turn on a multi-functional pressure cooker (such as Instant Pot®) and select z",
            },
            user_id=3,
        ),
    ]

    @classmethod
    def get_all(cls) -> list[Recipe]:
       return cls.saved_recipes

    @classmethod
    def get(cls, id: int) -> Recipe:
        for recipe in cls.saved_recipes:
            if recipe.id == id:
                return recipe
        raise Exception ("Recipe does not exist")

    @classmethod
    def create(cls, data: Recipe) -> Recipe:
        
        new_recipe = data
        if new_recipe.id is not None:
            raise Exception("New recipe should not have an id")

        new_recipe.id = cls.id_counter
        cls.id_counter += 1

        cls.saved_recipes.append(new_recipe)
        return new_recipe
             
            
    @classmethod
    def update(cls, id: int, data: Recipe) -> Recipe:
        for recipe in cls.saved_recipes:
            if recipe.id == id:
                recipe.name =data.name
                recipe.ingredients = data.ingredients
                recipe.directions = data.directions
                return recipe
        raise Exception('Recipe not found')

    @classmethod
    def delete(cls, id: int) -> bool:
        recipe_to_delete = cls.get(id)
        cls.saved_recipes.remove(recipe_to_delete)
        return True
        
