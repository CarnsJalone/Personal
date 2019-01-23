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
        // var extension = file_input.val().split('.').pop()

        var file = event.target.files[0];
        var filename = file.name
        var file_size = file.size
        var has_file_extension = filename.includes('.')

        if (has_file_extension) {

            var extension = filename.split('.').pop()

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
                    "<p>The file you are attempting to upload appears to be a(n) " + extension + " file. The server side processing will not be able to properly parse the data. Please try again with a pdf file.</p>"
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
                    "<p>The file you are attempting to upload is " + file_size + " bytes. There's nothing here to convert. Please upload a file with data in it.</p>"
                )
                file_submit.prop(
                    'disabled', true
                    )
            }

        } else {

            verification_div.css({
                'display' : 'block'
            })

            verification_div.html(
                "<p>Hmm... The file you are attempting to upload doesn't appear to have a format associated with it or is improperly named. Beware that files not in .pdf format will not parse properly.</p>"
            )
            file_submit.prop(
                'disabled', false
                )
        }
        
    })
})