from flask import Flask,render_template, request
app = Flask(__name__)
import model
@app.route("/", methods=['GET', 'POST'])
def index():
 if request.method == 'POST':
 if request.form.get('action1') == 'submit1':
 video = request.form["url"]
 # transcript = model.f(video)
 text = model.summ(video)
 if(text == "not available"):
 return render_template('notfound.html')
 return render_template('pop.html',text=text)
 elif request.method == 'GET':
 return render_template('index.html')
 
 return render_template("index.html")
 
if __name__ == '__main__':
 app.run(debug=True)
