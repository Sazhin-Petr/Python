from parserdz import Parsing


def main():
    pars = Parsing('https://iwant.games/bestgames-pc/', 'games.txt')
    pars.run()


if __name__ == '__main__':
    main()
