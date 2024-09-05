from rest_framework import mixins, viewsets


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    '''
    Набор представлений, который обеспечивает действия `create` и `list`.

    Для его использования, переопределите класс и установите
    атрибуты `.queryset` и `.serializer_class`.
    '''
