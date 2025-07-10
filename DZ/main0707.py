from parserdz import Parsing


def main():
    for i in range(1, 64):
        par = Parsing(f'https://iwant.games/bestgames-pc/page/{i}', 'games.txt')
        par.run()
        par.save()


if __name__ == '__main__':
    main()
