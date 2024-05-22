class marine():
    
    name = ''
    id = ''
    years_in_field = 0

    def __init__(self, name, id, years_in_field):
        self.name = name
        self.id = id
        self.years_in_field = years_in_field

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_years_in_field(self):
        return self.years_in_field
    
    def chant(self):
        print("Sir Yes Sir!")


class super_marine(marine):

    def is_enlisted(self):
        return True
    
    def super_chant(self):
        print("Glory to the High Power!")


m = marine("Johnson", "IDX891", 5)
print(m.get_name(), m.get_id(), m.get_years_in_field())
m.chant()

sm = super_marine("DeRickson", "IDXX281", 14)
sm.super_chant()
sm.chant()
print(sm.get_name(), sm.get_id(), sm.get_years_in_field())