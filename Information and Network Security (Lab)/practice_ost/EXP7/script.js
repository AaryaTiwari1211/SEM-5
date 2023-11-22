function sendPSWD() {
    // alert("hello");
    dispPSWD.value = pswd.value
}

function sendRAND() {
    dispRAND.value = RAND.value
}


function genRAND() {
    const randomNUM = Math.floor(Math.random() * (999 - 100 + 1) + 100);
    RAND.value = randomNUM
    return randomNUM
}

function authenticate() {
    num1 = pswd.value % dispRAND.value
    num2 = dispPSWD.value % RAND.value

    if (num1 == num2) {
        result.innerHTML = "Authentication Successful"
    }
    else {
        result.innerHTML = "Authentication Unsuccessful"
    }
}