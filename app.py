"""Main app."""

from __future__ import annotations

import argparse

import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html

app = Dash(
    "MatPES",
    use_pages=True,
    external_stylesheets=[dbc.themes.DARKLY],
    title="MatPES",
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.Nav(
            [
                html.Img(src=dash.get_asset_url("logo.svg"), alt="MatPES", id="header-logo"),
                dbc.NavbarBrand("MatPES.ai", className="ms-2"),
                dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
                dbc.NavItem(dbc.NavLink("Explorer", href="/explorer", active="exact")),
                dbc.NavItem(dbc.NavLink("Dataset", href="/dataset", active="exact")),
                dbc.NavItem(dbc.NavLink("Benchmarks", href="/benchmarks", active="exact")),
                dbc.NavItem(
                    dbc.ButtonGroup(
                        [
                            dbc.Button("PBE", href="matpes_pbe.json.gz", color="danger"),
                            dbc.Button("r2SCAN", href="matpes_r2scan.json.gz", color="warning"),
                        ],
                        className="me-1",
                    ),
                ),
            ],
        ),
    ],
    color="primary",
    dark=True,
    links_left=True,
)

content = html.Div(children=dash.page_container, id="page-content")

app.layout = html.Div([dcc.Location(id="url"), navbar, content])

server = app.server


def main():
    """Main entry point for MatPES Webapp."""
    parser = argparse.ArgumentParser(
        description="""MatPES.ai is a Dash Interface for MatPES.""",
        epilog="Author: Shyue Ping Ong",
    )

    parser.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        help="Whether to run in debug mode.",
    )
    parser.add_argument(
        "-hh",
        "--host",
        dest="host",
        type=str,
        nargs="?",
        default="0.0.0.0",
        help="Host in which to run the server. Defaults to 0.0.0.0.",
    )
    parser.add_argument(
        "-p",
        "--port",
        dest="port",
        type=int,
        nargs="?",
        default=8050,
        help="Port in which to run the server. Defaults to 8050.",
    )

    args = parser.parse_args()

    app.run(debug=args.debug, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
