from tkinter.ttk import Entry
import re
# ADDITION TO NORMAL TK ENTRY, JUSTIFY CENTER IS USED ON EVERY ENTRY IN CODE
class BaseEntry(Entry):
    def __init__(self, parent, justify="center", numbers=False,floating=False,positive=False, **kwargs):
        # TODO do some comments
        if numbers:
            super().__init__(parent, justify=justify, **kwargs)
            self.vcmd_digit = (self.register(self.__is_integer_callback))
            super().__init__(parent,justify=justify,validate='all',validatecommand=(self.vcmd_digit, '%P'), **kwargs)
        elif floating:
            super().__init__(parent, justify=justify, **kwargs)
            self.vcmd_float = (self.register(self.__is_float_callback))
            super().__init__(parent, justify=justify, validate='all', validatecommand=(self.vcmd_float, '%P'), **kwargs)
        elif positive:
            super().__init__(parent, justify=justify, **kwargs)
            self.vcmd_positive = (self.register(self.__is_positive_callback))
            super().__init__(parent, justify=justify, validate='all', validatecommand=(self.vcmd_positive, '%P'), **kwargs)
        else:
            super().__init__(parent, justify=justify, **kwargs)

    # TODO do some comments
    def __is_integer_callback(self, P):
        if P == "":
            return True
        if P == "-":
            return True
        try:
            int(P)
            return True
        except:
            return False
    def __is_positive_callback(self ,P):
        if P.isdigit() or P == "":
            return True
        return False


    def __is_float_callback(self,P):
        regex = re.compile(r"(\+)?[0-9.]*$")
        result = regex.match(P)
        return (P == ""
                or (P.count('+') <= 1
                    and P.count('-') <= 1
                    and P.count('.') <= 1
                    and result is not None
                    and result.group(0) != ""))