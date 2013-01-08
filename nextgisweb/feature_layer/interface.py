# -*- coding: utf-8 -*-
from zope.interface import Interface, Attribute


class GEOM_TYPE(object):
    POINT = 'POINT'
    LINESTING = 'LINESTING'
    POLYGON = 'POLYGON'

    enum = (POINT, LINESTING, POLYGON)


class FIELD_TYPE(object):
    INTEGER = 'INTEGER'
    REAL = 'REAL'
    STRING = 'STRING'
    DATE = 'DATE'
    TIME = 'TIME'
    DATETIME = 'DATETIME'

    enum = (INTEGER, REAL, STRING, DATE, TIME, DATETIME)


class IFeatureLayer(Interface):

    geometry_type = Attribute(""" Тип геометрии слоя GEOM_TYPE """)
    fields = Attribute(""" Список полей """)
    
    feature_query = Attribute(""" Класс запроса объектов """)

    def field_by_keyname(self, keyname):
        """ Получить поле по ключу. Если поле не найдено, то должно
        вызываться исключение KeyError. """


class IFeatureQuery(Interface):

    def fields(self, *args):
        """ Установить список полей запроса. Если список полей
        не установлен, то запрос должен возращать все поля элемента. """


class IFeatureQueryFilterBy(IFeatureQuery):

    def filter_by(self, **kwargs):
        """ Установить отбор по значениям аттрибутов """


class IFeatureQueryOrderBy(IFeatureQuery):

    def order_by(self, *args):
        """ Установить порядок сортировки """