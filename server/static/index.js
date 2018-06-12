const textAreaOne = document.querySelector('.user__text_one');
const textAreaTwo = document.querySelector('.user__text_two');

const nextWordOne = document.querySelector('.user__prediction_one');
const nextWordTwo = document.querySelector('.user__prediction_two');

const container = document.getElementById('container');

//const ip = '138.68.93.61'
const ip = '127.0.0.1';
const port = '8080';


textAreaOne.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') ev.preventDefault();
}, false);


textAreaTwo.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') ev.preventDefault();
}, false);


textAreaOne.addEventListener('input', async (ev) => {
    const text = textAreaOne.value;
    const sentence = text.split(" ");

    const data = await fetchNextWord(ip, sentence[sentence.length - 1]);
    nextWordOne.innerHTML = data;

}, false);


textAreaTwo.addEventListener('input', async (ev) => {
    const text = textAreaTwo.value;
    const sentence = text.split(" ");

    const data = await fetchNextWord(ip, sentence[sentence.length - 1]);
    nextWordTwo.innerHTML = data;

}, false);


textAreaOne.addEventListener('keyup', async (ev) => {
    const text = textAreaOne.value;
    const predictedWord = nextWordOne.innerHTML;
    if (ev.key === 'Enter' && predictedWord) {
        textAreaOne.value = text + " " + predictedWord;
        nextWordOne.innerHTML = await fetchNextWord(ip, predictedWord);
        return;
    }
}, false);


textAreaTwo.addEventListener('keyup', async (ev) => {
    const text = textAreaTwo.value;
    const predictedWord = nextWordTwo.innerHTML;
    if (ev.key === 'Enter' && predictedWord) {
        textAreaTwo.value = text + " " + predictedWord;
        nextWordTwo.innerHTML = await fetchNextWord(ip, predictedWord);
        return;
    }
}, false);


document.body.addEventListener('keypress', (ev) => {
    const shifted = ev.shiftKey;
    const ctrl = ev.ctrlKey;
    const end_key = ev.keyCode;

    if (ctrl && end_key === 35) {
        const text = textAreaOne.value;
        if (!text) return;
        textAreaOne.value = "";
        nextWordOne.innerHTML = "";
        container.appendChild(new Message('one', text).render());

    }
    if (shifted && end_key === 35) {
        const text = textAreaTwo.value;
        if (!text) return;
        textAreaTwo.value = "";
        nextWordTwo.innerHTML = "";
        container.appendChild(new Message('two', text).render());
    }

}, false);


class Message {
    constructor(modifier, text) {
        this.modifier = modifier;
        this.text = text;
    }

    render() {
        const messageBox = document.createElement('div');
        messageBox.classList.add('chat__message');
        messageBox.classList.add('chat__message_' + this.modifier);

        const message = document.createElement('p');
        message.classList.add("chat__box");
        message.classList.add("chat__box_" + this.modifier);
        message.innerHTML = this.text;

        messageBox.appendChild(message);

        return messageBox;

    }
}


const fetchNextWord = (ip, word) => {
    return fetch('http://' + ip + ':' + port + '/api/v1', {
        method: 'POST',
        headers: new Headers(),
        body: word

    }).then((res) => {
        return res.text()
    })
        .then((data) => {
            return data;
        })

};
