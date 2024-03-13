from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hi Melbourne')
])

if __name__ == '__main__':
    app.run(debug=True)