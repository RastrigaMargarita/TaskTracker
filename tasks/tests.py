from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee
from tasks.models import Task


class TestCase(APITestCase):

    def setUp(self):
        Employee.objects.create(name="Иван",
                                second_name="Иванов",
                                role="программист",
                                level=Employee.Level.MIDDLE)
        Employee.objects.create(name="Василий",
                                second_name="Васильевич",
                                role="программист",
                                level=Employee.Level.JUNIOR)

    def test_CRUD_task(self):
        data = {"title": "Задача 1",
                "description": "Описание 1",
                "status": Task.TaskStatus.NEW,
                "estimated_duration": 60
                }

        data_update = {'id': 1,
                       "responsible_person": "1"}

        response_data = {'deadline': None,
                         'description': 'Описание 1',
                         'estimated_duration': '60.00',
                         'id': 2,
                         'previouse_task': None,
                         'responsible_person': None,
                         'status': 'new',
                         'title': 'Задача 1'}

        response_data_updated = {'deadline': None,
                                 'description': 'Описание 1',
                                 'estimated_duration': '60.00',
                                 'id': 2,
                                 'previouse_task': None,
                                 'responsible_person': None,
                                 'status': 'new',
                                 'title': 'Задача 1'}

        response_list = {'count': 1,
                         'next': None,
                         'previous': None,
                         'results': [{'id': 2,
                                      'title': 'Задача 1',
                                      'description': 'Описание 1',
                                      'status': 'new',
                                      'estimated_duration': '60.00',
                                      'deadline': None,
                                      'previouse_task': None,
                                      'responsible_person': None}]}
        # CREATE
        response = self.client.post('/tasks/task/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("CREATE")
        self.assertEqual(response.json(), response_data)
        self.assertTrue(Task.objects.all().exists())

        # UPDATE
        self.client.patch('/tasks/task/2/', data=data_update)
        print("UPDATE")

        # GET
        response = self.client.get('/tasks/task/2/')
        print("GET")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response_data_updated)

        # GET_LIST
        response = self.client.get('/tasks/task/')
        print("LIST")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response_list)

        # DELETE
        response = self.client.delete('/tasks/task/2/')
        print("DELETE")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_important_tasks(self):

        data_task1 = {"title": "Задача 1",
                      "description": "Описание 1",
                      "responsible_person": "5",
                      "status": Task.TaskStatus.TAKEN,
                      "estimated_duration": 60,
                      "deadline": "2025-03-10"
                      }
        data_task2 = {"title": "Задача 1",
                      "description": "Описание 1",
                      "previouse_task": "3",
                      "status": Task.TaskStatus.NEW,
                      "estimated_duration": 60
                      }
        data_task3 = {"title": "Задача 1",
                      "description": "Описание 1",
                      "previouse_task": "4",
                      "status": Task.TaskStatus.NEW,
                      "estimated_duration": 60}
        data_task4 = {"title": "Задача 1",
                      "description": "Описание 1",
                      "status": Task.TaskStatus.NEW,
                      "estimated_duration": 60
                      }
        data_task5 = {"title": "Задача 1",
                      "description": "Описание 1",
                      "responsible_person": "1",
                      "status": Task.TaskStatus.DONE,
                      "estimated_duration": 60
                      }

        self.client.post('/tasks/task/', data=data_task1)
        self.client.post('/tasks/task/', data=data_task2)
        self.client.post('/tasks/task/', data=data_task3)
        self.client.post('/tasks/task/', data=data_task4)
        self.client.post('/tasks/task/', data=data_task5)

        response_data = [{'id': 4,
                          'title': 'Задача 1',
                          'description': 'Описание 1',
                          'deadline': None,
                          'estimated_duration': '60.00',
                          'employees_to_assign': [{'name': 'Иван',
                                                   'second_name': 'Иванов'}]}]
        response_data_updated = [{'id': 4,
                                  'title': 'Задача 1',
                                  'description': 'Описание 1',
                                  'deadline': None,
                                  'estimated_duration': '60.00',
                                  'employees_to_assign': [{'name': 'Василий',
                                                           'second_name': 'Васильевич'}]}]

        print("IMPORTANT TASKS")
        response = self.client.get('/tasks/important_works')
        self.assertEqual(response.json(), response_data)

        data_update = {"responsible_person": "5"}
        self.client.patch('/tasks/task/5/', data=data_update)
        self.client.patch('/tasks/task/6/', data=data_update)

        response = self.client.get('/tasks/important_works')
        self.assertEqual(response.json(), response_data_updated)
