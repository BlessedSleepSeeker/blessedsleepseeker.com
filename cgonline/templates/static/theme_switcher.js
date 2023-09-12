
function themeSwitch() {
    const theme = localStorage.getItem('theme')
    if (theme == 'dark') {
        localStorage.setItem('theme', "light")
        document.documentElement.setAttribute('data-bs-theme','light')
        document.getElementById('iconSwitch').setAttribute('class', 'bi bi-moon-stars-fill')
    }
    else {
        localStorage.setItem('theme', "dark")
        document.documentElement.setAttribute('data-bs-theme','dark')
        document.getElementById('iconSwitch').setAttribute('class', 'bi bi-brightness-high-fill')
    }
}

function updateTheme() {
    const theme = localStorage.getItem('theme')
    if (theme == 'dark') {
        document.documentElement.setAttribute('data-bs-theme','light')
        document.getElementById('iconSwitch').setAttribute('class', 'bi bi-moon-stars-fill')
        document.getElementById('navLogoLight').style.display = 'block'
        document.getElementById('navLogoDark').style.display = 'none'
    }
    else {
        document.documentElement.setAttribute('data-bs-theme','dark')
        document.getElementById('iconSwitch').setAttribute('class', 'bi bi-brightness-high-fill')
        document.getElementById('navLogoLight').style.display = 'none'
        document.getElementById('navLogoDark').style.display = 'block'
    }
}

document.getElementById('btnSwitch').addEventListener('click',()=>{
    themeSwitch()
    updateTheme()
})


updateTheme()