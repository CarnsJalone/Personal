from datetime import datetime
import os
import sys
import logging

now = datetime.now()
now = str(now)

class Employment_Calculator():


    def __init__(self):

        # Locate additional, necessary directories, probably not needed within class
        self.home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.employment_calculator_dir = os.path.dirname(os.path.abspath(__file__))
        self.logging_dir = os.path.join(self.home_dir, 'Logging')
        self.logger_txt_file = os.path.join(self.logging_dir, 'logger.txt')

        # Create logging file
        logging.basicConfig(filename=self.logger_txt_file, level=logging.DEBUG)

        # Append Home directory
        sys.path.append(self.home_dir)  

    # Get rid of the contents of the file before writing to it. 
    def write_logging_header(self):

        logging_file = open(self.logger_txt_file, 'a')
        logging_file.write('\nEmployment Calculator Logging Begun at ' + now + '\n\n')
        logging_file.close()

    def get_date_time_object(self):

        hire_date = '2015-02-09 05:30:00'
        # Years - Months - Days - Hours - Minutes - Seconds
        datetime_hire_date = datetime.strptime(hire_date, '%Y-%m-%d %H:%M:%S')

        logging.info('Date Succesfully Acquired; Hire-Date: {}'.format(datetime_hire_date))
        return datetime_hire_date

    def create_time_delta(self):

        hire_date = self.get_date_time_object()
        now = datetime.now()

        elapsed_time = now - hire_date

        print(elapsed_time)

        logging.info('Time Delta Created')

        return elapsed_time

    def calculate_elapsed_time(self):

        # plural_years, plural_months, plural_weeks, plural_days, plural_minutes, plural_seconds

        elapsed_time = self.create_time_delta()
        total_seconds = int(elapsed_time.total_seconds())
        
        years, years_remainder = divmod(total_seconds, 31536000)
        months, months_remainder = divmod(years_remainder, 2629746)
        weeks, weeks_remainder = divmod(months_remainder, 604800) 
        days, days_remainder = divmod(weeks_remainder, 86400)
        hours, hours_remainder = divmod(days_remainder, 3600)
        minutes, seconds = divmod(hours_remainder, 60)

        if years == 1:
            years_string = 'year'
        else:
            years_string = 'years'

        if months == 1:
            months_string = 'month'
        else: 
            months_string = 'months'
        
        if weeks == 1:
            weeks_string = 'week'
        else:
            weeks_string = 'weeks'

        if days == 1:
            days_string = 'day'
        else:
            days_string = 'days'

        if hours == 1:
            hours_string = 'hour'
        else: 
            hours_string = 'hours'

        if minutes == 1:
            minutes_string = 'minute'
        else:
            minutes_string = 'minutes'

        if seconds == 1:
            seconds_string = 'second'
        else:
            seconds_string = 'seconds'

        formatted_time_elapsed = '{} {}, {} {}, {} {}, {} {}, {} {}, {} {} and {} {} ago'.format(years, years_string, months, months_string, weeks, weeks_string, days, days_string, hours, hours_string, minutes, minutes_string, seconds, seconds_string)

        logging.info('Formatted Date Created')
        return formatted_time_elapsed

    def write_logging_footer(self):

        logging_file = open(self.logger_txt_file, 'a')
        logging_file.write('\nEmployment Calculator Logging Completed at ' + now + '\n')
        logging_file.close()
