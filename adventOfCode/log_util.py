import logging
import sys

parent_log_name = "AOC"
aoc_parent_logger = logging.getLogger(parent_log_name)
aoc_parent_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(module)s.py - %(message)s')

# Log to file
filehandler = logging.FileHandler("aoc.log", "a")
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)
aoc_parent_logger.addHandler(filehandler)
# Log to stdout
streamhandler = logging.StreamHandler(sys.stdout)
streamhandler.setLevel(logging.DEBUG)
streamhandler.setFormatter(formatter)
aoc_parent_logger.addHandler(streamhandler)

if __name__ == "__main__":
    logger = aoc_parent_logger.getChild("child_logger")
    logger.debug("Test Message")
    logger.info("Another test message")
