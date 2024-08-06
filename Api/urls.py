from django.urls import path
from .views import Register, Login, Logout, Mark_spam, Search_by_name, Search_By_num

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('mark_spam/', Mark_spam.as_view(), name='mark_spam'),
    path('search_by_name/', Search_by_name.as_view(), name='search_by_name'),
    path('search_by_number/', Search_By_num.as_view(), name='search_by_phone_number'),
]
