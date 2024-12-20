# This file generated by Quarto; do not edit by hand.
# shiny_mode: core

from __future__ import annotations

from pathlib import Path
from shiny import App, Inputs, Outputs, Session, ui

import seaborn as sns
from shiny import reactive
from shiny.express import render, ui
penguins = sns.load_dataset("penguins")

# ========================================================================




def server(input: Inputs, output: Outputs, session: Session) -> None:
    species = list(penguins["species"].value_counts().index)
    ui.input_checkbox_group(
        "species", "Species:",
        species, selected = species
    )

    islands = list(penguins["island"].value_counts().index)
    ui.input_checkbox_group(
        "islands", "Islands:",
        islands, selected = islands
    )

    @reactive.calc
    def filtered_penguins():
        data = penguins[penguins["species"].isin(input.species())]
        data = data[data["island"].isin(input.islands())]
        return data

    # ========================================================================

    ui.input_select("dist", "Distribution:", choices=["kde", "hist"])
    ui.input_checkbox("rug", "Show rug marks", value = False)

    # ========================================================================

    @render.plot
    def depth():
        return sns.displot(
            filtered_penguins(), x = "bill_depth_mm",
            hue = "species", kind = input.dist(),
            fill = True, rug=input.rug()
        )

    # ========================================================================

    @render.plot
    def length():
        return sns.displot(
            filtered_penguins(), x = "bill_length_mm",
            hue = "species", kind = input.dist(),
            fill = True, rug=input.rug()
        )

    # ========================================================================

    @render.data_frame
    def dataview():
        return render.DataGrid(filtered_penguins())

    # ========================================================================



    return None


_static_assets = ["app4_files","app4_files/libs/quarto-html/tippy.css","app4_files/libs/quarto-html/quarto-syntax-highlighting-e26003cea8cd680ca0c55a263523d882.css","app4_files/libs/bootstrap/bootstrap-icons.css","app4_files/libs/bootstrap/bootstrap-842c6241243a9a56aff9413bcd96e60d.min.css","app4_files/libs/clipboard/clipboard.min.js","app4_files/libs/quarto-html/quarto.js","app4_files/libs/quarto-html/popper.min.js","app4_files/libs/quarto-html/tippy.umd.min.js","app4_files/libs/quarto-html/anchor.min.js","app4_files/libs/bootstrap/bootstrap.min.js"]
_static_assets = {"/" + sa: Path(__file__).parent / sa for sa in _static_assets}

app = App(
    Path(__file__).parent / "app4.html",
    server,
    static_assets=_static_assets,
)
