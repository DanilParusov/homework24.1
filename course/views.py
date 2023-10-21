from rest_framework import viewsets, generics

from course.models import Course, Lesson, Payment, Subscription
from course.pagination import DataPaginator
from course.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from course.permissions import IsOwner, IsStaff
import stripe
from course.tasks import sendmail

stripe.api_key = "pk_test_51O2y1aAHG2EDoyGQA1ICrgZp8c26RT4LxOQgfeLLhpVixxlHo2LVM87jgvZ03DW2PAmQ7CuZGSoNaVej0OP3rxdI00qyklzcfM"


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

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.owner = self.request.user
        new_payment.save()

        # create user
        new_customer = self.request.user
        request_user = stripe.Customer.create(
            name=new_customer.email,
            email=new_customer.email,
        )
        current_id = request_user.id
        print(current_id)

        # create transaction
        request_payment = stripe.PaymentIntent.create(
            amount=new_payment.summ,
            currency="usd",
            automatic_payment_methods={"enabled": True},
            customer=current_id,
        )
        print(request_payment.id)
        # save remote id to base
        new_payment = serializer.save()
        new_payment.remote_id = request_payment.id
        new_payment.save()


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

class SubscriptionUpdateView(generics.UpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsStaff | IsOwner]

    def put(self, request, *args, **kwargs):
        sendmail.delay()
        return self.update(request, *args, **kwargs)