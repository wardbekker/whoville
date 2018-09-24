# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ImageSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image_catalog': 'str',
        'image_id': 'str',
        'os': 'str'
    }

    attribute_map = {
        'image_catalog': 'imageCatalog',
        'image_id': 'imageId',
        'os': 'os'
    }

    def __init__(self, image_catalog=None, image_id=None, os=None):
        """
        ImageSettings - a model defined in Swagger
        """

        self._image_catalog = None
        self._image_id = None
        self._os = None

        if image_catalog is not None:
          self.image_catalog = image_catalog
        if image_id is not None:
          self.image_id = image_id
        if os is not None:
          self.os = os

    @property
    def image_catalog(self):
        """
        Gets the image_catalog of this ImageSettings.
        custom image catalog URL

        :return: The image_catalog of this ImageSettings.
        :rtype: str
        """
        return self._image_catalog

    @image_catalog.setter
    def image_catalog(self, image_catalog):
        """
        Sets the image_catalog of this ImageSettings.
        custom image catalog URL

        :param image_catalog: The image_catalog of this ImageSettings.
        :type: str
        """

        self._image_catalog = image_catalog

    @property
    def image_id(self):
        """
        Gets the image_id of this ImageSettings.
        virtual machine image id from ImageCatalog, machines of the cluster will be started from this image

        :return: The image_id of this ImageSettings.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this ImageSettings.
        virtual machine image id from ImageCatalog, machines of the cluster will be started from this image

        :param image_id: The image_id of this ImageSettings.
        :type: str
        """

        self._image_id = image_id

    @property
    def os(self):
        """
        Gets the os of this ImageSettings.
        os type of the image, this property is only considered when no specific image id is provided

        :return: The os of this ImageSettings.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this ImageSettings.
        os type of the image, this property is only considered when no specific image id is provided

        :param os: The os of this ImageSettings.
        :type: str
        """

        self._os = os

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
        if not isinstance(other, ImageSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other