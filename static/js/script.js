
let btnResetear = document.querySelector('.btnReset');
let btnCoins = document.querySelectorAll('.getCoinsBtn');
let valueReset = document.getElementById('cantMov').getAttribute("value");
let HSDiv = document.querySelector('.highScore');

if (valueReset === '15') {
    btnResetear.style.display = "block";
    HSDiv.innerHTML = `<p> **** END OF THE GAME **** </p>`;

    for (i in btnCoins) {
        btnCoins[i].disabled = true;
    }
} else {
    btnResetear.style.display = "none";
    HSDiv.innerHTML = ""
}


function resetear() {
    let URL = '/destroy_session';
    let settings = {
        method: 'GET'
    }

    fetch(URL, settings)
        .then(response => {
            if (response.ok) {
                return response.json()
            }
        })
        .then(data => {
            window.location.href = '/';
        });
}

btnResetear.addEventListener('click', resetear)