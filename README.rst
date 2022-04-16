*******************************
Chronometria Paginarum (v. 0.2.4)
*******************************

A CLI application to track and handle Reverse Jenga sessions.

There are no plans on improving the current version.
Version 0.2.4 is functional (if you want some CSVs or whatever... that's what it does...), and will stay as is.

Next step is integrating the data from the CLI sessions with the Reverse Jenga Dashboard.

Reverse Jenga (with Taico)
##########################

Taico invites you to play a game of Reverse Jenga.

Rules
-----

.. container::

    Instead of removing tiles from a tower, you pile books on top of each other.

    The match is set with a *page threshold*. It is the number of pages the player wants to read everyday.

        If the average number of pages read reaches a number lower than the page threshold,
        the player is offered 7 days for redemption.

        The player loses if the average is still lower than the page threshold after that.

        The player wins if the Tower falls and the player has an average of pages read per day
        greater or equal to the page threshold.


    The player can have a fallback of a maximum of 150 pages, allowing more flexibility during the game.

        Those pages must come from a previous untracked/failed session.

        Otherwise, the player has no fallback.

    Winning the game grants no reward. Losing it presents no penalties.

*****
Setup
*****

To start a session, run:

    poetry run python main.py

First setup
###########

1. Setup poetry.
    1.1 - In PowerShell, run:
        (Invoke-WebRequest -Uri
        https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py
        -UseBasicParsing).Content | python -
    1.2 - At main folder, run: *poetry install*
2. Run tests.
    2.1 - In main folder, run: *poetry run pytest*
