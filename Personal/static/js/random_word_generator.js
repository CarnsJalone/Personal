$(document).ready(function(){

    console.log('hello')

    var submit_button = $("#random_word_generator_submit_button_ajax");

    submit_button.click(function(event){
        event.preventDefault();
        $.ajax({
            type: "GET",
            url: "/projects/random_word_generator",
            dataType: 'json',
            data: {'random_word' : random_word}, 
            success: function(data) {
                alert(data);
                console.log(data);
                // console.log("hello");
            }

        });
    });
});