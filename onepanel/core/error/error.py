
class OnepanelException(Exception):
    """Base-class for all exceptions raised by the OnepanelSubmitter"""


class MissingUsernameException(OnepanelException):
    """
    Happens when there is no provided username
    """

class MissingTokenException(OnepanelException):
    """
    Happens when there is no provided token and one can't be found on the system.
    """


class MissingHostException(OnepanelException):
    """
    Happens when there is no provided host and can't be found on the system
    """


class InvalidCredentialsException(OnepanelException):
    """
    Happens when the credentials to get the authentication token are incorrect.
    """


class LongWorkflowNameException(OnepanelException):
    """
    Happens when the workflow name is too long - which is >= 20 characters.
    """