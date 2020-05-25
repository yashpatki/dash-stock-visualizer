import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H2(children="""Symbol to graph:     """),
        dcc.Input(id="input", value="", type="text"),
        html.Div(
        children=[
        html.H2(children="""Select Dates:"""),    
        dcc.DatePickerRange(
        id='date-picker-range',
        start_date_placeholder_text='Start date',
        end_date_placeholder_text='End date',
        start_date='',
        end_date=''
    )]),
        html.Div(id="output-graph"),
    ]
)


@app.callback(
    Output(component_id="output-graph", component_property="children"),
    [Input(component_id="input", component_property="value"),
    Input(component_id="date-picker-range", component_property="start_date"),
    Input(component_id="date-picker-range", component_property="end_date")]
)
def update_value(input_data, start_date, end_date):
    #start = datetime.datetime(2015, 1, 1)
    start = start_date
    end = end_date
    df = web.DataReader(input_data, "yahoo", start, end)

    return dcc.Graph(
        id="example-graph",
        figure={
            "data": [
                {"x": df.index, "y": df.Close, "type": "line", "name": input_data},
            ],
            "layout": {"title": input_data},
        },
    )


if __name__ == "__main__":
    app.run_server(debug=True)
