function hideHeroMain() {
  var heroMain = document.querySelector('.hero-main');
  var heroTools = document.querySelector('.hero-tools');
  var duplicateHeroTools = document.querySelector('.hero-tools-duplicate');
  var heroContainer = document.querySelector('.hero-container');



  // Hero Main
  heroMain.style.opacity = 0;
  heroMain.style.transition = 'opacity 0.5s ease';

  setTimeout(function () {
    heroMain.style.display = 'none';
  }, 500);

  // Slide the image to the left with a smoother transition and zoom effect
  var previewImage = document.getElementById('previewImage');

  heroTools.style.opacity = 0;
  heroTools.style.transition = 'opacity 0.5s ease';
  

  setTimeout(function () {
    heroTools.style.opacity = 100;
    heroTools.style.transition = 'opacity 0.5s ease';
  }, 700);
  

  var duration = 1500;  // Adjust the duration here
  var startTime = null;
  var startMargin = 0; // Adjust the starting margin
  var startScale = 1.5; // Adjust the starting scale

  function animate(time) {
    if (!startTime) {
      startTime = time;
    }
    var progress = (time - startTime) / duration;
    var easedProgress = easeOutCubic(progress);

    previewImage.style.marginLeft = -startMargin * easedProgress + 'px';
    previewImage.style.transform = 'scale(' + (startScale + (7 - startScale) * easedProgress) + ')'; // Adjust the target scale value
    
    if (progress < 1) {
      requestAnimationFrame(animate);
    }
  }

  requestAnimationFrame(animate);
}

// Easing function for smoother animation
function easeOutCubic(t) {
  return 1 - Math.pow(1 - t, 3);
}

function showDuplicateHeroTools() {
  // Append the duplicate element to the existing flex container
  heroContainer.appendChild(duplicateHeroTools);
  
  duplicateHeroTools.style.display = 'flex'; // Or 'block' depending on the original display property
}