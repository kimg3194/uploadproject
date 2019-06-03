
from django.contrib import admin
from django.urls import path, include #include 포함
import blog.views 
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"), 
    path('blog/', include('blog.urls')), 
    # blog앱 안에 있는 urls에서 가져오고 형식은 blog/을 취해라
    path('accounts/', include('accounts.urls')),
    # accounts앱 안에 있는 urls에서 가져오고 형식은 accounts/를 취해라
]
