function updateTimer(deadline) {
    return {
        minutes: Math.floor(deadline / 60),
        seconds: Math.floor(deadline % 60),
        total: deadline
    };
}

function animateClock(span) {
    setTimeout(function () {
        span.className = "";
    }, 1000);
}

function startTimer(id, deadline) {
    var timer = updateTimer(deadline);

    var timerInterval = setInterval(function () {
        var clock = document.getElementById(id);
        var timer = updateTimer(deadline);

        if (timer.total < 0) {
            clearInterval(timerInterval);
            var a = document.querySelector(".row_main_body")
            a.setAttribute("style", "display:none !important")
       }
        
        clock.innerHTML =
            "<span>" +
            timer.minutes +
            "</span>" +
            "<span>" +
            timer.seconds +
            "</span>";

        // animation
        var spans = clock.getElementsByTagName("span");
        animateClock(spans[1]);
        if (timer.seconds == 59) animateClock(spans[0]);
    }, 1000);
}

window.onload = function () {
    startTimer("clock", 300);
};