from argparse import ArgumentParser
import importlib


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
        print(problem)
        print('{0} cannot be found.'.format(problem))


def get_args():
    """Returns parsed args passed to program. Provides description of program
    and parses any arguments passed.
    """
    UPPERBOUND = 498
    description = 'Execute program corresponding to passed problem.'
    parser = ArgumentParser(description=description)

    problem_help = 'Problem(s) to execute. Must be between 1 and '
    problem_help += '{bound}.'
    parser.add_argument('problems', type=int, nargs='+',
                        help=problem_help.format(**{'bound': UPPERBOUND}))

    args = parser.parse_args()

    args.problems = ['problems.problem_{0:04}'.format(problem) for
                     problem in args.problems]

    return args


if __name__ == '__main__':
    args = get_args()

    for problem in args.problems:
        execute_problem(problem)
