// Small JS for portfolio interactions
(function(){
  'use strict';
  // Example: close mobile nav after clicking a link
  document.addEventListener('click', function(e){
    var toggler = document.querySelector('.navbar-toggler');
    var nav = document.querySelector('.navbar-collapse');
    if(!toggler || !nav) return;
    if(e.target.matches('.nav-link')){
      if(window.getComputedStyle(toggler).display !== 'none'){
        toggler.click();
      }
    }
  });
})();
