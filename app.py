from flask import Flask, render_template

app = Flask(__name__)
JOBS=[
  {
    'id':0,
    'title':'Malaria Detection',
    'description':'Detection of Malaria parasites through blood smear slide images',
    'salary':'Rs 2 lakhs',
  },
  {
    'id':1,
    'title':'Leaf Disease Classification',
    'location':'Identify the type of disease present on a various Leaf image',
    'salary':'Rs 3.5 lakhs',
  },
  {
    'id':2,
    'title':'Fruit Price Prediction',
    'location':'Estimation of Fruit prices based on market trends & global hunger index',
    'salary':'Rs 1.5 lakhs',
  },

]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


if __name__ == '__main__':

  app.run(host='0.0.0.0', debug=True)
