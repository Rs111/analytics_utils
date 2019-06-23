import re


class SemanticVersion:
    """Holds methods to parse a semantic app version in the form of 'Major.Minor.Patch'

    """

    def __init__(self, s):
        """Initialize with a semantic app version String input"""
        self.s = s

    def clean(self):
        """Clean semantic app version String according to the logic below

        A semantic app version String is valid if:
        It contains only number and periods
        It is not an empty String
        It does not start with a period
        It does not end with a period
        It has between 0 and two periods
        It does not contain two periods in a row

        Clean a valid semantic app version String using the logic below:
        If a valid semantic app version contains only the major, set the minor and patch to 0
        If a valid semantic app version contains only the major and minor, set the patch to 0
        If a valid semantic app version contains the major, minor, and patch, leave as is

        If a semantic app version input is not valid, return None

        :return: cleaned semantic version String if input is valid, and None if input semantic version is invalid
        """

        valid_chars_regex = "|".join([str(i) for i in range(0, 10)] + ["\\."])
        length = len(self.s.split("."))

        if \
            len(re.sub(valid_chars_regex, "", self.s)) == 0 and \
            self.s != "" and \
            self.s[0] != "." and \
            self.s[-1] != "." and \
            1 <= length <= 3 and \
            ".." not in self.s:

            if length == 1:
                return self.s + ".0.0"
            elif length == 2:
                return self.s + ".0"
            else:
                return self.s
        else:
            return None


    def parse(self):
        """Return """
        cleaned = self.clean()
        if cleaned is None:
            return None
        else:
            return cleaned.split(".")


    def parse_semantic_version(self, i):
        parsed = self.parse()
        if parsed is None:
            return None
        else:
            return parsed[i]


    def parse_major(self):
        return self.parse_semantic_version(0)


    def parse_minor(self):
        return self.parse_semantic_version(1)


    def parse_patch(self):
        return self.parse_semantic_version(2)

print(len("".split(".")))
print(SemanticVersion("").parse())