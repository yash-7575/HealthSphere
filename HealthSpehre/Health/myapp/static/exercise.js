document.addEventListener('DOMContentLoaded', function() {
    const exerciseButtons = document.querySelectorAll('.exercise-button');

    exerciseButtons.forEach(button => {
        button.addEventListener('click', function() {
            const content = this.nextElementSibling;

            content.style.display = content.style.display === 'block' ? 'none' : 'block';
        });
    });
});