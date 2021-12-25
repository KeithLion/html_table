from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def table():
    name = [
        {'first_name': 'John','last_name':'salue'},
        {'first_name':'Terri','last_name':'marks'},
        {'first_name':'KB','last_name':'Tonel'},
        {'first_name':'Kayla','last_name':'Guillen'}
    ]
    return render_template('table.html', names = name)

if __name__ == "__main__":
    app.run(debug=True)