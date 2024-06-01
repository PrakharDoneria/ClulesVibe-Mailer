# Flask Email Sending Server

This is a Flask server that sends emails using the `mailer` package. It accepts the recipient's email, subject, and message body through URL parameters in a GET request.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository or download the source code.

    ```bash
    git clone https://github.com/yourusername/flask-email-sender.git
    cd flask-email-sender
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root of your project directory and add your email credentials:

    ```plaintext
    EMAIL=your_email@example.com
    PASSWORD=your_password
    ```

## Running the Server

1. Run the Flask application:

    ```bash
    python main.py
    ```

2. The server will start running on `http://127.0.0.1:5000`.

## API Endpoint

### Send Email

**URL**: `/sendMail`

**Method**: `GET`

**Query Parameters**:

- `email` (string, required): The recipient's email address.
- `subject` (string, required): The subject of the email.
- `body` (string, required): The body content of the email.

**Response**:

- `200 OK` if the email is sent successfully:

    ```json
    {
        "status": "success"
    }
    ```

- `500 Internal Server Error` if there is a failure in sending the email:

    ```json
    {
        "status": "failed"
    }
    ```

- `400 Bad Request` if the required fields are missing:

    ```json
    {
        "error": "Email, subject, and body are required"
    }
    ```

## Example cURL Request

To test the email sending functionality, you can use the following cURL command:

```bash
curl "http://127.0.0.1:5000/sendMail?email=recipient@example.com&subject=Test%20Subject&body=Hello%20from%20Flask!"
```

### Explanation:

- **Prerequisites**: Lists the required software.
- **Installation**: Provides steps to set up the project, including creating a virtual environment and installing dependencies.
- **Configuration**: Instructs how to create a `.env` file with email credentials.
- **Running the Server**: Shows how to start the Flask server.
- **API Endpoint**: Details the `/sendMail` endpoint, including the request format and possible responses.
- **Example cURL Request**: Provides a sample cURL command to test the API.