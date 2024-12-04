from django.shortcuts import render
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
import numpy as np

def finance_dashboard_view(request):
    # Load CSV data
    csv_file = "csv_data/apple_stock.csv"
    data = pd.read_csv(csv_file)

    # Candlestick Chart
    candlestick_chart = go.Figure(data=[go.Candlestick(
        x=data['Date'],
        open=data['AAPL.Open'],
        high=data['AAPL.High'],
        low=data['AAPL.Low'],
        close=data['AAPL.Close']
    )])
    candlestick_chart.update_layout(title='Apple Stock Candlestick Chart', xaxis_title='Date', yaxis_title='Price')
    candlestick_div = plot(candlestick_chart, output_type='div')

    # Line Chart for Moving Average
    line_chart = go.Figure()
    line_chart.add_trace(go.Scatter(x=data['Date'], y=data['mavg'], mode='lines', name='Moving Average'))
    line_chart.update_layout(title='Apple Stock Moving Average', xaxis_title='Date', yaxis_title='Price')
    line_chart_div = plot(line_chart, output_type='div')

    # Volume Bar Chart
    volume_chart = go.Figure()
    volume_chart.add_trace(go.Bar(x=data['Date'], y=data['AAPL.Volume'], name='Volume'))
    volume_chart.update_layout(title='Apple Stock Volume', xaxis_title='Date', yaxis_title='Volume')
    volume_chart_div = plot(volume_chart, output_type='div')

    # Pie Chart for Direction
    direction_counts = data['direction'].value_counts()
    pie_chart = go.Figure(data=[go.Pie(
        labels=direction_counts.index,
        values=direction_counts.values,
        hole=0.3  # Optional: Donut chart style
    )])
    pie_chart.update_layout(title='Price Direction Distribution')
    pie_chart_div = plot(pie_chart, output_type='div')

    # Scatter Plot
    scatter_chart = px.scatter(data, x='AAPL.Open', y='AAPL.Close', color='direction',
                                title='Scatter Plot: Open vs Close Prices',
                                labels={'AAPL.Open': 'Opening Price', 'AAPL.Close': 'Closing Price'})
    scatter_chart_div = plot(scatter_chart, output_type='div')

    # Histogram
    histogram_chart = px.histogram(data, x='AAPL.Close', nbins=20,
                                    title='Histogram of Closing Prices',
                                    labels={'AAPL.Close': 'Closing Price'})
    histogram_chart_div = plot(histogram_chart, output_type='div')

    # Box Plot
    box_chart = px.box(data, y='AAPL.Close', points='all',
                       title='Box Plot of Closing Prices',
                       labels={'AAPL.Close': 'Closing Price'})
    box_chart_div = plot(box_chart, output_type='div')

    # Area Chart
    data['Cumulative Volume'] = data['AAPL.Volume'].cumsum()
    area_chart = px.area(data, x='Date', y='Cumulative Volume',
                         title='Area Chart: Cumulative Volume',
                         labels={'Cumulative Volume': 'Cumulative Volume'})
    area_chart_div = plot(area_chart, output_type='div')

    # Dual Axis Line Chart
    dual_axis_chart = go.Figure()
    dual_axis_chart.add_trace(go.Scatter(x=data['Date'], y=data['AAPL.Close'], name='Closing Price'))
    dual_axis_chart.add_trace(go.Bar(x=data['Date'], y=data['AAPL.Volume'], name='Volume', yaxis='y2'))
    dual_axis_chart.update_layout(title='Dual Axis Line Chart: Closing Price & Volume',
                                  xaxis_title='Date',
                                  yaxis=dict(title='Closing Price'),
                                  yaxis2=dict(title='Volume', overlaying='y', side='right'))
    dual_axis_chart_div = plot(dual_axis_chart, output_type='div')

    # Heatmap
    heatmap_data = data[['AAPL.Open', 'AAPL.High', 'AAPL.Low', 'AAPL.Close']].corr()
    heatmap_chart = px.imshow(heatmap_data, title='Heatmap of Price Correlations',
                               labels=dict(color='Correlation'))
    heatmap_chart_div = plot(heatmap_chart, output_type='div')

    # Step Chart
    step_chart = go.Figure()
    step_chart.add_trace(go.Scatter(x=data['Date'], y=data['AAPL.Close'], mode='lines', name='Closing Price',
                                    line_shape='hv'))
    step_chart.update_layout(title='Step Chart: Closing Prices',
                             xaxis_title='Date', yaxis_title='Price')
    step_chart_div = plot(step_chart, output_type='div')

    context = {
        'candlestick_div': candlestick_div,
        'line_chart_div': line_chart_div,
        'volume_chart_div': volume_chart_div,
        'pie_chart_div': pie_chart_div,
        'scatter_chart_div': scatter_chart_div,
        'histogram_chart_div': histogram_chart_div,
        'box_chart_div': box_chart_div,
        'area_chart_div': area_chart_div,
        'dual_axis_chart_div': dual_axis_chart_div,
        'heatmap_chart_div': heatmap_chart_div,
        'step_chart_div': step_chart_div,
    }

    return render(request, 'finance_app/finance_dashboard.html', context)
