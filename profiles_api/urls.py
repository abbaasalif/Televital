from django.urls import path,include
from rest_framework.routers import DefaultRouter

from profiles_api import views
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)
router.register('vitals',views.PatientVitalsViewset)
router.register('actualvitals',views.ActualVitalsViewset)
urlpatterns=[
path('hello-view/',views.HelloApiView.as_view(),name=None),
path('login/', views.UserLoginApiView.as_view()),
path('',include(router.urls))
]
