
class Enquire:
    """Obtain user input safely."""

    def number(self, msg: str, allowed="", default=""):
        """
        Obtain integer input safely.

        Display a message asking for user input.
        Specify allowed input in format.
            "n_m" for a range including n and m
            "i,j,k" for distinct values
        Specify default value returned upon empty input.
        If given, default *must* be str.

        Repeat input until valid.

        Parameters
        msg (str): a message to show on input
        allowed (str): specs on allowed input
        default (str): default return value

        Returns
        int
        """
        ald = self.allowed_numbers(allowed)
        answer = self.ask_for(msg, ald)
        if answer:
            answer = int(answer)
        elif default:
            answer = int(default)
        else:
            answer = ""
        return answer

    def letter(self, msg: str, allowed="", default=""):
        """
        Obtain letter input safely.

        Display a message asking for user input.
        Specify allowed input in format.
            "a_z" for a range of consecutive letters
            "a,e,i,o,u" for distinct letters
        Specify default value returned upon empty input.

        Repeat input until valid.

        Parameters
        msg (str): a message to show on input
        allowed (str): specs on allowed input
        default (str): default return value

        Returns
        str
        """
        ald = self.allowed_letters(allowed)
        answer = self.ask_for(msg, ald)
        if not answer:
            answer = default.lower()
        return answer

    @staticmethod
    def ask_for(msg: str, allowed: list):
        """Get input until it is valid.
        """
        while True:
            inp = input(msg).lower()
            if inp in allowed:
                break
            else:
                print("Bad input.\nAllowed: "
                      + " ".join([c for c in allowed])
                      + "\nTry again!")
        return inp

    @staticmethod
    def allowed_numbers(spec: str) -> list:
        """
        Takes a short-cut description of valid numbers
        and turns it into a list of integers.

        "1_5": a range including 1 and 5
        "2,4,6": distinct values

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
            valid.extend([n.strip() for n in spec.split(",")])

        else:
            raise ValueError("Enquire: Bad number specification: {}".format(spec))

        return valid

    @staticmethod
    def allowed_letters(spec: str) -> list:
        """
        Takes a short-cut description of valid strings
        and turns it into a list of strings.
        Returned strings are all lower case.

        "a_z": A range of consecutive letters
        "b,d,f": A sequence of arbitrary letters
        "opt1,opt2,opt3": A sequence of arbitrary words/phrases/options

        :param spec: str
        :return: list
        """
        valid = ["", ]

        if not spec:
            valid.extend([chr(c) for c in range(97, 123)])

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
