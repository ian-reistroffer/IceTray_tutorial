from __future__ import annotations


def _iter_filter_items(mask):
    if hasattr(mask, "items"):
        yield from mask.items()
        return
    if hasattr(mask, "keys"):
        for name in mask.keys():
            yield name, mask[name]
        return
    for item in mask:
        try:
            name, result = item
        except Exception:
            name, result = item, mask[item]
        yield name, result


def filter_passed(frame, filter_name: str, mask_key: str = "QFilterMask") -> bool:
    """Return True when a named filter passed condition and prescale."""
    if mask_key not in frame:
        return False

    mask = frame[mask_key]
    try:
        result = mask[filter_name]
    except Exception:
        return False

    return bool(
        getattr(result, "condition_passed", False)
        and getattr(result, "prescale_passed", False)
    )


def passed_filter_names(frame, mask_key: str = "QFilterMask") -> list[str]:
    """Return all filters that passed condition and prescale."""
    if mask_key not in frame:
        return []

    passed = []
    mask = frame[mask_key]
    for name, result in _iter_filter_items(mask):
        if getattr(result, "condition_passed", False) and getattr(
            result, "prescale_passed", False
        ):
            passed.append(str(name))
    return passed


def filter_table(frame, mask_key: str = "QFilterMask") -> list[dict[str, object]]:
    """Return a row per filter decision."""
    if mask_key not in frame:
        return []

    rows = []
    for name, result in _iter_filter_items(frame[mask_key]):
        condition = bool(getattr(result, "condition_passed", False))
        prescale = bool(getattr(result, "prescale_passed", False))
        rows.append(
            {
                "filter": str(name),
                "condition_passed": condition,
                "prescale_passed": prescale,
                "passed": condition and prescale,
            }
        )
    return rows
