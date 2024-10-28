"""Mapping logic for `League` objects."""

from typing import Any


def map_league_properties(
    key: str, value: Any
) -> tuple[str, str | int | bool]:
    """Mapping rules for the individual properties of a
    :py:class:`~.model.League`.
    """

    if key in {
        'associationId',
        'currentRoundId',
        'displayKey',
        'displayKey2',
        'id',
        'imId',
        'priority',
        'ressortId',
        'ressortIdHome',
        'stateId',
        'sportId',
        'table',
        'trackRessortId',
    }:
        return key, int(value)
    if key in {
        'gamedayQuoteAd',
        'goalgetters',
        'hasTransfers',
        'history',
        'socialmedia',
        'tblcalc',
        'teamOrigin',
        'tickerQuoteAd',
    }:
        return key, bool(int(value))
    return key, value
