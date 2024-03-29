import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# color constants and palettes
#TODO: Change the color palette to T&E + fonts

CORAL = ["#D94535", "#ed8a84", "#f3b1ad", "#f9d8d6"]
DARK_GREY = ["#323C46", "#77949d", "#a4b7be", "#d2dbde"]
STONE = ["#7d8791", "#a5aaaa", "#d2d2d2", "#ebebeb"]
BLUE_GREY = ["#94b7bb", "#bfd4d6", "#d4e2e4", "#eaf1f1"]
BROWN = ["#7a6855", "#b4a594", "#cdc3b8", "#e6e1db"]
PURPLE = ["#8d89a5", "#bbb8c9", "#d1d0db", "#e8e7ed"]

FULL_PALETTE = np.vstack([CORAL, DARK_GREY, STONE, BLUE_GREY, BROWN, PURPLE]) #Artificial extension of the palette table for repetition 

PALETTE = dict(CYAN = "#00AEEF",
                GREEN = " #41AD49",
                BLUE = "#2A6ED1",
                DARK_GREEN = "#364951",
                STONE = "#F5F5F3",
                )

def charter_TandE_plotly(fig: go.Figure, 
                         width: int=1000, 
                         height: int=600, 
                         title_place: float=0.3,
                         make_title_bold: bool=True) -> go.Figure:
    """
    Formatting a plotly plot, can be made with go/px as long as it is a go.Figure object
    
    Need to be used AFTER producing the plot. All the modifications are inplace.

    Parameters
    ----------
    fig : go.Figure
        The figure to format
    width : int, optional
        The width to resize the graph, by default 1000
    height : int, optional
        The height to resize the graph, by default 600
    title_place : float, optional
        Where to put the title, by default 0.3
    make_title_bold : bool, optional
        Whether to make the title bold

    Returns
    -------
    go.Figure
        A formated plot
    """

    y_axis_title = fig.layout.yaxis.title["text"] 
    if not (y_axis_title is None):
        y_axis_title = "".join((y_axis_title[0].upper(), y_axis_title[1:])) if (len(y_axis_title) > 0) else "Value"
    
    x_axis_title = fig.layout.xaxis.title["text"] 
    if not (x_axis_title is None):
        x_axis_title = "".join((x_axis_title[0].upper(), x_axis_title[1:])) if (len(x_axis_title) > 0) else "Value"

    default_name = "Variables" if (len(fig.data) > 1) else 'Variable'

    legend_title = fig.layout.legend.title["text"]
    if not (legend_title is None):
        legend_title = "".join((legend_title[0].upper(), legend_title[1:])) if (len(legend_title) > 0) else default_name #NOTE Breakdown the string and capitalize each word

    title = fig.layout.title.text
    if (make_title_bold is True) & (not (title is None)):
        if not (("<b>" in title) & ("</b>" in title)):
            title = "".join(("<b>", title, "</b>")) #If the title is not bold, make bold

    fig.update_xaxes(
        title_font=dict(size=20, family="Raleway", color=PALETTE["DARK_GREEN"]),
        title_font_family="Raleway",
        title_text = x_axis_title,
        color=DARK_GREY[2],
        linecolor=DARK_GREY[2],
        zerolinecolor = 'rgba(0,0,0,0)',
        tickfont=dict(color="#323C46", size=12, family="Raleway"),
        title_standoff = 25,
        showgrid=False,
    )
    fig.update_yaxes(
        title_font=dict(size=20, family="Raleway", color=PALETTE["DARK_GREEN"]),
        title_font_family="Raleway",
        title_text = y_axis_title,
        color=DARK_GREY[2],
        linecolor=DARK_GREY[2],
        zerolinecolor = 'rgba(0,0,0,0)',
        tickfont=dict(color="#323C46", size=12, family="Raleway"),
        title_standoff = 5,
        showgrid=False,
    )
    fig.update_layout(
        paper_bgcolor='#eaf1f1',#"rgba(245,245,243,1)", #A9A9A9	Dark Gray
        plot_bgcolor= '#eaf1f1', #"rgba(245,245,243,1)",
        width=width,
        height=height,
        title=dict(x=title_place, 
                   text = title,
                   font=dict(family="Raleway", size=24, color=PALETTE["DARK_GREEN"]),
                   xanchor ='center'
                   ),
        legend=dict(title_font_family="Raleway", 
                    font=dict(family="Raleway", size=16, color=PALETTE["DARK_GREEN"]), 
                    title_text = legend_title
                    ),
    )

    return fig

def charter_graph(width: int=12, length: int=8) -> plt.Figure:
    """
    Formatting a matplotlib/seaborn plot. 
    
    Needs to be used BEFORE making the plot. 

    Parameters
    ----------
    width : int, optional
        The width of the plot, by default 12
    length : int, optional
        The length of the plot, by default 8

    Returns
    -------
    plt.Figure
        The formatted figure on which you can produce a plot
    """
    
    fig, ax = plt.subplots()
    fig.set_size_inches(width, length)
    
    plt.rcParams.update({"font.size": 12})
    plt.rcParams["font.family"] = "Raleway"
    
    ax.patch.set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_color(DARK_GREY[1])
    ax.spines["left"].set_color(DARK_GREY[1])
    ax.tick_params(colors=DARK_GREY[1])
    
    # ax.tick_params(axis='x', labelrotation=90)
    ax.spines["bottom"].set_color(DARK_GREY[2])
    ax.spines["left"].set_color(DARK_GREY[2])
    
    return fig, ax
