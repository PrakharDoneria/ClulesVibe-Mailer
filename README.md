# Flask Email Sending Server

This is a Flask server that sends emails using the `qick-mailer` package. It accepts the recipient's email, subject, and message body through a POST request.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository or download the source code.

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

**URL**: `/send_email`

**Method**: `POST`

**Content-Type**: `application/json`

**Request Body**:

```json
{
    "email": "recipient@example.com",
    "subject": "Your Subject Here",
    "message": "Your message here"
}
```

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
        "error": "Email, subject, and message are required"
    }
    ```

## Example cURL Request

To test the email sending functionality, you can use the following cURL command:

```bash
curl -X POST http://127.0.0.1:5000/send_email -H "Content-Type: application/json" -d '{"email":"recipient@example.com","subject":"Test Subject","message":"Hello from Flask!"}'
```

### Explanation:

- **Prerequisites**: Lists the required software.
- **Installation**: Provides steps to set up the project, including creating a virtual environment and installing dependencies.
- **Configuration**: Instructs how to create a `.env` file with email credentials.
- **Running the Server**: Shows how to start the Flask server.
- **API Endpoint**: Details the `/send_email` endpoint, including the request format and possible responses.
- **Example cURL Request**: Provides a sample cURL command to test the API.