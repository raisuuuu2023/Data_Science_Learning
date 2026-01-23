import numpy as np
arr=np.array([1,2,np.inf,6,-np.inf,5])
print(np.isinf(arr))
cleaned_arr=np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(cleaned_arr)