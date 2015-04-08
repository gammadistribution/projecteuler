Project Euler
-------------

This project aims to chronicle the work used to solve problems found on
[https://www.projecteuler.net](https://www.projecteuler.net), a website
consisting of "a series of challenging mathematical/computer programming
problems that will require more than just mathematical insights to solve."

These problems are solved using the Python programming language and a bit
of mathematical ingenuity.

Requirements
------------

This project uses the Python programming language. As a result, Python 3.2x or
greater is required to use this package. Additionally the Numpy, Scipy, and
pandas libraries, as well as their dependencies, are required to solve some
problems and should be installed as well.

If you have pip installed, you can run the following in the project's root
directory:

`pip install -r requirements/requirements.txt`

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

To summarize this information, just pass `-h`, the help flag:

`python solver.py -h`

Contacts
--------

Feel free to contact the author, Matthew Tiger, with any questions about this
project.

The author is available via email: matthew.c.tiger@gmail.com

Copyright
---------

Project Euler
Copyright (C) 2013-2015  Matthew Tiger

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.