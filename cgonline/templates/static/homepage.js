let wordlistEN = [
    'development',
    'art',
    'tinkering',
    'schmoovement'
]

let wordlistFR = [
    'developpement',
    'art',
    'bricolage',
    'schmoovement'
]

var currentPos = 0

function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
}

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

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function getCurrentLanguage() {
    let cookie = getCookie("django_language")
    switch (cookie) {
        case "en":
            return wordlistEN
        case "fr":
            return wordlistFR
    }
}

shuffle(wordlistEN)
shuffle(wordlistFR)
addTextAsChild(getCurrentLanguage())

//animate()
//setInterval(animate, 3000)