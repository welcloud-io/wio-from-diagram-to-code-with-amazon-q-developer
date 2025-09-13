import json

def lambda_handler(event, context):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Restaurant Reservation Assistant</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .chat-container { border: 1px solid #ccc; height: 400px; overflow-y: auto; padding: 10px; margin: 10px 0; }
            .message { margin: 10px 0; padding: 10px; border-radius: 5px; }
            .user { background-color: #e3f2fd; text-align: right; }
            .assistant { background-color: #f5f5f5; }
            input[type="text"] { width: 70%; padding: 10px; }
            button { padding: 10px 20px; background-color: #2196f3; color: white; border: none; cursor: pointer; }
            .error { color: red; margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>Restaurant Reservation Assistant</h1>
        <div id="chat-container" class="chat-container"></div>
        <div id="error-message" class="error" style="display: none;"></div>
        <div>
            <input type="text" id="message-input" placeholder="Ask me about reservations..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Send</button>
        </div>

        <script>
            const API_ENDPOINT = window.location.origin + '/prod/chat';
            
            function handleKeyPress(event) {
                if (event.key === 'Enter') {
                    sendMessage();
                }
            }
            
            async function sendMessage() {
                const input = document.getElementById('message-input');
                const message = input.value.trim();
                if (!message) return;
                
                addMessage(message, 'user');
                input.value = '';
                
                try {
                    const response = await fetch(API_ENDPOINT, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ message: message })
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        addMessage(data.response, 'assistant');
                        hideError();
                    } else {
                        showError('API Error: ' + (data.error || 'Unknown error'));
                    }
                } catch (error) {
                    showError('Network Error: ' + error.message);
                }
            }
            
            function addMessage(text, sender) {
                const container = document.getElementById('chat-container');
                const messageDiv = document.createElement('div');
                messageDiv.className = 'message ' + sender;
                messageDiv.textContent = text;
                container.appendChild(messageDiv);
                container.scrollTop = container.scrollHeight;
            }
            
            function showError(message) {
                const errorDiv = document.getElementById('error-message');
                errorDiv.textContent = message;
                errorDiv.style.display = 'block';
            }
            
            function hideError() {
                document.getElementById('error-message').style.display = 'none';
            }
        </script>
    </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html_content
    }