from django.test import TestCase, RequestFactory
from demo.models import Person, Role  # Import your Person and Role models
from demo.tables import PersonTable
from demo.views import index_view, IndexView, PersonsList, PersonDetailView, \
    PersonUpdateView, PersonDeleteView, PersonCreateView  # Import the views you want to test
from django.urls import reverse, resolve  # Import reverse and resolve
from django.template.response import TemplateResponse
from demo.views import index_view
from demo.forms import PersonForm


class PersonModelTest(TestCase):
    """
    This class defines test cases for the Person model.
    It inherits from Django's TestCase, which provides a test environment.
    """

    def setUp(self):
        """
        Set up method to create a Person instance before each test.
        This ensures each test starts with a clean state.
        """
        self.role1 = Role.objects.create(name="Editor")
        self.role2 = Role.objects.create(name="Reviewer")
        self.john = Person.objects.create(
            lastname="Doe",
            firstname="John",
            language="en",  # Set a valid language
            currency=10, # Set a valid currency
        )
        self.john.roles.add(self.role1)

    def test_person_creation(self):
        """
        Test that a Person object is created correctly.
        It retrieves the Person object created in setUp() and checks
        if its attributes match the expected values.
        """
        john = Person.objects.get(firstname="John")
        self.assertEqual(john.lastname, "Doe")
        self.assertEqual(john.firstname, "John")
        self.assertEqual(john.language, "en")
        self.assertEqual(john.currency, 10)
        self.assertEqual(john.is_active, True)
        self.assertIn(self.role1, john.roles.all())


    def test_person_string_representation(self):
        """
        Test the string representation of the Person object.
        Checks if the __str__ method of the Person model returns
        the expected string.
        """
        john = Person.objects.get(firstname="John")
        self.assertEqual(str(john), "John Doe")

    def test_person_default_values(self):
        """
        Test the default values of a Person object.
        Creates a new Person object with only the required fields
        and checks if the other fields have the correct default values.
        """
        jane = Person.objects.create(
            lastname="Smith",
            firstname="Jane",
            language="pl",  # Set a valid language
            currency=20, # Set a valid currency
        )
        self.assertIsNone(jane.comment)
        self.assertIsNone(jane.email)
        self.assertIsNone(jane.website)
        self.assertEqual(jane.language, "pl")
        self.assertEqual(jane.currency, 20)

    def test_person_uniqueness(self):
        """
        Test the uniqueness of a field.  Your Person model doesn't enforce
        uniqueness on email or username, so this test is not appropriate.
        """
        pass # there is no unique field


    def test_person_custom_methods(self):
        """
        Test custom methods of the Person model.
        This test calls a custom method (e.g., `get_full_name()`)
        and checks if it returns the expected value.
        """
        john = Person.objects.get(firstname="John")
        self.assertEqual(john.__str__(), "John Doe") # Corrected to use __str__()

    def test_person_add_method(self):
        """Test the Person.add() static method."""
        new_person = Person.add("Robert", "Frost")
        self.assertEqual(new_person.firstname, "Robert")
        self.assertEqual(new_person.lastname, "Frost")
        self.assertIsNotNone(new_person.username)

    def test_person_save_username(self):
        """Test that the username is correctly set on save."""
        person1 = Person.objects.create(firstname="Albert", lastname="Einstein", language="en", currency=10)
        self.assertEqual(person1.username, "aeinstein")

        person2 = Person.objects.create(firstname="Michael", lastname="Jordan", language="en", currency=10)
        self.assertEqual(person2.username, "mjordan")

class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_redirect(self):
        """
        Test the index_view function, which should redirect to 'demo-index-view'.
        """
        # Use reverse to get the URL for the view you want to test
        url = reverse('demo-index-view')
        request = self.factory.get(url)  # Create a GET request
        response = index_view(request)  # Call the view

        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a redirect
        self.assertEqual(response.url, reverse('demo-index-view'))  # Check the redirect URL

    def test_index_view_dispatch(self):
        """
        Test the dispatch method of the IndexView.
        This test checks if the dispatch method is called and returns a valid response.
        """
        url = reverse('demo-index-view')
        request = self.factory.get(url)
        view = IndexView()
        view.setup(request)  # You need to call setup
        response = view.dispatch(request)

        self.assertEqual(response.status_code, 200)


class PersonViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.john = Person.objects.create(
            lastname="Doe",
            firstname="John",
            language="en",  # Set a valid language
            currency=10,  # Set a valid currency
        )

    def test_persons_list_view(self):
        """
        Test the PersonsList view.
        This view should display a list of Person objects.
        """
        url = reverse('demo-person-list')  # Replace with your actual URL name
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, TemplateResponse)
        self.assertTemplateUsed(response, 'person-list.html')  # Check the template name
        self.assertEqual(response.context_data['persons'].count(),
                         1)  # Check that the person created in setUp is in the context
        self.assertIsInstance(response.context_data['table'], PersonTable)  # check the table class

    def test_person_detail_view(self):
        """
        Test the PersonDetailView.
        This view should display the details of a single Person object.
        """
        url = reverse('demo-person-detail', kwargs={'pk': self.john.pk})  # Use the pk of the Person created in setUp
        response = self.client.get(url) # Pass pk to the view

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, TemplateResponse)
        self.assertTemplateUsed(response, 'person-detail.html')
        self.assertEqual(response.context_data['person'], self.john)

    def test_person_update_view(self):
        """
        Test the PersonUpdateView.
        This view should allow updating an existing Person object.
        """
        url = reverse('demo-person-update', kwargs={'pk': self.john.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, TemplateResponse)
        self.assertTemplateUsed(response, 'person-update.html')

        # Test the POST request to update the Person
        form_data = {
            'firstname': 'UpdatedJohn',
            'lastname': 'UpdatedDoe',
            'language': 'en',  # Include other required fields
            'currency': 10,
        }
        request = self.factory.post(url, data=form_data)
        response = PersonUpdateView.as_view()(request, pk=self.john.pk)

        self.assertEqual(response.status_code, 302)  # Check for redirect after successful update
        self.john.refresh_from_db()  # Refresh the Person object from the database
        self.assertEqual(self.john.firstname, 'UpdatedJohn')  # Check that the update was successful

    def test_person_delete_view(self):
        """
        Test the PersonDeleteView.
        This view should allow deleting an existing Person object.
        """
        url = reverse('demo-person-delete', kwargs={'pk': self.john.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, TemplateResponse)
        self.assertTemplateUsed(response, 'person-delete.html')

        # Test the POST request to delete the Person
        request = self.factory.post(url)
        response = PersonDeleteView.as_view()(request, pk=self.john.pk)

        self.assertEqual(response.status_code, 302)  # Check for redirect after successful deletion
        self.assertFalse(Person.objects.filter(pk=self.john.pk).exists())  # Check that the Person is deleted

    def test_person_create_view(self):
        """
        Test the PersonCreateView.
        This view should allow creating a new Person object.
        """
        url = reverse('demo-person-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, TemplateResponse)
        self.assertTemplateUsed(response, 'person-create.html')

        # Test the POST request to create a new Person
        form_data = {
            'firstname': 'NewPerson',
            'lastname': 'Test',
            'language': 'en',  # Include all required fields
            'currency': 10,
        }
        request = self.factory.post(url, data=form_data)
        response = PersonCreateView.as_view()(request)

        self.assertEqual(response.status_code, 302)  # Check for redirect after successful creation
        new_person = Person.objects.get(firstname='NewPerson')  # Get the newly created Person
        self.assertEqual(new_person.lastname, 'Test')


class PersonFormTest(TestCase):
    def setUp(self):
        # Create a Person object to use for testing the form's initial data or saving
        self.person_data = {
            'lastname': 'Doe',
            'firstname': 'John',
            'language': 'en',
            'currency': 10,
        }
        self.person = Person.objects.create(**self.person_data)

    def test_valid_form(self):
        """
        Test that the form is valid with valid data.
        """
        form_data = {
            'lastname': 'Smith',
            'firstname': 'Jane',
            'language': 'pl',
            'currency': 20,
        }
        form = PersonForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Test that the form is invalid with invalid data.
        """
        form_data = {
            'lastname': '',  # Lastname is required, so this should make the form invalid
            'firstname': 'Jane',
            'language': 'pl',
            'currency': 20,
        }
        form = PersonForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('lastname', form.errors)  # Check for the specific error

    def test_form_save(self):
        """
        Test that the form saves correctly.
        """
        form_data = {
            'lastname': 'Smith',
            'firstname': 'Jane',
            'language': 'pl',
            'currency': 20,
        }
        form = PersonForm(data=form_data)
        self.assertTrue(form.is_valid())
        person = form.save()  # Save the form data
        self.assertEqual(person.lastname, 'Smith')  # Check if the data was saved correctly
        self.assertEqual(person.firstname, 'Jane')
        self.assertEqual(person.language, 'pl')
        self.assertEqual(person.currency, 20)

    def test_form_with_instance(self):
        """
        Test that the form is populated correctly when initialized with an instance.
        """
        form = PersonForm(instance=self.person)
        self.assertEqual(form.initial['lastname'], 'Doe')
        self.assertEqual(form.initial['firstname'], 'John')
        self.assertEqual(form.initial['language'], 'en')
        self.assertEqual(form.initial['currency'], 10)
