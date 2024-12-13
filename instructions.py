import click

class Instruction():
    """Instruction class"""
    def __init__(self, instruction: str = "", step_num: int = 0):
        self.instruction = instruction
        self.step_num = step_num
