from django.urls import path, include
from rest_framework import routers
from . import views
from .views import LessonCreateApiView, LessonListApiView, LessonRetrieveApiView, LessonUpdateApiView, \
    LessonDestroyApiView, PaymentCreateAPIView, PaymentListAPIView, SubscriptionCreateView, SubscriptionDeleteView, \
    SubscriptionUpdateView

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('lesson/create', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/', LessonListApiView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', LessonRetrieveApiView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>', LessonUpdateApiView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDestroyApiView.as_view(), name='lesson_delete'),

    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/all/', PaymentListAPIView.as_view(), name='payment_list'),

    path("subscription/create/", SubscriptionCreateView.as_view(), name="subscription_create"),
    path("subscription/delete/<int:pk>/", SubscriptionDeleteView.as_view(), name="subscription_delete"),
    path("subscription/update/<int:pk>/", SubscriptionUpdateView.as_view(), name="subscription_update"),
]
