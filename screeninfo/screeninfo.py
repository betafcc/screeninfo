import typing as T

from screeninfo import enumerators
from screeninfo.common import Enumerator, Monitor, ScreenInfoError

ENUMERATOR_MAP = {
    Enumerator.Windows: enumerators.windows,
    Enumerator.Cygwin: enumerators.cygwin,
    Enumerator.Xrandr: enumerators.xrandr,
    Enumerator.Xinerama: enumerators.xinerama,
    Enumerator.DRM: enumerators.drm,
    Enumerator.OSX: enumerators.osx,
}


def _get_monitors(enumerator: Enumerator) -> T.List[Monitor]:
    return list(ENUMERATOR_MAP[enumerator].enumerate_monitors())


def get_monitors(
    name: T.Union[Enumerator, str, None] = None
) -> T.List[Monitor]:
    """Returns a list of :class:`Monitor` objects based on active monitors."""
    enumerator = Enumerator(name) if name is not None else None

    if enumerator is not None:
        return _get_monitors(enumerator)

    for enumerator in Enumerator:
        try:
            result = _get_monitors(enumerator)
            assert result
            return result
        except Exception:
            pass

    raise ScreenInfoError("No enumerators available")
