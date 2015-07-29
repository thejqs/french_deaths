function showDeaths() {
    $('.revealdeaths').show();

    $.ajax({
            url: '/all_deaths/',
            success: function(result) {
                $('.revealdeaths').show();

                $(result).each(function() {
                    console.log(this);

                    var causes = this.fields.year + " :: <b>" +
                    this.fields.number_of_deaths + "</b> :: " +
                    this.fields.sex + "</br"


                })

                // $('#posts').html(result);
            }
        })
}




// $('#cause').mouseenter(
//         function() {
//                 this.show();
//         },
//         function() {
//         $(this).hide();
//         }
// );