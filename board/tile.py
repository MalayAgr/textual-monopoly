from enums import Color, Icon, Position
from rich.console import Console, ConsoleOptions
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from textual.widget import Widget


class Tile(Widget):
    def __init__(
        self,
        text: str,
        position: Position,
        value: int = None,
        pay: bool = False,
        icon: Icon = None,
        color: Color = None,
    ) -> None:
        self.text = text
        self.position = position
        self.value = value
        self.pay = pay
        self.icon = icon
        self.color = color

    def render(self) -> Panel:
        grid = Table.grid(expand=True)

        grid.add_column(justify="center")

        if self.color is not None:
            cell = Text(" " * 10, style=f"on {self.color.value}")
            grid.add_row(cell)

        cell = Text(self.text.upper(), style="bold")
        grid.add_row(cell)

        if self.icon is not None:
            grid.add_row(f":{self.icon.value}:")

        if self.value is not None:
            value = f"Pay ${self.value}" if self.pay is True else f"${self.value}"

            grid.add_row(Text(value, style="bold"))

        return Panel(grid)
