from aircraft_template import Aircraft_Template

class Aircraft(Aircraft_Template):
    
    def __init__(self):
        super().__init__()
        self.name = 'wing_e216'
        
if __name__=='__main__':
    airplane = Aircraft()