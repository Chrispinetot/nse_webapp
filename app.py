# Import the libraries required
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output


# Initiating the application
app = Dash(__name__)
server = app.server
# Loading the data through pandas
data = pd.read_csv("./data.csv")
print(data.head())

app.title = "Nairobi Security Exchange Stock Prices"
app.description = "NSE Prices for Companies between October and November 2020"

# Designing the app layout
app.layout = html.Div([
    html.Link(rel='shortcut icon', type='favicon.ico', href="assets/nse.png"),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('nse.png'), id="ads-img", style={
                'height': '60px',
                'width': 'auto',
                'margin-bottom': '25px'
            })
        ], className='one-third column'),
        html.Div([
            html.Div([
                html.H2("NSE STOCK PRICES", style={'margin-bottom': '0px',
                                                   'color': 'white', "text-align": "center"}),
                html.H5("October 16th to November 29th", style={'margin-bottom': '0px', 'color': 'white',
                                                                "text-align": "center"})
            ])
        ], className="one-third column", id='title')
    ]),

    # Dropdown Layout

    html.Div([

        html.Div([
            html.Label("Select Company", style={"color": "white", "font-family": "Georgia, serif"}),
            dcc.Dropdown(
                id="select_ticker",
                options=[
                    {"label": "Absa Bank Kenya Plc", "value": "ABSA"},
                    {"label": "ARM Cement Limited", "value": "ARM"},
                    {"label": "Bamburi Cement Limited", "value": "BAMB"},
                    {"label": "British American Tobacco", "value": "BAT"},
                    {"label": "Crown Paints Kenya", "value": "BERG"},
                    {"label": "Bank of Kigali", "value": "BKG"},
                    {"label": "BOC Kenya", "value": "BOC"},
                    {"label": "Britam Holdings", "value": "BRIT"},
                    {"label": "Car and General Kenya", "value": "C&G"},
                    {"label": "East African Cables", "value": "CABL"},
                    {"label": "Carbacid Investments", "value": "CARB"},
                    {"label": "Stanbic Holdings", "value": "CFC"},
                    {"label": "Liberty Kenya Holdings", "value": "CFCI"},
                    {"label": "CIC Insurance Group", "value": "CIC"},
                    {"label": "Co-operative Bank", "value": "COOP"},
                    {"label": "Deacons East Africa", "value": "DCON"},
                    {"label": "Diamond Trust Bank", "value": "DTK"},
                    {"label": "East African Breweries", "value": "EABL"},
                    {"label": "Eaagads Limited", "value": "EGAD"},
                    {"label": "Equity Group Holdings", "value": "EQTY"},
                    {"label": "Eveready East Africa", "value": "EVRD"},
                    {"label": "STANLIB Fahari Income", "value": "FAHR"},
                    {"label": "Sameer Africa", "value": "FIRE"},
                    {"label": "Flame Tree Group Holdings", "value": "FTGH"},
                    {"label": "NewGold Exchange Traded Fund", "value": "GLD"},
                    {"label": "Home Afrika Limited", "value": "HAFR"},
                    {"label": "Housing Finance", "value": "HFCK"},
                    {"label": "I&M Holdings Plc", "value": "I&M"},
                    {"label": "Centum Investment", "value": "ICDC"},
                    {"label": "Jubilee Holdings Limited", "value": "JUB"},
                    {"label": "Kapchorua Tea Company Limited", "value": "KAPC"},
                    {"label": "KCB Bank Kenya Limited", "value": "KCB"},
                    {"label": "KENGEN", "value": "KEGN"},
                    {"label": "Kenya Re-Insurance", "value": "KNRE"},
                    {"label": "Kenya Power & Lighting", "value": "KPLC"},
                    {"label": "Kenya Power Pref. Shares at 4%", "value": "KPLC-P4"},
                    {"label": "Kenya Power Pref. Shares at 7%", "value": "KPLC-P7"},
                    {"label": "Kenya Airways Limited", "value": "KQ"},
                    {"label": "Kakuzi Limited", "value": "KUKZ"},
                    {"label": "Kurwitu Ventures Limited", "value": "KURV"},
                    {"label": "Limuru Tea Company Limited", "value": "LIMT"},
                    {"label": "Longhorn Publishers Limited", "value": "LKL"},
                    {"label": "Mumias Sugar Company Limited", "value": "MSC"},
                    {"label": "National Bank of Kenya Limited", "value": "NBK"},
                    {"label": "Nairobi Business Ventures Ltd", "value": "NBV"},
                    {"label": "NIC Bank Limited", "value": "NIC"},
                    {"label": "Nation Media Group", "value": "NMG"},
                    {"label": "Nairobi Securities Exchange", "value": "NSE"},
                    {"label": "Olympia Capital Holdings", "value": "OCH"},
                    {"label": "Kenya Orchards Limited", "value": "ORCH"},
                    {"label": "Sanlam Kenya Plc", "value": "PAFR"},
                    {"label": "East African Portland Cement", "value": "PORT"},
                    {"label": "Sasini Tea and Coffee Limited", "value": "SASN"},
                    {"label": "ScanGroup Limited", "value": "SCAN"},
                    {"label": "Standard Chartered Bank Limited", "value": "SCBK"},
                    {"label": "Safaricom Limited", "value": "SCOM"},
                    {"label": "Standard Group Limited", "value": "SGL"},
                    {"label": "Trans Century Limited", "value": "TCL"},
                    {"label": "Total Kenya Limited", "value": "TOTL"},
                    {"label": "TPS Eastern Africa (Serena)", "value": "TPSE"},
                    {"label": "Uchumi Supermarket Limited", "value": "UCHM"},
                    {"label": "Umeme Limited", "value": "UMME"},
                    {"label": "Unga Group Limited", "value": "UNGA"},
                    {"label": "Williamson Tea Kenya", "value": "WTK"},
                    {"label": "Express Kenya Limited", "value": "XPRS"}
                ],
                value="ABSA",
                multi=False,
                searchable=True,
                clearable=True,
                placeholder="click on dropdown or search"
            )
        ], className='card_container three columns')

    ], className="row flex display"),

    # End of Dropdown Section
    # dcc.Graph layout
    html.Div([
        html.Div([
            dcc.Graph(
                id='graph', config={'displayModeBar': False}
            ),
        ], className='card_container twelve columns')
    ], className='row flex display')

], id='mainContainer', style={'display': 'flex', 'flex-direction': 'column'}
)

# Callbacks


@app.callback(
    Output(component_id="graph", component_property="figure"),
    Input(component_id="select_ticker", component_property="value")
)
def enter_input(ticker):
    df = data.copy()
    df["price"] = df["price"].str.replace(",", "").astype("float")
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = df["date"].dt.strftime("%d/%m/%Y")
    df = df[(df["ticker"] == ticker)]
    fig = px.line(df, x="date", y="price")
    fig.update_layout(title_text=f"{ticker} Prices", title_x=0.5, font_family="Georgia, serif",
                      font_color="#0070ff", title_font_family="Georgia, serif", title_font_color="black",
                      legend_title_font_color="green")
    fig.update_xaxes(title_font_family="Georgia, serif")
    fig["data"][0]["line"]["color"] = "#ff6347"
    fig["data"][0]["line"]["width"] = 2

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
