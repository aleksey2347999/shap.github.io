from flask import Flask, request, jsonify
from flask_cors import CORS
import chess
import chess.engine
import base64
import io
from PIL import Image
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__)
CORS(app)

# Загрузка модели распознавания шахматных фигур (заглушка, нужна реальная модель)
def load_chess_recognition_model():
    # Здесь должна быть загрузка обученной модели (например, CNN на PyTorch/TensorFlow)
    # Для примера - заглушка
    print("Модель распознавания фигур загружена (заглушка)")
    return None

model = load_chess_recognition_model()

# Функция распознавания позиции с фото (заглушка)
def recognize_position_from_image(image):
    # Реальная реализация:
    # 1. Преобразование изображения в тензор
    # 2. Предсказание фигур для всех 64 клеток
    # 3. Возврат FEN строки
    return "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Функция расчета лучшего хода
def calculate_best_move(fen_position, depth=15):
    try:
        board = chess.Board(fen_position)
        with chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish") as engine:
            result = engine.play(board, chess.engine.Limit(depth=depth))
            best_move = result.move
            # Оценка позиции
            info = engine.analyse(board, chess.engine.Limit(depth=depth))
            score = info["score"].relative.score()
            return {
                "best_move": board.san(best_move),
                "best_move_uci": best_move.uci(),
                "score": score,
                "fen": fen_position
            }
    except Exception as e:
        return {"error": str(e)}

@app.route('/api/analyze', methods=['POST'])
def analyze_position():
    try:
        data = request.json
        image_data = data.get('image')
        
        if image_data:
            # Декодируем base64 изображение
            image_bytes = base64.b64decode(image_data.split(',')[1])
            image = Image.open(io.BytesIO(image_bytes))
            
            # Распознаем позицию
            fen = recognize_position_from_image(image)
        else:
            fen = data.get('fen')
        
        if not fen:
            return jsonify({"error": "No image or FEN provided"}), 400
        
        # Получаем лучший ход
        analysis = calculate_best_move(fen)
        return jsonify(analysis)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "active"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
