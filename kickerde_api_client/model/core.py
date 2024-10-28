"""Miscellaneous root entities of the upstream model."""

from typing import Any, TypedDict


type CountryId = str

# Used as a reference in both directions, so this can’t be in the
# `league` module.
type LeagueId = int

type ObjectId = int
type RessortId = int
type SportId = int
type StadiumId = int
type StateId = int


class Country(TypedDict):
    """Upstream model for a country."""

    id: CountryId
    shortName: str
    longName: str
    isoName: str
    iconSmall: str


type MediaObject = Any
"""Upstream abstraction for a document, slideshow, or video."""


class Stadium(TypedDict):
    """Upstream model for a sports venue."""

    id: StadiumId
    name: str
    city: str
