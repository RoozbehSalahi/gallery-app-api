from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test__creat_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = 'roozbehsalahi@ymail.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@ROOZBEH.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_user_invalid_email_parts(self):
        """Test the email for a new user have neccessety parts"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('@asd.com', 'test123')
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('rooz@asd', 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_no_pass(self):
        """Test setting the password empty  should not work"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('rooz@gmail.com', '')