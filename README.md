Flask
==============

Installation
------------

Install requirements

    python -m pip install -r requirements.txt



Example
-------

```py
from flask import Flask, render_template
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        # create()
        # data()
        app.run(debug=True)
```

Resources
---------

- [Documentation](https://flask.palletsprojects.com/en/stable/)

