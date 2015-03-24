from settings import solver_settings
from argparse import ArgumentParser
import glob
import importlib
import logging
import logging.config
import os


logger = logging.config.fileConfig(solver_settings.LOGGING_CONF_FILE)
logger = logging.getLogger('solver')


def execute_problem(problem):
    """Import problem name space and execute main method associated
    with each problem. If problem not found, state as such. If problem has no
    main method, state as such.
    """
    try:
        namespace = importlib.import_module(problem)
        answer = namespace.main()
        logger.info('{0} answer: {1}'.format(problem, answer))
    except AttributeError:
        logger.critical('{0} has no main method.'.format(problem))
    except ImportError:
        logger.critical('{0} cannot be found.'.format(problem))


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

    args.problem_modules = get_modules(args)

    return args


def get_modules(args):
    """Return list of modules of problems to solve. From passed args, if
    args.problems exists, i.e. subset of problems have been chosen, then
    get module names for those problems. Otherwise get module names for
    all problems in problems package.
    """
    modules = []

    if args.problems:
        for problem in args.problems:
            if 1 <= problem <= solver_settings.UPPERBOUND:
                path = solver_settings.PROBLEMS_PATH_TEMPLATE.format(problem)
                modules.append(path)
            else:
                message = 'Problem(s) must be between 1 and {bound}. Skipping '
                message += 'problem {problem}.'
                kwargs = {'bound': solver_settings.UPPERBOUND,
                          'problem': problem}
                logger.warning(message.format(**kwargs))
    else:
        files = glob.glob(solver_settings.PROBLEMS_MODULE_GLOB_PATTERN)
        for path in files:
            directory, filename = os.path.split(path)
            base, ext = os.path.splitext(filename)
            modules.append('.'.join([solver_settings.PROBLEMS_PACKAGE, base]))

        modules.sort()

    return modules


def main(args):
    for problem in args.problem_modules:
        execute_problem(problem)


if __name__ == '__main__':
    args = get_args()

    main(args)
