import base64

class Util:
    def base64_from_hex(self, hexstr):
        """
        Returns the base64 string for the hex string specified

        :param hexstr: The hex string to convert to base64
        :return: The base64 value for the specified hes string
        """
        return base64.b64encode(bytes(bytearray.fromhex(hexstr))).decode("utf8")
