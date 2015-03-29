from settings import solver_settings
from argparse import ArgumentParser
import glob
import importlib
import logging
import logging.config
import os


logging.config.fileConfig(solver_settings.LOGGING_CONF_FILE)
logger = logging.getLogger('solver')


def execute_problem(problem):
    """Import problem name space and execute main method associated
    with each problem. If problem not found, state as such. If problem has no
    main method, state as such.
    """
    try:
        namespace = importlib.import_module(problem)
        answer = namespace.main()
    except ImportError:
        message = '{0} cannot be found.'
        logger.critical(message.format(problem))
        answer = None
    except AttributeError:
        message = '{0} has no main method.'
        logger.critical(message.format(problem))
        answer = None

    return answer


def get_args():
    """Returns parsed args passed to program. Provides description of program
    and parses any arguments passed.
    """
    description = 'Solve corresponding Project Euler program in problems '
    description += 'package. If no argument is passed, solves all problems, '
    description += 'otherwise solves only for specified problems passed '
    description += 'through -p, --problems flag.'
    parser = ArgumentParser(description=description)

    problem_help = 'Problem(s) to execute. Must be between 1 and '
    problem_help += '{bound}.'
    problem_help = problem_help.format(**{'bound': solver_settings.UPPERBOUND})
    parser.add_argument('-p', '--problems', type=int, nargs='+',
                        help=problem_help)

    args = parser.parse_args()

    args.problem_modules = get_modules(args.problems,
                                       **solver_settings.GET_MODULES_SETTINGS)

    return args


def get_modules(problems, package, module_template, glob_pattern, upper_bound):
    """Return list of modules of problems to solve. From passed args, if
    args.problems exists, i.e. subset of problems have been chosen, then
    get module names for those problems. Otherwise get module names for
    all problems in problems package.
    """
    modules = []

    if problems:
        for problem in problems:
            if 1 <= problem <= upper_bound:
                path = '.'.join([package, module_template]).format(problem)
                modules.append(path)
            else:
                message = 'Problem(s) must be between 1 and {bound}. Skipping '
                message += 'problem {problem}.'
                kwargs = {'bound': upper_bound,
                          'problem': problem}
                logger.warning(message.format(**kwargs))

    else:
        files = glob.glob(glob_pattern)
        for path in files:
            directory, filename = os.path.split(path)
            base, ext = os.path.splitext(filename)
            modules.append('.'.join([package, base]))

        modules.sort()

    return modules


def main(args):
    for problem in args.problem_modules:
        logger.info('Starting {0}'.format(problem))

        answer = execute_problem(problem)

        if answer:
            logger.info('{0} answer: {1}'.format(problem, answer))


if __name__ == '__main__':
    args = get_args()

    main(args)
