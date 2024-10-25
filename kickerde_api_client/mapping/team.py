"""Mapping logic for `Team` (or team-ish) objects."""

from typing import Any


def map_team_properties(key: str, value: Any) -> tuple[str, str | int]:
    """Mapping rules for basic properties of a team."""

    if key in {
        'id',
        'defaultLeagueId',
    }:
        return key, int(value)
    return key, value
