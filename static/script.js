const darkModeButton = document.getElementById('dark-mode-toggle');

function updateDarkModeButtonText() {
    if (!darkModeButton) {
        return;
    }

    if (document.body.classList.contains('dark-mode')) {
        darkModeButton.textContent = '☀️ Light Mode';
    } else {
        darkModeButton.textContent = '🌙 Dark Mode';
    }
}

if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
}

updateDarkModeButtonText();

if (darkModeButton) {
    darkModeButton.addEventListener('click', function () {
        document.body.classList.toggle('dark-mode');

        if (document.body.classList.contains('dark-mode')) {
            localStorage.setItem('darkMode', 'enabled');
        } else {
            localStorage.setItem('darkMode', 'disabled');
        }
        updateDarkModeButtonText();
    });
}