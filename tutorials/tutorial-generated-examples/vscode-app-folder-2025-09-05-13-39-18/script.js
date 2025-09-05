// API Gateway endpoint URL (replace with actual endpoint)
const API_ENDPOINT = 'https://your-api-gateway-endpoint.amazonaws.com/prod';

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('feedbackForm');
    const loading = document.getElementById('loading');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading state
        form.style.display = 'none';
        loading.classList.remove('hidden');

        // Collect form data
        const formData = new FormData(form);
        const feedbackData = {
            name: formData.get('name'),
            email: formData.get('email'),
            category: formData.get('category'),
            rating: formData.get('rating'),
            message: formData.get('message'),
            timestamp: new Date().toISOString()
        };

        try {
            // Simulate API call (replace with actual API call)
            await submitFeedback(feedbackData);
            
            // Redirect to confirmation page with data
            const params = new URLSearchParams({
                name: feedbackData.name,
                email: feedbackData.email,
                category: feedbackData.category,
                rating: feedbackData.rating || '',
                message: feedbackData.message
            });
            
            window.location.href = `confirmation.html?${params.toString()}`;
            
        } catch (error) {
            console.error('Error submitting feedback:', error);
            alert('There was an error submitting your feedback. Please try again.');
            
            // Hide loading and show form again
            loading.classList.add('hidden');
            form.style.display = 'block';
        }
    });
});

async function submitFeedback(data) {
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // In a real implementation, this would make an actual API call:
    /*
    const response = await fetch(`${API_ENDPOINT}/feedback`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });
    
    if (!response.ok) {
        throw new Error('Failed to submit feedback');
    }
    
    return await response.json();
    */
    
    // For demo purposes, just log the data
    console.log('Feedback submitted:', data);
    return { success: true, id: Math.random().toString(36).substr(2, 9) };
}