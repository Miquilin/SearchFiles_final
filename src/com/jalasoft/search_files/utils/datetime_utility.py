import datetime
from src.com.jalasoft.search_files.utils.logging_config import logger


class DateTimeUtility(object):
    """
    This class contains utils related to datetime
    """

    def convert_string_to_datetime(self, datetime_string):
        """
        This method converts an input string in a datetime
        :param datetime_string:
        :return: datetime_criteria
        """
        logger.info("Starting the method")
        logger.debug("The datetime string is: %s", datetime_string)
        try:
            date_criteria, time_criteria = map(str, datetime_string.split(' '))
            year, month, day = map(int, date_criteria.split('-'))
            hour, minutes, seconds = map(int, time_criteria.split(':'))
            datetime_criteria = datetime.datetime(year, month, day, hour, minutes, seconds)
        except Exception as inst:
            logger.debug("The exception instance is: %s", type(inst))
            logger.debug ("Arguments stored in .args are: %s", inst.args)
            logger.debug("An exception has been generated: %s", inst)
            datetime_criteria = ""
        logger.debug("The datetime criteria returned is: %s", datetime_criteria)
        logger.info("Ending the method")
        return datetime_criteria
