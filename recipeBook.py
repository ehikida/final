import json
from typing import List

from recipe import Recipe

class RecipeBook():
    def __init__(self, index: dict[str, int] = dict(), recipe_list : List[Recipe] = []):
        self.index : dict[str, int] = index
        self.recipe_list : List[Recipe] = recipe_list

    def addRecipeToIndex(self, recipe_name: str, idx: int):
        self.index[recipe_name] = idx

    def write_book(self):
        j_string = json.dumps(self.__dict__, default=vars)
        with open("book.json", 'w') as data:
            json.dump(j_string, data)
            
    def view_book(self):
        for key, val in self.index.items():
            print(f"{val} {key}")
        for blob in self.recipe_list:
            print(blob)