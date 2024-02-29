from rest_framework import pagination


class PagePagination(pagination.PageNumberPagination):
    # Количество элементов на странице
    page_size = 20
    # Параметр запроса: количества элементов на странице
    page_size_query_param = 'page_size'
    # Максимальное количество элементов на странице
    max_page_size = 30
