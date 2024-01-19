import json
from jsonschema.validators import validate


class Validator:

    def validate_schema(self,json_file,schema_file):

        """
        This function validates a JSON file against a JSON schema

        :param json_file: The path to the JSON file to be validated
        :type json_file: str
        :param schema_file: The path to the JSON schema file used foe validation
        :type schema_file: str
        :return: True if validation succeeds , False otherwise 
        :rtype: bool

        """

        with open(json_file,'r') as json_handler:
            json_content = json.load(json_handler)

        with open(schema_file,'r') as schema_handler:
            json_schema = json.load(schema_handler)

        try:
            validate(json_content,json_schema)
            return True
        except Exception as e:
            print(f"validation failed {e}")
            return False

obj = Validator()
result = obj.validate_schema("example.json","schema.json")
print(result)