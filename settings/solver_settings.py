import os


# This is the package where all problems are stored.
PROBLEMS_PACKAGE = 'problems'

# Each problem module starts with 'problem_' followed by four digit number
# corresponding to numbered project euler problem.
PROBLEMS_MODULE_TEMPLATE = 'problem_{0:04}'

# Template for Python path to an individual problem
PROBLEM_PATH_TEMPLATE = '.'.join([PROBLEMS_PACKAGE, PROBLEMS_MODULE_TEMPLATE])

# Maximum number of problems on project euler.
UPPERBOUND = 498

# Path to logging ini file.
LOGGING_CONF_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'logging', 'logging.ini')
