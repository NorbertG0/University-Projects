from flask import Flask, request, jsonify
from engine.game_manager import GameManager
from engine.check_winner import check_winner
from engine.move import create_new_matrix, print_board
from engine.computer_move import computer_move

app = Flask(__name__)
manager = GameManager()

@app.route('/games', methods=['POST'])
def create_game():
    vs_computer = request.json.get("vs_computer", False)
    game_id = manager.create_game()
    game = manager.get_game(game_id)
    game.vs_computer = vs_computer
    return jsonify({"game_id": game_id, "vs_computer": vs_computer})

@app.route('/games', methods=['GET'])
def get_all_games():
    return jsonify(manager.list_games())

@app.route('/games/<game_id>', methods=['GET'])
def get_game(game_id):
    game = manager.get_game(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404
    return jsonify({
        "id": game.id,
        "player": game.player,
        "board": game.matrix
    })

@app.route('/games/<game_id>/move', methods=['POST'])
def move(game_id):
    game = manager.get_game(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404

    data = request.json
    if game.vs_computer and game.player == 2:
        computer_move(2, game.matrix)
    else:
        x = data.get("x")
        y = data.get("y")
        if not (0 <= x <= 4 and 0 <= y <= 4):
            return jsonify({"error": "Invalid coordinates"}), 400
        if game.matrix[x][y] != 0:
            return jsonify({"error": "Cell already taken"}), 400
        game.matrix[x][y] = game.player

    if check_winner(game.matrix, game.player):
        winner = game.player
        manager.delete_game(game_id)
        return jsonify({"message": f"Gracz {winner} wygrał!", "board": game.matrix})

    game.player = 2 if game.player == 1 else 1
    return jsonify({
        "message": "Move accepted",
        "next_player": game.player,
        "board": game.matrix
    })

@app.route('/games/<game_id>/end', methods=['POST'])
def end_game(game_id):
    if not manager.get_game(game_id):
        return jsonify({"error": "Game not found"}), 404
    manager.delete_game(game_id)
    return jsonify({"message": "Game ended"})

@app.route('/games/<game_id>/board', methods=['GET'])
def get_board(game_id):
    game = manager.get_game(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404
    return jsonify({"board": game.matrix})
