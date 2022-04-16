
def main():
    from src.setup import setup_parameters
    setup_parameters()
    from src.timer import Chrono
    Chrono.dialogue_begin()
    Chrono()


if __name__ == '__main__':
    main()
