from flask import Flask, request, make_response, render_template, redirect  # type: ignore
from flask import url_for, Response, send_from_directory, jsonify  # type: ignore
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route for the homepage. Handles both GET and POST requests.
    - GET: Renders the index.html template.
    - POST: Validates the username and password; returns "Success" or "Failure".
    """
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'deadpool' and password == 'password':
            return "Success"
        else:
            return "Failure"

@app.route('/file_upload', methods=['POST'])
def file_upload():
    """
    Route to handle file uploads.
    - Expects a file from the request.
    - If the file is a plain text file, returns its content.
    - If the file is an Excel file, reads it into a DataFrame and returns its HTML representation.
    """
    file = request.files['file']
    
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 
                                 'application/vnd.ms-excel']:
        df = pd.read_excel(file)
        return df.to_html()

    return "Unsupported file type", 415  # Returns a 415 error for unsupported file types

@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    """
    Route to convert an uploaded Excel file to CSV format.
    - Reads the uploaded file into a DataFrame.
    - Returns the DataFrame as a CSV file in the response.
    """
    file = request.files['file']
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=result.csv'}
    )
    return response

@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    """
    Route to convert an uploaded Excel file to CSV format and save it on the server.
    - Reads the uploaded file into a DataFrame.
    - Creates a downloads directory if it doesn't exist.
    - Saves the DataFrame as a CSV file with a unique filename and renders a download page.
    """
    file = request.files['file']
    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    filename = f'{uuid.uuid4()}.csv'  # Generates a unique filename
    df.to_csv(os.path.join('downloads', filename))

    return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
    """
    Route to handle file downloads.
    - Serves the CSV file stored in the downloads directory.
    - Sets the response to download the file with the name 'result.csv'.
    """
    downloads_dir = os.path.join(app.root_path, "downloads")  # Absolute path
    return send_from_directory(downloads_dir, filename, as_attachment=True, download_name="result.csv")

@app.route('/handle_post', methods=['POST'])
def handle_post():
    """
    Route to handle a POST request with JSON data.
    - Expects a JSON payload with 'greeting' and 'name' fields.
    - Writes the received data to a text file and returns a success message.
    """
    greeting = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting},{name}')

    return jsonify({'message': 'Successfully written!'})

@app.route('/index2')
def index2():
    """
    Route to render a second index page (index2.html).
    - Passes variables for rendering: a string, a calculation result, and a list of numbers.
    """
    myvalue = 'Deadpool'
    myresult = 10 + 30
    mylist = [10, 20, 30, 40, 50]
    return render_template('index2.html', myvalue=myvalue, myresult=myresult, mylist=mylist)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    """
    Route to demonstrate redirection.
    - Redirects the user to the 'other' endpoint.
    """
    return redirect(url_for('other'))

@app.route('/other')
def other():
    """
    Route for another page (other.html).
    - Passes a variable for rendering to the template.
    """
    some_text = 'Other World'
    return render_template('other.html', some_text=some_text)

@app.template_filter('reverse_string')
def reverse_string(s):
    """
    Template filter to reverse a string.
    """
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    """
    Template filter to repeat a string a specified number of times.
    Default is 2 times.
    """
    return (s * times)

@app.template_filter('alternate_case')
def alternate_case(s):
    """
    Template filter to alternate the case of characters in a string.
    """
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

@app.route('/hello')
def hello():
    """
    Route to return a simple greeting message.
    - Returns a 'Hello World' message with a 404 status code (not typically recommended).
    """
    return 'Hello World', 404

@app.route('/hello_make_response')  # Curl custom responses
def hello_make_response():
    """
    Route to demonstrate creating a custom response.
    - Returns a response with a 202 status code and a custom content type.
    """
    response = make_response()
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'
    return response

@app.route('/hello_methods', methods=['GET', 'POST'])
def hello_methods():
    """
    Route to handle both GET and POST requests.
    - Returns a message indicating the type of request made.
    """
    if request.method == 'GET':
        return 'You made a GET request \n'
    elif request.method == 'POST':
        return 'You made a POST request \n'
    else:
        return "You will never see this message"

@app.route('/greet/<name>')  # Dynamic route
def greet(name):
    """
    Route to greet a user with a dynamic name parameter.
    """
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')  # Dynamic route
def add(number1, number2):
    """
    Route to add two numbers passed as parameters.
    - Returns the sum of the two numbers.
    """
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params')
def handle_params():
    """
    Route to demonstrate handling URL query parameters.
    - Returns a greeting message if 'greeting' and 'name' parameters are provided.
    """
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']  # Accessing the parameter directly
        name = request.args.get('name')  # Using get method for safer access
        return f'{greeting}, {name}'
    else:
        return 'Some parameters are missing'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)  # Runs the app in debug mode
