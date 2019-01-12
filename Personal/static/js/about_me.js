$(document).ready(function(){

    var image = $('#resume_page_img_img');
    var resume = $('#resume_page_img_div');
    var modal = $('#full_page_modal');
    var close_button = $('#full_page_modal_close');
    var close_button_i = $('#close_button_close_button');

    var modal_container = $('#about_me_click_for_full_size_modal_container');
    var modal_span = $('#about_me_click_for_full_size_modal_span');

    // var download_resume = $('#resume_page_download_resume_button');
    var resume_form = $('#resume_page_download_resume_form')


    function enlarge() {
        image.attr('class', 'enlarged_resume_img_img');
        resume.attr('class', 'enlarged_resume_img_div');
        modal.attr('class', 'enlarged_modal');
        close_button.attr('class', 'enlarged_close_button');
        modal_container.fadeOut(50);
    }

    function minimize() {
        image.attr('class', 'minimized_resume_img_img');
        resume.attr('class', 'minimized_resume_img_div');
        modal.attr('class', 'minimized_modal');
        close_button.attr('class' , 'minimized_close_button');
        modal_container.fadeOut(50);
    }

    function display_help_box() {
        if (image.hasClass("minimized_resume_img_img")){
            modal_container.fadeIn(250);
            modal_container.html("<p>Click inside the r&#233sum&#233 to enlarge.</p>")
        }
    }


    image.click(function(event){
        if (image.hasClass("minimized_resume_img_img")){
            enlarge()
        } 
    })

    image.hover(function(event){
        display_help_box()
    });

    image.mouseleave(function(event){
        if (image.hasClass("minimized_resume_img_img")){
            minimize()
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
        if (image.hasClass("enlarged_resume_img_img")){
            minimize()
        }
    })

    resume_form.submit(function(event){
        // event.preventDefault();
        // console.log(event)
        $.ajax({
            type: "GET",
            url: "/about_me/download_resume",
            dataType: 'text', 
            contentType: 'application/pdf',
            success: function(data){
                console.dir(data)
                // console.log(data.name)
                console.log(data['Content-Disposition'])
            }

        })
    })
})