
var sperm = document.getElementById("sperm");
var spermLeft = 0;
var spermTop = 0;
var proj1 = document.getElementById("projectile1");
var txt = document.getElementById("text");
var socket = io.connect({transports: ['websocket']})
socket.on('gamestate',parseGameState);

function move(e) {                                  //gives "You Win!" even if you're not in the exit, you just have
    if (e.keyCode === 39) {                         //to be so far left and so far down to trigger the "You Win" text
        spermLeft += 5;
        sperm.style.left = spermLeft + 'px'
        socket.emit()
        if (spermLeft >= 580) {
            spermLeft -= 5;
        }
        if (spermLeft >= 240 && spermTop >= 180) {
            txt.innerHTML = "You Win!";
            txt.style.color = 'blue';
            txt.style.fontSize = '350%';
        }
    }
    if (e.keyCode === 37) {
        spermLeft -= 5;
        sperm.style.left = spermLeft + 'px'
        if (spermLeft <= 0) {
            spermLeft += 5;
        }
        if (spermLeft >= 240 && spermTop >= 180) {
            txt.innerHTML = "You Win!";
            txt.style.color = 'blue';
            txt.style.fontSize = '350%';
        }
    }
    if (e.keyCode === 38) {
        spermTop -= 5;
        sperm.style.top = spermTop + 'px'
        if (spermTop <= 0) {
            spermTop += 5;
        }
        if (spermLeft >= 240 && spermTop >= 180) {
            txt.innerHTML = "You Win!";
            txt.style.color = 'blue';
            txt.style.fontSize = '350%';
        }
    }
    if (e.keyCode === 40) {
        spermTop += 5;
        sperm.style.top = spermTop + 'px'
        if (spermTop >= 380) {
            spermTop -= 5;
        }
        if (spermLeft >= 240 && spermTop >= 180) {
            txt.innerHTML = "You Win!";
            txt.style.color = 'blue';
            txt.style.fontSize = '350%';
        }
    }
}
document.onkeydown = move;