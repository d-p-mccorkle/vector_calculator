"""
This module comprises the UI for the Path app, writtem with Textual.
The layout will be annotated in the comments, but will consist of an 
input area for each vector alongside a menu for the operations desired,
and the output.
"""

#imports
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import (
    Header, Digits, Input, Button, Static, RadioButton,
    Placeholder, Label, RadioSet, Switch, Widget,
)

from textual.containers import (
    Horizontal, Vertical, ItemGrid,
)
from sympy.printing import pretty
#remember to prepend a from . when you get ready to wrap this up
import vector_math as vm

#body
#def make_hrznt_cnt(text: str, id: str, border_title: str) -> Container:
class Output(Widget):
    """
    Takes the given inputs, calculates the output and displays it.
    """
    vec_v = reactive(None)
    vec_u = reactive(None)
    theta = reactive(None)
    scalar = reactive(None)
    operation = reactive(None)
    #vec_out = reactive(None)

    def calc(self):
        """
        A method to operate on the given inputs based on the selected
        operation.
        """
        ops_dict = {
            "magsqr" : self.vec_v.vm.mag_square
            "mag" : self.vec_v.vm.magnitude
            "unit" : self.vec_v.vm.unit_vector
            "sclr" : self.vec_v.vm.scalar(
                self.scalar
            )
            "add" : vm.add_vectors(
                self.vec_v, self.vec_u
            )
            "sub" : vm.subtract_vectors(
                self.vec_v, self.vec_u
            )
            "cross" : vm.cross_product(
                self.vec_v, self.vec_u
            )
            "dot" : vm.dot(
                self.vec_v, self.vec_u
            )
            "ang_bet" : vm.angle_between(
                self.vec_v, self.vec_u
            )
            "work" : vm.work_by_angle(
                self.vec_v, self.vec_u, self.theta
            )
            "ortho" : vm.ortho_check(
                self.vec_v, self.vec_u
            )
            "proj" : vm.proj(
                self.vec_v, self.vec_u
            )
        }

        """ops_list = [
            magsqr, mag, unit, sclr, add, sub, cross, dot, ang_bet,
            work, ortho, proj
        ]
        """
        for k, v in ops_dict:
            if self.operation == k:
                out = v
        return out

    def disp_out(self):
        vec_out = self.calc()
        pretty_out = pretty(vec_out)
        return pretty_out

    def render(self):
        return f"{pretty_out}"


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
            yield Button("Store->v", classes="store", id="sto_v")
        with Horizontal(classes="cntnr") as hrznt_2:
            hrznt_2.border_title = "Vector: u"
            yield Input(placeholder="i", id="u_i")
            yield Input(placeholder="j", id="u_j")
            yield Input(placeholder="k", id="u_k")
            yield Button("Store->u", classes="store", id="sto_u")
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
