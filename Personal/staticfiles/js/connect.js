$(document).ready(function(){

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


})