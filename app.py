from flask import Flask, render_template

app = Flask(__name__)
JOBS=[
  {
    'id':0,
    'title':'Data Analyst',
    'location':'Bangalore',
    'salary':'Rs 6.5 lpa',
  },
  {
    'id':1,
    'title':'Data Scientist',
    'location':'Mumbai',
    'salary':'Rs 10.5 lpa',
  },
  {
    'id':2,
    'title':'DevOps Engineer',
    'location':'Delhi',
    'salary':'Rs 12.5 lpa',
  },
  {
    'id':3,
    'title':'Data Engineering',
    'location':'Germany',
    'salary':'Euro 5k',
  }

]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


if __name__ == '__main__':

  app.run(host='0.0.0.0', debug=True)
