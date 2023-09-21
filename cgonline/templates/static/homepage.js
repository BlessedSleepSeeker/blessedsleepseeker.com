const wordlistEN = [
    'development',
    'pixel art',
    'tinkering',
    'schmoovement'
]

const wordlistFR = [
    'code',
    'art',
    'FLTM',
]

var currentPos = 0

function getNext(language) {
    if (currentPos + 1 > language.length) {
        currentPos = 0
    }
    return language[currentPos++];
}

function changeText(new_word) {
    //document.getElementById('changing-text').textContent = new_word
}

function animate() {
    //changeText(getNext(wordlistEN))
}

function addTextAsChild(wordlist) {
    for (const word of wordlist) {
        let elem = document.createElement('li')
        elem.classList.add('changing-text-item')
        elem.classList.add('list-unstyled')
        elem.textContent = word
        document.getElementById('changingText').appendChild(elem)
    }
}

addTextAsChild(wordlistEN)

//animate()
//setInterval(animate, 3000)