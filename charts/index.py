from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
# import squarify 
import seaborn as sns
import plotly.express as px


def groupBarChart(newWindow, title, data, x, ylabel, legend):
    fig, ax = plt.subplots(nrows=1, figsize=(10, 10), sharex=True)
    ax.set(title=title)
    data.plot.bar( x=x, stacked=False, ax=ax)
    for label in ax.get_xticklabels():
        label.set_rotation(0)

    ax.set(ylabel=ylabel)
    ax.legend(legend)
    
    canvas = FigureCanvasTkAgg(fig, master=newWindow)
    canvas.draw()
    
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, newWindow)
    toolbar.update()
    toolbar.pack(side=TOP, fill=X)

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
    
def simplePlot(newWindow, title, firstRegionData, secondRegionData):

    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(firstRegionData, firstRegionData, label='linear')  # Plot some data on the axes.
    ax.plot(firstRegionData, secondRegionData, label='quadratic')  # Plot more data on the axes...
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title(title)  # Add a title to the axes.
    ax.legend();  # Add a legend.
    
    canvas = FigureCanvasTkAgg(fig, master=newWindow)
    canvas.draw()
    
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, newWindow)
    toolbar.update()
    toolbar.pack(side=TOP, fill=X)

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH) 
    
def horizontalBarChart(newWindow, data, groupLabel):    
    plt.rcParams.update({'figure.autolayout': True})
    
    fig, ax = plt.subplots()
    ax.barh(groupLabel, data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    
    canvas = FigureCanvasTkAgg(fig, master=newWindow)
    canvas.draw()
    
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, newWindow)
    toolbar.update()
    toolbar.pack(side=TOP, fill=X)
    
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH) 
    
def lineChart(newWindow, title, plotTitleOne, plotTitleTwo, data, x, y, ax0Legend, plotLabel1, plotLabel2, ylabel, legends):
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), sharex=True)
      
    fig.suptitle(title)
    
    ax0.set(title=plotTitleOne)
    ax1.set(title=plotTitleTwo)

    data.plot.area( x=x, y=y, stacked=False, ax=ax0)
    ax0.set(ylabel="Cases")
    ax0.legend([ax0Legend])
    # ["date", "newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+"]

    data[[x, plotLabel1 , plotLabel2]].plot.area(x=x, stacked=False, ax=ax1)
    
    ax1.set(ylabel=ylabel)
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, legends)

    canvas = FigureCanvasTkAgg(fig, master=newWindow)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, newWindow)
    toolbar.update()
    toolbar.pack(side=TOP, fill=X)
    
def TreeMap(newWindow, df, path, values,
            # size, labels
        ):
    
    colors=['#fae588','#f79d65','#f9dc5c','#e8ac65','#e76f51','#ef233c','#b7094c'] #color palette
    # sns.set_style(style="whitegrid") # set seaborn plot style
    # sizes= size
    # label= labels
    # squarify.plot(sizes=sizes, label=label, alpha=0.6,color=colors).set(title='Treemap with Squarify')
    # plt.axis('off')
    # mng = plt.get_current_fig_manager()
    # mng.full_screen_toggle()
    # plt.show()
    
    fig = px.treemap(df, path=path,values=values, width=800, height=400)
    fig.update_layout(
        treemapcolorway = colors, #defines the colors in the treemap
        margin = dict(t=50, l=25, r=25, b=25))
    # fig.show()
    canvas = FigureCanvasTkAgg(fig, master=newWindow)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, newWindow)
    toolbar.update()
    toolbar.pack(side=TOP, fill=X)