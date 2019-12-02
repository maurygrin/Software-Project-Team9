import xml.etree.cElementTree as ET

def writeXML(file_name):
    tree = ET.parse(file_name)

    root = tree.getroot()
    child = ET.Element("item")
    subName = ET.SubElement(child, "nameStrings")
    subType = ET.SubElement(child, "typeStrings")
    subOutput = ET.SubElement(child, "outputString")
    subName.text = "Ping"
    subType.text = "String"
    subOutput.text = "Pong"

    root.append(child)


    tree.write(file_name)
if __name__ == "__main__":
   writeXML("netWorkPlugin.xml")