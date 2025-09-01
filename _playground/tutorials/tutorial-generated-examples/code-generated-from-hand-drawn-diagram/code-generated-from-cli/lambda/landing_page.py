import json
import logging
from typing import Dict, Any

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler for serving the landing page.
    
    Args:
        event: API Gateway event object
        context: Lambda context object
        
    Returns:
        API Gateway response object
    """
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        # Get the HTTP method and path
        http_method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        
        logger.info(f"Processing {http_method} request for path: {path}")
        
        # Generate HTML content for the landing page
        html_content = generate_landing_page_html()
        
        # Return successful response
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Pragma': 'no-cache',
                'Expires': '0'
            },
            'body': html_content
        }
        
        logger.info("Successfully generated landing page response")
        return response
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        
        # Return error response
        error_response = {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': 'Internal Server Error',
                'message': 'An error occurred while processing your request'
            })
        }
        
        return error_response

def generate_landing_page_html() -> str:
    """
    Generate the HTML content for the landing page.
    
    Returns:
        HTML string for the landing page
    """
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Serverless Web Application</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            
            .container {
                text-align: center;
                max-width: 800px;
                padding: 2rem;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }
            
            h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .subtitle {
                font-size: 1.2rem;
                margin-bottom: 2rem;
                opacity: 0.9;
            }
            
            .architecture-info {
                background: rgba(255, 255, 255, 0.1);
                padding: 1.5rem;
                border-radius: 15px;
                margin: 2rem 0;
                text-align: left;
            }
            
            .architecture-info h2 {
                color: #4ecdc4;
                margin-bottom: 1rem;
                text-align: center;
            }
            
            .tech-stack {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1rem;
                margin-top: 1.5rem;
            }
            
            .tech-item {
                background: rgba(255, 255, 255, 0.1);
                padding: 1rem;
                border-radius: 10px;
                text-align: center;
            }
            
            .tech-item h3 {
                color: #ff6b6b;
                margin-bottom: 0.5rem;
            }
            
            .status {
                display: inline-block;
                background: #4ecdc4;
                color: #333;
                padding: 0.5rem 1rem;
                border-radius: 25px;
                font-weight: bold;
                margin-top: 1rem;
            }
            
            .footer {
                margin-top: 2rem;
                opacity: 0.7;
                font-size: 0.9rem;
            }
            
            @media (max-width: 768px) {
                h1 {
                    font-size: 2rem;
                }
                
                .container {
                    margin: 1rem;
                    padding: 1.5rem;
                }
                
                .tech-stack {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Serverless Web App</h1>
            <p class="subtitle">Powered by AWS Lambda, API Gateway, and Python</p>
            
            <div class="status">✅ Application Running Successfully</div>
            
            <div class="architecture-info">
                <h2>🏗️ Architecture Overview</h2>
                <p>This serverless web application demonstrates a modern cloud-native architecture:</p>
                
                <div class="tech-stack">
                    <div class="tech-item">
                        <h3>🌐 Frontend</h3>
                        <p>HTML5, CSS3, JavaScript served directly from Lambda</p>
                    </div>
                    
                    <div class="tech-item">
                        <h3>🔗 API Gateway</h3>
                        <p>Amazon API Gateway handles HTTP requests and routing</p>
                    </div>
                    
                    <div class="tech-item">
                        <h3>⚡ AWS Lambda</h3>
                        <p>Python 3.11 runtime serving dynamic content</p>
                    </div>
                    
                    <div class="tech-item">
                        <h3>🏗️ Infrastructure</h3>
                        <p>AWS CDK v2 for Infrastructure as Code</p>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <p>Built with ❤️ using AWS Serverless Technologies</p>
                <p>Request processed by AWS Lambda function</p>
            </div>
        </div>
        
        <script>
            // Add some interactivity
            document.addEventListener('DOMContentLoaded', function() {
                console.log('🚀 Serverless Web App Loaded Successfully!');
                console.log('Architecture: User → Browser → API Gateway → Lambda');
                
                // Add click animation to tech items
                const techItems = document.querySelectorAll('.tech-item');
                techItems.forEach(item => {
                    item.addEventListener('click', function() {
                        this.style.transform = 'scale(1.05)';
                        this.style.transition = 'transform 0.2s ease';
                        setTimeout(() => {
                            this.style.transform = 'scale(1)';
                        }, 200);
                    });
                });
            });
        </script>
    </body>
    </html>
    """
    
    return html
