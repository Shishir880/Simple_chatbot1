# AI Chatbot Application

This is a Flask-based AI chatbot application that uses the LangChain framework and the Ollama LLM to provide intelligent conversational capabilities.

## Project Structure

```
.env
app.py
main.py
static/
    widget.js
templates/
    chat.html
    index.html
```

### Key Files:
- **`app.py`**: The main Flask application that handles routes and integrates with the LangChain framework.
- **`templates/chat.html`**: The front-end interface for the chatbot.
- **`static/widget.js`**: A script to embed the chatbot as an iframe widget.
- **`templates/index.html`**: A basic landing page for the chatbot website.

## Features

- **AI-Powered Conversations**: Uses LangChain and Ollama LLM for generating responses.
- **Interactive UI**: A responsive chat interface built with HTML, CSS, and JavaScript.
- **API Integration**: A `/chat` endpoint to handle user messages and return AI-generated responses.
- **Embeddable Widget**: Easily integrate the chatbot into other websites using the `widget.js` script.

## Installation

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## API Endpoints

### `/`
- **Method**: GET
- **Description**: Renders the chatbot interface (`chat.html`).

### `/chat`
- **Method**: POST
- **Description**: Accepts user input and returns AI-generated responses.
- **Request Body**:
  ```json
  {
    "message": "Your question or message"
  }
  ```
- **Response**:
  ```json
  {
    "reply": "AI's response"
  }
  ```

## How to Embed the Chatbot

To embed the chatbot on another website, include the following script in your HTML:
```html
<script src="static/widget.js"></script>
```

## Dependencies

- **Flask**: Web framework for building the application.
- **Flask-CORS**: To handle cross-origin requests.
- **LangChain**: Framework for building LLM-powered applications.
- **Ollama LLM**: The AI model used for generating responses.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [LangChain](https://www.langchain.com/)
- [Ollama LLM](https://www.ollama.ai/)
