
def main():
    from src.setup import setup_parameters
    setup_parameters()
    from src.timer import basic_timer_loop
    basic_timer_loop()


if __name__ == '__main__':
    main()
