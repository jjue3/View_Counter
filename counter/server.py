from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'secret_key'

counter = 0

@app.route('/')
def index():
    session['counter'] += 1
    counter = session['counter']
    print(session['counter'])
    return render_template('index.html', counter_total=counter)



@app.route('/destroy_session', methods=['POST'])
def restart():
    session['counter']= 0
    return redirect('/')
    
@app.route('/add2points', methods=['POST'])
def addpoint():
    session['counter'] += 2
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)