const textAreaYour = document.querySelector('.word_your');
const textAreaUser = document.querySelector('.word_user');

const nextWord = document.querySelector('.predict_your');
const nextWordSec = document.querySelector('.predict_user');
const button = document.querySelector('.click_your');
const buttonSec = document.querySelector('.click_user');

const container = document.getElementById('container');

//const ip = '138.68.93.61'
const ip = '127.0.0.1'
const port = '8080'


textAreaYour.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') ev.preventDefault();
}, false);


textAreaUser.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') ev.preventDefault();
}, false);


textAreaYour.addEventListener('input', (ev) => {
    const text = textAreaYour.value;
    const sentence = text.split(" ");
    if (ev.key === 'Enter') {
        textAreaYour.value = text + nextWord.innerHTML;
        nextWord.innerHTML = " ";
        return;
    }
    fetch('http://' + ip + ':' + port + '/api/v1', {
        method: 'POST',
        headers: new Headers(),
        body: sentence[sentence.length - 1]

    }).then((res) => {
            // console.log(res);
            return res.text()
        })
        .then((data) => {
             nextWord.innerHTML = data;
            // console.log(document.getElementById('predict_your').value);

        })
}, false);


textAreaUser.addEventListener('input', (ev) => {
    const text = textAreaUser.value;
    const sentence = text.split(" ");
    if (ev.key === 'Enter') {
        textAreaUser.value = text + nextWordSec.innerHTML;
        nextWordSec.innerHTML = " ";
        return;
    }
    fetch('http://' + ip + ':' + port + '/api/v1', {
        method: 'POST',
        headers: new Headers(),
        body: sentence[sentence.length - 1]

    }).then((res) => {
            // console.log(res);
            return res.text()
        })
        .then((data) => {
             nextWordSec.innerHTML = data;
            // console.log(document.getElementById('predict_your').value);

        })
}, false);




document.body.addEventListener('keypress', (ev) => {
    const shifted = ev.shiftKey;
    const ctrl = ev.ctrlKey;
    const end_key = ev.keyCode;
    if (ctrl && end_key == 35) {
        const x = document.getElementById("predict_your").value;
        container.innerHTML += 'User1:   '+ x + '<br />';
        document.getElementById("predict_your").value = "";

    }
    if (shifted && end_key == 35) {
    const x = document.getElementById("predict_user").value;
    document.getElementById("predict_user").value = "";
    container.innerHTML += 'User2:   '+ x + '<br />';
    }

}, false )
