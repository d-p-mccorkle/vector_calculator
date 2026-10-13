"""
This module comprises the UI for the Path app, writtem with Textual.
The layout will be annotated in the comments, but will consist of an 
input area for each vector alongside a menu for the operations desired,
and the output.
"""

#imports
from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import (
    Header, Digits, Input, Button, Static, RadioButton,
    Placeholder, Label, RadioSet, Switch,
)
from textual.widget import Widget
from textual.containers import (
    Horizontal, Vertical, ItemGrid,
)
from sympy.printing import pretty
#remember to prepend a from . when you get ready to wrap this up
import vector_math as vm

#body
#def make_hrznt_cnt(text: str, id: str, border_title: str) -> Container:
"""class Output(Widget):
    Takes the given inputs, calculates the output and displays it.
    vec_v = reactive(None)
    vec_u = reactive(None)
    theta = reactive(None)
    scalar = reactive(None)
    operation = reactive(None)
    #vec_out = reactive(None)

    def calc(self):
        A method to operate on the given inputs based on the selected
        operation.
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

        ops_list = [
            magsqr, mag, unit, sclr, add, sub, cross, dot, ang_bet,
            work, ortho, proj
        ]
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
"""

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
            yield Button("Store->v", classes="store", id="store_v")

        with Horizontal(classes="cntnr") as hrznt_2:
            hrznt_2.border_title = "Vector: u"
            yield Input(placeholder="i", id="u_i")
            yield Input(placeholder="j", id="u_j")
            yield Input(placeholder="k", id="u_k")
            yield Button("Store->u", classes="store", id="store_u")

        with ItemGrid(classes="cntnr_ops", id="oprtns_2") as oprtns:
            oprtns.border_title = "Vector Operations"
            yield Button(
                "Add", classes="op2_but", id="add"
            )
            yield Button(
                "Subtract", classes="op2_but", id="sub"
            )
            yield Button(
                "Cross Product", classes="op2_but", id="cross"
            )
            yield Button(
                "Dot Product", classes="op2_but", id="dot"
            )
            yield Button(
                "Angle Between", classes="op2_but", id="ang_bet"
            )
            yield Button(
                "Work", classes="op2_but", id="work"
            )
            yield Button(
                "Orthogonal", classes="op2_but", id="ortho"
            )
            yield Button(
                "Projection v->u", classes="op2_but", id="proj"
            )

        with ItemGrid(classes="cntnr_ops", id="oprtns_1") as oprtns_1:
            oprtns_1.border_title = "Single Vector Operations"
            oprtns_1.border_subtitle = "Performed on v"
            yield Button(
                "Magnitude", classes="op1_but", id="mag"
            )
            yield Button(
                "Magnitude Squared", classes="op1_but", id="magsqr"
            )
            yield Button(
                "Unit Vector", classes="op1_but", id="unit"
            )
            yield Button(
                "Scalar Multiplication", classes="op1_but", id="sclr"
            )

        with Horizontal(classes="cntnr", id="theta_scal") as theta_scl:
            theta_scl.border_title = "Theta"
            theta_scl.border_subtitle = "Scalar"
            yield Input(placeholder="Theta (rad)", id="theta")
            yield Input(placeholder="Scalar", id="scalar")

        with Horizontal(classes="cntnr", id="test") as test:
            test.border_title = "TEST"
            test.border_subtitle = "TEST"
            yield Static(id="test_wid")

    display = self.query_one("#test_wid", Static)

    @on(Button.Pressed, "#store_v")
    def store_v(self):
        """A method to store the v inputs and generate a v vector."""
        v_i = float(self.query_one("#v_i", Input).value)
        v_j = float(self.query_one("#v_j", Input).value)
        v_k = float(self.query_one("#v_k", Input).value)
        self.vector_v = vm.Vector(
            "v",
            v_i,
            v_j,
            v_k
        )

    @on(Button.Pressed, "#store_u")
    def store_u(self):
        """A method to store the u inputs and generate a u vector."""
        u_i = float(self.query_one("#u_i", Input).value)
        u_j = float(self.query_one("#u_j", Input).value)
        u_k = float(self.query_one("#u_k", Input).value)
        self.vector_u = vm.Vector(
            "u",
            u_i,
            u_j,
            u_k
        )

    @on(Button.Pressed, "#add")
    def add(self):
        self.added_vecs = vm.add_vectors(self.vector_v, self.vector_u)
        display.update(f"{self.added_vecs}")

    @on(Button.Pressed, "#sub")
    def sub(self):
        self.subbed_vecs = vm.subtract_vectors(
            self.vector_v, self.vector_u
        )
        display.update(f"{self.subbed_vecs}")

    @on(Button.Pressed, "#cross")
    def cross(self):
        self.cross_prod = vm.cross_product(
            self.vector_v, self.vector_u
        )
        display.update(f"{self.cross_prod}")

    @on(Button.Pressed, "#dot")
    def dot(self):
        self.dot_prod = vm.dot(self.vector_v, self.vector_u)
        dot_disp = "v"+"\u22C5"+"u ="+" "+f"{self.dot_prod}"
        display.update(f"{dot_disp}")

    @on(Button.Pressed, "#ang_bet")
    def ang_bet(self):
        self.ang_bet = vm.angle_between(
            self.vector_v, self.vector_u
        )
        display.update(f"{self.ang_bet}")

    @on(Button.Pressed, "#work")
    def work(self):
        theta = float(self.query_one("#theta", Input).value)
        self.work = vm.work_by_dot(
            self.vector_v, self.vector_u, theta
        )
        display.update(f"{self.work}")

    @on(Button.Pressed, "#ortho")
    def ortho(self):
        self.ortho = vm.ortho_check(self.vector_v, self.vector_u)
        ortho_true = "The vectors v and u are orthoganal."
        ortho_false = "The vectors v and u are not orthoganal."
        ortho_out = ortho_true if self.ortho else ortho_false
        display.update(f"{ortho_out}")

    @on(Button.Pressed, "#proj")
    def proj(self):
        self.proj = vm.proj(self.vector_v, self.vector_u)
        display.update(f"{self.proj}")

    @on(Button.Pressed, "#mag")
    def mag(self):
        self.mag = self.vector_v.magnitude()
        display.update(f"{self.mag}")

    @on(Button.Pressed, "#magsqr")
    def magsqr(self):
        self.magsqr = self.vector_v.mag_square()
        display.update(f"{self.magsqr}")

    @on(Button.Pressed, "#unit")
    def unit(self):
        self.unit = self.vector_v.unit_vector()
        display.update(f"{self.unit}")

    @on(Button.Pressed, "#sclr")
    def sclr(self):
        scalar_mult = float(self.query_one("#scalar", Input).value)
        self.vector_v.scalar(scalar_mult)
        display.update(f"{self.vector_v}")

if __name__ == "__main__":
    app = Vector_Calculator()
    app.run()
