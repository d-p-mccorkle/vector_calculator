"""
This module comprises the UI for the Path app, writtem with Textual.
The layout will be annotated in the comments, but will consist of an 
input area for each vector alongside a menu for the operations desired,
and the output.
"""

#imports
from textual.app import App, ComposeResult
from textual.widgets import (
        Header, Digits, Input, Button, Static,
)
from textual.containers import Horizontal, Vertical

#body
class VectorScreen(App):
    """A Textual app to manage the vector calculator"""

    #BINDINGS = 
    CSS_PATH = "../css/calc_style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("v:", classes="vec_inp", id="v")
        yield Input(placeholder="i")
        yield Input(placeholder="j")
        yield Input(placeholder="k")
        yield Button("Add", classes="opr", id="add")
        yield Button("Subtract", classes="opr", id="sub")
        yield Button("Cross Product", classes="opr", id="cross")
        yield Button("Dot Product", classes="opr", id="dot")
        yield Button("Angle Between", classes="opr", id="ang_bet")
        yield Button("Work", classes="opr", id="work")
        yield Static("u:", classes="vec_inp", id="u")
        yield Input(placeholder="i")
        yield Input(placeholder="j")
        yield Input(placeholder="k")
        yield Button("=", classes="opr", id="equals")
        yield Static("output", classes=output, id="output")



"""
v - i j k
operations: add sub cross dot angle
u - i j k
equals
output
"""

if __name__ == "__main__":
    app = VectorScreen()
    app.run()
