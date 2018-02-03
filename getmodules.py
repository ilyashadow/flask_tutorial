#!venv/bin/python3

import pip

inst_pack = pip.get_installed_distributions()
inst_pack_list = sorted(["%s==%s" % (i.key, i.version)
    for i in inst_pack])
f = open("request_modules.txt", "w")
print("Request modules in project:", file=f)

for i in inst_pack_list:
    print(i, file=f)

f.close()