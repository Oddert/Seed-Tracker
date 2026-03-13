from datetime import datetime

import dash
from dash import html, dcc
import plotly
import plotly.express as px
import pandas as pd


VALID_MONTHS = [
    'jan',
    'feb',
    'mar',
    'apr',
    'may',
    'jun',
    'jul',
    'aug',
    'sep',
    'oct',
    'nov',
    'dec',
]


def process_column(
    task_name: str, column_value: str | None, row: pd.Series
) -> dict | None:
    """Parse a single cell value from the spreadsheet and return a row
    suitable for the gantt-chart dataframe.
    """
    if column_value is None or not isinstance(column_value, str):
        return None

    ranges = [segment.strip() for segment in column_value.split(',')]

    for pair in ranges:
        if '-' in pair:
            start_str, end_str = pair.split('-')
            start_month_str = start_str.strip()[:3].lower()
            end_month_str = end_str.strip()[:3].lower()
        else:
            start_month_str = pair.strip()[:3].lower()
            end_month_str = 'dec'

        if start_month_str not in VALID_MONTHS:
            # skip invalid rows silently; original script logged to stdout
            continue

        if end_month_str not in VALID_MONTHS:
            end_month_str = 'dec'

        start_parsed = datetime.strptime(f'01 {start_month_str} 2026', '%d %b %Y')
        end_parsed = datetime.strptime(f'28 {end_month_str} 2026', '%d %b %Y')

        return {
            'Task': task_name,
            'Start': start_parsed,
            'Finish': end_parsed,
            'Resource': row['Name'],
        }
    return None


def make_figure(
    selected_categories: list[str] | None = None,
) -> plotly.graph_objs._figure.Figure:
    """Read the CSV file and return a Plotly timeline figure.

    If `selected_categories` is provided, only rows whose "Cattegory" value
    is in the list will be included.
    """
    csv_df = pd.read_csv('./seed-tracker.csv')

    # apply category filter early to reduce work
    if selected_categories is not None:
        csv_df = csv_df[csv_df['Cattegory'].isin(selected_categories)]

    rows_list: list[dict] = []

    groups = [
        {'label': 'Sow Indoors', 'column': 'Sow Indoors'},
        {'label': 'Sow Outdoors', 'column': 'Sow Outdoors'},
        {'label': 'Plant Out', 'column': 'Plant Out'},
        {'label': 'Harvest', 'column': 'Harvest'},
        {'label': 'Flowers', 'column': 'Flowers'},
    ]

    for _, row in csv_df.iterrows():
        for group in groups:
            processed = process_column(group['label'], row[group['column']], row)
            if processed is not None:
                rows_list.append(processed)

    df = pd.DataFrame(rows_list)
    df.sort_values(by=['Resource', 'Start'], ascending=False, inplace=True)

    fig = px.timeline(df, x_start='Start', x_end='Finish', y='Resource', color='Task')
    fig.update_layout(bargroupgap=0.1, bargap=0.2)
    fig.update_xaxes(
        tickmode='linear',
        dtick='M1',
        tickformat='%b',
        range=[datetime(2026, 1, 1), datetime(2026, 12, 31)],
    )
    return fig


app = dash.Dash(__name__)

# read the CSV once to populate filter options
_initial_csv = pd.read_csv('./seed-tracker.csv')
_category_options = sorted(_initial_csv['Cattegory'].dropna().unique().tolist())

app.layout = html.Div(
    [
        html.H1('Seed Tracker Gantt Chart'),
        dcc.Dropdown(
            id='category-filter',
            options=[{'label': c, 'value': c} for c in _category_options],
            value=_category_options.copy(),  # select all by default
            multi=True,
            placeholder='Filter by category',
            style={'width': '300px', 'margin-bottom': '1rem'},
        ),
        dcc.Graph(id='gantt', figure=make_figure()),
    ]
)


# callback to update figure when categories change
@app.callback(
    dash.dependencies.Output('gantt', 'figure'),
    [dash.dependencies.Input('category-filter', 'value')],
)
def update_figure(selected_categories):
    # if the dropdown is cleared, show nothing
    if not selected_categories:
        return px.timeline(
            pd.DataFrame([]), x_start='Start', x_end='Finish', y='Resource'
        )

    return make_figure(selected_categories)


if __name__ == '__main__':
    # use the modern `run` method; `run_server` is deprecated/removed
    app.run(debug=True)
