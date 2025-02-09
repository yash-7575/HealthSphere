// Start Timer Function
function startTimer() {
    const minutes = document.getElementById('timer').value;
    const timerDisplay = document.getElementById('timer-display');
    let seconds = minutes * 60;
  
    timerDisplay.innerText = `Timer: ${minutes} minutes`;
    const interval = setInterval(() => {
      seconds--;
      const min = Math.floor(seconds / 60);
      const sec = seconds % 60;
      timerDisplay.innerText = `Timer: ${min}:${sec < 10 ? '0' + sec : sec}`;
      if (seconds <= 0) {
        clearInterval(interval);
        timerDisplay.innerText = 'Time is up!';
      }
    }, 1000);
  }
  
  // Toggle Ambient Sound
//   function toggleSound() {
//     const audio = document.getElementById('bg-sound');
//     if (audio.paused) audio.play();
//     else audio.pause();
//   }

  
// Add your JavaScript code here



function toggleSound() {

    var audio = document.getElementById('bg-sound');
  
    if (audio.paused) {
  
      audio.play();
  
    } else {
  
      audio.pause();
  
    }
  
  }
  
  
  // Quote Carousel
  const quotes = [
    "Meditation brings wisdom; lack of meditation leaves ignorance.",
    "Calm your mind, and the rest will follow.",
    "Inner peace begins when you choose to let go of distractions.",
    "Quiet the mind, and the soul will speak.",
    "The thing about meditation is: You become more and more you."

  ];
  let currentQuote = 0;
  
  setInterval(() => {
    document.getElementById('quote-carousel').innerText = quotes[currentQuote];
    currentQuote = (currentQuote + 1) % quotes.length;
  }, 5000);
  
  // Toggle Tips
  function toggleTips() {
    const tips = document.getElementById('tips');
    tips.style.display = tips.style.display === 'none' ? 'block' : 'none';
  }
  