import json


class Solution:

    def more_then_one_asterisk(self, path: str) -> bool:
        """
        This method returns False if "Resource"\n
        property include only one asterisk.\n
        Every other case returns True.
        """

        if path is None or path.endswith(".json") is not True:
            print("Please provide a path to a json file")
            return None

        try:

            with open(path, "r") as file:
                data = file.read()
                if not data:
                    print("JSON file is empty")
                    return None

                js = json.loads(data)
                asterisk = js["PolicyDocument"]["Statement"][0]["Resource"]
                return asterisk.count("*") != 1

        except Exception as e:
            print(f"Error occurred while loading json file: {e}")
