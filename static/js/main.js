// Theme toggle and simple UI enhancements
(() => {
  const root = document.documentElement;
  const btn = document.getElementById('themeToggle');
  const storageKey = 'sooraj_theme';

  function applyTheme(t) {
    root.setAttribute('data-theme', t);
  }

  function readPreference(){
    return localStorage.getItem(storageKey) || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }

  let theme = readPreference();
  applyTheme(theme);

  if(btn){
    btn.addEventListener('click', () => {
      theme = theme === 'dark' ? 'light' : 'dark';
      applyTheme(theme);
      localStorage.setItem(storageKey, theme);
    });
  }
})();

