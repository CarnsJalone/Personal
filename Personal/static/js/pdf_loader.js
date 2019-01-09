$(document).ready(function(){

    var file_input = $('#pdf_parser_file_upload_form_file_upload');
    var file_submit = $('#pdf_parser_file_upload_form_submit_button');

    var verification_div = $('#pdf_extension_verification_div')

    file_submit.click(function(event){
        var extension = file_input.val().split('.').pop()

        if (extension != 'pdf') {
            event.preventDefault()
            alert('This is not a PDF, it will not parse properly.')
        } 
    })

    file_input.change(function(event){

        console.log($(this))
        var extension = file_input.val().split('.').pop()

        if (extension != 'pdf') {
            verification_div.css({
                'display' : 'block'
            })
            file_submit.prop(
                'disabled', true
                )
        }
        else {
            verification_div.css({
                'display' : 'none'
            })
            file_submit.prop(
                'disabled', false
            )
        }
    })


})