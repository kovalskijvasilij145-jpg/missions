import sys
import json
import xml.etree.ElementTree as ET

def json_to_xml(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    root = ET.Element("Missions")

    for mission in data:
        m = ET.SubElement(root, "Mission")
        ET.SubElement(m, "date").text = mission["date"]
        ET.SubElement(m, "branch").text = mission["equip"]
        ET.SubElement(m, "task").text = mission["task"]
        ET.SubElement(m, "performers").text = ", ".join(mission["pilots"])
        ET.SubElement(m, "description").text = mission["description"]
        ET.SubElement(m, "starttime").text = mission["starttime"]

        coords = ET.SubElement(m, "coordinates")
        for lat, lon in mission["points"]:
            p = ET.SubElement(coords, "point")
            ET.SubElement(p, "latitude").text = str(lat)
            ET.SubElement(p, "longitude").text = str(lon)

    xml_file = json_file.rsplit(".", 1)[0] + ".xml"
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"XML saved to {xml_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: python script.py missions.json")
    else:
        json_to_xml(sys.argv[1])
