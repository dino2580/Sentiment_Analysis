from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

# Load the trained pipeline
with open('pipeline.pkl', 'rb') as file:
    loaded_pipeline = pickle.load(file)

@app.route('/')
def index():
    l = request.args.get('l', '')
    t = request.args.get('t', '')
    return render_template('home.html', l=l, t=t)

@app.route('/handle_post', methods=['POST'])
def handle_post():
    text = request.form['user_input']
    result = loaded_pipeline.predict([text])
    
    if result == [1.]:
        l = 'Positive'
    elif result == [0.]:
        l = 'Neutral'
    else:
        l = 'Negative'
    
    return redirect(url_for('index', t=text, l=l))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
