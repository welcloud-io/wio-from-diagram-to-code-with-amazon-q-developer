import json

def handler(event, context):
    """
    Lambda function that serves the landing page for the feedback application.
    
    This function returns an HTML form that allows users to submit feedback.
    """
    # HTML for the landing page with a feedback form
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Feedback Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }
            .form-group {
                margin-bottom: 15px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
            input[type="text"],
            input[type="email"],
            textarea {
                width: 100%;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            textarea {
                height: 100px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>We Value Your Feedback</h1>
        <p>Please take a moment to share your thoughts with us.</p>
        
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
                <label for="feedback">Your Feedback:</label>
                <textarea id="feedback" name="feedback" required></textarea>
            </div>
            
            <div class="form-group">
                <label for="rating">Rating (1-5):</label>
                <input type="number" id="rating" name="rating" min="1" max="5" required>
            </div>
            
            <button type="submit">Submit Feedback</button>
        </form>
        
        <div id="response" style="margin-top: 20px;"></div>
        
        <script>
            document.getElementById('feedbackForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const formData = {
                    name: document.getElementById('name').value,
                    email: document.getElementById('email').value,
                    feedback: document.getElementById('feedback').value,
                    rating: document.getElementById('rating').value
                };
                
                fetch('/prod/feedback', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('response').innerHTML = 
                        `<div style="padding: 15px; background-color: #dff0d8; border-radius: 4px;">
                            <p><strong>Thank you for your feedback!</strong></p>
                            <p>${data.message}</p>
                        </div>`;
                    document.getElementById('feedbackForm').reset();
                })
                .catch(error => {
                    document.getElementById('response').innerHTML = 
                        `<div style="padding: 15px; background-color: #f2dede; border-radius: 4px;">
                            <p><strong>Error:</strong> ${error.message}</p>
                        </div>`;
                });
            });
        </script>
    </body>
    </html>
    """
    
    # Return the HTML content with appropriate headers
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content
    }