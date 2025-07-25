def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False

    if not plate.isalnum():
        return False

    if not plate[:2].isalpha():
        return False

    if not plate[-1].isdigit() or plate.startswith("0"):
        return False

    if any(char in ". ,;:!?@#$%^&*()-_=+{}[]|<>/`~" for char in plate):
        return False

    return True
