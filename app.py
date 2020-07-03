from flask import Flask,render_template,redirect,request
import numpy as np
import pickle
import caption_it
from keras.models import Model, load_model

app = Flask(__name__)
model = load_model("model_9.h5")

@app.route('/')
def home():
    return render_template('index.html')


								
@app.route('/',methods= ['POST'])
def marks():

	if request.method == 'POST':
		f = request.files['userfile']
		path = "./static/{}".format(f.filename)
		f.save(path)

		caption = caption_it.caption_this_image(path)
		
		result_dic = {
		'image' : path,
		'caption' :caption
		}
		

		return render_template("index.html",your_result = result_dic)
		
if __name__=='__main__':
	   
	app.run(debug = True )








