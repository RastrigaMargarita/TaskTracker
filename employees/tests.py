from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee
from tasks.models import Task


class EmployeeTestCase(APITestCase):

    def test_CRUD_employee(self):
        data = {"name": "Иван",
                "second_name": "Иванов",
                "role": "программист",
                "level": Employee.Level.MIDDLE,
                }

        data_update = {'id': 1,
                       'level': Employee.Level.SENIOR,
                       'name': 'Иван',
                       'role': 'программист',
                       'second_name': 'Иванов'}
        response_data = {'id': 1,
                         'level': 'middle',
                         'name': 'Иван',
                         'role': 'программист',
                         'second_name': 'Иванов'}
        response_data_updated = {'id': 1,
                                 'level': 'senior',
                                 'name': 'Иван',
                                 'role': 'программист',
                                 'second_name': 'Иванов'}

        response_list = [{'id': 1,
                          'name': 'Иван',
                          'second_name': 'Иванов',
                          'role': 'программист',
                          'level': 'senior'}]

        # CREATE
        response = self.client.post('/employees/employee/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("CREATE")
        self.assertEqual(response.json(), response_data)
        self.assertTrue(Employee.objects.all().exists())

        # UPDATE
        self.client.patch('/employees/employee/1/', data=data_update)
        print("UPDATE")

        # GET
        response = self.client.get('/employees/employee/1/')
        print("GET")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response_data_updated)

        # GET_LIST
        response = self.client.get('/employees/employee/')
        print("LIST")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), response_list)

        # DELETE
        response = self.client.delete('/employees/employee/1/')
        print("DELETE")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_current_works(self):
        data_employee = {"name": "Иван",
                         "second_name": "Иванов",
                         "role": "программист",
                         "level": Employee.Level.MIDDLE
                         }

        response = self.client.post('/employees/employee/', data=data_employee)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data_task = {"title": "Задача 1",
                     "description": "Описание 1",
                     "responsible_person": "2",
                     "status": Task.TaskStatus.NEW,
                     "estimated_duration": 60
                     }

        response = self.client.post('/tasks/task/', data=data_task)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data_response = [{'employee': 'Иванов Иван - программист (middle)',
                          'task_quantity': 0,
                          'task_list': [{'title': 'Задача 1',
                                         'estimated_duration': '60.00',
                                         'deadline': None}]}]

        print("CURRENT WORKS")
        response = self.client.get('/employees/current_works')
        self.assertEqual(response.json(), data_response)
