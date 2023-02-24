# # # from transliterate import translit
# # # import json
# # # import random
# # #
# # # with open('kurultay.json', 'r') as file:
# # #     data = json.load(file)
# # #
# # #
# # # error_user = ''
# # #
# # # users = []
# # # for i in data:
# # #     try:
# # #         if 'First_name' in i:
# # #
# # #             name = translit(i['First_name'], 'ru', reversed=True).split(' ')[0].lower()
# # #             if name in users:
# # #                 error_user = i
# # #                 user = {
# # #                     'username': name + str(random.randint(100, 999)),
# # #                     'first_name': i['First_name'],
# # #                     'living_place': i['living_place'],
# # #                     'nation': i['nation'],
# # #                     'occupation': i['occupation'],
# # #                     'is_delegat': True,
# # #                     'phone_number': i['phone_number']
# # #                 }
# # #                 users.append(user)
# # #             else:
# # #
# # #                 user = {
# # #                     'username': name,
# # #                     'first_name': i['First_name'],
# # #                     'living_place': i['living_place'],
# # #                     'nation': i['nation'],
# # #                     'occupation': i['occupation'],
# # #                     'is_delegat': True,
# # #                     'phone_number': i['phone_number']
# # #                 }
# # #                 users.append(user)
# # #         else:
# # #             print(i)
# # #
# # #     except:
# # #         print(i)
# # #
# # #
# # # print(error_user, 'dastan')
# # #
# # # with open('users.json', 'w') as file:
# # #     json.dump(users, file, ensure_ascii=False)
# # import json
# #
# # with open('users.json', 'r') as f:
# #     data = json.load(f)
# #
# # error = []
# # #
# # new_data = []
# # #
# # for i in data:
# #     try:
# #         das = int(str(i['phone_number']).split('\n')[0])
# #         new_data.append(i)
# #     except:
# #         phone = ''
# #
# #         for j in str(i['phone_number']).split('\n')[0]:
# #             if j.isdigit():
# #                 phone += j
# #         i['phone_number'] = phone
# #         new_data.append(i)
# #
# # with open('users.json', 'w') as f:
# #     json.dump(new_data, f, ensure_ascii=False)
# #
# #
# #
# # print(error)
# #
# import json
#
# with open('users.json', 'r') as f:
#     data = json.load(f)
#
# i = 0
# page = 0
# new_data = []
# while True:
#
#     new_data.append(data[i])
#     i += 1
#     if i == 100:
#         with open('users_1.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 200:
#         with open('users_2.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 300:
#         with open('users_3.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 400:
#         with open('users_4.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 500:
#         with open('users_5.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 600:
#         with open('users_6.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 700:
#         with open('users_7.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 800:
#         with open('users_8.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 900:
#         with open('users_9.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 1000:
#         with open('users_10.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#     if i == 1100:
#         with open('users_11.json', 'w') as f:
#             json.dump(new_data, f, ensure_ascii=False)
#             new_data = []
#
#
import json
with open('users_1.json', 'r') as f:
    data = json.load(f)

i = 0
page = 1
new_data = []
while True:
    new_data.append(data[i])
    i += 1
    if i == 50:
        with open(f'users_{page}_0.json', 'w') as f:
            json.dump(new_data, f, ensure_ascii=False)
    elif i == 100:
        with open(f'users_{page}_1.json', 'w') as f:
            json.dump(new_data, f, ensure_ascii=False)
        i = 0
        page += 1
    with open(f'users_{page}.json', 'r') as f:
        data = json.load(f)

