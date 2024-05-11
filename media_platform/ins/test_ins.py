from instagrapi import Client

cl = Client()
LOGIN_USERNAME = "sunwhite9587@gmail.com"
cl_login = cl.login(username=LOGIN_USERNAME, password="sunwhiteins1234")
username = "sunwhite9587"
user_id = cl.user_id_from_username(username)
print(user_id)
user_info = cl.user_info_by_username(username=username)
print(user_info)
medias = cl.user_medias(user_id)
print(medias)