#!/usr/bin/env python

"""
Simple browser for the mastodon-snap postgres database

requirements:
  psycopg2-binary
  textual
"""

from textual.app import App
from textual.widgets import Header, Footer, Static, DataTable, Select, Button
from textual.binding import Binding
from textual.events import Key
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive

import psycopg2
import psycopg2.extras


class VIDataTable(DataTable):
    BINDINGS = [
        Binding("k", "cursor_up", "Cursor up", show=True),
        Binding("j", "cursor_down", "Cursor down", show=True),
        Binding("l", "cursor_right", "Cursor right", show=True),
        Binding("h", "cursor_left", "Cursor left", show=True),
        Binding("g", "scroll_top", "Scroll top", show=True),
        Binding("G", "scroll_bottom", "Scroll bottom", show=True),
    ]

class MastodonSnapPGClient:
    def __init__(
        self,
        dbname="mastodon",
        user="mastodon",
        host="/tmp/snap-private-tmp/snap.mastodon-server/tmp/sockets/postgres",
        password_file="/var/snap/mastodon-server/common/secrets/postgres",
    ):
        with open(password_file, "r") as password:
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password.read(),
                host=host,
                cursor_factory=psycopg2.extras.DictCursor,
            )

    def list_tables(self):

        cur = self.conn.cursor()
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema='public'
            ORDER BY table_name;
        """)

        return [row[0] for row in cur.fetchall()]

    def fetch_table(self, table_name):
        cur = self.conn.cursor()
        cur.execute(f'SELECT * FROM "{table_name}";')
        colnames = [desc.name for desc in cur.description]
        rows = cur.fetchall()

        return colnames, rows


class PGBrowser(App):
    CSS = """
    Screen {
        layout: horizontal;
    }
    #sidebar {
        width: 30%;
        border: solid #666;
        layout: vertical;
    }
    #main {
        width: 70%;
        border: solid #666;
    }
    """

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
    ]

    selected_table = reactive("")

    def __init__(self, pg_client):
        super().__init__()
        self.pg = pg_client

    def compose(self):
        yield Header()

        with Horizontal():
            with Vertical(id="sidebar"):
                yield Static("Tables")
                self.table_list = Select(id="table_list", options=[], allow_blank=True)
                yield self.table_list

            with Vertical(id="main"):
                self.data_table = VIDataTable(id="data_table")
                yield self.data_table

        yield Footer()

    def on_mount(self, event):
        tables = self.pg.list_tables()

        if tables:
            self.table_list.set_options([(t, t) for t in tables])
        else:
            self.table_list.set_options([])

        self.table_list.refresh()

    def on_select_changed(self, event):
        if event.value in [None, Select.BLANK]:
            return
        if event.value:
            self._load_table(event.value)

    def _clear_table(self):
        self.data_table.clear(columns=True)

    def _load_table(self, table_name):
        self._clear_table()

        cols, rows = self.pg.fetch_table(table_name)
        self.data_table.add_columns(*cols)
        for row in rows:
            self.data_table.add_row(*[str(v) for v in row])


if __name__ == "__main__":
    pg = MastodonSnapPGClient()
    app = PGBrowser(pg)
    app.run()
