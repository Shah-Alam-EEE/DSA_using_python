import pandas as pd
my_dict={'employee':{'Habib':{'age':'13','nationality':'bangladeshi'},
                     'Hasib':{'age':'29','nationality':'bangladeshi'}
                     }
        }             
x=pd.DataFrame(my_dict['employee'])
print(x)