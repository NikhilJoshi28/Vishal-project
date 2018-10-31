from flask import Flask, render_template,request
import os
from script import hydrophobicity as hp
from corrcoef import correlation as cr

app = Flask(__name__)

atomic_kernel= None

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/plot/', methods=['GET','POST'])
def plot():
    return render_template('plot.html')

@app.route('/correlation/', methods=['GET','POST'])
def plot2():
    return render_template('correlation.html')

@app.route('/generate2/', methods=['GET','POST'])
def getplot2():
    try:
        if request.method=="POST":
            amino_acid_sequence = request.form['sequence']
            window_size = request.form['Wsize']
            menu =request.form['menu']
            # print(amino_acid_sequence)
            # print(window_size)
            # print(menu)
            cof = cr()
            cof.get_coefficient_plot(amino_acid_sequence,window_size,menu)

    except Exception as e:
        print(e)
    return render_template('correlation.html')

@app.route('/generate/', methods=['GET','POST'])
def getplot():
    try:
        if request.method=="POST":
            amino_acid_sequence = request.form['sequence']
            window_size = request.form['Wsize']
            # print(amino_acid_sequence)
            # print(window_size)
            h = hp()
            hp.get_plot(amino_acid_sequence,window_size)

    except Exception as e:
        print(e)
    return render_template('plot.html')

"""
if __name__=='__main__':
	app.run(host='0.0.0.0', port=4141, debug=True, threaded=True)
"""
if __name__=='__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port, debug=True)
