**********************
Chronometria Paginarum
**********************

A CLI application to store and evaluate effectiveness and distraction rate while reading books.

TODO:

1. Basic timer loop
2. Quit condition (Key listen)
3. Basic calculations
4. Save data to file
5. Allow step back (re-do page count last instance)

***********
First setup
***********

1. Setup poetry.
    1.1 - In PowerShell, run:
        (Invoke-WebRequest -Uri
        https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py
        -UseBasicParsing).Content | python -
    1.2 - At main folder, run: *poetry install*
2. Run tests.
    2.1 - In main folder, run: *poetry run pytest*
