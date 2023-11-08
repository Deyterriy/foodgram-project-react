from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Кастомная пагинация, вывод 6 элементов"""

    page_size_query_param = 'limit'
    page_size = 6
