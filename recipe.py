import json
import click

from typing import List

from ingredients import Ingredient
from instructions import Instruction


class Recipe():
    """Recipe class"""
    def __init__(self, name: str = "", instructions: List[Instruction] = [], ingredients : List[Ingredient] = []):
        self.name = name
        self.instructions = instructions
        self.ingredients = ingredients

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    
        