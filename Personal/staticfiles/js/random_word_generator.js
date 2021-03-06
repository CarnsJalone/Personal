$(document).ready(function(){

    var submit_button = $("#random_word_generator_submit_button_ajax");
    var name_generation_submit_button = $('#random_name_generator_submit_button_ajax');

    var destination_span = $("#random_word_generator_destination_span");
    var name_destination_span = $('#random_name_generator_destination_span');

    submit_button.click(function(event){
        event.preventDefault();
        $.ajax({
            type: "GET",
            url: "/projects/random_word_generator_ajax",
            dataType: 'json',
            success: function(data) {
                destination_span.html(data.random_word)
            }

        });
    });

    name_generation_submit_button.click(function(event){
        event.preventDefault();
        $.ajax({
            type: "GET",
            url: "/projects/random_name_generator",
            dataType: 'json', 
            success: function(data) {
                name_destination_span.html(data.randomly_generated_name)
            }
        })
    })


});