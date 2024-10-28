"""Upstream model for sports associations."""

from enum import IntEnum


class Association(IntEnum):
    """Integer that represents a sports association."""

    UNSPECIFIED = 0
    """This can mean that a league does not belong to a particular
    sports association, that an association has not been specified,
    or that the association is known but has no ID in the system.
    """

    BADEN_BFV = 1
    """Baden Football Association („Badischer Fußballverband“),
    a football association that covers the north-western part of
    the German state of Baden-Württemberg.
    """

    BAVARIAN_BFV = 2
    """Bavarian Football Association („Bayerischer Fußballverband“),
    a football association in the German state of Bavaria.
    """

    BERLIN_BFV = 3
    """Berlin Football Association („Berliner Fußballverband“), a
    football association in the German capital Berlin.
    """

    FLB = 4
    """Brandenburg Football Association („Fußball-Landesverband
    Brandenburg“), a football association in the German state of
    Brandenburg.
    """

    HAMBURG_HFV = 5
    """Hamburg Football Association („Hamburger Fußball-Verband“),
    a football association in the German state of Hamburg.
    """

    HESSIAN_HFV = 6
    """Hessian Football Association („Hessischer Fußball-Verband“),
    a football association in the German state of Hesse.
    """

    LFV = 7
    """Mecklenburg-Vorpommern Football Association
    („Landesfußballverband Mecklenburg-Vorpommern“), a football
    association in the German state of Mecklenburg-Vorpommern.
    """

    FVM = 8
    """Middle Rhine Football Association
    („Fußballverband Mittelrhein“), an association of football clubs
    in Germany’s mid-Rhine area.
    """

    FVN = 9
    """Lower Rhine Football Association
    („Fußballverband Niederrhein“), an association of football clubs
    in Germany’s Lower Rhine region.
    """

    NFV = 10
    """Lower Saxony Football Association („Niedersächsischer
    Fußball-Verband“), a football association in the German state of
    Lower Saxony.
    """

    FVR = 11
    """Rhineland Football Association
    („Fußballverband Rheinland“), an association of football clubs
    in the northern part of the German state Rhineland-Palatinate.
    """

    SAARLAND_SFV = 12
    """Saarland Football Association („Saarländischer
    Fußball-Verband“), a football association in the German state of
    Saarland.
    """

    SAXONIAN_SFV = 13
    """Saxony Football Association („Sächsischer Fußball-Verband“),
    a football association in the German state of Saxony.
    """

    FSA = 14
    """Saxony-Anhalt Football Association („Fußballverband
    Sachsen-Anhalt“), a football association in the German state of
    Saxony-Anhalt.
    """

    SHFV = 15
    """Schleswig-Holstein Football Association
    („Schleswig-Holsteinischer Fußball-Verband“), a football
    association in the German state of Schleswig-Holstein.
    """

    SBFV = 16
    """Südbaden Football Association („Südbadischer Fußballverband“),
    a football association covering the south-western part of the
    German state of Baden-Württemberg.
    """

    SWFV = 17
    """Southwest German Football Association („Südwestdeutscher
    Fußballverband“), a football association covering the southern
    part of the German state of Rheinland-Palatinate.
    """

    TFV = 18
    """Thuringian Football Association („Thüringer Fußball-Verband“),
    a football association in the German state of Thuringia.
    """

    FLVW = 19
    """Westphalia Football and Athletics Association („Fußball- und
    Leichtathletik-Verband Westfalen“), an association in the German
    Westphalia area.
    """

    WFV = 20
    """Württemberg Football Association (Württembergischer
    Fußballverband“), a football association that covers the
    north-eastern part of the German state of Baden-Württemberg.
    """

    BREMEN_BFV = 21
    """Bremen Football Association („Bremer Fußball-Verband“),
    a football association in the German state of Bremen.
    """

    DFB = 25
    """Germany’s federal football association,
    “Deutscher Fußball-Bund”.
    """
