$(document).ready(function(){

    var image = $('#resume_page_img_img')
    var modal_container = $('#about_me_click_for_full_size_modal_container');
    var modal_span = $('#about_me_click_for_full_size_modal_span');
    var resume = $('#resume_page_img_div')

    image.hover(function(event){
        modal_container.fadeIn(250)
        modal_span.html('<p>Click on resume for view full page image.</p>')
        image.css({
            'cursor' : 'zoom-in'
        })
    })

    image.mouseleave(function(event){
        modal_container.fadeOut(250)
        modal_span.html('<p>Click on resume for view full page image.</p>')
        resume.css({
            'transform' : 'scale(1)',
            'cursor' : 'pointer'
        })
    })

    // Function handling clicking on resume
    image.click(function(event){
        if (image.hasClass("enlarged")) {
            minimize_resume()
        }
        else {
            enlarge_resume()
        }
    })

    function enlarge_resume(){
        resume.css({
            'transform' : 'scale(1.275)',
            'cursor' : 'zoom-out',
        })
        modal_span.html("<p>Click again or move mouse outside enlarged r&#233sum&#233 to resume browsing.")
        image.addClass("enlarged")
    }

    function minimize_resume(){
        resume.css({
            'transform' : 'scale(1)',
            'cursor' : 'zoom-in',
        })
        modal_span.html("<p>Click on resume for view full page image.</p>")
        image.removeClass("enlarged")
    }

})