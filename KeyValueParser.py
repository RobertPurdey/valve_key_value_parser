# Don't forget to comment !!


class ValveKeyValueParser:
    """ API to Parse Valve Key-Value Pairs.
    """
    def __init__(self):
        """ Inits ValveKeyValueParser.
        """

    @staticmethod
    def get_key_value(line):
        """ Finds the Key-Value pair and returns it.

            Returns:
                String representation of Key-Value pair delimited by a comma "Key,Value".
        """
        key_value = ""
        # remove leading spaces
        line = line.lstrip()

        if ValveKeyValueParser.is_key_value_pair(line):
            # Get the index for the start and end of both the key and value (allows them to be substringed)
            key_value_indexes = [pos for pos, char in enumerate(line) if char == "\""]

            key   = line[(key_value_indexes[0] + 1):key_value_indexes[1]]
            value = line[(key_value_indexes[2] + 1):key_value_indexes[3]]

            key_value = key + "," + value

        return key_value

    @staticmethod
    def is_key_value_pair(line):
        """ Validates that the line is a key-value pair line.

        Note:
            A key value pair format is <"Key"        "Value"> where the whitespace is not a fixed amount.
        Args:
            line (str): A line from a valve kvp file.

        Returns:
            True if the line is a kvp, False otherwise.
        """
        is_valid = True

        if not line:
            is_valid = False

        # Key-value pair lines always start with a double quotation
        if not line.startswith("\""):
            is_valid = False

        # Key-value pair lines have 4 double-quotations
        if not line.count("\"") == 4:
            is_valid = False
            s = 1
        return is_valid


#if __name__ == '__main__':
 #   test_line = "\"Key\"---    \"Value\""
  #  parser    = ValveKeyValueParser()
#
 #   key_val = ValveKeyValueParser.get_key_value(parser, test_line)
  #  print(key_val)

