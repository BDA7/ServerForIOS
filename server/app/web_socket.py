from fastapi import FastAPI, WebSocket
from typing import Dict
import logging

app = FastAPI()
clients: Dict[str, WebSocket] = {}

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        message_data = {"username": "Server", "message": "Write your username"}
        await websocket.send_json(message_data)
        username = await websocket.receive_text()

        # Проверяем уникальность имени пользователя
        if username in clients:
            await websocket.send_text("Username already exists. Please choose another one.")
            await websocket.close()
            return

        # Добавляем клиента в словарь
        clients[username] = websocket
        logger.info(f'{username} connecting')

        # Цикл обработки сообщений
        while True:
            data = await websocket.receive_text()
            # Отправляем JSON-сообщение всем подключенным клиентам
            for client_username, client_websocket in clients.items():
                if client_username != username:
                    message_data = {"username": username, "message": data}
                    await client_websocket.send_json(message_data)
                    logger.info(f'{username} send: {data}')
    except Exception as e:
        logger.error(f"WebSocket connection closed with exception: {e}")
        del clients[username]
    finally:
        # Удаляем клиента из словаря
        if username in clients:
            del clients[username]
