import os

# Directory of this file and parent directory of directory.
SETTINGS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PARENT_DIRECTORY = os.path.dirname(SETTINGS_DIRECTORY)

# Maximum number of problems on project euler.
UPPERBOUND = 498

# This is the package where all problems are stored.
PROBLEMS_PACKAGE = 'problems'

# Each problem module starts with 'problem_' followed by four digit number
# corresponding to numbered project euler problem.
PROBLEMS_MODULE_TEMPLATE = 'problem_{0:04}'

# Template for Python path to an individual problem
PROBLEMS_PATH_TEMPLATE = '.'.join([PROBLEMS_PACKAGE, PROBLEMS_MODULE_TEMPLATE])

# Glob pattern for all problem modules

PROBLEMS_MODULE_GLOB_PATTERN = os.path.join(PARENT_DIRECTORY, PROBLEMS_PACKAGE,
                                            'problem_*')

# Path to logging ini file.
LOGGING_CONF_FILE = os.path.join(SETTINGS_DIRECTORY, 'logging', 'logging.ini')
