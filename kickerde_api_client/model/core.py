"""Miscellaneous root entities of the upstream model."""

from enum import IntEnum
from typing import Any, TypedDict


type CountryId = str
"""Upstream ID for a country that hosts a league or tournament.
Alternatively, a reserved artificial ID for tournaments hosted by
supranational bodies.
"""

type MediaObject = Any
"""Abstract supertype for a document, slideshow, or video."""


type ObjectId = int
"""Upstream ID for a document, slideshow, or video."""


class RessortId(IntEnum):
    """Upstream ID for a (possibly historical) news section."""

    BUNDESLIGA = 3100
    """German Bundesliga"""

    BUNDESLIGA_2 = 4100
    """German 2. Bundesliga"""

    REGIONALLIGA = 5100
    """Regionalliga"""

    DFB_POKAL = 6100
    """DFB-Pokal"""

    LANDESPOKAL = 6500
    """Football cup competitions hosted by football associations
    on German state level
    """

    GERMAN_NATIONAL_TEAM_UNDER_21 = 7011
    """The German U-21 national team"""

    GERMAN_NATIONAL_TEAM = 7100
    """The German national team"""

    NON_DOMESTIC_TIER_1 = 8100
    """Association football outside Germany, tier 1."""

    NON_DOMESTIC_TIER_2 = 8600
    """Association football outside Germany, tier 2."""

    NON_DOMESTIC_TIER_3 = 8605
    """Association football outside Germany, tier 3."""

    UEFA_CHAMPIONS_LEAGUE = 9100
    """UEFA Champions League"""

    EUROPA_LEAGUE = 11100
    """UEFA Europa League"""

    FIFA_WORLD_CUP = 12100
    """FIFA World Cup"""

    UEFA_CONFERENCE_LEAGUE = 13100
    """UEFA Europa Conference League"""

    FIFA_CONFEDERATIONS_CUP = 18100
    """The historical FIFA Confederations Cup.
    Currently tracked under :py:obj:`.TrackRessortId.WORLD_CUPS`.
    """

    WOMEN = 23100
    """Women"""

    FIFA_WORLD_CUP_WOMEN = 23155
    """FIFA Women’s World Cup.
    Currently tracked under :py:obj:`.TrackRessortId.WOMEN`.
    """

    WOMEN_UNKNOWN_23230 = 23230
    """Ressort ID with unknown semantics."""

    GERMAN_NATIONAL_TEAM_WOMEN = 23300
    """German women’s national team.
    Currently tracked under :py:obj:`.TrackRessortId.WOMEN`.
    """

    YOUTH = 24100
    """Youth"""

    DFB_LIGA_3 = 26100
    """German 3. Liga"""

    UEFA_NL = 28050
    """UEFA Nations League"""

    UEFA_EURO = 28100
    """UEFA European Championship"""

    ICE_HOCKEY_TIER_1 = 31100
    """Ice hockey, tier 1"""

    ICE_HOCKEY_TIER_2 = 31500
    """Ice hockey, tier 2"""

    BASKETBALL_TIER_1 = 36100
    """Basketball, tier 1"""

    BASKETBALL_TIER_2 = 36500
    """Basketball, tier 2"""

    HANDBALL = 37100
    """Handball"""

    AMERICAN_FOOTBALL = 38251
    """American Football"""

    OLYMPICS = 508100
    """Olympics"""


class RessortIdHome(IntEnum):
    """Upstream ID for a news subsection with a dedicated home page.

    Typically used for German Regionalliga associations.
    """

    REGIONALLIGA_NORD = 5410
    """Regionalliga Nord"""

    REGIONALLIGA_NORDOST = 5420
    """Regionalliga Nordost"""

    REGIONALLIGA_WEST = 5430
    """Regionalliga West"""

    REGIONALLIGA_SUEDWEST = 5440
    """Regionalliga Südwest"""

    REGIONALLIGA_BAYERN = 5450
    """Regionalliga Bayern"""


class TrackRessortId(IntEnum):
    """Upstream ID for a set of news sections. Each such set contains
    at least one contemporary news section, and optionally one or more
    additional news sections, which may be historical or on hiatus or
    have been subsumed for other reasons.

    For example, :py:obj:`.TrackRessortId.FIFA_WORLD_CUP` tracks both
    the contemporary :py:obj:`.RessortId.FIFA_WORLD_CUP` section and
    the historical :py:obj:`.RessortId.FIFA_CONFEDERATIONS_CUP` section.
    """

    HOME = 2000
    """Home

    Tracks :py:obj:`.RessortId.FRIENDLIES`.
    """

    BUNDESLIGA = 3000
    """German Bundesliga"""

    BUNDESLIGA_2 = 4000
    """German 2. Bundesliga"""

    REGIONALLIGA = 5000
    """Regionalliga"""

    DFB_POKAL = 6000
    """DFB-Pokal

    Tracks both :py:obj:`.RessortId.DFB_POKAL` and
    :py:obj:`.RessortId.LANDESPOKAL` sections.
    """

    GERMAN_NATIONAL_TEAM = 7000
    """The German national team"""

    UNDER_21 = 7010
    """Under 21"""

    NON_DOMESTIC = 8000
    """Association football outside Germany.

    Tracks the :py:obj:`.RessortId.NON_DOMESTIC_TIER_1`,
    :py:obj:`.RessortId.NON_DOMESTIC_TIER_2`, and
    :py:obj:`.RessortId.NON_DOMESTIC_TIER_3` sections.
    """

    UEFA_CHAMPIONS_LEAGUE = 9000
    """UEFA Champions League"""

    EUROPA_LEAGUE = 11000
    """UEFA Europa League"""

    FIFA_WORLD_CUP = 12000
    """FIFA World Cup

    Tracks both :py:obj:`.RessortId.FIFA_WORLD_CUP` and
    :py:obj:`.RessortId.FIFA_CONFEDERATIONS_CUP` sections.
    """

    UEFA_CONFERENCE_LEAGUE = 13000
    """UEFA Europa Conference League"""

    WOMEN = 23000
    """Women"""

    YOUTH = 24000
    """Youth"""

    DFB_LIGA_3 = 26000
    """German 3. Liga"""

    UEFA_EURO = 28000
    """UEFA European Championship"""

    UEFA_NL = 28050
    """UEFA Nations League"""

    ICE_HOCKEY = 31000
    """Ice hockey

    Tracks both :py:obj:`.RessortId.ICE_HOCKEY_TIER_1` and
    :py:obj:`.RessortId.ICE_HOCKEY_TIER_2` sections.
    """

    BASKETBALL = 36000
    """Basketball

    Tracks both :py:obj:`.RessortId.BASKETBALL_TIER_1` and
    :py:obj:`.RessortId.BASKETBALL_TIER_2` sections.
    """

    HANDBALL = 37000
    """Handball"""

    AMERICAN_FOOTBALL = 38250
    """American Football"""

    OLYMPICS = 508024
    """Olympics"""


class SportId(IntEnum):
    """Upstream ID for a type of sport."""

    ASSOCIATION_FOOTBALL = 1
    """Association football"""

    HANDBALL = 2
    """Handball"""

    ICE_HOCKEY = 3
    """Ice hockey"""

    BASKETBALL = 4
    """Basketball"""

    MOTORSPORTS = 5
    """Motorsports"""

    AMERICAN_FOOTBALL = 6
    """American football"""

    CYCLING = 7
    """Cycle sport"""

    TENNIS = 8
    """Tennis"""

    WINTER_SPORTS = 15
    """Winter sports"""

    ESPORTS = 32
    """Electronic sports"""


type StadiumId = int
"""Upstream ID for a sports venue."""


class StateId(IntEnum):
    """Upstream ID for a German state (Bundesland)."""

    BADEN_WUERTTEMBERG = 1
    """The German state of Baden-Württemberg"""

    BAVARIA = 2
    """The German Free State of Bavaria"""

    BERLIN = 3
    """The German capital Berlin"""

    BRANDENBURG = 4
    """The German state of Brandenburg"""

    BREMEN = 5
    """The German Free Hanseatic City of Bremen"""

    HAMBURG = 6
    """The German Free and Hanseatic City of Hamburg"""

    HESSE = 7
    """The German state of Hesse"""

    MECKLENBURG_VORPOMMERN = 8
    """The German state of Mecklenburg-Vorpommern"""

    LOWER_SAXONY = 9
    """The German state of Lower Saxony"""

    NORTH_RHINE_WESTPHALIA = 10
    """The German state of North Rhine-Westphalia"""

    RHINELAND_PALATINATE = 11
    """The German state of Rhineland-Palatinate"""

    SAARLAND = 12
    """The German state of Saarland"""

    SAXONY = 13
    """The German Free State of Saxony"""

    SAXONY_ANHALT = 14
    """The German state of Saxony-Anhalt"""

    SCHLESWIG_HOLSTEIN = 15
    """The German state of Schleswig-Holstein"""

    THURINGIA = 16
    """The German Free State of Thuringia"""


class Country(TypedDict):
    """Upstream model for a country."""

    id: CountryId
    shortName: str
    longName: str
    isoName: str
    iconSmall: str


class Stadium(TypedDict):
    """Upstream model for a sports venue."""

    id: StadiumId
    name: str
    city: str
