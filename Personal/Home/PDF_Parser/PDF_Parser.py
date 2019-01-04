from os import path, system, remove, listdir

class PDF_Handler():

    def __init__(self):

        # Initialize the directories needed for the upload
        self.CURRENT_FILE_DIRECTORY = path.dirname(path.abspath(__file__))
        self.UPLOADED_FILE_DIRECTORY = path.join(self.CURRENT_FILE_DIRECTORY, 'Uploaded_Files')
        self.CONVERTED_FILE_DIRECTORY = path.join(self.CURRENT_FILE_DIRECTORY, 'Converted_Files')

        self.valid_pdf_files = []

    # Search folder for TXT
    def find_txt_files(self):
        
        all_uploaded_files = listdir(self.UPLOADED_FILE_DIRECTORY)

        txt_files = []

        if len(all_uploaded_files) == 0:
            print('There is nothing inside this directory')
            return
        else:
            for file in all_uploaded_files:
                file_path = path.join(self.UPLOADED_FILE_DIRECTORY, file)
                filename, extension = path.splitext(file)

                if extension == '.txt':
                    txt_files.append({file_path : file})

        return txt_files

    # Search folder for PDF
    def find_pdf_files(self):
        
        all_uploaded_files = listdir(self.UPLOADED_FILE_DIRECTORY)

        pdf_files = []

        if len(all_uploaded_files) == 0:
            print('There is nothing inside this directory')
            return
        else:
            for file in all_uploaded_files:
                file_path = path.join(self.UPLOADED_FILE_DIRECTORY, file)
                filename, extension = path.splitext(file)
                if extension == '.pdf':
                    pdf_files.append({file_path : file})

        return pdf_files
   
    # Convert PDF file to text
    def convert_pdf_to_txt(self):

        pdf_files = self.find_pdf_files()

        for each_file in pdf_files:
           for pdf_file_path, pdf_file in each_file.items():
               
                # Create a linux-based conversion command
                # pdftotext -layout NAME_OF_PDF.pdf
                formatted_conversion_command = '{} {} {}'.format(
                    'pdftotext',
                    '-layout',
                    pdf_file_path
                )
                system(formatted_conversion_command)
                print(pdf_file,'converted to .txt')

    def delete_unecessary_txt_files(self):

        txt_files = self.find_txt_files()

        for text_file in txt_files:
            for file_path, file_name in text_file.items():
                name, extension = path.splitext(file_name)
                if extension == '.txt':
                    remove(file_path)
                    print(file_name,'at',file_path,'removed.')


    def main(self):
        self.find_txt_files()
        self.delete_unecessary_txt_files()
        self.find_pdf_files()
        self.convert_pdf_to_txt()

handler_1 = PDF_Handler()

# handler_1.find_pdf_files()
# handler_1.print_test()
# handler_1.convert_pdf_to_txt()
handler_1.main()


