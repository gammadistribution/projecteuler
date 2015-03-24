from argparse import ArgumentParser
import importlib
from settings import solver_settings


def execute_problem(problem):
    """Import problem name space and execute main method associated
    with each problem. If problem not found, state as such. If problem has no
    main method, state as such.
    """
    try:
        namespace = importlib.import_module(problem)
        answer = namespace.main()
        print('{0} answer: {1}'.format(problem, answer))
    except AttributeError:
        print('{0} has no main method.'.format(problem))
    except ImportError:
        print('{0} cannot be found.'.format(problem))


def get_args():
    """Returns parsed args passed to program. Provides description of program
    and parses any arguments passed.
    """
    description = 'Execute program corresponding to passed problem.'
    parser = ArgumentParser(description=description)

    problem_help = 'Problem(s) to execute. Must be between 1 and '
    problem_help += '{bound}.'
    problem_help = problem_help.format(**{'bound': solver_settings.UPPERBOUND})
    parser.add_argument('problems', type=int, nargs='+', help=problem_help)

    args = parser.parse_args()

    args.problem_modules = get_modules(args)

    return args


def get_modules(args):
    """Return list of modules of problems to solve. Check to see if each
    problem passed in args is a number between 1 and
    solver_settings.UPPERBOUND. If it is not, then log message saying as such.
    """
    modules = []

    for problem in args.problems:
        if 1 <= problem <= solver_settings.UPPERBOUND:
            path = solver_settings.PROBLEM_PATH_TEMPLATE.format(problem)
            modules.append(path)
        else:
            message = 'Problem(s) must be between 1 and {bound}.'
            print(message.format(**{'bound': solver_settings.UPPERBOUND}))

    return modules


def main(args):
    for problem in args.problem_modules:
        execute_problem(problem)


if __name__ == '__main__':
    args = get_args()

    main(args)
