## BlueprintJsonLibrary Objects

```python
class BlueprintJsonLibrary(BlueprintFunctionLibrary)
```

Blueprint Json Library

**C++ Source:**

- **Plugin**: BlueprintJson
- **Module**: BlueprintJson
- **File**: BlueprintJsonLibrary.h

<a id="unreal.BlueprintJsonLibrary.not_equal_json_value"></a>

#### not\_equal\_json\_value

```python
@classmethod
def not_equal_json_value(cls, a: BlueprintJsonValue,
                         b: BlueprintJsonValue) -> bool
```

X.not_equal_json_value(a, b) -> bool
Returns true if the values are not equal (A != B)

Args:
    a (BlueprintJsonValue): 
    b (BlueprintJsonValue): 

Returns:
    bool:

<a id="unreal.BlueprintJsonLibrary.json_type"></a>

#### json\_type

```python
@classmethod
def json_type(cls, json_value: BlueprintJsonValue) -> JsonType
```

X.json_type(json_value) -> JsonType
Return the type of json value

Args:
    json_value (BlueprintJsonValue): 

Returns:
    JsonType:

<a id="unreal.BlueprintJsonLibrary.json_set_field"></a>

#### json\_set\_field

```python
@classmethod
def json_set_field(cls, json_object: BlueprintJsonObject, field_name: str,
                   json_value: BlueprintJsonValue) -> BlueprintJsonObject
```

X.json_set_field(json_object, field_name, json_value) -> BlueprintJsonObject
Sets the value of the field with the specified name.

Args:
    json_object (BlueprintJsonObject): The stored json object
    field_name (str): The name of the field to set.
    json_value (BlueprintJsonValue): 

Returns:
    BlueprintJsonObject: The stored json object

<a id="unreal.BlueprintJsonLibrary.json_remove_field"></a>

#### json\_remove\_field

```python
@classmethod
def json_remove_field(cls, json_object: BlueprintJsonObject,
                      field_name: str) -> BlueprintJsonObject
```

X.json_remove_field(json_object, field_name) -> BlueprintJsonObject
Removes the field with the specified name.

Args:
    json_object (BlueprintJsonObject): The stored json object
    field_name (str): The name of the field to remove.

Returns:
    BlueprintJsonObject: The stored json object

<a id="unreal.BlueprintJsonLibrary.json_make_field"></a>

#### json\_make\_field

```python
@classmethod
def json_make_field(cls, json_object: BlueprintJsonObject, field_name: str,
                    value: BlueprintJsonValue) -> BlueprintJsonObject
```

X.json_make_field(json_object, field_name, value) -> BlueprintJsonObject
Sets the value of the field with the specified name.

Args:
    json_object (BlueprintJsonObject): The stored json object
    field_name (str): The name of the field to set.
    value (BlueprintJsonValue): The json value to set.

Returns:
    BlueprintJsonObject: The stored json object

<a id="unreal.BlueprintJsonLibrary.json_is_null"></a>

#### json\_is\_null

```python
@classmethod
def json_is_null(cls, json_value: BlueprintJsonValue) -> bool
```

X.json_is_null(json_value) -> bool
Return true if the json value is null, false otherwise

Args:
    json_value (BlueprintJsonValue): 

Returns:
    bool:

<a id="unreal.BlueprintJsonLibrary.json_has_typed_field"></a>

#### json\_has\_typed\_field

```python
@classmethod
def json_has_typed_field(cls, json_object: BlueprintJsonObject,
                         field_name: str, type: JsonType) -> bool
```

X.json_has_typed_field(json_object, field_name, type) -> bool
Checks whether a field with the specified name and type exists in the object.

Args:
    json_object (BlueprintJsonObject): The stored json object
    field_name (str): The name of the field to check.
    type (JsonType): The type of the field to check.

Returns:
    bool: true if the field exists, false otherwise.

<a id="unreal.BlueprintJsonLibrary.json_has_field"></a>

#### json\_has\_field

```python
@classmethod
def json_has_field(cls, json_object: BlueprintJsonObject,
                   field_name: str) -> bool
```

X.json_has_field(json_object, field_name) -> bool
Checks whether a field with the specified name exists in the json object.

Args:
    json_object (BlueprintJsonObject): The stored json object
    field_name (str): The name of the field to check.

Returns:
    bool: true if the field exists, false otherwise.

<a id="unreal.BlueprintJsonLibrary.equa_equal_json_value"></a>

#### equa\_equal\_json\_value

```python
@classmethod
def equa_equal_json_value(cls, a: BlueprintJsonValue,
                          b: BlueprintJsonValue) -> bool
```

X.equa_equal_json_value(a, b) -> bool
Returns true if the values are equal (A == B)

Args:
    a (BlueprintJsonValue): 
    b (BlueprintJsonValue): 

Returns:
    bool:

<a id="unreal.BlueprintJsonLibrary.conv_string_to_json_object"></a>

#### conv\_string\_to\_json\_object

```python
@classmethod
def conv_string_to_json_object(cls, json_string: str) -> BlueprintJsonObject
```

X.conv_string_to_json_object(json_string) -> BlueprintJsonObject
Convert json string to json object

Args:
    json_string (str): The string to convert

Returns:
    BlueprintJsonObject: The json object

<a id="unreal.LowEntryBitDataEntry"></a>