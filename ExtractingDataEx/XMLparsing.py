import xml.etree.ElementTree as ET

data = '''<person>
<name>Hypo</name>
<phone type="intl">
    +1 734 303 4456
 </phone>
 <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
# this can blow up if data has error

print(tree)
print(type(tree.find("name")))
print("Name: ",tree.find("name").text)
#extracts the text from the tag


print("Attr: ",tree.find("email").get("hide"))
#extracts the atribute value, text does not exist