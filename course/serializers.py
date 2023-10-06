from rest_framework import serializers

from course.models import Course, Lesson, Payment

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lessons_count(self, instance):
        return instance.lessons.all().count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'image', 'description', 'lessons_count', 'lessons']




class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'