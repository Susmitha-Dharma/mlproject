import sys
import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)  # Fixed super() call
        self.error_message = error_message_detail(error_message, error_detail=error_details)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    logging.basicConfig(filename="your_log_file.log", level=logging.INFO, format="%(asctime)s - %(message)s")

    try:
        a = 1 / 10  # This will not raise an exception, adjust for testing
    except ZeroDivisionError as e:
        logging.info("Divide by Zero")
        raise CustomException("Custom Exception: A division by zero occurred", sys)

        