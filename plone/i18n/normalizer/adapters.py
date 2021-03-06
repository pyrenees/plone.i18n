from plone.i18n.normalizer.interfaces import IFileNameNormalizer
from plone.i18n.normalizer.interfaces import IURLNormalizer
from plone.i18n.normalizer.interfaces import IUserPreferredFileNameNormalizer
from plone.i18n.normalizer.interfaces import IUserPreferredURLNormalizer

from zope.component import queryUtility
from zope.interface import implementer
from zope.i18n.interfaces import IUserPreferredLanguages


@implementer(IUserPreferredFileNameNormalizer)
class UserPreferredFileNameNormalizer(object):
    """
    An adapter for the HTTPRequest to provide user preferred language
    dependent normalization.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IUserPreferredFileNameNormalizer, UserPreferredFileNameNormalizer)
      True
    """

    def __init__(self, context):
        self.context = context # the context must be the request

    def normalize(self, text):
        """Returns a normalized Unicode string."""
        locale = None
        langs = IUserPreferredLanguages(self.context).getPreferredLanguages()
        if langs:
            locale = langs[0]

        util = queryUtility(IFileNameNormalizer)
        return util.normalize(text, locale=locale)


@implementer(IUserPreferredURLNormalizer)
class UserPreferredURLNormalizer(object):
    """
    An adapter for the HTTPRequest to provide user preferred language
    dependent normalization.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IUserPreferredURLNormalizer, UserPreferredURLNormalizer)
      True
    """

    def __init__(self, context):
        self.context = context # the context must be the request

    def normalize(self, text):
        """Returns a normalized Unicode string."""
        locale = None
        langs = IUserPreferredLanguages(self.context).getPreferredLanguages()
        if langs:
            locale = langs[0]

        util = queryUtility(IURLNormalizer)
        return util.normalize(text, locale=locale)
