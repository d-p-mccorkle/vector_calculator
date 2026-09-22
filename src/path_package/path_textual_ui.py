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
    #CSS =

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            with Horizontal():
                yield Static()
                yield Input()
                yield Input()
                yield Input()
            with Horizontal():
                yield Button()
                yield Button()
                yield Button()
                yield Button()
            yield Button()
            with Horizontal():
                yield Static()
                yield Input()
                yield Input()
                yield Input()
            yield Button()
            yield Digits()



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
