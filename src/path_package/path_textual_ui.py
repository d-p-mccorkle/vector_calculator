"""
This module comprises the UI for the Path app, writtem with Textual.
The layout will be annotated in the comments, but will consist of an 
input area for each vector alongside a menu for the operations desired,
and the output.
"""

#imports
from textual.app import App, ComposeResult
from textual.widgets import (
    Header, Digits, Input, Button, Static, RadioButton,
    Placeholder, Label,
)

from textual.containers import (
    Horizontal, Vertical, ItemGrid,
)

#body
#def make_hrznt_cnt(text: str, id: str, border_title: str) -> Container:
class VectorScreen(App):
    """A Textual app to manage the vector calculator"""

    #BINDINGS = 
    CSS_PATH = "../css/calc_style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(classes="cntnr") as hrznt_1:
            hrznt_1.border_title = "Vector: v"
            yield Input(placeholder="i")
            yield Input(placeholder="j")
            yield Input(placeholder="k")
        with ItemGrid(classes="cntnr", id="oprtns") as oprtns:
            oprtns.border_title = "Vector Operations"
            yield RadioButton("Add", classes="opr", id="add")
            yield RadioButton("Subtract", classes="opr", id="sub")
            yield RadioButton("Cross Product", classes="opr", id="cross")
            yield RadioButton("Dot Product", classes="opr", id="dot")
            yield RadioButton("Angle Between", classes="opr", id="ang_bet")
            yield RadioButton("Work", classes="opr", id="work")
        with Horizontal(classes="cntnr") as hrznt_2:
            hrznt_2.border_title = "Vector: u"
            yield Input(placeholder="i")
            yield Input(placeholder="j")
            yield Input(placeholder="k")
        with Horizontal(id="calc"):
            yield Button("Calculate", classes="equals", id="equals")

        # The following variable needs to be calculated and linked to
        # the app messages to display the output.  It needs to be
        # declared here.
        calc_output = "Vector:"

        lbl = Label(calc_output, classes="output", id="output")
        lbl.border_title = "Result"
        yield lbl


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
