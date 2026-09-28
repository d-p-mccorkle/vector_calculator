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
    Placeholder, Label, RadioSet, Switch,
)

from textual.containers import (
    Horizontal, Vertical, ItemGrid,
)

#body
#def make_hrznt_cnt(text: str, id: str, border_title: str) -> Container:
class Vector_Calculator(App):
    """A Textual app to manage the vector calculator"""

    #BINDINGS = 
    CSS_PATH = "../css/calc_style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(classes="cntnr") as hrznt_1:
            hrznt_1.border_title = "Vector: v"
            yield Input(placeholder="i", id="v_i")
            yield Input(placeholder="j", id="v_j")
            yield Input(placeholder="k", id="v_k")
        with Horizontal(classes="cntnr") as hrznt_2:
            hrznt_2.border_title = "Vector: u"
            yield Input(placeholder="i", id="u_i")
            yield Input(placeholder="j", id="u_j")
            yield Input(placeholder="k", id="u_k")
        with RadioSet(classes="cntnr_rad", id="oprtns_2") as oprtns:
            oprtns.border_title = "Vector Operations"
            yield RadioButton("Add", id="add")
            yield RadioButton("Subtract", id="sub")
            yield RadioButton("Cross Product", id="cross")
            yield RadioButton("Dot Product", id="dot")
            yield RadioButton("Angle Between", id="ang_bet")
            yield RadioButton("Work", id="work")
            yield RadioButton("Orthogonal", id="ortho")
            yield RadioButton("Projection v->u", id="proj")
        with RadioSet(classes="cntnr_rad", id="oprtns_1") as oprtns_1:
            oprtns_1.border_title = "Single Vector Operations"
            oprtns_1.border_subtitle = "Performed on v"
            yield RadioButton("Magnitude", id="mag")
            yield RadioButton("Magnitude Squared", id="magsqr")
            yield RadioButton("Unit Vector", id="unit")
            yield RadioButton("Scalar Multiplication", id="sclr")
        with Horizontal(classes="cntnr", id="theta_scal") as theta_scal:
            theta_scal.border_title = "Theta"
            theta_scal.border_subtitle = "Scalar"
            yield Input(placeholder="Theta (rad)", id="theta")
            yield Input(placeholder="Scalar", id="scalar")

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
    app = Vector_Calculator()
    app.run()
