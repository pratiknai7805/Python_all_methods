class Tuple_function:
    def __init__(self):
        self.t=(22,12,45,2)
    
    def tuple_function(self):
        print('Tuple function:')
        print(self.t.count(2))
        print(self.t.index(45))

    
obj=Tuple_function()
obj.tuple_function()