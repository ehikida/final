import json
import click
from typing import Protocol



class LineItem(Protocol):
    def loadLineItem(self):
        ...


class Quantity():
  """Quantity class"""
  def __init__(self, amount: float = 0.0, quantifier: str = ""):
    self.amount = amount
    self.quantifier = quantifier

    def add_amount(amount):
        click.echo(f"added amount: {amount}, ")
    
    def add_quantifier(unit):
        click.echo(f"added unit: {unit}, ")

class Ingredient():
    """Ingredient class"""
    def __init__(self, ingredient: str = "", quantity: Quantity = Quantity()):
        self.ingredient = ingredient
        self.quantity = quantity

    def add_ingredient(recipe_name, ingredient):
        click.echo(f"added ingredient: {ingredient}, to {recipe_name}")


