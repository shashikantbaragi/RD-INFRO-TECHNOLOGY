from flask import Flask, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Customer Support Chatbot</title>
    </head>
    <body>
        <h2>AI Customer Support Chatbot</h2>

        <input type="text" id="msg" placeholder="Type your message">
        <button onclick="sendMsg()">Send</button>

        <div id="chatbox"></div>

        <script>
        function sendMsg() {

            let message = document.getElementById("msg").value;

            fetch("/chat", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({message: message})
            })
            .then(response => response.json())
            .then(data => {

                document.getElementById("chatbox").innerHTML +=
                "<p><b>You:</b> " + message + "</p>" +
                "<p><b>Bot:</b> " + data.response + "</p>";

                document.getElementById("msg").value = "";
            });
        }
        </script>

    </body>
    </html>
    """

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)