import string


def enquire(msg: str, returntype, allowed="", default=""):
    """
    Obtain user input safely.

    Display a message asking for user input.
    Specify desired return type: "letter" or "number".
    Specify allowed input in format.
        "n_m" for a range
        "i,j,k" for distinct values
        examples "number": "1_5", "2,4,6,8"
        examples "letter": "a_z", "a,e,i,o,u"
    Specify default value returned upon empty input.
    If given, default *must* be str.

    Parameters
    msg (str): a message to show on input
    returntype (str): "letter" or "number"
    allowed (str): specs on allowed input
    default (str): default return value

    Returns
    str, int or float
    """

    if returntype == "number":
        ald = allowed_numbers(allowed)
        answer = ask_for(msg, ald)
        if answer:
            answer = int(answer)
        elif default:
            answer = int(default)
        else:
            answer = ""

    elif returntype == "letter":
        ald = allowed_letters(allowed)
        answer = ask_for(msg, ald)
        if not answer:
            answer = default.lower()

    else:
        raise ValueError("Enquired unknown type. 'letter' or 'number' only.")

    return answer


def ask_for(msg: str, allowed: list):
    while True:
        inp = input(msg).lower()
        if inp in allowed:
            break
        else:
            print("Bad input.\nAllowed: "
                  + " ".join([c for c in allowed])
                  + "\nTry again!")
    return inp


def allowed_numbers(spec: str) -> list:
    """
    List of valid numbers.

    :param spec: str
    :return: list
    """
    valid = ["", ]

    if not spec:
        valid.extend([str(n) for n in range(10)])

    elif spec.count("_") == 1:
        part = spec.split("_")
        hi, lo = int(part[0]), int(part[1])
        if lo > hi:
            hi, lo = lo, hi
        valid.extend([str(n) for n in range(lo, hi+1)])

    elif spec.count(",") > 0:
        valid.extend([n for n in spec.split(",")])

    else:
        raise ValueError("Enquire: Bad number specification: {}".format(spec))

    return valid


def allowed_letters(spec: str) -> list:
    """
    List of valid letters.

    :param spec: str
    :return: list
    """
    valid = ["", ]

    if not spec:
        valid.extend([c for c in string.ascii_lowercase])

    elif spec.count("_") == 1:
        part = spec.split("_")
        if len(part[0]) != 1 or len(part[1]) != 1:
            raise ValueError(f"Enquire: Bad range limits: {spec}")
        hi, lo = ord(part[0].lower()), ord(part[1].lower())
        if lo > hi:
            hi, lo = lo, hi
        if lo < 97 or hi > 122:
            raise ValueError(f"Enquire: letter out of range: {spec}")
        valid.extend([chr(c) for c in range(lo, hi+1)])

    elif spec.count(",") > 0:
        valid.extend([n.lower().strip() for n in spec.split(",")])

    else:
        valid = ["", spec]

    return valid
