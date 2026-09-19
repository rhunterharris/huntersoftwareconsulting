(() => {
  document.documentElement.classList.add('js');
  const menu = document.querySelector('.menu-toggle');
  const nav = document.getElementById('site-nav');
  const setMenu = (open) => {
    menu.setAttribute('aria-expanded', String(open));
    nav.toggleAttribute('data-open', open);
  };
  menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
      setMenu(false);
      menu.focus();
    }
  });
  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) setMenu(false);
  });
  window.matchMedia('(min-width: 56rem)').addEventListener('change', () => setMenu(false));
  const themeButton = document.getElementById('theme-toggle');
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  let chosenTheme;
  try { chosenTheme = localStorage.getItem('hsc-theme'); } catch (_) { /* Preference storage is optional. */ }
  const applyTheme = (theme) => {
    const dark = theme === 'dark';
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    themeButton.textContent = dark ? 'Use light theme' : 'Use dark theme';
    themeButton.setAttribute('aria-pressed', String(dark));
  };
  applyTheme(chosenTheme || (systemTheme.matches ? 'dark' : 'light'));
  themeButton.hidden = false;
  themeButton.addEventListener('click', () => {
    chosenTheme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    applyTheme(chosenTheme);
    try { localStorage.setItem('hsc-theme', chosenTheme); } catch (_) { /* The current page still works. */ }
  });
  systemTheme.addEventListener('change', () => {
    if (!chosenTheme) applyTheme(systemTheme.matches ? 'dark' : 'light');
  });
})();
