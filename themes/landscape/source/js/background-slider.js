(function() {
  'use strict';

  var config = window.backgroundConfig || { backgrounds: [], autoPlayInterval: 5000 };
  var backgrounds = config.backgrounds;
  var currentIndex = 0;
  var autoPlayTimer = null;
  var isTransitioning = false;

  var bgImages = document.querySelectorAll('.bg-image');
  var subtitleEl = document.getElementById('hero-subtitle');
  var prevBtn = document.getElementById('nav-prev');
  var nextBtn = document.getElementById('nav-next');

  function init() {
    if (backgrounds.length === 0) {
      console.warn('No backgrounds configured');
      return;
    }

    // Initialize background images
    bgImages.forEach(function(img, index) {
      if (backgrounds[index]) {
        img.style.backgroundImage = 'url(' + backgrounds[index].image + ')';
      }
    });

    // Update subtitle
    updateSubtitle();

    // Preload next image
    preloadImage(1);

    // Start autoplay
    startAutoPlay();

    // Bind events
    bindEvents();
  }

  function updateSubtitle() {
    if (subtitleEl && backgrounds[currentIndex]) {
      subtitleEl.style.opacity = '0';
      setTimeout(function() {
        subtitleEl.textContent = backgrounds[currentIndex].subtitle;
        subtitleEl.style.opacity = '0.9';
      }, 300);
    }
  }

  function preloadImage(index) {
    if (index >= backgrounds.length) {
      index = 0;
    }
    if (backgrounds[index]) {
      var img = new Image();
      img.src = backgrounds[index].image;
    }
  }

  function goToSlide(index) {
    if (isTransitioning || index === currentIndex || backgrounds.length === 0) {
      return;
    }

    isTransitioning = true;

    // Normalize index
    if (index < 0) {
      index = backgrounds.length - 1;
    } else if (index >= backgrounds.length) {
      index = 0;
    }

    // Update background images
    var currentBg = bgImages[currentIndex % bgImages.length];
    var nextBg = bgImages[index % bgImages.length];

    // Set next background image
    if (backgrounds[index]) {
      nextBg.style.backgroundImage = 'url(' + backgrounds[index].image + ')';
    }

    // Switch active class
    currentBg.classList.remove('active');
    nextBg.classList.add('active');

    // Update index
    currentIndex = index;

    // Update subtitle
    updateSubtitle();

    // Preload next image
    preloadImage((currentIndex + 1) % backgrounds.length);

    // Reset transition flag
    setTimeout(function() {
      isTransitioning = false;
    }, 800);

    // Reset autoplay
    resetAutoPlay();
  }

  function nextSlide() {
    goToSlide(currentIndex + 1);
  }

  function prevSlide() {
    goToSlide(currentIndex - 1);
  }

  function startAutoPlay() {
    if (backgrounds.length <= 1) return;
    autoPlayTimer = setInterval(nextSlide, config.autoPlayInterval);
  }

  function stopAutoPlay() {
    if (autoPlayTimer) {
      clearInterval(autoPlayTimer);
      autoPlayTimer = null;
    }
  }

  function resetAutoPlay() {
    stopAutoPlay();
    startAutoPlay();
  }

  function bindEvents() {
    if (prevBtn) {
      prevBtn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        prevSlide();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        nextSlide();
      });
    }

    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowLeft') {
        prevSlide();
      } else if (e.key === 'ArrowRight') {
        nextSlide();
      }
    });

    // Pause autoplay on hover
    var heroSection = document.getElementById('hero-section');
    if (heroSection) {
      heroSection.addEventListener('mouseenter', stopAutoPlay);
      heroSection.addEventListener('mouseleave', startAutoPlay);
    }

    // Visibility API - pause when tab is hidden
    document.addEventListener('visibilitychange', function() {
      if (document.hidden) {
        stopAutoPlay();
      } else {
        startAutoPlay();
      }
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
