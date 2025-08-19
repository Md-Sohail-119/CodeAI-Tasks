l = []
for i in range(1,6):
    l.append(str(input("Enter a fruit name.  ")))

for i in l:
    if len(i) >= 5:
        print(f"The fruit {i} has {len(i)} characters.")
        
