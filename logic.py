import vk_api, urllib3, random
from vk_api.longpoll import VkLongPoll, VkEventType
from defs import wm, wms, balance, send, history, garden, garden_balance, delete, uichat, user, delete_msg
from keyboards import k_menu, k_else, k_bay, k_obmen, k_valutes

token = "d1c8f9abdcb87650014e6e1fa8de766d9e5fe43e89b07e9a6a91a9a6a3595ccf80d03111c0e1198f31a60"
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

urllib3.disable_warnings()

print("Бот запущен")

id_w = []
promo = 2000; promo_u = []

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_user and event.to_me:
            ans = event.text
            id = event.user_id
            if ans == "Меню":
                wm(id, "Вы находитесь на Торговой Площадке CTM", k_menu)
            elif ans == "Купить":
                wm(id, "Выберите валюту.", k_valutes)
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.from_user and event.to_me:
                            ans = event.text
                            id = event.user_id
                            if ans == "CoronaCoins":
                                wm(id, "Покупка CoronaCoins преостановлена.", k_else)
                            elif ans == "Меню":
                                wm(id, "Вы находитесь на Торговой Площадке CTM", k_menu)
                                break
                            else:
                                wm(id, "Такой команды нет, перейдите в Меню", k_else)
            elif ans == "Продать":
                wm(id, "Продажа недоступна.", k_else)

            elif ans == "Курс":
                wm(id, "Недоступно.", k_else)

            elif ans == "Баланс":
                scores = balance(id)
                wm(id, "Наш резерв:\n&#12288;CoronaCoins: " + scores[0] + "\n&#12288;VKCoin: " + scores[3] + "\n\nВаш баланс:\n&#12288;CoronaCoins: " + scores[1] + "\n&#12288;VKCoins: " +scores[2], k_else)

            elif ans == "Обменять":
                wm(id, "Обмен недоступен. ", k_else)

            elif ans == "История":
                hstr = history()
                wm(id, "История последних полученных переводов:\n\n" + "От @id" + str(hstr[1]) + "\n&#12288;Сумма: " + str(hstr[0]) + "\nОт @id" + str(hstr[3]) + "\n&#12288;Сумма: " + str(hstr[2]) + "\nОт @id" + str(hstr[5]) + "\n&#12288;Сумма: " + str(hstr[4]) + "\nОт @id" + str(hstr[7]) + "\n&#12288;Сумма: " + str(hstr[6]) + "\nОт @id" + str(hstr[9]) + "\n&#12288;Сумма: " + str(hstr[8]), k_else)

            elif ans == "ZNDK-OWKD-NDND" and promo > 0:
                if id not in promo_u:
                    promo = promo - 1
                    promo_u.append(id)
                    send(id, 1)
                    wm(id, "Промокод активирован.\n\n Вы получили " + str(0.001) + " CoronaCoins!\n\n Обманул)", k_menu)
                elif id in promo_u:
                    wm(id, "Вы уже активировали этот промокод.\n\nВключайте уведомления и ждите следующий :D", k_menu)
            elif ans == "ZNDK-OWKD-NDND" and promo <= 0:
                wm(id, "Промокод закончился.\n\nВключайте уведомления и ждите следующий :D", k_menu)
            elif ans == "Отправить" and id == 244533400:
                for i in id_w:
                    send(i, 10000000)
                wm(id, "Призы отправлены", k_else)
                break

            else:
                wm(id, "Такой команды нет, перейдите в Меню", k_else)


        if event.from_chat and event.to_me:
            ans = event.text
            chat = event.peer_id
            id = event.user_id
            chat_id = event.chat_id
            if ans == "/панель" or ans == "Меню":
                wms(chat, "Команды Администрации: \n1. /баланс\n2. /собрать урожай\n3. /кик\n4. /перевод\n5. /число\n6. /кто\n7. /роль\n8. /онлайн\n9. /суицид\n\n Команды Пользователей:\n1. /баланс\n2. /число\n3. /кто\n4. /роль\n5. /онлайн\n6. /суицид")
            elif ans == "/собрать урожай" and id == 244533400 or ans == "/собрать урожай" and id == 377571282:
                col = garden()
                col_col = col[0] + col[1] + col[2]
                ti = col_col / 406800
                wms(chat, "Вы собрали урожай!\n\nАккаунт Андрея собрал: " + str(col[1]) + "\nАккаунт Лёхи собрал: " + str(col[0]) + "\nФейк собрал: " + str(col[2]) + "\n\nСобрано всего: " + str(col_col) + "\nЗа: " + str(round(ti, 1)) + " минут")
                if id == 244533400:
                    wm(377571282, "Лёха собрал урожай! \nЦелых " + str(col_col) + " коинов!", k_else)
                elif id == 377571282:
                    wm(244533400, "Андрей собрал урожай!\nЦелых " + str(col_col) + " коинов!", k_else)
            elif ans == "/баланс" and id == 244533400 or ans == "/баланс" and id == 377571282:
                col = garden_balance()
                wms(chat, "Баланс:\n\n Общий баланс: " + str(col[4]) + "\n\nБаланс основного аккаунта: " + str(col[3]) + "\nБаланс Андрея: " + str(col[1]) + "\nБаланс Лёхи: " + str(col[0]) + "\nБаланс фейка: " + str(col[2]))
            elif ans[:4] == "/кик" and id == 244533400 or ans[:4] == "/кик" and id == 377571282:
                kick = ans[5:]
                kick = kick[3:12]
                if kick.isdigit() == True:
                    delete(chat_id, kick)
                    wms(chat, "Пользователь: @id" + str(kick) + " исключен из беседы.")
                elif kick.isdigit() == False:
                    wms(chat, "Неверная команда.")
            elif ans[:4] == "/кик" or ans == "/суицид":
                kick = ans[5:]
                kick = kick[3:12]
                if ans[:4] == "/кик":
                    if int(kick) == id:
                        if kick.isdigit() == True:
                            delete(chat_id, kick)
                            wms(chat, "Пользователь: @id" + str(kick) + " совершил самоубийство.")
                        elif kick.isdigit() == False:
                            wms(chat, "Неверная команда.")
                    elif int(kick) != id:
                        wms(chat, "Нет доступа.")
                elif ans == "/суицид":
                    delete(chat_id, id)
                    wms(chat, "Пользователь: @id" + str(id) + " совершил самоубийство.")
            elif ans[:8] == "/перевод" and id == 244533400 or ans[:8] == "/перевод" and id == 1:
                scores = balance(id)
                ans = ans.split()
                id_send = ans[1][3:12]
                sum = ans[2]
                scores1 = scores[0].replace('.', '')
                if sum <= scores1:
                    send(id_send, sum)
                    wms(chat, "Пользователю: @id" + str(id_send) + " отправлено " + str(sum) + " коинов.")
                elif sum > scores1:
                    wms(chat, "Недостаточно коинов.\nБаланс: " + str(scores[0]))
            elif ans == "/баланс" and id != 244533400 and id != 377571282:
                scores = balance(id)
                wms(chat, "Ваш баланс: " + scores[1])
            elif ans[:4] == "/кто":
                cto = ans[4:]
                users = uichat(chat)
                num_users = len(users['profiles'])
                rand_u = random.randint(1, num_users)
                if len(cto) < 100:
                    wms(chat,"[" + str(users['profiles'][rand_u]['screen_name']) + "|@" + str(users['profiles'][rand_u]['first_name']) + "]" + str(cto))
                elif len(cto) > 100:
                    wms(chat,"Максимальное количество знаков: 100")
            elif ans[:6] == "/число":
                num = ans.split()
                if len(num) == 3 and (num[1].isdigit() and num[2].isdigit()) == True:
                    if int(num[1]) < int(num[2]) <= 100000000000000:
                        wms(chat, str(random.randint(int(num[1]), int(num[2]))))
                    elif int(num[2]) > 100000000000000:
                        wms(chat, "Превышено максимально допустимое значение.")
                    elif int(num[1]) > int(num[2]):
                        wms(chat, "Неправльно введён диапазон.\n\n a < b")
                elif len(num) != 3 or num[1].isdigit() == False or num[2].isdigit() == False:
                    wms(chat, "Недопустимое значение.")
            elif ans[:2] == "/я" or ans[:5] == "/роль":
                user_name = user(id)
                users = uichat(chat)
                num_users = len(users['items'])
                rol = "Пользователь"
                for i in range(1, num_users):
                    if users['items'][i]['member_id'] == id and 'is_admin' in users['items'][i]:
                        rol = "Администратор"
                wms(chat, "Вы: " + user_name[0]['first_name'] + " " + user_name[0]['last_name'] + "\nРоль: " + str(rol))
            elif ans == "/онлайн":
                users = uichat(chat)
                num_users = len(users['profiles'])
                online = ""
                for i in range(1, num_users):
                    if users['profiles'][i]['online'] == 1:
                        online = online + "\n" + "[" + str(users['profiles'][i]['screen_name']) + "|@" + str(users['profiles'][i]['first_name']) + "]"
                wms(chat,"Пользователи онлайн:\n" + str(online))
            elif "https" in ans or "http" in ans or "com" in ans or "ru" in ans:
                users = uichat(chat)
                num_users = len(users['items'])
                rol = 0
                for i in range(1, num_users):
                    if users['items'][i]['member_id'] == id and 'is_admin' in users['items'][i]:
                        rol = 1
                        if rol == 1:
                            wms(chat,"Вы Администратор.")
                if rol == 0:
                        delete_msg(chat)
                        wms(chat,"Сообщение удалено.\n\nСпам.")