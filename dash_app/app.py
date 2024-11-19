import dash
from dash import html

# Dash-App initialisieren
app = dash.Dash(__name__)

# Layout der App definieren
app.layout = html.Div([
    html.H1("Hallo, Dash!"),
    html.P("Dies ist eine einfache Dash-Anwendung.")
])

# Server starten
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
