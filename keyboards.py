import json
k_menu = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Купить"
                },
                "color": "positive"
        },
        {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Продать"
                },
                "color": "negative"
        }],
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Обменять"
                }, "color": "primary"
        }],
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Курс"
                }, "color": "secondary"
        },
        {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Баланс"
                }, "color": "secondary"
        },
        {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "История"
                }, "color": "secondary"
        }]]}
k_menu = json.dumps(k_menu, ensure_ascii=False).encode('utf-8')
k_menu = str(k_menu.decode('utf-8'))

k_else = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Меню"
                },
                "color": "negative"
            }]]}
k_else = json.dumps(k_else, ensure_ascii=False).encode('utf-8')
k_else = str(k_else.decode('utf-8'))

k_bay = {
    "one_time": False,
    "buttons": [
            [{
                "action": {
                    "type": "open_link",
                    "link": "https://vk.com/cointm?w=app6471849_-194011139",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Купить"
            }}],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Меню"
                },
                "color": "negative"
            }]]}
k_bay = json.dumps(k_bay, ensure_ascii=False).encode('utf-8')
k_bay = str(k_bay.decode('utf-8'))

k_valutes = {
    "one_time": False,
    "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "CoronaCoins"
                },
                "color": "negative"
            }],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Меню"
                },
                "color": "negative"
            }]]}
k_valutes = json.dumps(k_valutes, ensure_ascii=False).encode('utf-8')
k_valutes = str(k_valutes.decode('utf-8'))

k_obmen = {
    "one_time": False,
    "buttons": [
            [{
                "action": {
                    "type": "open_link",
                    "link": "https://vk.com/coin#x591494343_1000_1_1",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Обменять"
            }}],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Меню"
                },
                "color": "negative"
            }]]}
k_obmen = json.dumps(k_obmen, ensure_ascii=False).encode('utf-8')
k_obmen = str(k_obmen.decode('utf-8'))