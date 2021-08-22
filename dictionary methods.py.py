d={"Name":"Sam","Dept":"ECE","Roll no":138,"CGPA":9.5}
dic=d.copy()
print(dic)
print(d.get("Name"))
print(d.items())
print(d.keys())
print(d.pop("CGPA"))
print(d.popitem())
print(d.setdefault("Age",18))
print(d.values())
d1={}
seq=["Maths","Circuit theory"]
print(d1.fromkeys(seq,"pass"))
d2={"Age":19}
d.update(d2)
print(d)
d.clear()
print(d)
      
      
