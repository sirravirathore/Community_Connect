from django.urls import pathfrom a_users.views import profile_viewfrom .views import chat_view, chat_file_upload, private_viewurlpatterns = [    path('chatting/public-chat/', chat_view, name='chat_view'),    path('chatting/fileupload/', chat_file_upload, name="chat-file-upload"),    # path('chatting/<username>', get_or_create_chatroom, name="start-chat"),    path('chatting/<chatroom_name>', private_view, name="chatroom")]