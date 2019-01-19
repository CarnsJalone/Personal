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

    // Phone Animation

    var phone_span = $('#connect_by_phone_span');
    var phone_text = $('#connect_by_phone_p');
    var phone_icon = $('#connect_by_phone_i');

    phone_span.hover(function(event){
        activate_phone_animation()
    })

    phone_span.mouseleave(function(event){
        deactivate_phone_animation()
    })

    function activate_phone_animation() {
        phone_icon.attr('class', 'fas fa-mobile-alt phone_animation');
        phone_text.attr('class', 'emboldened_font connect_centered_li');
    }

    function deactivate_phone_animation() {
        phone_icon.attr('class', 'fas fa-mobile-alt');
        phone_text.attr('class', 'connect_centered_li');
    }

    // Email Animation

    var email_span = $('#connect_by_mail_span');
    var email_text = $('#connect_by_mail_p');
    var email_icon = $('#connect_by_email_i');

    email_span.hover(function(event){
        activate_mail_animation()
    })

    email_span.mouseleave(function(event){
        deactivate_mail_animation()
    })

    function activate_mail_animation() {
        email_icon.attr('class', 'far fa-envelope mail_animation');
        email_text.attr('class' , 'emboldened_font connect_centered_li');
    }

    function deactivate_mail_animation() {
        email_icon.attr('class', 'far fa-envelope-open');
        email_text.attr('class', 'connect_centered_li');
    }

    // Contact Form Animation

    var contact_form_span = $('#connect_by_contact_form');
    var contact_form_i = $('#connect_by_contact_form_i');
    var contact_form_p = $('#connect_by_contact_form_p');
    var first_name_field = $('#connect_page_form_first_name')
    var input_string = 'Give Me A Shout!';
    var current_index = 0;

    contact_form_span.hover(function(event){
        activate_placeholder_animation();
        activate_contact_form_animation();
    })

    contact_form_span.mouseleave(function(event){
        deactivate_placeholder_animation();
        deactivate_contact_form_animation();
    })

    function verify_placeholder(){
        
        var current_placeholder = first_name_field.attr('placeholder');

        if (current_placeholder != input_string) {
            first_name_field.attr('placeholder', '');
        } else if (current_placeholder != '') {
            first_name_field.attr('placeholder', '');
        } else if (current_placeholder != None) {
            first_name_field.attr('placeholder', '');
        }
    }

    // Credit to Michael Smart (Sorry I took your function from codepen)
    function randDelay(min, max) {
        return Math.floor(Math.random() * (max-min+1)+min);
    }

    function ph_letter_tick(string, input_field) {
        var placeholder_array = string.split('');
        var original_string = string;
        var input = input_field;
        var current_letter = input_field.attr("placeholder");
        var placeholder = current_letter + placeholder_array[current_index];

        setTimeout(function(){
            input_field.attr("placeholder", placeholder);
            current_index++;

            if (current_index < placeholder_array.length) {
                ph_letter_tick(original_string, input)
            }
        }, randDelay(50,90));
    }

    function placeholder() {
        first_name_field.attr("placeholder", "");
        ph_letter_tick(input_string, first_name_field);
    }

    function activate_placeholder_animation(){
        current_index = 0;
        placeholder();
        verify_placeholder();
    }

    function deactivate_placeholder_animation(){
        first_name_field.attr('placeholder', '');
        verify_placeholder();
        // first_name_field.blur()
    }
    
    function activate_contact_form_animation(){
        contact_form_i.attr('class', 'far fa-file-alt contact_form_animation')
        contact_form_p.attr('class', 'emboldened_font connect_centered_li');
    }

    function deactivate_contact_form_animation(){
        contact_form_i.attr('class', 'far fa-file-alt');
        contact_form_p.attr('class', 'connect_centered_li');
    }






})