"""
export FLASK_APP=flask_script_1
export FLASK_ENV=development
flask run
"""

from flask import Flask, render_template, url_for

# Instantiate the object
app=Flask(__name__)

# Call the Flask decorator
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


# Python assigns the __name__ variable as __main__ in the same script so the following condition works.
if __name__=="__main__":
    app.run(debug=True)
