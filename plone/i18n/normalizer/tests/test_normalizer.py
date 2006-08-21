# -*- coding: UTF-8 -*-
"""
    Normalizer tests.
"""

import unittest

import plone.i18n.normalizer
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.i18n.normalizer.interfaces import IURLNormalizer

import zope.component
from zope.component import queryUtility
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocTestSuite

def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('configure.zcml', plone.i18n.normalizer)()

def testIDNormalizer():
    """
      >>> util = queryUtility(IIDNormalizer)
      >>> util
      <plone.i18n.normalizer.IDNormalizer object at ...>

      >>> util.normalize(u'simpleandsafe')
      'simpleandsafe'

      >>> util.normalize(u' Whitespace and capital Letters  ')
      'whitespace-and-capital-letters'

      >>> util.normalize(u">here's another!")
      'heres-another'
    """

def testURLNormalizer():
    """
      >>> util = queryUtility(IURLNormalizer)
      >>> util
      <plone.i18n.normalizer.URLNormalizer object at ...>
      
      >>> util.normalize(u'simpleandsafe')
      'simpleandsafe'

      >>> util.normalize(u' Whitespace and capital Letters  ')
      'Whitespace and capital Letters'

      >>> util.normalize(u">here's another!")
      'heres another'
    """

def testLocaleAwareURLNormalizer():
    """
      >>> util = queryUtility(IURLNormalizer)
      >>> util
      <plone.i18n.normalizer.URLNormalizer object at ...>

      >>> util.normalize(u'simpleandsafe', locale='de')
      'simpleandsafe'

      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de')
      'text with umlaeut'

    Make sure we get the de normalizer as there's no special one for de_DE
    registered.
       
      >>> util.normalize(unicode('text with umläut', 'utf-8'), locale='de_DE')
      'text with umlaeut'

      >>> util.normalize(u'simpleandsafe', locale='pt_BR')
      'simpleandsafe'

      >>> util.normalize(u'simpleandsafe', locale='sr@Latn')
      'simpleandsafe'
    """

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('plone.i18n.normalizer'),
        DocTestSuite('plone.i18n.normalizer.de'),
        DocTestSuite('plone.i18n.normalizer.el'),
        DocTestSuite('plone.i18n.normalizer.ru'),
        DocTestSuite('plone.i18n.normalizer.tr'),
        DocTestSuite(setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")