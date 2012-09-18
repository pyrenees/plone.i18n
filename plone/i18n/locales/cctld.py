# This file contains a map from internet top level domains to the spoken
# language(s) in the country associated with the domain.

# Top level domain list taken from
# http://data.iana.org/TLD/tlds-alpha-by-domain.txt
# Descriptions for most TLDs a can be found at
# http://en.wikipedia.org/wiki/List_of_Internet_top-level_domains

from plone.i18n.locales.interfaces import ICcTLDInformation
from zope.interface import implements


class CcTLDInformation(object):
    """A list of country code top level domains their relevant languages.
    """

    implements(ICcTLDInformation)

    def getAvailableTLDs(self):
        """Return a sequence of country code top level domains.
        """
        return _tld_to_language.keys()

    def getTLDs(self):
        """Return a sequence of ccTLDs and their languages.
        """
        return _tld_to_language.copy()

    def getLanguagesForTLD(self, tld):
        """Return the relevant languages for a top level domain.
        """
        return _tld_to_language[tld]

ccTLDInformation = CcTLDInformation()

_tld_to_language = {
    u"ac"        : [],
    u"ad"        : [],
    u"ae"        : [],
    u"aero"      : [],
    u"af"        : [],
    u"ag"        : [],
    u"ai"        : [],
    u"al"        : [],
    u"am"        : [],
    u"an"        : [],
    u"ao"        : [],
    u"aq"        : [u"en"],
    u"ar"        : [u"pt"],
    u"arpa"      : [u"en"],
    u"as"        : [u"en"],
    u"at"        : [u"de"],
    u"au"        : [u"en"],
    u"aw"        : [],
    u"ax"        : [],
    u"az"        : [],
    u"ba"        : [u"bs"],
    u"bb"        : [],
    u"bd"        : [],
    u"be"        : [u"nl", u"fr"],
    u"bf"        : [],
    u"bg"        : [],
    u"bh"        : [],
    u"bi"        : [],
    u"biz"       : [],
    u"bj"        : [],
    u"bm"        : [],
    u"bn"        : [],
    u"bo"        : [],
    u"br"        : [u"pt"],
    u"bs"        : [],
    u"bt"        : [],
    u"bv"        : [],
    u"bw"        : [],
    u"by"        : [],
    u"bz"        : [],
    u"ca"        : [u"en"],
    u"cat"       : [u"ca"],
    u"cc"        : [],
    u"cd"        : [],
    u"cf"        : [],
    u"cg"        : [],
    u"ch"        : [u"de"],
    u"ci"        : [],
    u"ck"        : [],
    u"cl"        : [],
    u"cm"        : [],
    u"cn"        : [u"zh"],
    u"co"        : [],
    u"com"       : [],
    u"coop"      : [],
    u"cr"        : [u"es"],
    u"cu"        : [],
    u"cv"        : [],
    u"cx"        : [],
    u"cy"        : [],
    u"cz"        : [],
    u"de"        : [u"de"],
    u"dj"        : [],
    u"dk"        : [u"da"],
    u"dm"        : [],
    u"do"        : [],
    u"dz"        : [],
    u"ec"        : [],
    u"edu"       : [u"en"],
    u"ee"        : [u"et"],
    u"eg"        : [],
    u"er"        : [],
    u"es"        : [u"es"],
    u"et"        : [],
    u"eu"        : [],
    u"fi"        : [u"fi"],
    u"fj"        : [],
    u"fk"        : [],
    u"fm"        : [],
    u"fo"        : [u"fo"],
    u"fr"        : [u"fr"],
    u"ga"        : [],
    u"gb"        : [u"en"],
    u"gd"        : [],
    u"ge"        : [u"ka"],
    u"gf"        : [],
    u"gg"        : [],
    u"gh"        : [],
    u"gi"        : [],
    u"gl"        : [],
    u"gm"        : [],
    u"gn"        : [],
    u"gov"       : [u"en"],
    u"gp"        : [],
    u"gq"        : [],
    u"gr"        : [u"gr"],
    u"gs"        : [],
    u"gt"        : [],
    u"gu"        : [],
    u"gw"        : [],
    u"gy"        : [],
    u"hk"        : [],
    u"hm"        : [],
    u"hn"        : [],
    u"hr"        : [u"hr"],
    u"ht"        : [],
    u"hu"        : [u"hu"],
    u"id"        : [],
    u"ie"        : [],
    u"il"        : [u"he"],
    u"im"        : [u"en"],
    u"in"        : [u"hi"],
    u"info"      : [],
    u"int"       : [],
    u"io"        : [u"en"],
    u"iq"        : [u"ar"],
    u"ir"        : [u"ar"],
    u"is"        : [u"is"],
    u"it"        : [u"it"],
    u"je"        : [u"en"],
    u"jm"        : [],
    u"jo"        : [],
    u"jobs"      : [],
    u"jp"        : [u"ja"],
    u"ke"        : [],
    u"kg"        : [],
    u"kh"        : [],
    u"ki"        : [],
    u"km"        : [],
    u"kn"        : [],
    u"kr"        : [u"ko"],
    u"kw"        : [],
    u"ky"        : [],
    u"kz"        : [u"kk"],
    u"la"        : [],
    u"lb"        : [],
    u"lc"        : [],
    u"li"        : [],
    u"lk"        : [],
    u"lr"        : [],
    u"ls"        : [],
    u"lt"        : [],
    u"lu"        : [u"lb"],
    u"lv"        : [u"lv"],
    u"ly"        : [],
    u"ma"        : [],
    u"mc"        : [],
    u"md"        : [u"mo"],
    u"me"        : [],
    u"mg"        : [u"mg"],
    u"mh"        : [],
    u"mil"       : [u"en"],
    u"mk"        : [],
    u"ml"        : [],
    u"mm"        : [],
    u"mn"        : [u"mn"],
    u"mo"        : [],
    u"mobi"      : [],
    u"mp"        : [],
    u"mq"        : [],
    u"mr"        : [],
    u"ms"        : [],
    u"mt"        : [u"mt"],
    u"mu"        : [],
    u"museum"    : [],
    u"mv"        : [],
    u"mw"        : [],
    u"mx"        : [],
    u"my"        : [],
    u"mz"        : [],
    u"na"        : [],
    u"name"      : [],
    u"nc"        : [],
    u"ne"        : [],
    u"net"       : [],
    u"nf"        : [],
    u"ng"        : [],
    u"ni"        : [],
    u"nl"        : [u"nl"],
    u"no"        : [u"no"],
    u"np"        : [],
    u"nr"        : [],
    u"nu"        : [],
    u"nz"        : [],
    u"om"        : [u"en"],
    u"org"       : [],
    u"pa"        : [],
    u"pe"        : [],
    u"pf"        : [],
    u"pg"        : [],
    u"ph"        : [],
    u"pk"        : [],
    u"pl"        : [u"pl"],
    u"pm"        : [],
    u"pn"        : [],
    u"pr"        : [u"es"],
    u"pro"       : [],
    u"ps"        : [u"ar"],
    u"pt"        : [u"pt"],
    u"pw"        : [],
    u"py"        : [],
    u"qa"        : [],
    u"re"        : [],
    u"ro"        : [u"ro"],
    u"rs"        : [],
    u"ru"        : [u"ru"],
    u"rw"        : [],
    u"sa"        : [u"ar"],
    u"sb"        : [],
    u"sc"        : [],
    u"sd"        : [u"su"],
    u"se"        : [u"sv"],
    u"sg"        : [u"si"],
    u"sh"        : [],
    u"si"        : [u"sl"],
    u"sj"        : [],
    u"sk"        : [u"sk"],
    u"sl"        : [],
    u"sm"        : [],
    u"sn"        : [u"fr"],
    u"so"        : [u"so"],
    u"sr"        : [u"nl"],
    u"st"        : [],
    u"su"        : [u"ru"],
    u"sv"        : [],
    u"sy"        : [],
    u"sz"        : [],
    u"tc"        : [u"tr"],
    u"td"        : [],
    u"tel"       : [],
    u"tf"        : [],
    u"tg"        : [u"to"],
    u"th"        : [u"th"],
    u"tj"        : [u"fa"],
    u"tk"        : [u"tk"],
    u"tl"        : [u"pt"],
    u"tm"        : [u"tk"],
    u"tn"        : [],
    u"to"        : [],
    u"tp"        : [u"pt"],
    u"tr"        : [],
    u"travel"    : [],
    u"tt"        : [],
    u"tv"        : [],
    u"tw"        : [u"zh"],
    u"tz"        : [],
    u"ua"        : [],
    u"ug"        : [],
    u"uk"        : [u"en"],
    u"um"        : [u"en"],
    u"us"        : [u"en"],
    u"uy"        : [],
    u"uz"        : [],
    u"va"        : [u"it"],
    u"vc"        : [],
    u"ve"        : [],
    u"vg"        : [],
    u"vi"        : [u"en"],
    u"vn"        : [u"vi"],
    u"vu"        : [],
    u"wf"        : [],
    u"ws"        : [u"sm"],
    u"ye"        : [],
    u"yt"        : [],
    u"yu"        : [u"sh"],
    u"za"        : [u"af"],
    u"zm"        : [],
    u"zw"        : [],
}
