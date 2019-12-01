import xml.etree.cElementTree as ET

def writeXML(file_name):
    tree = ET.parse(file_name)

    root = tree.getroot()
    child = ET.Element("item")
    child.text = "3"

    root.append(child)

    tree.write(file_name)
if __name__ == "__main__":
   writeXML("netWorkPlugin.xml")