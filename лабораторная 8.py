#1
'''
ip = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"] ; ip_new = []
for i in ip :
    if ip_new.count(i)==0 : ip_new.append(i)
print(ip_new)
'''
#2
'''
s = {"root","admin","test"}
s.add("hacker") ; s.remove("test")
print(list(sorted(s, reverse = True)))
'''
#3
'''
z = {21, 22, 23, 25}
if int(input()) in z: print("port zapreshen")
else: print("port ne zapreshen")
'''
#4
'''
a = {"mal.com", "bad.net"} ; n = {"bad.net", "xevil.org"}
for i in n:
    if i not in a: print(i)
'''
#5
'''
w = {"alice", "bob", "root"} ; b = {"root", "admin"}
for i in w:
    if i in b:print(i)
'''
#6
'''
a = {"cve-1","cve-2"} ; b = {"cve-2","cve-3"}
print(a|b)
'''
#7
'''
admin = {"read", "write", "delete"} ; user = {"read", "download"}
print(admin ^ user)
'''
#8
'''
logs = ["123","qwerty","test","123","qwerty","admin"] ; ban = {"test"}
print(set(logs) - ban)
'''
#9
'''
global_ips = {"10.0.0.1", "10.0.0.2", "192.168.1.1"} ; local_ips = {"10.0.0.2", "10.0.0.3"}
for i in local_ips:
    if i in global_ips:print(i)
'''
#10
'''
logs = ["scan", "debug_mode", "scan", "connect", "debug_info"]
print({x for x in logs if "debug" not in x})
'''