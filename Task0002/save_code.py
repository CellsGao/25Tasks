import uuid
import MySQLdb


def creat_code(number=20):
    codes = []
    while True is True:
        code = str(uuid.uuid1()).replace("-", "")
        if code not in codes:
            codes.append(code)
        if len(codes) == number:
            break
    return codes
