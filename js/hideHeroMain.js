function hideHeroMain() {
  var heroMain = document.querySelector('.hero-main');
  var heroTools = document.querySelector('.hero-tools');

  // Hero Main
  heroMain.style.opacity = 0;
  heroMain.style.transition = 'opacity 0.1s ease';

  setTimeout(function () {
    heroMain.style.display = 'none';
  }, 500);

  // Slide the image to the left 
  var previewImage = document.getElementById('previewImage');
  var duration = 3000;  
  var startTime = null;
  var startMargin = 0; 
  var startScale = 1.2; 

  function animate(time) {
    if (!startTime) {
      startTime = time;
    }
    var progress = (time - startTime) / duration;
    var easedProgress = easeOutCubic(progress);

    previewImage.style.marginLeft = -startMargin * easedProgress + 'px';
    previewImage.style.transform = 'scale(' + (startScale + (7 - startScale) * easedProgress) + ')'; 

    if (progress < 1) {
      requestAnimationFrame(animate);
    }
  }

  requestAnimationFrame(animate);
}


function easeOutCubic(t) {
 return 1 - Math.pow(1 - t, 3);
}


