import logging
import sys
import traceback
# logging.basicConfig(filename="sample.log", level=logging.INFO)
# log = logging.getLogger("ex")
#
# try:
#     raise RuntimeError
# except RuntimeError:
#     log.exception("Error!")

def get_exception_info() -> str:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(
        exc_type, exc_value, exc_traceback)
    log = "".join("!! " + line for line in lines)
    return log

def funcii():
    try:
        print(14 / 0)
        print(int('ds'))
        print(14 / 0)

    except (ZeroDivisionError, ValueError):
        return get_exception_info()
    # except ValueError as e:
    #     return e


def po(func):
    with open('err_log.txt', 'w', -1, 'utf-8') as f:
        f.write(str(func()))
    print(func)


po(funcii)