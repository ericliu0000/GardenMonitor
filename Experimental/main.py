from flask import Flask, request, render_template 
  
app = Flask(__name__)   
  
@app.route('/', methods =["GET", "POST"])
def test():
    if request.method == "POST":
      pass
      #use like this
      # first_name = request.form.get("fname")
       #last_name = request.form.get("lname") 
      # return "Your name is "+ first_name + last_name
    return render_template("testing.html")
  
if __name__=='__main__':
   app.run(debug=True, host="0.0.0.0")
