
from typing import Any


def remove_nones(obj: Any) -> Any:
    """ ToDo: DocString """
    if isinstance(obj, dict):
        return {k: remove_nones(v) for k, v in obj.items() if v is not None}
    elif isinstance(obj, list):
        return [remove_nones(x) for x in obj if x is not None]
    else:
        return obj