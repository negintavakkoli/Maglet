

from rest_framework import routers
from recom_api import views
from django.urls import path,include


router = routers.DefaultRouter()
router.register(r'journal_info', views.JournalViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', views.snippet_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#
#
# urlpatterns = [
#     path('lookup',views.lookup),
#     path('viewdata',views.t1),
# ]


# myapi/urls.pyfrom django.urls import include, path

