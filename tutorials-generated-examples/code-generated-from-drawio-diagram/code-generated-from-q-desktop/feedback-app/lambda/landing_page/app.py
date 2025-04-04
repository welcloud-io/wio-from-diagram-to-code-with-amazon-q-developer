import json
import os

def handler(event, context):
    """
    Landing page Lambda function that returns an HTML form for user feedback
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Feedback Form</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; }
            input[type="text"], input[type="email"], textarea {
                width: 100%;
                padding: 8px;
                margin-bottom: 10px;
            }
            button { padding: 10px 20px; background-color: #007bff; color: white; border: none; }
        </style>
    </head>
    <body>
        <h1>Feedback Form</h1>
        <form id="feedbackForm">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="feedback">Feedback:</label>
                <textarea id="feedback" name="feedback" rows="4" required></textarea>
            </div>
            <button type="submit">Submit Feedback</button>
        </form>
        <script>
            document.getElementById('feedbackForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const formData = {
                    name: document.getElementById('name').value,
                    email: document.getElementById('email').value,
                    feedback: document.getElementById('feedback').value
                };
                
                try {
                    const response = await fetch('/prod/submit-feedback', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(formData)
                    });
                    
                    if (response.ok) {
                        alert('Thank you for your feedback!');
                        document.getElementById('feedbackForm').reset();
                    } else {
                        alert('Error submitting feedback. Please try again.');
                    }
                } catch (error) {
                    console.error('Error:', error);
                    alert('Error submitting feedback. Please try again.');
                }
            });
        </script>
    </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content
    }