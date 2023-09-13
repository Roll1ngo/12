import logging
import datetime

a = "2"


datetime.time()

logging.basicConfig(
    format="%(asctime)s %(funcName)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("program.log"), logging.StreamHandler()],
)


def foo(n: int):
    result = n**2
    logging.DEBUG(f"result:{result}")
    return result


if __name__ == "__main__":
    foo(5)
