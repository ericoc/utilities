from rest_framework.pagination import PageNumberPagination


#class APIUtilityPagination(CursorPagination):
#    """
#    Base Django-Rest-Framework (DRF) pagination for utility usage API view-sets.
#    """
#    fields = "__all__"

class APIUtilityPagination(PageNumberPagination):
    """
    Base Django-Rest-Framework (DRF) pagination for utility usage API view-sets.
    """
    page_size = 100
    page_size_query_param = "limit"
