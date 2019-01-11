$(document).ready(function(){

    var image = $('#resume_page_img_img')
    var resume = $('#resume_page_img_div')
    var modal = $('#full_page_modal')

    var modal_container = $('#about_me_click_for_full_size_modal_container');
    var modal_span = $('#about_me_click_for_full_size_modal_span');


    function enlarge() {
        image.attr('class', 'enlarged_resume_img_img');
        resume.attr('class', 'enlarged_resume_img_div');
        modal.attr('class', 'enlarged_modal');
    }

    function minimize() {
        image.attr('class', 'minimized_resume_img_img');
        resume.attr('class', 'minimized_resume_img_div');
        modal.attr('class', 'minimized_modal')
    }

    image.click(function(event){
        if (image.hasClass("minimized_resume_img_img")){
            enlarge()
        } 
        else if (image.hasClass("enlarged_resume_img_img")) {
            minimize()
        }
        else {
            alert('Something happened...')
        }
    })

    modal.click(function(){
        if (image.hasClass("enlarged_resume_img_img")) {
            minimize()
        }
    })

    modal.mouseleave(function(){
        if (image.hasClass("enlarged_resume_img_img")) {
            minimize()
        }
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