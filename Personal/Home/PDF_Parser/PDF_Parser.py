from os import path, system, remove

class PDF_Handler():

    def __init__(self):

        # Initialize the directories needed for the upload
        self.CURRENT_FILE_DIRECTORY = path.dirname(path.abspath(__file__))
        self.UPLOADED_FILE_DIRECTORY = path.join(self.CURRENT_FILE_DIRECTORY, 'Uploaded_Files')
        self.CONVERTED_FILE_DIRECTORY = path.join(self.CURRENT_FILE_DIRECTORY, 'Converted_Files')


    def convert_uploaded_pdf_to_txt(self):

        # Find Uploaded PDF
        pdf_file_link = path.join(self.UPLOADED_FILE_DIRECTORY, 'STOCKZERO.pdf')


        # Create name for converted text file into correct directory
        temp_converted_text_file_name = str(self.CONVERTED_FILE_DIRECTORY) + '/temp_pdf.txt'
       
        # Create conversion command
        # $ pdf2txt.py -o output.html samples/naacl06-shinyama.pdf    
        # (extract text as an HTML file whose filename is output.html)
        formatted_conversion_command = '{} {} {} {}'.format(
            'pdf2txt.py',
            '-o',
            temp_converted_text_file_name,
            pdf_file_link)

        # Check if file exists, if it does delete it, then reissue the command
        file_exists = path.isfile(temp_converted_text_file_name)

        if file_exists:
            print('File Already Exists, Removing File...')
            remove(temp_converted_text_file_name)
            print('Converting New File...')
            system(formatted_conversion_command)
            print('File Converted')

        # If the file does not already exist, run the command to create it
        else:
            print('File Doesn\'t Yet Exist, Creating File...')
            system(formatted_conversion_command)
            print('File Converted')


    def open_and_parse_txt(self):
            text_file_link = str(self.CONVERTED_FILE_DIRECTORY) + '/temp_pdf.txt'

            opened_file = open(text_file_link, 'rb')

            for line in opened_file:
                line = line.decode('utf-8')
                print(line)



handler_1 = PDF_Handler()

handler_1.open_and_parse_txt()



