"""Home page."""

from __future__ import annotations

from pathlib import Path

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

dash.register_page(__name__, path="/")

readme = Path(__file__).parent.absolute() / ".." / "README.md"

with open(readme, encoding="utf-8") as f:
    MARKDOWN_CONTENT = f.read()

MARKDOWN_CONTENT = "\n".join(MARKDOWN_CONTENT.split("\n")[2:])

jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("MatPES", className="display-3", id="matpes-title"),
            html.P(
                "A Foundational Potential Energy Surface Dataset for Materials.",
                className="lead",
            ),
            html.Hr(className="my-2"),
            dbc.Row(
                html.Div(
                    [
                        dbc.Button(
                            "PBE",
                            href="https://mavrl-web.s3.us-east-1.amazonaws.com/matpes/MatPES-PBE-2025.1.json.gz",
                            class_name="me-1 download-button",
                            color="info",
                            external_link=True,
                            size="lg",
                            id="pbe-download-button",
                        ),
                        dbc.Tooltip(
                            "Download PBE dataset (434,712 structures)",
                            target="pbe-download-button",
                            placement="bottom",
                        ),
                        dbc.Button(
                            "r2SCAN",
                            href="https://mavrl-web.s3.us-east-1.amazonaws.com/matpes/MatPES-r2SCAN-2025.1.json.gz",
                            class_name="me-1 download-button",
                            color="success",
                            external_link=True,
                            size="lg",
                            id="r2scan-download-button",
                        ),
                        dbc.Tooltip(
                            "Download r2SCAN dataset (387,897 structures)",
                            target="r2scan-download-button",
                            placement="bottom",
                        ),
                    ]
                ),
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-body-secondary rounded-3",
)


layout = dbc.Container(
    [
        jumbotron,
        dbc.Row(
            html.Div([dcc.Markdown(MARKDOWN_CONTENT)]),
            className="mt-4",
        ),
    ]
)
