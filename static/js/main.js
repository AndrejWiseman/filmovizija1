

// mobilni meni //////////////
document.addEventListener('DOMContentLoaded', () => {
  const navbar = document.querySelector('#navbar');
  let lastScrollTop = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
    if (currentScroll > lastScrollTop) {
      // Skrolovanje na dole
      navbar.classList.add('-translate-y-full');
    } else {
      // Skrolovanje na gore
      navbar.classList.remove('-translate-y-full');
    }
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // Za mobilne uređaje ili negativno skrolovanje
  });

  const mobileMenuButton = document.querySelector('button[aria-expanded]');
  const mobileMenu = document.querySelector('.lg\\:hidden > .z-30');
  const menuOverlay = document.querySelector('.lg\\:hidden > .z-20');
  const closeMenuButton = document.querySelector('.lg\\:hidden .bg-white .h-6.w-6');

  mobileMenuButton.addEventListener('click', () => {
    const expanded = mobileMenuButton.getAttribute('aria-expanded') === 'true' || false;
    mobileMenuButton.setAttribute('aria-expanded', !expanded);
    mobileMenu.classList.toggle('hidden', expanded);
    menuOverlay.classList.toggle('hidden', expanded);
  });

  closeMenuButton.addEventListener('click', () => {
    mobileMenuButton.setAttribute('aria-expanded', false);
    mobileMenu.classList.add('hidden');
    menuOverlay.classList.add('hidden');
  });

  // Zatvori mobilni meni kada se klikne van njega
  document.addEventListener('click', (event) => {
    if (!mobileMenu.contains(event.target) && !mobileMenuButton.contains(event.target) && !closeMenuButton.contains(event.target)) {
      mobileMenuButton.setAttribute('aria-expanded', false);
      mobileMenu.classList.add('hidden');
      menuOverlay.classList.add('hidden');
    }
  });

  // Osiguraj da je meni inicijalno sakriven
  mobileMenuButton.setAttribute('aria-expanded', false);
  mobileMenu.classList.add('hidden');
  menuOverlay.classList.add('hidden');
});