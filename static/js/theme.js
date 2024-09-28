// Seleziona l'elemento del pulsante e il tema attuale
const themeToggle = document.getElementById('theme-toggle');
const theme = document.getElementById('theme');

// Funzione per impostare il tema
function setTheme(mode) {
    if (mode === 'dark') {
        theme.classList.add('dark-mode');
        theme.classList.remove('light-mode');
        themeToggle.textContent = '☀️'; // Cambia icona per il tema chiaro
    } else {
        theme.classList.add('light-mode');
        theme.classList.remove('dark-mode');
        themeToggle.textContent = '🌙'; // Cambia icona per il tema scuro
    }
    localStorage.setItem('theme', mode); // Salva il tema scelto nel localStorage
}

// Carica il tema salvato o imposta di default la modalità dark
const savedTheme = localStorage.getItem('theme') || 'dark';
setTheme(savedTheme);

// Cambia il tema al clic del pulsante
themeToggle.addEventListener('click', () => {
    const currentTheme = theme.classList.contains('dark-mode') ? 'dark' : 'light';
    setTheme(currentTheme === 'dark' ? 'light' : 'dark');
});
