from shiny import App, ui, reactive
import os
from pathlib import Path

html =  Path(__file__).parent / "www" / "index.html"


app_ui = ui.page_fluid(
    ui.HTML(html),
)

app = App(app_ui, server=None)

