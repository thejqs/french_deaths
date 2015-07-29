 var toggle = true



$('#cause').click(function(e) {
    e.preventDefault;
    console.log(toggle)

    if (toggle) {
            
        $(this).next().fadeIn()
        toggle = false
        
    } else {

        $(this).next().fadeOut()
        toggle = true
        
    };

});


// $('#cause').click(function() {
//     $('#revealdeaths').hide()
// });


// $('#cause').mouseenter(
//         function() {
//                 this.show();
//         },
//         function() {
//         $(this).hide();
//         }
// );