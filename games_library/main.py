class GamesLibrary:
    games = []
    game_id = 0

    def __init__(self, title: str, price: float or int, genre: tuple, release_date: str):
        self.__title = title
        self.__price = str(price)
        self.__genre = genre
        self.__release_date = release_date

        GamesLibrary.game_id += 1
        game_info = {
            'title': title,
            'price': str(price) + '$',
            'genre': genre,
            'release date': release_date
        }
        game_all_info = (GamesLibrary.game_id, game_info)
        GamesLibrary.games.append(game_all_info)

    @staticmethod
    def print_all_information_about_the_game_by_id():
        all_game_id = 0

        # def check_input_id():
        #     input_user_id = None
        #     try:
        #         input_user_id = int(input('Введите ID игры которую желаете найти: '))
        #     except ValueError:
        #         print('ID может быть только цифрой, попробуйте еще раз!!')
        #         check_input_id()
        #     finally:
        #         return input_user_id

        input_id = int(input('Введите ID игры которую желаете найти: '))

        for game in GamesLibrary.games:
            if game[0] == input_id:
                all_game_id = game[0]
                game_dict = game[1]
                for item in game_dict.items():
                    print(item)

        if all_game_id == 0:
            print('Игры с таким ID не существует')

    @staticmethod
    def print_all_in_games_library():
        print(GamesLibrary.games)


my_first_game = GamesLibrary('Diablo', 99.99, ('RPG', 'Action'), '1996.03.01')
my_second_game = GamesLibrary('Diablo 2', 150, ('RPG', 'Action'), '2001.06.01')
my_third_game = GamesLibrary('Diablo 3', 200, ('RPG', 'Action'), '2001.06.01')
my_fourth_game = GamesLibrary('Fallout', 150, ('RPG', 'Action'), '1999.09.15')
# GamesLibrary.print_all_in_games_library()
GamesLibrary.print_all_information_about_the_game_by_id()
