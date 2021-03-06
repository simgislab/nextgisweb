# -*- coding: utf-8 -*-
from zope.interface import Interface, Attribute

from ..resource import IResourceBase


class GEOM_TYPE(object):
    POINT = 'POINT'
    LINESTRING = 'LINESTRING'
    POLYGON = 'POLYGON'
    MULTIPOINT = 'MULTIPOINT'
    MULTILINESTRING = 'MULTILINESTRING'
    MULTIPOLYGON = 'MULTIPOLYGON'

    enum = (POINT, LINESTRING, POLYGON, MULTIPOINT,
            MULTILINESTRING, MULTIPOLYGON)


class FIELD_TYPE(object):
    INTEGER = 'INTEGER'
    BIGINT = 'BIGINT'
    REAL = 'REAL'
    STRING = 'STRING'
    DATE = 'DATE'
    TIME = 'TIME'
    DATETIME = 'DATETIME'

    enum = (INTEGER, BIGINT, REAL, STRING, DATE, TIME, DATETIME)


class IFeatureLayer(IResourceBase):

    geometry_type = Attribute(""" Layer geometry type GEOM_TYPE """)
    fields = Attribute(""" List of fields """)

    feature_query = Attribute(""" Feature query class """)

    def field_by_keyname(self, keyname):
        """ Get field by key. If field is not found, 
        KeyError exception should be raised. """


class IWritableFeatureLayer(IFeatureLayer):
    """ Feature layer that supports writing """

    def feature_create(self, feature):
        """ Create new feature with description from feature

        :param feature: feature description
        :type feature:  dict

        :return:        ID of new feature
        """

    def feature_delete(self, feature_id):
        """ Remove feature with id

        :param feature_id: feature id
        :type feature_id:  int or bigint
        """

    def feature_delete_all(self):
        """ Remove all features """

    def feature_put(self, feature):
        """ Save feature in a layer """


class IFeatureQuery(Interface):

    def fields(self, *args):
        """ Set a list of request fields. If list of fields not set
        return all fields. """

    def limit(self, limit, offset=0):
        """ Set request limit similarly to SQL
        LIMIT limit OFFSET offset """

    def geom(self):
        """ Include geometry in request result """

    def srs(self, srs):
        """ Include CRS if
        it was included in request """

    def box(self):
        """ Include extent in request result """


class IFeatureQueryFilter(IFeatureQuery):

    def filter(self, *args):
        """ Set query rules """


class IFeatureQueryFilterBy(IFeatureQuery):

    def filter_by(self, **kwargs):
        """ Set query by attributes """


class IFeatureQueryOrderBy(IFeatureQuery):

    def order_by(self, *args):
        """ Set sort order """


class IFeatureQueryLike(IFeatureQuery):

    def like(self, value):
        """ Set query by substring """


class IFeatureQueryIntersects(IFeatureQuery):

    def intersects(self, geom):
        """ Set query by spatial intersection """
