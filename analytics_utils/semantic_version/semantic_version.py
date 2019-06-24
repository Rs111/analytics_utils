import re
from typing import Optional, List


class SemanticVersion:
    """Holds methods to parse input semantic version.

    All method return None if input is not a valid semantic version.

    A semantic version input is valid if:
    It contains only number and periods
    It is not an empty String
    It does not start with a period
    It does not end with a period
    It has between 0 and two periods
    It does not contain two periods in a row

    :param s: semantic version in the form of 'Major.Minor.Patch'
    :type s: str
    """

    def __init__(self, s: str):
        """Initialize with `s`"""
        if type(s) != str:
            raise TypeError("input semantic version must be a `str`")
        self.s = s

    def __str__(self, clean: bool = True) -> Optional[str]:
        """Represent the instance as `s` (either cleaned or not).

        :param clean: whether to clean `s`
        :return: `s`
        """
        if clean:
            return self.clean()
        else:
            return self.s

    def clean(self) -> Optional[str]:
        """Clean `s` according to the logic below.

        Return None if `s` is invalid
        If `s` is valid:
        Return `s` with minor and patch set to 0 if `s` is missing minor and patch
        Return `s` with patch set to 0 if `s` is missing patch
        Return `s` unchanged when it contains major, minor, and patch

        :return: cleaned `s`
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

    def parse(self) -> Optional[List[int]]:
        """Return cleaned `s` as a `List[int]` of major, minor, patch"""
        cleaned = self.clean()
        if cleaned is None:
            return None
        else:
            return [int(semantic_version_string) for semantic_version_string in cleaned.split(".")]

    def __parse_semantic_version(self, i) -> Optional[int]:
        """Return the ith element from the output of `parse`"""
        parsed = self.parse()
        if parsed is None:
            return None
        else:
            return parsed[i]

    def parse_major(self) -> Optional[int]:
        """Return the major from the output of `parse`"""
        return self.__parse_semantic_version(0)

    def parse_minor(self) -> Optional[int]:
        """Return the minor from the output of `parse`"""
        return self.__parse_semantic_version(1)

    def parse_patch(self) -> Optional[int]:
        """Return the patch from the output of `parse`"""
        return self.__parse_semantic_version(2)
