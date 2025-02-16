// Guided Meditations
function playMeditation(duration) {
    let audio = new Audio();
    switch (duration) {
        case 'short':
            audio.src = 'audio/guided-meditation-short.mp3';
            break;
        case 'medium':
            audio.src = 'audio/guided-meditation-medium.mp3';
            break;
        case 'long':
            audio.src = 'audio/guided-meditation-long.mp3';
            break;
    }
    audio.play();
}

// Breathing Exercises
function startBreathingExercise() {
    const circle = document.getElementById('breathing-circle');
    circle.style.animation = 'breathe 12s infinite';
}

// Gratitude Journal
function saveGratitude() {
    const input = document.getElementById('journal-input').value;
    const savedEntries = document.getElementById('saved-entries');

    if (input) {
        const newEntry = document.createElement('div');
        newEntry.textContent = input;
        newEntry.classList.add('entry');
        savedEntries.appendChild(newEntry);
        document.getElementById('journal-input').value = '';
    }
}

// Mood-Based Suggestions
function getSuggestions() {
    const mood = document.getElementById('mood').value;
    const suggestions = document.getElementById('suggestions');
    suggestions.innerHTML = '';

    if (mood === 'stressed') {
        suggestions.innerHTML = '<p>Try a short guided meditation for stress relief.</p>';
    } else if (mood === 'calm') {
        suggestions.innerHTML = '<p>Enjoy some quiet breathing exercises or write in your gratitude journal.</p>';
    } else if (mood === 'tired') {
        suggestions.innerHTML = '<p>Take a nap or try a meditation for better sleep.</p>';
    }
}
