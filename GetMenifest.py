import axmlparserpy.apk as apk
ap = apk.APK('Apps/temp.apk')

per =  ap.get_permissions()
permissions=[]
for line in per:
    s=''
    for i in reversed(line):
        if i != '.':
            s+=i
        else:
            break
    s = s[::-1]
    permissions.append(s.upper())
permissions.sort()

for line in permissions:
    print line