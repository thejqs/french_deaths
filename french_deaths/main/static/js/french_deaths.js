$('.cause').click(function(e) {
    e.preventDefault();
    if ($(this).next().next().is(":visible")) {
        $(this).next().next().fadeOut()
    } else {
        $(this).next().next().fadeIn()
    }
});


$(function() {
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});




// $('.cause').click(function() {
//     $('.reveadeaths').fadeIn()
//     //     if ($(this).next().is(":visible")) {
//     //     $(this).next().fadeOut()
        
//     // };
// });




// $('.cause').click(function() {
//     // console.log($(this).next().is(":visible"));
//     if ($(this).next().fadeOut().is(":visible")) {
//         $(this).next().fadeOut()

//     };

// )};



// $('.cause').click(function() {
//     $(this).show()
// });

