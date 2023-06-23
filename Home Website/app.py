from flask import Flask, render_template, request
import random
from passwordgen import main

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    global votes
    if votes > 0:
        votes=votes
    return render_template("home.html",votes=votes)


@app.route("/scramble", methods=['POST','GET'])
def scrambler():
    return render_template("template.html")

#scramble result
@app.route("/result", methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    word = list(output['word'])
    shuffled = ''.join(random.sample(word, len(word)))
    return render_template("template.html",word=shuffled)


@app.route("/passwordgen", methods=['GET','POST'])
def passwordgen():
    return render_template("passwordgen.html")
    

#password generator result
@app.route("/resultpass", methods=['POST','GET'])
def passwordresult():
    try:
        password = main()
        return render_template("passwordresult.html",password=password)
    except:
        password = main()
        return render_template("passwordresult.html",password=password)
    

@app.route('/setvariable')
def set_variable():
    # global password
    password = main()
    print(password)
    return render_template("setvariable.html", password=password)

if __name__=='__main__':
    app.run(debug=True,port=5001)
