const wordlistEN = [
    'code',
    'art',
    'DIY',
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
    document.getElementById('changing-text').textContent = new_word
}

function animate() {
    changeText(getNext(wordlistEN))
}

animate()
setInterval(animate, 3000)