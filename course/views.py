from rest_framework import viewsets, generics

from course.models import Course, Lesson, Payment, Subscription
from course.pagination import DataPaginator
from course.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from course.permissions import IsOwner, IsStaff


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsOwner | IsStaff]
    
    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()
    
    

class LessonCreateApiView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsStaff]
    
    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()
    

class LessonListApiView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]
    pagination_class = DataPaginator

class LessonRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]
    pagination_class = DataPaginator

class LessonUpdateApiView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]

class LessonDestroyApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsOwner | IsStaff]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('payment_data',)
    permission_classes = [IsOwner | IsStaff]

class SubscriptionCreateView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]

    def perform_create(self, serializer):
        new_subscription = serializer.save()
        new_subscription.owner = self.request.user
        new_subscription.save()

class SubscriptionDeleteView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]