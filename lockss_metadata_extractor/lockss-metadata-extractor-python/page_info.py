# coding: utf-8

"""
    LOCKSS Metadata Extraction Service REST API

    API of the LOCKSS Metadata Extraction REST Service  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: lockss-support@lockss.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PageInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'total_count': 'int',
        'results_per_page': 'int',
        'current_page': 'int',
        'cur_link': 'str',
        'next_link': 'str'
    }

    attribute_map = {
        'total_count': 'totalCount',
        'results_per_page': 'resultsPerPage',
        'current_page': 'currentPage',
        'cur_link': 'curLink',
        'next_link': 'nextLink'
    }

    def __init__(self, total_count=None, results_per_page=None, current_page=None, cur_link=None, next_link=None):  # noqa: E501
        """PageInfo - a model defined in Swagger"""  # noqa: E501

        self._total_count = None
        self._results_per_page = None
        self._current_page = None
        self._cur_link = None
        self._next_link = None
        self.discriminator = None

        self.total_count = total_count
        self.results_per_page = results_per_page
        self.current_page = current_page
        self.cur_link = cur_link
        if next_link is not None:
            self.next_link = next_link

    @property
    def total_count(self):
        """Gets the total_count of this PageInfo.  # noqa: E501

        The total number of elements to be paginated  # noqa: E501

        :return: The total_count of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PageInfo.

        The total number of elements to be paginated  # noqa: E501

        :param total_count: The total_count of this PageInfo.  # noqa: E501
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

    @property
    def results_per_page(self):
        """Gets the results_per_page of this PageInfo.  # noqa: E501

        The number of results per page  # noqa: E501

        :return: The results_per_page of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._results_per_page

    @results_per_page.setter
    def results_per_page(self, results_per_page):
        """Sets the results_per_page of this PageInfo.

        The number of results per page  # noqa: E501

        :param results_per_page: The results_per_page of this PageInfo.  # noqa: E501
        :type: int
        """
        if results_per_page is None:
            raise ValueError("Invalid value for `results_per_page`, must not be `None`")  # noqa: E501

        self._results_per_page = results_per_page

    @property
    def current_page(self):
        """Gets the current_page of this PageInfo.  # noqa: E501

        The current page number  # noqa: E501

        :return: The current_page of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this PageInfo.

        The current page number  # noqa: E501

        :param current_page: The current_page of this PageInfo.  # noqa: E501
        :type: int
        """
        if current_page is None:
            raise ValueError("Invalid value for `current_page`, must not be `None`")  # noqa: E501

        self._current_page = current_page

    @property
    def cur_link(self):
        """Gets the cur_link of this PageInfo.  # noqa: E501

        The link to the current page  # noqa: E501

        :return: The cur_link of this PageInfo.  # noqa: E501
        :rtype: str
        """
        return self._cur_link

    @cur_link.setter
    def cur_link(self, cur_link):
        """Sets the cur_link of this PageInfo.

        The link to the current page  # noqa: E501

        :param cur_link: The cur_link of this PageInfo.  # noqa: E501
        :type: str
        """
        if cur_link is None:
            raise ValueError("Invalid value for `cur_link`, must not be `None`")  # noqa: E501

        self._cur_link = cur_link

    @property
    def next_link(self):
        """Gets the next_link of this PageInfo.  # noqa: E501

        The link to the next page  # noqa: E501

        :return: The next_link of this PageInfo.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this PageInfo.

        The link to the next page  # noqa: E501

        :param next_link: The next_link of this PageInfo.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PageInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
