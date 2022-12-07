from flask import Flask, jsonify, request, render_template
#import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/google-charts/pie-chart')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Work' : 15, 'Eat' : 3, 'Commute' : 4, 'Watching TV' : 5, 'Sleeping' : 2}
    return render_template('pie-chart.html', data=data)

@app.route('/google-charts/HTMLPage1')
def google_pie_chart2():
    return render_template('HTMLPage1.html')

@app.route('/google-charts/HTMLPage2')
def google_pie_chart3():
    return render_template('HTMLPage2.html')

if __name__ == "__main__":
    app.run()