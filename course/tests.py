from rest_framework.test import APITestCase
from course.models import Lesson, Course, Subscription
from rest_framework import status
from users.models import User


class CourseTestCase(APITestCase):
    """ Testing Application Course """

    def setUp(self):
        """ Prepare testing """
        self.user = User(
            email="test3@gmail.com"
        )
        self.user.set_password("0000")
        self.user.save()

        response = self.client.post(
            "/users/token/",
            {"email": "test3@gmail.com", "password": "0000"}
        )

        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.course = Course.objects.create(
            title="Test Course",
            description="Test Course",
        )

        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="Test Lesson",
            course=self.course
        )

    def test_create_subscription(self):
        data = {'id': 1,
                'is_subscribed': False,
                "owner": 1,
                "course": 1
                }

        response = self.client.post("/subscription/create/", data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertTrue(Subscription.objects.all().exists())

    def test_get_lessons(self):
            response = self.client.get("/lesson/")

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )

    def test_validate_lesson(self):
        data = {"title": "Test Lesson23",
                "description": "https://vk.com"
                }

        response = self.client.post("/lesson/create/", data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_get_courses(self):
            response = self.client.get("/courses/")

            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )

    def test_validate_course(self):
            data = {"title": "Test Lesson23",
                    "description": "https://vk.com"
                    }

            response = self.client.post("/course/", data)

            self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST
            )

