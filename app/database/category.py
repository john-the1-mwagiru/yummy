from dataclasses import dataclass
from typing import Optional

@dataclass
class Category:
    """Class representing a single category"""

    id: Optional[int]
    name: str
    description: str
    user_id: int

class CategoryModel:
    """Category data class"""

    id_counter = 7
    saved_categories = [
       Category(id=1, name="Breakfast", description="a quick meal", user_id=1),
        Category(id=2, name="Sweet Snacks", description="a quick meal", user_id=1),
        Category(id=3, name="Savory Snacks", description="a quick meal", user_id=2),
        Category(id=4, name="Quick Breakfasts", description="a quick meal", user_id=2),
        Category(id=5, name="Quick Snacks", description="a quick meal", user_id=3),
        Category(id=6, name="Dinner Snacks", description="a quick meal", user_id=3),
     
    ]
    @classmethod
    def get_all(cls) -> list[Category]:
        return cls.saved_categories
    @classmethod
    def get(cls, id:int) -> Category:
      
        for category in cls.saved_categories :
            if category.id == id:
                return category
        raise Exception("Category Not Found")
    @classmethod
    def create(cls, data: Category) -> Category:
        new_category = data
        if new_category.id is not None:
            raise Exception("New category should not have an id")
        
        new_category.id = cls.id_counter
        cls.id_counter+=1

        cls.saved_categories.append(new_category)
        return new_category

    @classmethod
    def update(cls, id:int, data:Category) -> Category:
        for category in cls.saved_categories:
            if category.id == id:
                category.description = data.description
                category.name = data.name
                return category  
            
        raise Exception("Category does not exist")
        
    @classmethod
    def delete(cls, id:int) -> bool:
        category_to_delete = cls.get(id)
        cls.saved_categories.remove(category_to_delete)
        return True


