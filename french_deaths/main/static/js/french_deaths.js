$('.cause').click(function(e) {
    e.preventDefault();
    if ($(this).next().next().is(":visible")) {
        $(this).next().next().fadeOut()
    } else {
        $(this).next().next().fadeIn()
    }
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

