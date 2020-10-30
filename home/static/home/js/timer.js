function updateTimer(deadline) {
    var time = deadline - new Date();
    return {
        minutes: Math.floor(time / 1000 / 60),
        seconds: Math.floor((time / 1000) % 60),
        total: time
    };
}


function startTimer(id, deadline) {
    var timer = updateTimer(deadline);

    var timerInterval = setInterval(function () {
        var clock = document.getElementById(id);
        var timer = updateTimer(deadline);

        if (timer.total <= 60) {
            clearInterval(timerInterval);
            var a = document.querySelector(".main_body")
            a.setAttribute("style", "display:none")
            timer.minutes = 0
            timer.seconds = 0
       }
        
        clock.innerHTML = ""

        if (timer.minutes < 10){
            clock.innerHTML += "<span> 0" + timer.minutes + "</span>"
        }
        else {
            clock.innerHTML += "<span>" + timer.minutes + "</span>"
        }
        clock.innerHTML += "<span> : </span>"
        if (timer.seconds < 10){
            clock.innerHTML += "<span> 0" + timer.seconds + "</span>"
        }
        else {
            clock.innerHTML += "<span>" + timer.seconds + "</span>"
        }
        
    }, 1000);
}


window.onload = function () {
    var deadline = new Date("August 22, 2020 10:25:10");
   setTimeout("location.reload(true);", 35000);
    startTimer("clock", deadline);
};