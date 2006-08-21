import re

from plone.i18n.normalizer.base import baseNormalize
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.i18n.normalizer.interfaces import IURLNormalizer

from zope.component import queryUtility
from zope.interface import implements

# Define and compile static regexes
FILENAME_REGEX = re.compile(r"^(.+)\.(\w{,4})$")
IGNORE_REGEX = re.compile(r"[']")
NON_WORD_REGEX = re.compile(r"[\W\-]+")
DANGEROUS_CHARS_REGEX = re.compile(r"[?&/:\\#<>!$%^*()]+")
EXTRA_DASHES_REGEX = re.compile(r"(^\-+)|(\-+$)")

class IDNormalizer(object):
    """
    This normalizer can normalize any unicode string and returns a
    version that only contains of ASCII characters allowed in a typical
    scripting or programming language id, such as CSS class names or Python
    variable names for example.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IIDNormalizer, IDNormalizer)
      True
    """
    implements(IIDNormalizer)

    def normalize(self, text, locale=None):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt_BR', 'sr@Latn' or 'de'
        """
        if locale is not None:
            # Try to get a normalizer for the locale
            util = queryUtility(IDNormalizer, name=locale)
            parts = locale.split('_')
            if util is None and len(parts) > 1:
                # Try to get a normalizer for the base language if we asked
                # for one for a language/country combination and found none
                util = queryUtility(IDNormalizer, name=parts[0])
            if util is not None:
                return util.normalize(text, locale=locale)

        text = baseNormalize(text)

        # lowercase text
        base = text.lower()
        ext  = ''

        # replace whitespace and punctuation, but preserve filename extensions
        m = FILENAME_REGEX.match(text)
        if m is not None:
            base = m.groups()[0]
            ext  = m.groups()[1]

        base = IGNORE_REGEX.sub('', base)
        base = NON_WORD_REGEX.sub('-', base)
        base = EXTRA_DASHES_REGEX.sub('', base)

        if ext != '':
            base = base + '.' + ext

        return base


class URLNormalizer(object):
    """
    This normalizer can normalize any unicode string and returns a URL-safe
    version that only contains of ASCII characters allowed in a URL.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IURLNormalizer, URLNormalizer)
      True
    """
    implements(IURLNormalizer)

    def normalize(self, text, locale=None):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt_BR', 'sr@Latn' or 'de'
        """
        if locale is not None:
            # Try to get a normalizer for the locale
            util = queryUtility(IURLNormalizer, name=locale)
            parts = locale.split('_')
            if util is None and len(parts) > 1:
                # Try to get a normalizer for the base language if we asked
                # for one for a language/country combination and found none
                util = queryUtility(IURLNormalizer, name=parts[0])
            if util is not None:
                return util.normalize(text, locale=locale)

        # Replace whitespace and punctuation, but preserve filename extensions
        base = baseNormalize(text)
        ext  = ''

        m = FILENAME_REGEX.match(text)
        if m is not None:
            base = m.groups()[0]
            ext  = m.groups()[1]

        base = IGNORE_REGEX.sub('', base)
        base = DANGEROUS_CHARS_REGEX.sub('-', base)
        base = EXTRA_DASHES_REGEX.sub('', base)

        if ext != '':
            base = base + '.' + ext

        return base

idnormalizer = IDNormalizer()
urlnormalizer = URLNormalizer()