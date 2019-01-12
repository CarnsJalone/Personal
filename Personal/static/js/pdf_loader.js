$(document).ready(function(){

    var file_input = $('#pdf_parser_file_upload_form_file_upload');
    var file_submit = $('#pdf_parser_file_upload_form_submit_button');

    var verification_div = $('#pdf_extension_verification_div')

    // file_submit.click(function(event){
    //     var extension = file_input.val().split('.').pop()

    //     if (extension == '') {

    //     }

    //     if (extension != 'pdf') {
    //         event.preventDefault()
    //         alert('This is not a PDF, it will not parse properly.')
    //     } 
    // })

    file_input.change(function(event){

        console.log($(this))
        // var extension = file_input.val().split('.').pop()

        var file = event.target.files[0];
        
        var filename = file.name
        var extension = filename.split('.').pop()
        var file_size = file.size

        if (extension == '') {
            verification_div.css({
                'display' : 'block'
            })
            verification_div.html(
                "<p>The verification script has not detected a file format. Please be aware that if this is not a .pdf, the conversion will not take place successfully.</p>"
            )
            file_submit.prop(
                'disabled', false
                )
        } else if (extension == 'pdf') {
            verification_div.css({
                'display' : 'none'
            })
            file_submit.prop(
                'disabled', false
            )
        } else {
            verification_div.css({
                'display' : 'block'
            })

            verification_div.html(
                "<p>The file you are attempting to upload is in ." + extension + " format. The server side processing will not be able to properly parse the document. Please upload a file with a .pdf extension.</p>"
            )
            file_submit.prop(
                'disabled', true
                )
            }

        if (file_size < 1) {
            verification_div.css({
                'display' : 'block'
            })

            verification_div.html(
                "<p>The file you are attempting to upload is " + file_size + " bytes. Please upload a file with data in it.</p>"
            )
            file_submit.prop(
                'disabled', true
                )
        }
    })

    function grab_json() {
        
    }


})