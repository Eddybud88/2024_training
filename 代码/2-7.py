name = "\tLeon \n Scott \n Kenndy \t"
name_lstrip = name.lstrip()
print(f"使用lstrip()处理后：'{name_lstrip}'")
name_rstrip = name.rstrip()
print(f"使用rstrip()处理后：'{name_rstrip}'")
name_strip = name.strip()
print(f"使用strip()处理后：'{name_strip}'")

输出：
使用lstrip()处理后：
'Leon 
 Scott 
 Kenndy 	'
rstrip()处理后：
'	Leon 
 Scott 
 Kenndy'
使用strip()处理后：
'Leon 
 Scott 
 Kenndy'
