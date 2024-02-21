import dash
import dash_html_components as html

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Hello, World!')
])

if __name__ == '__main__':
    # Run the Dash app
    app.run_server(debug=True)
