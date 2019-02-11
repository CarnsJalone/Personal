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
        $(window).scrollTop(0);
    }

    function minimize() {
        image.attr('class', 'minimized_resume_img_img');
        resume.attr('class', 'minimized_resume_img_div');
        modal.attr('class', 'minimized_modal');
        close_button.attr('class' , 'minimized_close_button');
        modal_container.fadeOut(50);
        $(window).scrollTop(image.offset().top);
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

    contact_form_span.mouseover(function(event){
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

    var input_field_position = first_name_field.position();

    contact_form_p.click(function(event){
        scroll(0, input_field_position.top);
    })

    // Dancing MJ Animation Code Block

    var modal_with_opacity = $('#connect_full_page_loader_background');
    var modal_without_opacity = $('#connect_full_page_loader_no_opacity');
    var dancing_mj_loader = $('#connect_dancing_mj_gif');
    var curtain_1 = $('#connect_mj_curtain_1');
    var curtain_2 = $('#connect_mj_curtain_2');
    var submit_button = $('#connect_page_form_submit_button');

    submit_button.click(function(event){
        engage_loader();
    })

    function engage_loader(){
        modal_with_opacity.attr('class', 'modal_background_engaged');
        modal_without_opacity.attr('class', 'modal_no_opacity_engaged');
        dancing_mj_loader.attr('class', 'modal_gif_engaged');
        curtain_1.attr('class', 'modal_curtain_1_engaged');
        curtain_2.attr('class', 'modal_curtain_2_engaged');
    }

    // Link Animations

    // link_text_array.forEach(function(letter, index){
    //     replaced_html = ''
    //     replaced_html += '<span class="inset_wave">' + letter + '</span>';
    //     // temp_array = temp_array.splice(index, 1, replaced_html);
    //     // temp_array = temp_array.push(replaced_html)
    //     window.setTimeout(function(){
    //         replaced_html_array.push(replaced_html)
    //         functional_link.html(replaced_html_array)
    //     }, 3000);   

    // })
          
    // var functional_link = $('.functional_link')
    // var vanilla_func_link = document.getElementsByClassName('functional_link')
    // var alteration_speed = 60;
    // var link_text = functional_link.text();
    // var current_array = link_text.split("");
    // var target_array = []
    // index = 0;

    // console.log(current_array);

    // function reset_html() {
    //     functional_link.html("");
    // }

    // function inset_wave() {

    //     altered_html = '';
    //     functional_link.html();
    //     if (index < link_text.length) {
    //         altered_html += '<span class="inset_wave">' + link_text[index] + '</span>';
    //         target_array.push(altered_html)
    //         console.log(target_array);
    //         current_array[index] = target_array[index]
    //         functional_link.append(current_array[index])
    //         index++;
    //         setTimeout(inset_wave, alteration_speed);
    //     }
    // }




    // functional_link.hover(function(event){
    //     reset_html()
    //     inset_wave();
    // })

})