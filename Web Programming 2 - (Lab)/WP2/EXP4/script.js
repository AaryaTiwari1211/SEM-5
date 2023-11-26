document.getElementById("startButton").addEventListener("click", startCountdown);

function startCountdown() {
    const countdownElement = document.getElementById("countdown");
    let remainingTime = 20; // in seconds

    const countdownInterval = setInterval(() => {
        countdownElement.textContent = `Time remaining: ${remainingTime} seconds`;
        remainingTime--;

    }, 1000);
}