import dash
from dash import html, dcc
from sqlalchemy import create_engine
import pandas as pd

# Datenbankverbindung
DATABASE_URL = "postgresql://postgres:your_password@db:5432/postgres"
engine = create_engine(DATABASE_URL)

# Beispiel-Daten
def fetch_data():
    query = "SELECT * FROM your_table LIMIT 10;"  # Ersetze 'your_table' mit deinem Tabellennamen
    with engine.connect() as connection:
        return pd.read_sql(query, connection)

# Dash-App initialisieren
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Dash Dashboard"),
    dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": ["A", "B", "C"], "y": [1, 2, 3], "type": "bar", "name": "Example"}
            ],
            "layout": {"title": "Simple Example"}
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
