import xml.etree.ElementTree as ET

data = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Hypo</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Bru</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(data)

lst = tree.findall('users/user')
#give me all the users inside users branch

print(lst)
print()

print("User count:", len(lst))
print()
for i in lst:
    print("Name:", i.find('name').text)
    print("ID:", i.find('id').text)
    print("Attribute:", i.get("x"))
    print()
