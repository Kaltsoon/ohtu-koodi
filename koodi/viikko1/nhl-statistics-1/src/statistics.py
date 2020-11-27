from player_reader import PlayerReader


def sort_by_points(player):
    return player.points


class Statistics:
    def __init__(self):
        reader = PlayerReader(
            "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
        )

        self.players = reader.get_players()

    def search(self, name):
        for player in self.players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self.players
        )

        return list(players_of_team)

    def top_scorers(self, how_many):
        sorted_players = sorted(
            self.players,
            reverse=True,
            key=sort_by_points
        )

        return sorted_players[:how_many]