async function askKiro() {
    const question = document.getElementById('question').value;
    const category = document.getElementById('category').value;
    
    if (!question.trim()) {
        alert('Please enter your question!');
        return;
    }
    
    try {
        const response = await fetch('/ask-kiro', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: new URLSearchParams({question, category})
        });
        
        if (!response.ok) throw new Error('Network error');
        
        const data = await response.json();
        showResponse(data.answer);
    } catch (error) {
        console.error('Error:', error);
        showResponse('Sorry, something went wrong! Please try again.');
    }
}

function showResponse(answer) {
    const responseDiv = document.getElementById('response');
    const contentDiv = document.getElementById('responseContent');
    contentDiv.textContent = answer;
    responseDiv.classList.remove('hidden');
    responseDiv.scrollIntoView({ behavior: 'smooth' });
}

function clearResponse() {
    document.getElementById('response').classList.add('hidden');
}

// Allow Enter key to submit
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('question').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            askKiro();
        }
    });
});
