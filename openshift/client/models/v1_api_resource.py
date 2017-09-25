# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1APIResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, categories=None, kind=None, name=None, namespaced=None, short_names=None, singular_name=None, verbs=None):
        """
        V1APIResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'categories': 'list[str]',
            'kind': 'str',
            'name': 'str',
            'namespaced': 'bool',
            'short_names': 'list[str]',
            'singular_name': 'str',
            'verbs': 'list[str]'
        }

        self.attribute_map = {
            'categories': 'categories',
            'kind': 'kind',
            'name': 'name',
            'namespaced': 'namespaced',
            'short_names': 'shortNames',
            'singular_name': 'singularName',
            'verbs': 'verbs'
        }

        self._categories = categories
        self._kind = kind
        self._name = name
        self._namespaced = namespaced
        self._short_names = short_names
        self._singular_name = singular_name
        self._verbs = verbs

    @property
    def categories(self):
        """
        Gets the categories of this V1APIResource.
        categories is a list of the grouped resources this resource belongs to (e.g. 'all')

        :return: The categories of this V1APIResource.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this V1APIResource.
        categories is a list of the grouped resources this resource belongs to (e.g. 'all')

        :param categories: The categories of this V1APIResource.
        :type: list[str]
        """

        self._categories = categories

    @property
    def kind(self):
        """
        Gets the kind of this V1APIResource.
        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')

        :return: The kind of this V1APIResource.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1APIResource.
        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')

        :param kind: The kind of this V1APIResource.
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1APIResource.
        name is the plural name of the resource.

        :return: The name of this V1APIResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1APIResource.
        name is the plural name of the resource.

        :param name: The name of this V1APIResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def namespaced(self):
        """
        Gets the namespaced of this V1APIResource.
        namespaced indicates if a resource is namespaced or not.

        :return: The namespaced of this V1APIResource.
        :rtype: bool
        """
        return self._namespaced

    @namespaced.setter
    def namespaced(self, namespaced):
        """
        Sets the namespaced of this V1APIResource.
        namespaced indicates if a resource is namespaced or not.

        :param namespaced: The namespaced of this V1APIResource.
        :type: bool
        """
        if namespaced is None:
            raise ValueError("Invalid value for `namespaced`, must not be `None`")

        self._namespaced = namespaced

    @property
    def short_names(self):
        """
        Gets the short_names of this V1APIResource.
        shortNames is a list of suggested short names of the resource.

        :return: The short_names of this V1APIResource.
        :rtype: list[str]
        """
        return self._short_names

    @short_names.setter
    def short_names(self, short_names):
        """
        Sets the short_names of this V1APIResource.
        shortNames is a list of suggested short names of the resource.

        :param short_names: The short_names of this V1APIResource.
        :type: list[str]
        """

        self._short_names = short_names

    @property
    def singular_name(self):
        """
        Gets the singular_name of this V1APIResource.
        singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.

        :return: The singular_name of this V1APIResource.
        :rtype: str
        """
        return self._singular_name

    @singular_name.setter
    def singular_name(self, singular_name):
        """
        Sets the singular_name of this V1APIResource.
        singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.

        :param singular_name: The singular_name of this V1APIResource.
        :type: str
        """
        if singular_name is None:
            raise ValueError("Invalid value for `singular_name`, must not be `None`")

        self._singular_name = singular_name

    @property
    def verbs(self):
        """
        Gets the verbs of this V1APIResource.
        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)

        :return: The verbs of this V1APIResource.
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """
        Sets the verbs of this V1APIResource.
        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)

        :param verbs: The verbs of this V1APIResource.
        :type: list[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")

        self._verbs = verbs

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1APIResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other