document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('queryForm');
    const loading = document.getElementById('loading');
    const submitBtn = document.querySelector('.submit-btn');
    const textarea = document.getElementById('prompt');
    
    // Handle form submission
    form.addEventListener('submit', function() {
        loading.classList.add('active');
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="btn-text">Processing...</span>';
    });
    
    // Auto-resize textarea
    textarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = Math.max(120, this.scrollHeight) + 'px';
    });
    
    // Handle textarea focus
    textarea.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });
    
    textarea.addEventListener('blur', function() {
        this.parentElement.classList.remove('focused');
    });
    
    // Keyboard shortcuts
    textarea.addEventListener('keydown', function(e) {
        // Submit with Ctrl/Cmd + Enter
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            e.preventDefault();
            form.submit();
        }
    });
    
    // Clear form after successful submission
    if (window.location.search.includes('success')) {
        textarea.value = '';
    }
});