\* smartcity *\
Minimize
OBJ: 0.19 camera_0___edge_0___obj_1 + 0.95 camera_0___edge_0___obj_4
 + 1.9 camera_0___edge_0___obj_5_copy_device_0
 + 1.9 camera_0___edge_0___obj_5_copy_device_1
 + 0.0520833333333 camera_0___func_1 + 0.000126 center___edge_0___obj_1
 + 0.00063 center___edge_0___obj_4
 + 0.00126 center___edge_0___obj_5_copy_device_0
 + 0.00126 center___edge_0___obj_5_copy_device_1 + 0.05 center___func_1
 + 0.19 device_0___edge_0___obj_1 + 0.95 device_0___edge_0___obj_4
 + 1.9 device_0___edge_0___obj_5_copy_device_0
 + 1.9 device_0___edge_0___obj_5_copy_device_1 + 0.25 device_0___func_1
 + 0.19 device_1___edge_0___obj_1 + 0.95 device_1___edge_0___obj_4
 + 1.9 device_1___edge_0___obj_5_copy_device_0
 + 1.9 device_1___edge_0___obj_5_copy_device_1 + 0.25 device_1___func_1
 + 0.19 edge_0___camera_0___obj_1 + 0.95 edge_0___camera_0___obj_4
 + 1.9 edge_0___camera_0___obj_5_copy_device_0
 + 1.9 edge_0___camera_0___obj_5_copy_device_1
 + 0.000126 edge_0___center___obj_1 + 0.00063 edge_0___center___obj_4
 + 0.00126 edge_0___center___obj_5_copy_device_0
 + 0.00126 edge_0___center___obj_5_copy_device_1
 + 0.19 edge_0___device_0___obj_1 + 0.95 edge_0___device_0___obj_4
 + 1.9 edge_0___device_0___obj_5_copy_device_0
 + 1.9 edge_0___device_0___obj_5_copy_device_1
 + 0.19 edge_0___device_1___obj_1 + 0.95 edge_0___device_1___obj_4
 + 1.9 edge_0___device_1___obj_5_copy_device_0
 + 1.9 edge_0___device_1___obj_5_copy_device_1 + 0.25 edge_0___func_1
Subject To
_C1: - center___edge_0___obj_1 - center___func_1 + edge_0___center___obj_1 = 0
_C10: - camera_0___edge_0___obj_4 + camera_0___func_1 - camera_0___func_2
 + edge_0___camera_0___obj_4 = 0
_C11: - camera_0___edge_0___obj_5_copy_device_0
 + edge_0___camera_0___obj_5_copy_device_0 = 0
_C12: - camera_0___edge_0___obj_5_copy_device_1
 + edge_0___camera_0___obj_5_copy_device_1 = 0
_C13: - device_0___edge_0___obj_1 - device_0___func_1
 + edge_0___device_0___obj_1 = 0
_C14: - device_0___edge_0___obj_4 + device_0___func_1 - device_0___func_2
 + edge_0___device_0___obj_4 = 0
_C15: - device_0___edge_0___obj_5_copy_device_0
 + edge_0___device_0___obj_5_copy_device_0 = 1
_C16: - device_0___edge_0___obj_5_copy_device_1
 + edge_0___device_0___obj_5_copy_device_1 = 0
_C17: - device_1___edge_0___obj_1 - device_1___func_1
 + edge_0___device_1___obj_1 = 0
_C18: - device_1___edge_0___obj_4 + device_1___func_1 - device_1___func_2
 + edge_0___device_1___obj_4 = 0
_C19: - device_1___edge_0___obj_5_copy_device_0
 + edge_0___device_1___obj_5_copy_device_0 = 0
_C2: - center___edge_0___obj_4 + center___func_1 - center___func_2
 + edge_0___center___obj_4 = 0
_C20: - device_1___edge_0___obj_5_copy_device_1
 + edge_0___device_1___obj_5_copy_device_1 = 1
_C21: 25 center___func_1 <= 53500000
_C22: 25 edge_0___func_1 <= 6500000
_C23: 25 camera_0___func_1 <= 1
_C24: 25 device_0___func_1 <= 2000
_C25: 25 device_1___func_1 <= 2000
_C26: 10 center___edge_0___obj_1 + 50 center___edge_0___obj_4
 + 100 center___edge_0___obj_5_copy_device_0
 + 100 center___edge_0___obj_5_copy_device_1 <= 4480000000
_C27: 10 edge_0___center___obj_1 + 50 edge_0___center___obj_4
 + 100 edge_0___center___obj_5_copy_device_0
 + 100 edge_0___center___obj_5_copy_device_1 <= 4480000000
_C28: 10 edge_0___camera_0___obj_1 + 50 edge_0___camera_0___obj_4
 + 100 edge_0___camera_0___obj_5_copy_device_0
 + 100 edge_0___camera_0___obj_5_copy_device_1 <= 150000
_C29: 10 camera_0___edge_0___obj_1 + 50 camera_0___edge_0___obj_4
 + 100 camera_0___edge_0___obj_5_copy_device_0
 + 100 camera_0___edge_0___obj_5_copy_device_1 <= 150000
_C3: - center___edge_0___obj_5_copy_device_0
 + edge_0___center___obj_5_copy_device_0 = 0
_C30: 10 edge_0___device_0___obj_1 + 50 edge_0___device_0___obj_4
 + 100 edge_0___device_0___obj_5_copy_device_0
 + 100 edge_0___device_0___obj_5_copy_device_1 <= 150000
_C31: 10 device_0___edge_0___obj_1 + 50 device_0___edge_0___obj_4
 + 100 device_0___edge_0___obj_5_copy_device_0
 + 100 device_0___edge_0___obj_5_copy_device_1 <= 150000
_C32: 10 edge_0___device_1___obj_1 + 50 edge_0___device_1___obj_4
 + 100 edge_0___device_1___obj_5_copy_device_0
 + 100 edge_0___device_1___obj_5_copy_device_1 <= 150000
_C33: 10 device_1___edge_0___obj_1 + 50 device_1___edge_0___obj_4
 + 100 device_1___edge_0___obj_5_copy_device_0
 + 100 device_1___edge_0___obj_5_copy_device_1 <= 150000
_C34: 1.5 camera_0___edge_0___obj_1 + 1.5 camera_0___edge_0___obj_4
 + 1.5 camera_0___edge_0___obj_5_copy_device_0
 + 1.5 camera_0___edge_0___obj_5_copy_device_1 + 2 camera_0___func_1
 + 2 camera_0___func_2 + center___edge_0___obj_1 + center___edge_0___obj_4
 + center___edge_0___obj_5_copy_device_0
 + center___edge_0___obj_5_copy_device_1 + center___func_1 + center___func_2
 + 1.5 device_0___edge_0___obj_1 + 1.5 device_0___edge_0___obj_4
 + 1.5 device_0___edge_0___obj_5_copy_device_0
 + 1.5 device_0___edge_0___obj_5_copy_device_1 + 1.2 device_0___func_1
 + 1.2 device_0___func_2 + 1.5 device_1___edge_0___obj_1
 + 1.5 device_1___edge_0___obj_4 + 1.5 device_1___edge_0___obj_5_copy_device_0
 + 1.5 device_1___edge_0___obj_5_copy_device_1 + 1.2 device_1___func_1
 + 1.2 device_1___func_2 + 1.5 edge_0___camera_0___obj_1
 + 1.5 edge_0___camera_0___obj_4 + 1.5 edge_0___camera_0___obj_5_copy_device_0
 + 1.5 edge_0___camera_0___obj_5_copy_device_1 + edge_0___center___obj_1
 + edge_0___center___obj_4 + edge_0___center___obj_5_copy_device_0
 + edge_0___center___obj_5_copy_device_1 + 1.5 edge_0___device_0___obj_1
 + 1.5 edge_0___device_0___obj_4 + 1.5 edge_0___device_0___obj_5_copy_device_0
 + 1.5 edge_0___device_0___obj_5_copy_device_1 + 1.5 edge_0___device_1___obj_1
 + 1.5 edge_0___device_1___obj_4 + 1.5 edge_0___device_1___obj_5_copy_device_0
 + 1.5 edge_0___device_1___obj_5_copy_device_1 + 1.1 edge_0___func_1
 + 1.1 edge_0___func_2 <= 100000
_C4: - center___edge_0___obj_5_copy_device_1
 + edge_0___center___obj_5_copy_device_1 = 0
_C5: camera_0___edge_0___obj_1 + center___edge_0___obj_1
 + device_0___edge_0___obj_1 + device_1___edge_0___obj_1
 - edge_0___camera_0___obj_1 - edge_0___center___obj_1
 - edge_0___device_0___obj_1 - edge_0___device_1___obj_1 - edge_0___func_1 = 0
_C6: camera_0___edge_0___obj_4 + center___edge_0___obj_4
 + device_0___edge_0___obj_4 + device_1___edge_0___obj_4
 - edge_0___camera_0___obj_4 - edge_0___center___obj_4
 - edge_0___device_0___obj_4 - edge_0___device_1___obj_4 + edge_0___func_1
 - edge_0___func_2 = 0
_C7: camera_0___edge_0___obj_5_copy_device_0
 + center___edge_0___obj_5_copy_device_0
 + device_0___edge_0___obj_5_copy_device_0
 + device_1___edge_0___obj_5_copy_device_0
 - edge_0___camera_0___obj_5_copy_device_0
 - edge_0___center___obj_5_copy_device_0
 - edge_0___device_0___obj_5_copy_device_0
 - edge_0___device_1___obj_5_copy_device_0 = 0
_C8: camera_0___edge_0___obj_5_copy_device_1
 + center___edge_0___obj_5_copy_device_1
 + device_0___edge_0___obj_5_copy_device_1
 + device_1___edge_0___obj_5_copy_device_1
 - edge_0___camera_0___obj_5_copy_device_1
 - edge_0___center___obj_5_copy_device_1
 - edge_0___device_0___obj_5_copy_device_1
 - edge_0___device_1___obj_5_copy_device_1 = 0
_C9: - camera_0___edge_0___obj_1 - camera_0___func_1
 + edge_0___camera_0___obj_1 = -1
Bounds
camera_0___edge_0___obj_1 <= 1
camera_0___edge_0___obj_4 <= 1
camera_0___edge_0___obj_5_copy_device_0 <= 1
camera_0___edge_0___obj_5_copy_device_1 <= 1
center___edge_0___obj_1 <= 1
center___edge_0___obj_4 <= 1
center___edge_0___obj_5_copy_device_0 <= 1
center___edge_0___obj_5_copy_device_1 <= 1
device_0___edge_0___obj_1 <= 1
device_0___edge_0___obj_4 <= 1
device_0___edge_0___obj_5_copy_device_0 <= 1
device_0___edge_0___obj_5_copy_device_1 <= 1
device_1___edge_0___obj_1 <= 1
device_1___edge_0___obj_4 <= 1
device_1___edge_0___obj_5_copy_device_0 <= 1
device_1___edge_0___obj_5_copy_device_1 <= 1
edge_0___camera_0___obj_1 <= 1
edge_0___camera_0___obj_4 <= 1
edge_0___camera_0___obj_5_copy_device_0 <= 1
edge_0___camera_0___obj_5_copy_device_1 <= 1
edge_0___center___obj_1 <= 1
edge_0___center___obj_4 <= 1
edge_0___center___obj_5_copy_device_0 <= 1
edge_0___center___obj_5_copy_device_1 <= 1
edge_0___device_0___obj_1 <= 1
edge_0___device_0___obj_4 <= 1
edge_0___device_0___obj_5_copy_device_0 <= 1
edge_0___device_0___obj_5_copy_device_1 <= 1
edge_0___device_1___obj_1 <= 1
edge_0___device_1___obj_4 <= 1
edge_0___device_1___obj_5_copy_device_0 <= 1
edge_0___device_1___obj_5_copy_device_1 <= 1
Binaries
camera_0___func_1
camera_0___func_2
center___func_1
center___func_2
device_0___func_1
device_0___func_2
device_1___func_1
device_1___func_2
edge_0___func_1
edge_0___func_2
End
