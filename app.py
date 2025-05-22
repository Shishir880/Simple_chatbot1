from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

app = Flask(__name__)
CORS(app)

# LangChain + Ollama LLM setup
llm = ChatOllama(model="llama3.2", temperature=0.7)

prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the question: {question}"
)

chain = prompt | llm

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"reply": "Please enter a valid message."})
    response = chain.invoke({"question": user_input})
    return jsonify({"reply": response.content})

if __name__ == "__main__":
    app.run(debug=True)
