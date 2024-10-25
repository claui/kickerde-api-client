"""Mapping and transformation features."""

from collections.abc import Callable, Mapping, MutableSequence, Sequence
from typing import Any


type Submapper = Callable[[str, Any], tuple[str, Any] | None]
"""Function that accepts a key-value pair and returns another
(transformed) key-value pair. Used for on-the-fly post-processing
while mapping an object hierarchy from a source to a target format.

A `Submapper` is conceptually similar to, but not the same thing as,
a callback function used in the `postprocessor` kwarg of xmltodict’s
`parse` method. A submapper is less flexible than a `postprocessor`
kwarg because the latter accepts a complex path that points to
an element location in the object hierarchy. On the other hand, a
submapper assumes a fixed (implied) location, so it only accepts
`key` and `value` as arguments but not the element’s location in
the hierarchy.

(The name `Submapper` was chosen to emphasize that any given
function of this type is usually focused on mapping a specific
sub-element in an object hierarchy.)

A submapper may return `None` instead of a key-value pair. If a
caller receives `None` as a return value, it is supposed to discard
the element, i.e. not include it in the target hierarchy.
"""


type SubmapperKey = str | tuple[str, ...]
"""Immutable key that describes a location in an object hierarchy.
Used internally to look up functions of the `Submapper` type by
location.

If the key is a **string**, then the key matches a location if and
only if the element name is equal to the key.

Example: The key `"baz"` matches elements located at `foo.bar.baz`
and `qux.baz`. However, it does not match `qux.baz.quux`.

If the key is a **tuple of strings**, then it matches a location if
and only if the tuple is equal to the chain of element names.

Example: The key `("foo", "bar", "baz")` matches elements located
at `foo.bar.baz`. It does not match any other elements.
"""


class XmlMappingHelper:  # pylint: disable=too-few-public-methods
    """Mapping helper that can be plugged into `xmltodict`. Its purpose
    is to aggregate and dispatch `Submapper` functions for various
    elements in an XML document while it is parsed.

    See `Submapper` for details about submappers.

    The `map` method of this class is designed to be used as a value
    for the `postprocessor` kwarg of xmltodict’s `parse` method.
    """

    filter_rules: MutableSequence[Callable[..., bool]]

    def __init__(
        self,
        submappers: Mapping[SubmapperKey, Submapper],
    ) -> None:
        self.filter_rules = [
            lambda key, _: key.startswith('xmlns:'),
            lambda key, _: key in {'banner', 'taboola'},
        ]
        self.submappers = submappers

    def map(
        self,
        path: Sequence[tuple[str, ...]],
        original_key: str,
        value: Any,
    ) -> tuple[str, Any] | None:
        """Transforms an XML key-value pair into a Pythonic type that
        matches the domain type as closely as possible.
        """
        element_names = [entry[0] for entry in path]
        key = original_key.lstrip('@')

        if any(rule(key, value) for rule in self.filter_rules):
            return None

        def match_leaf(element_name: str) -> bool:
            return element_name == element_names[-1]

        for candidate, submapper in self.submappers.items():
            match candidate:
                case str(element_name) if match_leaf(element_name):
                    return submapper(key, value)
                case [*names] if names == element_names:
                    return submapper(key, value)
                case _:
                    pass  # Candidate does not match, keep searching

        return key, value


def map_default(key: str, value: Any) -> tuple[str, str | int]:
    """Mapping helper that maps the `id` property to an integer and
    keeps everything else as is.
    """
    if key in {
        'id',
    }:
        return key, int(value)
    return key, value
