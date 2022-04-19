import logging

# logging.basicConfig(filename="sample.log", level=logging.INFO)
# log = logging.getLogger("ex")
#
# try:
#     raise RuntimeError
# except RuntimeError:
#     log.exception("Error!")


def funcii():
    try:
        print(int('ds'))
        print(14 / 0)

    except (ZeroDivisionError, ValueError) as e:
        return e
    # except ValueError as e:
    #     return e


def po(func):
    with open('err_log.txt', 'w', -1, 'utf-8') as f:
        f.write(str(func))
    print(func)


po(funcii())