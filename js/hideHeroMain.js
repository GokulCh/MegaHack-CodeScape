function hideHeroMain() {
  var heroMain = document.querySelector('.hero-main');
  var heroTools = document.querySelector('.hero-tools');

  // Hero Main
  heroMain.style.opacity = 0;
  heroMain.style.transition = 'opacity 0.5s ease';

  setTimeout(function () {
    heroMain.style.display = 'none';
  }, 500);

  // Hero Tools

}