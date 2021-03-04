from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def hello_Dojo():
    return 'Dojo'

@app.route('/say/flask')          # The "@" decorator associates this route with the function immediately following
def hello_flask():
    return 'Hi Flask'

@app.route('/say/michael')          # The "@" decorator associates this route with the function immediately following
def hello_Michael():
    return 'Hi Michael'

@app.route('/say/john')          # The "@" decorator associates this route with the function immediately following
def hello_John():
    return 'Hi John'

@app.route('/repeat/35/hello')          # The "@" decorator associates this route with the function immediately following
def hello_repeat():
    return 'Hello'*35 

@app.route('/repeat/80/bye')          # The "@" decorator associates this route with the function immediately following
def bye_repeat():
    return 'Bye'*80

@app.route('/repeat/99/dogs')          # The "@" decorator associates this route with the function immediately following
def dogs_repeat():
    return 'Dogs'*99



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  