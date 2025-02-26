# Flask API Playground

## Overview
Flask API Playground is a simple Flask web application designed to revisit and reinforce fundamental API concepts. This project includes user authentication, file uploads, CSV conversions, dynamic routing, and JSON handling, serving as a hands-on refresher for core Flask functionalities.
Since I’m currently working with Kafka and MongoDB, where I need to build APIs for data streaming and database interactions, I wanted to brush up on Flask concepts before diving deeper into those technologies. This project was developed to reinforce key concepts and facilitate my transition into API development with NoSQL-based systems for real-time applications.

## Features
- **User Authentication**: A simple login form that checks for a hardcoded username and password.
- **File Uploads**: Supports uploading text and Excel files.
- **File Processing:**
  - Displays content for text files.
  - Reads and converts Excel files into HTML tables.
- **Convert to CSV:**
  - Direct download response as CSV.
  - Save file in the server and provide a download link.
- **Dynamic Routing**: Handles dynamic parameters in URLs.
- **JSON Handling**: Accepts and processes JSON requests.
- **Custom Jinja Filters**: Implements string manipulation filters.
- **JavaScript Integration**: Demonstrates an API call using JavaScript.

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd flask-api-project
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Access the app in your browser:
   ```
   http://127.0.0.1:5000
   ```

## Endpoints
| Method  | Route                           | Description |
|---------|--------------------------------|-------------|
| GET, POST | `/` | Renders login form and handles authentication |
| POST | `/file_upload` | Handles file uploads (text and Excel) |
| POST | `/convert_csv` | Converts an Excel file to CSV and returns it |
| POST | `/convert_csv_two` | Converts an Excel file to CSV and provides a download link |
| GET | `/download/<filename>` | Downloads the converted CSV file |
| POST | `/handle_post` | Accepts JSON and writes to a file |
| GET | `/index2` | Demonstrates Jinja templating |
| GET | `/redirect_endpoint` | Redirects to another endpoint |
| GET | `/greet/<name>` | Greets a user dynamically |
| GET | `/add/<int:number1>/<int:number2>` | Adds two numbers dynamically |
| GET | `/handle_url_params` | Handles URL query parameters |

## Project Structure
```
flask-api-project/
│── static/                # Static files (JS, CSS, images)
│── templates/             # HTML templates
│── downloads/             # Directory for storing converted CSV files
│── app.py                 # Main Flask application
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

## Future Enhancements
- Implement a database for user authentication.
- Add more API endpoints for data processing.
- Improve frontend UI with Bootstrap or React.
- Add better error handling and logging.

This project is for learning purposes
