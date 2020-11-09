# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class WorkspaceStatisticReport(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'total': 'int',
        'last_created': 'str',
        'launching': 'int',
        'running': 'int',
        'updating': 'int',
        'pausing': 'int',
        'paused': 'int',
        'terminating': 'int',
        'terminated': 'int',
        'failed_to_pause': 'int',
        'failed_to_resume': 'int',
        'failed_to_terminate': 'int',
        'failed_to_launch': 'int',
        'failed_to_update': 'int',
        'failed': 'int'
    }

    attribute_map = {
        'total': 'total',
        'last_created': 'lastCreated',
        'launching': 'launching',
        'running': 'running',
        'updating': 'updating',
        'pausing': 'pausing',
        'paused': 'paused',
        'terminating': 'terminating',
        'terminated': 'terminated',
        'failed_to_pause': 'failedToPause',
        'failed_to_resume': 'failedToResume',
        'failed_to_terminate': 'failedToTerminate',
        'failed_to_launch': 'failedToLaunch',
        'failed_to_update': 'failedToUpdate',
        'failed': 'failed'
    }

    def __init__(self, total=None, last_created=None, launching=None, running=None, updating=None, pausing=None, paused=None, terminating=None, terminated=None, failed_to_pause=None, failed_to_resume=None, failed_to_terminate=None, failed_to_launch=None, failed_to_update=None, failed=None, local_vars_configuration=None):  # noqa: E501
        """WorkspaceStatisticReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._last_created = None
        self._launching = None
        self._running = None
        self._updating = None
        self._pausing = None
        self._paused = None
        self._terminating = None
        self._terminated = None
        self._failed_to_pause = None
        self._failed_to_resume = None
        self._failed_to_terminate = None
        self._failed_to_launch = None
        self._failed_to_update = None
        self._failed = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if last_created is not None:
            self.last_created = last_created
        if launching is not None:
            self.launching = launching
        if running is not None:
            self.running = running
        if updating is not None:
            self.updating = updating
        if pausing is not None:
            self.pausing = pausing
        if paused is not None:
            self.paused = paused
        if terminating is not None:
            self.terminating = terminating
        if terminated is not None:
            self.terminated = terminated
        if failed_to_pause is not None:
            self.failed_to_pause = failed_to_pause
        if failed_to_resume is not None:
            self.failed_to_resume = failed_to_resume
        if failed_to_terminate is not None:
            self.failed_to_terminate = failed_to_terminate
        if failed_to_launch is not None:
            self.failed_to_launch = failed_to_launch
        if failed_to_update is not None:
            self.failed_to_update = failed_to_update
        if failed is not None:
            self.failed = failed

    @property
    def total(self):
        """Gets the total of this WorkspaceStatisticReport.  # noqa: E501


        :return: The total of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this WorkspaceStatisticReport.


        :param total: The total of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def last_created(self):
        """Gets the last_created of this WorkspaceStatisticReport.  # noqa: E501


        :return: The last_created of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: str
        """
        return self._last_created

    @last_created.setter
    def last_created(self, last_created):
        """Sets the last_created of this WorkspaceStatisticReport.


        :param last_created: The last_created of this WorkspaceStatisticReport.  # noqa: E501
        :type: str
        """

        self._last_created = last_created

    @property
    def launching(self):
        """Gets the launching of this WorkspaceStatisticReport.  # noqa: E501


        :return: The launching of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._launching

    @launching.setter
    def launching(self, launching):
        """Sets the launching of this WorkspaceStatisticReport.


        :param launching: The launching of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._launching = launching

    @property
    def running(self):
        """Gets the running of this WorkspaceStatisticReport.  # noqa: E501


        :return: The running of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this WorkspaceStatisticReport.


        :param running: The running of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._running = running

    @property
    def updating(self):
        """Gets the updating of this WorkspaceStatisticReport.  # noqa: E501


        :return: The updating of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._updating

    @updating.setter
    def updating(self, updating):
        """Sets the updating of this WorkspaceStatisticReport.


        :param updating: The updating of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._updating = updating

    @property
    def pausing(self):
        """Gets the pausing of this WorkspaceStatisticReport.  # noqa: E501


        :return: The pausing of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._pausing

    @pausing.setter
    def pausing(self, pausing):
        """Sets the pausing of this WorkspaceStatisticReport.


        :param pausing: The pausing of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._pausing = pausing

    @property
    def paused(self):
        """Gets the paused of this WorkspaceStatisticReport.  # noqa: E501


        :return: The paused of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this WorkspaceStatisticReport.


        :param paused: The paused of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._paused = paused

    @property
    def terminating(self):
        """Gets the terminating of this WorkspaceStatisticReport.  # noqa: E501


        :return: The terminating of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._terminating

    @terminating.setter
    def terminating(self, terminating):
        """Sets the terminating of this WorkspaceStatisticReport.


        :param terminating: The terminating of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._terminating = terminating

    @property
    def terminated(self):
        """Gets the terminated of this WorkspaceStatisticReport.  # noqa: E501


        :return: The terminated of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this WorkspaceStatisticReport.


        :param terminated: The terminated of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._terminated = terminated

    @property
    def failed_to_pause(self):
        """Gets the failed_to_pause of this WorkspaceStatisticReport.  # noqa: E501


        :return: The failed_to_pause of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._failed_to_pause

    @failed_to_pause.setter
    def failed_to_pause(self, failed_to_pause):
        """Sets the failed_to_pause of this WorkspaceStatisticReport.


        :param failed_to_pause: The failed_to_pause of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._failed_to_pause = failed_to_pause

    @property
    def failed_to_resume(self):
        """Gets the failed_to_resume of this WorkspaceStatisticReport.  # noqa: E501


        :return: The failed_to_resume of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._failed_to_resume

    @failed_to_resume.setter
    def failed_to_resume(self, failed_to_resume):
        """Sets the failed_to_resume of this WorkspaceStatisticReport.


        :param failed_to_resume: The failed_to_resume of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._failed_to_resume = failed_to_resume

    @property
    def failed_to_terminate(self):
        """Gets the failed_to_terminate of this WorkspaceStatisticReport.  # noqa: E501


        :return: The failed_to_terminate of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._failed_to_terminate

    @failed_to_terminate.setter
    def failed_to_terminate(self, failed_to_terminate):
        """Sets the failed_to_terminate of this WorkspaceStatisticReport.


        :param failed_to_terminate: The failed_to_terminate of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._failed_to_terminate = failed_to_terminate

    @property
    def failed_to_launch(self):
        """Gets the failed_to_launch of this WorkspaceStatisticReport.  # noqa: E501


        :return: The failed_to_launch of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._failed_to_launch

    @failed_to_launch.setter
    def failed_to_launch(self, failed_to_launch):
        """Sets the failed_to_launch of this WorkspaceStatisticReport.


        :param failed_to_launch: The failed_to_launch of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._failed_to_launch = failed_to_launch

    @property
    def failed_to_update(self):
        """Gets the failed_to_update of this WorkspaceStatisticReport.  # noqa: E501


        :return: The failed_to_update of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._failed_to_update

    @failed_to_update.setter
    def failed_to_update(self, failed_to_update):
        """Sets the failed_to_update of this WorkspaceStatisticReport.


        :param failed_to_update: The failed_to_update of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._failed_to_update = failed_to_update

    @property
    def failed(self):
        """Gets the failed of this WorkspaceStatisticReport.  # noqa: E501


        :return: The failed of this WorkspaceStatisticReport.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this WorkspaceStatisticReport.


        :param failed: The failed of this WorkspaceStatisticReport.  # noqa: E501
        :type: int
        """

        self._failed = failed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkspaceStatisticReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkspaceStatisticReport):
            return True

        return self.to_dict() != other.to_dict()
