from pymeter.api import ContentType
from pymeter.api.config import TestPlan, ThreadGroupSimple, ThreadGroupWithRampUpAndHold
from pymeter.api.postprocessors import JsonExtractor
from pymeter.api.samplers import HttpSampler
from pymeter.api.timers import UniformRandomTimer
from pymeter.api.reporters import HtmlReporter
from pymeter.api.config import CsvDataset

csv_data = CsvDataset('test_data.csv')

timer = UniformRandomTimer(500, 2000)

test_profiles =  [
    {'threads': 10, 'rampup': 30, 'hold': 100},
    {'threads': 30, 'rampup': 100, 'hold': 200},
    {'threads': 150, 'rampup': 200, 'hold': 300},
]

create_game = (
    HttpSampler('create_games_request', 'http://127.0.0.1:5000/games')
    .post({'vs_computer': '${vs_computer}'}, ContentType.APPLICATION_JSON)
)
json_extractor = JsonExtractor('game_id', '[0]')

get_games = HttpSampler('get_games_request', 'http://127.0.0.1:5000/games', json_extractor)

move = (
    HttpSampler('move_request', 'http://127.0.0.1:5000/games/${game_id}/move')
    .post({'x': '${x}', 'y': '${y}'}, ContentType.APPLICATION_JSON)
)

get_board = (HttpSampler('get_board_request', 'http://127.0.0.1:5000/games/${game_id}/board'))

end_game = (
    HttpSampler('end_games_request', 'http://127.0.0.1:5000/games/${game_id}/end')
    .post({}, ContentType.APPLICATION_JSON)
)



for profile in test_profiles:
    print(f'test dla profilu: {profile}')
    thread_group = ThreadGroupWithRampUpAndHold(
        profile['threads'],
        profile['rampup'],
        profile['hold'],
        csv_data,
        create_game,
        timer,
        get_games,
        timer,
        move,
        timer,
        get_board,
        timer,
        end_game
        )

html_reporter = HtmlReporter()

test_plan = TestPlan(thread_group, html_reporter)

stats = test_plan.run()