class Hash:
    def make(value):
        return value

    def check(hashedValue, value):
        return hashedValue == Hash.make(value)