# This is what has been generated after we ask Q to send json format to the API/Lambda function
# I just had to change a small typo (feedback has been replace by feedbacks (with ans s at the end))
import json

def handler(event, context):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Feedback Form</title>
        <script>
        function submitFeedback(event) {
            event.preventDefault();
            const feedback = document.getElementById('feedback').value;
            const data = JSON.stringify({ feedback: feedback });
            
            fetch('/prod/feedbacks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: data
            })
            .then(response => response.json())
            .then(data => {
                alert('Feedback submitted successfully');
                document.getElementById('feedbackForm').reset();
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('An error occurred while submitting feedback');
            });
        }
        </script>
    </head>
    <body>
        <h1>Feedback Form</h1>
        <form id="feedbackForm" onsubmit="submitFeedback(event)">
            <label for="feedback">Your Feedback:</label><br>
            <textarea id="feedback" name="feedback" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': html_content
    }
