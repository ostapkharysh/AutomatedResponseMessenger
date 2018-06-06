const textArea = document.querySelector('.word');
const nextWord = document.querySelector('.predict');
const button = document.querySelector('.click');

textArea.addEventListener('keydown', (ev) => {
    if (ev.key === 'Enter') ev.preventDefault();
}, false);


textArea.addEventListener('keyup', (ev) =>{
    const text = textArea.value;
    if (ev.key === 'Enter'){
        textArea.value = text + nextWord.innerHTML;
        nextWord.innerHTML = " ";
        return;
    }
    nextWord.innerHTML = ' aaaa ';
}, false);



button.addEventListener('click', (ev) => {
    fetch('http://127.0.0.1:5000/api/v1', {
        method: 'POST',
        headers : new Headers()
    })

        .then((res) => {
            console.log(res);
            return res.text() })
        .then((data) => {
//            console.log(data)
             console.log(document.getElementById('predict').value);
        })

}, false);
