def main():
    # TODO: Start Session with info
    from src.parameters import PARAMS
    PARAMS['PAGE_GOAL'] = int(input('What is your page goal? '))

    from src.timer import basic_timer_loop
    basic_timer_loop()


if __name__ == '__main__':
    main()
