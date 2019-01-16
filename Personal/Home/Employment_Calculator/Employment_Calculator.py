from datetime import datetime
import os
import sys

class Employment_Calculator():

    def __init__(self):

        self.home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.employment_calculator_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(self.home_dir)

    def get_date_time_object(self):

        hire_date = '2015-02-09 05:30:00'
        # Years - Months - Days - Hours - Minutes - Seconds
        datetime_hire_date = datetime.strptime(hire_date, '%Y-%m-%d %H:%M:%S')

        return datetime_hire_date

    def create_time_delta(self):

        hire_date = self.get_date_time_object()
        now = datetime.now()

        elapsed_time = now - hire_date

        print(elapsed_time)

        return elapsed_time

    def calculate_elapsed_time(self):

        elapsed_time = self.create_time_delta()
        total_seconds = int(elapsed_time.total_seconds())
        
        years, years_remainder = divmod(total_seconds, 31536000)
        months, months_remainder = divmod(years_remainder, 2629746)
        weeks, weeks_remainder = divmod(months_remainder, 604800) 
        days, days_remainder = divmod(weeks_remainder, 86400)
        hours, hours_remainder = divmod(days_remainder, 3600)
        minutes, seconds = divmod(hours_remainder, 60)

        formatted_time_elapsed = '{} years, {} months, {} weeks, {} days, {} hours, {} minutes and {} seconds ago'.format(years, months, weeks, days, hours, minutes, seconds)

        return formatted_time_elapsed

calc = Employment_Calculator()
calc.calculate_elapsed_time()