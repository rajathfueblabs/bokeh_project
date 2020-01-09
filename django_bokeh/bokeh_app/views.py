from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap

# Create your views here.
def home(request):

    x = [1,2,3,4,5,6,7]
    y = [1,3,2,5,4,7,6]

    plot = figure(title="Line Graph", x_axis_label='X-Axis', y_axis_label='Y-Axis',plot_height=300,plot_width=400)
    plot.line(x,y,line_width=2)
    plot.toolbar.logo = None
    plot.sizing_mode = "scale_width"
    script1,div1 = components(plot)
    # print(script)
    # print(div)

    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    years = ['2015','2016','2017']

    data = {
                'fruits': fruits,
                '2015': [2,1,4,3,2,4],
                '2016': [5,4,3,2,4,6],
                '2017': [3,2,4,4,5,3]
            }
    x_values = [(fruit, year) for fruit in fruits for year in years ]
    counts = sum(zip(data['2015'], data['2016'], data['2017']), ())

    source = ColumnDataSource(data=dict(x=x_values, counts=counts))
    plot2 = figure(x_range=FactorRange(*x_values), title="Fruit Counts by year")
    plot2.vbar(x='x', top='counts', width=0.9, source=source, line_color="white", fill_color=factor_cmap('x',palette=Spectral6, factors=years, start=1, end=2))

    plot2.y_range.start = 0
    plot2.x_range.range_padding = 0.1
    plot2.xaxis.major_label_orientation = 1
    plot2.xgrid.grid_line_color = None
    plot2.sizing_mode = "scale_width"

    script2, div2 = components(plot2)
    return render_to_response('base.html',{'script1':script1,'div1':div1, 'script2':script2, 'div2':div2 })
