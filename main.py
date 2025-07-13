
import json, unittest, datetime
from dateutil import parser  # For ISO to epoch conversion

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):
    # data-1.json format: flat structure with deviceID, timestamp (number), temp
    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],  # Already in epoch ms
        "location": {
            "country": jsonObject["location"].split("/")[0],
            "city": jsonObject["location"].split("/")[1], 
            "area": jsonObject["location"].split("/")[2],
            "factory": jsonObject["location"].split("/")[3],
            "section": jsonObject["location"].split("/")[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }


def convertFromFormat2(jsonObject):
    # data-2.json format: nested structure with device.id, ISO timestamp, data.temperature
    # Convert ISO timestamp to epoch ms
    dt = parser.parse(jsonObject["timestamp"])
    epoch_ms = int(dt.timestamp() * 1000)
    
    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": epoch_ms,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }


def main(jsonObject):
    # Detect format based on structure
    # Format 1 has flat deviceID, Format 2 has nested device.id
    if "deviceID" in jsonObject:
        return convertFromFormat1(jsonObject)
    else:
        return convertFromFormat2(jsonObject)


class TestSolution(unittest.TestCase):

    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )


if __name__ == '__main__':
    unittest.main()
