from os import path, system, remove, listdir, rename, mkdir
import sys
import time
import subprocess
import logging
import datetime

now = datetime.datetime.now()
now = str(now)

HOME_DIR = path.dirname(path.dirname(path.abspath(__file__)))
BASE_DIR = path.dirname(HOME_DIR)
TXT_DIR = path.join(BASE_DIR, 'static/txt')

sys.path.append(TXT_DIR)

PDF_PARSER_LOG_FILE = path.join(TXT_DIR, 'logger.txt')

logging.basicConfig(filename=PDF_PARSER_LOG_FILE, level=logging.DEBUG)

class PDF_Handler():

    def __init__(self):

        # Initialize the directories needed for the upload
        self.CURRENT_FILE_DIRECTORY = path.dirname(path.abspath(__file__))
        self.UPLOADED_FILE_DIRECTORY = path.join(self.CURRENT_FILE_DIRECTORY, 'Uploaded_Files')
        self.CONVERTED_FILE_DIRECTORY = path.join(self.CURRENT_FILE_DIRECTORY, 'Converted_Files')

        self.UPLOADED_FILE = ''

    def write_logging_header(self):

        logging_file = open(PDF_PARSER_LOG_FILE, 'a')
        logging_file.write('\n-----PDF Parser Logging Begun at ' + now + '-----')
        logging_file.close()

    def check_and_create_folders(self):

        if path.isdir(self.UPLOADED_FILE_DIRECTORY):
            logging.info('Uploaded File Directory Exists at ' + self.UPLOADED_FILE_DIRECTORY + ' at ' + now)
        else:
            logging.critical('Uploaded File Directory Does Not Exist, Creating Directory at ' + self.UPLOADED_FILE_DIRECTORY + 'at ' + now)
            mkdir(path.join(self.CURRENT_FILE_DIRECTORY, 'Uploaded_Files'))
            logging.info('Uploaded File Directory Created at ' + self.UPLOADED_FILE_DIRECTORY + ' at ' + now)


        if path.isdir(self.CONVERTED_FILE_DIRECTORY):
            logging.info('Converted File Directory Exists at ' + self.CONVERTED_FILE_DIRECTORY + ' at ' + now)

        else:
            logging.critical('Converted File Directory Does Not Exist, Creating Directory at ' + self.CONVERTED_FILE_DIRECTORY + 'at ' + now)
            mkdir(path.join(self.CURRENT_FILE_DIRECTORY, 'Converted_Files'))
            logging.info('Converted File Directory Created at ' + self.CONVERTED_FILE_DIRECTORY + ' at ' + now)


    # Search folder for TXT
    def find_txt_files(self):
        
        all_uploaded_files = listdir(self.UPLOADED_FILE_DIRECTORY)

        txt_files = []

        if len(all_uploaded_files) == 0:
            logging.warning('There is nothing inside this directory')
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
            logging.warning('There is nothing inside this directory')
            return
        else:
            for file in all_uploaded_files:
                file_path = path.join(self.UPLOADED_FILE_DIRECTORY, file)
                filename, extension = path.splitext(file)
                if extension == '.pdf':
                    pdf_files.append({file_path : file})
                    logging.info(filename,'appended to Array...')
            
        logging.info('All available PDF files located.')

        return pdf_files
   
    # Convert PDF file to text
    def convert_pdf_to_txt(self):

        pdf_files = self.find_pdf_files()

        if pdf_files == None:
            logging.debug('There are no PDF Files in this directory.')
        else:
            for each_file in pdf_files:
                for pdf_file_path, pdf_file in each_file.items():

                    # subprocess.call(['pdftotext', '-layout', 'somefile.pdf'])
                    
                    formatted_conversion_command = ['pdftotext', '-layout', pdf_file_path]
                    conversion_call = subprocess.call(formatted_conversion_command)
                    if conversion_call != 0:
                        logging.critical('There was an error. The subprocess returned a code of ' + conversion_call)
                    else:
                        logging.info('Conversion properly called. -> ' + pdf_file,'converted to .txt.')

    def delete_unecessary_txt_files(self):

        txt_files = self.find_txt_files()

        for text_file in txt_files:
            for file_path, file_name in text_file.items():
                name, extension = path.splitext(file_name)
                if extension == '.txt':
                    remove(file_path)
                    logging.info(file_name,'at',file_path,'removed.')


    # Empty the converted folder
    def clean_converted_folder(self):

        converted_file_with_directory = []

        converted_dir = self.CONVERTED_FILE_DIRECTORY

        converted_dir_files = listdir(converted_dir)

        for file in converted_dir_files:
            temp_name = path.join(converted_dir, file)
            converted_file_with_directory.append(temp_name)

        for file in converted_file_with_directory:
            remove(file)
            logging.info(file,'cleared from Converted Folder...')
        
        logging.info('Converted Folder Cleared, Ready For Move...')
        

    def clean_upload_folder(self):

        uploaded_file_with_directory = []

        uploaded_dir = self.UPLOADED_FILE_DIRECTORY

        uploaded_dir_files = listdir(uploaded_dir)

        for file in uploaded_dir_files:
            temp_name = path.join(uploaded_dir, file)
            uploaded_file_with_directory.append(temp_name)

        for file in uploaded_file_with_directory:
            remove(file)
            print(file,'cleared from Upload Folder...')
           
        logging.info('Upload Folder Cleared, Ready For Upload...')

    def verify_upload_folder_contents(self):

        uploaded_dir = self.UPLOADED_FILE_DIRECTORY

        uploaded_dir_files = listdir(uploaded_dir)

        if len(uploaded_dir_files) < 1:
            print('There is nothing in this folder for exhange.')
            self.convert_pdf_to_txt()
        else:
            self.move_converted_files_into_converted_folder()

    def move_converted_files_into_converted_folder(self):

        current_dir = self.UPLOADED_FILE_DIRECTORY
        destination_dir = self.CONVERTED_FILE_DIRECTORY
        current_dir_contents = listdir(current_dir)

        # filename_replace_regex = r'[\\/:"*?<>|]+'

        file_existence_check = 0

        try:
            while file_existence_check < 2:
                for file in current_dir_contents:
                    file_name, extension = path.splitext(file)
                    if extension == '.txt': 
                        current_file = path.join(current_dir, file)
                        destination_file = path.join(destination_dir, file)
                        if path.isdir(destination_dir) and not path.isfile(destination_file):
                            rename(current_file, destination_file)
                            logging.info('{} {} {} {}'.format('Moving', file, 'into', destination_dir))
                        else:
                            logging.info('Destination file already exists, removing current file and reiterating through check.')
                            remove(destination_file)
                    file_existence_check += 1   
        except Exception as e:
            logging.critical('There was an error with moving the converted file. Error: ' + e)

    def write_logging_footer(self):

        logging_file = open(PDF_PARSER_LOG_FILE, 'a')
        logging_file.write('-----PDF Parser Logging Completed at ' + now + '-----\n\n')
        logging_file.close()

class TextHandler():

    def __init__(self):

        self.CURRENT_FILE_DIRECTORY = path.dirname(path.abspath(__file__))
        self.CONVERTED_FILE_DIRECTORY = path.join(self.CURRENT_FILE_DIRECTORY, 'Converted_Files')

    def find_txt_files(self):

        converted_files_dir = self.CONVERTED_FILE_DIRECTORY

        converted_files = listdir(converted_files_dir)

        for file in converted_files:
            print(file)



pdf_handler = PDF_Handler()
# pdf_handler.clean_converted_folder()
# pdf_handler.convert_pdf_to_txt()
pdf_handler.verify_upload_folder_contents()
                



