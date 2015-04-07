Usage
-----

To present the solution to every problem present in folder problems, run the
`solver.py` program as so:

`python solver.py`

If you want to solve a specific problem or problems, pass the `-p` flag and a
space separated list of problem numbers to solve. For example, to present the
solutions to problems 11 and 13, run:

`python solver.py -p 11 13`

If any of the passed problems are not present in the problems folder, a message
will be presented stating that the problem cannot be found and it will be
skipped.

To summarize this information, just pass the help flag:

`python solver.py -h`
