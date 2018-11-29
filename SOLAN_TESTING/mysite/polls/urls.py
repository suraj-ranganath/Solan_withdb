from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='dashboardS.html'), name='dashboard'),
    #path(name='home', 'home', )
]
#if settings.DEBUG:
#    urlpatterns += static(settings.BASE_URL, document_root=settings.BASE_ROOT)  # uploaded media
#    urlpatterns += staticfiles_urlpatterns()  # files in each app's static/ dir