# api\tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from status.models import Status

# Create your tests here.
# function which will be tested
# def add(a, b):
#     return a + b


# class TestAddTwoValue(TestCase):
#     # test add fn
#     # test fn_name name hbe test_fn_name dte hbe
#     # must "test_" likhte hbe fn name er age
#     def test_add(self):
#         sum = add(3, 5)
#         print(sum)
#         # to set expected test case
#         self.assertEqual(sum, 8)


# from myproject.apps.core.models import Account


class StatusTests(APITestCase):

    # setUp fn age call hbe auto
    def setUp(self):
        # create a new user, cz status create korte user lagbe
        new_user = User(username="rafid1", password="11111")
        new_user.save()

        # create new status
        status = Status(text="sample text-3", user=new_user)
        status.save()

        status2 = Status(text="sample text-4", user=new_user)
        status2.save()

    def test_create_account(self):
        url = reverse("status_view")
        # get request
        response = self.client.get(url, format="json")
        status_List = response.data
        # chk length == 1 or not
        self.assertEqual(len(status_List), 2)
        self.assertEqual(response.status_code, 200)  # 200 means success
