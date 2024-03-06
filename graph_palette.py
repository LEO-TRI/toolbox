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

def charter_plotly(fig: go.Figure, width: int=1000, height: int=600, title_place: float=0.3) -> go.Figure:
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

    Returns
    -------
    go.Figure
        A formated plot
    """
    fig.update_xaxes(
        title_font=dict(size=24, family="FuturaTOT", color=DARK_GREY[1]),
        title_font_family="FuturaTOT",
        color=DARK_GREY[2],
        linecolor=DARK_GREY[2],
        tickfont=dict(size=12),
        showgrid=False,
    )
    fig.update_yaxes(
        title_font=dict(size=24, family="FuturaTOT", color=DARK_GREY[1]),
        title_font_family="FuturaTOT",
        color=DARK_GREY[2],
        linecolor=DARK_GREY[2],
        tickfont=dict(size=12),
        showgrid=False,
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        width=width,
        height=height,
        title=dict(
            x=title_place, font=dict(family="FuturaTOT", size=28, color=DARK_GREY[1]),
        ),
        legend=dict(font=dict(family="FuturaTOT", size=24, color=DARK_GREY[1],)),
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
    plt.rcParams["font.family"] = "FuturaTOT"
    
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