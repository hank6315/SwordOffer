def replaceSpace(self, s):
        return ''.join(x if x != ' ' else '%20' for x in s)