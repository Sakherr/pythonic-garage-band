class Musician:
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        pass

    def play_solo(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
        return [member.play_solo() for member in self.members]


