$(document).ready(function(){

    var image = $('#resume_page_img_img');
    var resume = $('#resume_page_img_div');
    var modal = $('#full_page_modal');
    var close_button = $('#full_page_modal_close');
    var close_button_i = $('#close_button_close_button');

    var modal_container = $('#about_me_click_for_full_size_modal_container');
    var modal_span = $('#about_me_click_for_full_size_modal_span');


    function enlarge() {
        image.attr('class', 'enlarged_resume_img_img');
        resume.attr('class', 'enlarged_resume_img_div');
        modal.attr('class', 'enlarged_modal');
        close_button.attr('class', 'enlarged_close_button');
    }

    function minimize() {
        image.attr('class', 'minimized_resume_img_img');
        resume.attr('class', 'minimized_resume_img_div');
        modal.attr('class', 'minimized_modal');
        close_button.attr('class' , 'minimized_close_button');
    }


    image.click(function(event){
        if (image.hasClass("minimized_resume_img_img")){
            enlarge()
        } 
    })

    close_button.click(function(event){
        if (image.hasClass("enlarged_resume_img_img")) {
            minimize()
        }
    })

    close_button.hover(function(event){
        close_button_i.attr('class', 'fas fa-times fa-3x');
    })

    close_button.mouseleave(function(event){
        close_button_i.attr('class', 'fas fa-times fa-2x');
    })

    $(document).mouseleave(function(event){
        minimize()
    })

    image.hover(function(event){
        if (image.hasClass("minimized_resume_img_img")) {
            setTimeout(function(){
                alert('Hello')
            }, 5000
        });
    })


    // image.hover(function(event){
    //     modal_container.fadeIn(250)
    //     modal_span.html('<p>Click on resume for view full page image.</p>')
    //     image.css({
    //         'cursor' : 'zoom-in'
    //     })
    // })

    // image.mouseleave(function(event){
    //     modal_container.fadeOut(250)
    //     modal_span.html('<p>Click on resume for view full page image.</p>')
    //     resume.css({
    //         'transform' : 'scale(1)',
    //         'cursor' : 'pointer'
    //     })
    // })

    // // Function handling clicking on resume
    // image.click(function(event){
    //     if (image.hasClass("enlarged")) {
    //         minimize_resume()
    //     }
    //     else {
    //         enlarge_resume()
    //     }
    // })

    // function enlarge_resume(){
    //     resume.css({
    //         'cursor' : 'zoom-out',
    //     })
    //     modal_span.html("<p>Click again or move mouse outside enlarged r&#233sum&#233 to resume browsing.")
    //     image.addClass("enlarged")
    // }

    // function minimize_resume(){
    //     resume.css({
    //         'cursor' : 'zoom-in',
    //     })
    //     modal_span.html("<p>Click on resume for view full page image.</p>")
    //     image.removeClass("enlarged")
    // }

})