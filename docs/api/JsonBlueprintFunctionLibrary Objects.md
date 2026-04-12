## JsonBlueprintFunctionLibrary Objects

```python
class JsonBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Json Blueprint Function Library

**C++ Source:**

- **Plugin**: JsonBlueprintUtilities
- **Module**: JsonBlueprintUtilities
- **File**: JsonBlueprintFunctionLibrary.h

<a id="unreal.JsonBlueprintFunctionLibrary.to_string"></a>

#### to\_string

```python
@classmethod
def to_string(cls, json_object: JsonObjectWrapper) -> Optional[str]
```

X.to_string(json_object) -> str or None
Creates a Json string from the provided JsonObject.

Args:
    json_object (JsonObjectWrapper): 

Returns:
    str or None: 

    out_json_string (str):

<a id="unreal.JsonBlueprintFunctionLibrary.to_file"></a>

#### to\_file

```python
@classmethod
def to_file(cls, json_object: JsonObjectWrapper, file: FilePath) -> bool
```

X.to_file(json_object, file) -> bool
Creates a file from the provided JsonObject.

Args:
    json_object (JsonObjectWrapper): 
    file (FilePath): 

Returns:
    bool:

<a id="unreal.JsonBlueprintFunctionLibrary.has_field"></a>

#### has\_field

```python
@classmethod
def has_field(cls, json_object: JsonObjectWrapper, field_name: str) -> bool
```

X.has_field(json_object, field_name) -> bool
Checks if the field exists on the object.

Args:
    json_object (JsonObjectWrapper): 
    field_name (str): 

Returns:
    bool:

<a id="unreal.JsonBlueprintFunctionLibrary.get_field_names"></a>

#### get\_field\_names

```python
@classmethod
def get_field_names(cls,
                    json_object: JsonObjectWrapper) -> Optional[Array[str]]
```

X.get_field_names(json_object) -> Array[str] or None
Gets all field names on the JsonObject

Args:
    json_object (JsonObjectWrapper): 

Returns:
    Array[str] or None: 

    field_names (Array[str]):

<a id="unreal.JsonBlueprintFunctionLibrary.from_string"></a>

#### from\_string

```python
@classmethod
def from_string(cls, json_string: str) -> Optional[JsonObjectWrapper]
```

X.from_string(json_string) -> JsonObjectWrapper or None
Creates a JsonObject from the provided Json string.

Args:
    json_string (str): 

Returns:
    JsonObjectWrapper or None: 

    out_json_object (JsonObjectWrapper):

<a id="unreal.JsonBlueprintFunctionLibrary.from_file"></a>

#### from\_file

```python
@classmethod
def from_file(cls, file: FilePath) -> Optional[JsonObjectWrapper]
```

X.from_file(file) -> JsonObjectWrapper or None
Creates a JsonObject from the provided Json file.

Args:
    file (FilePath): 

Returns:
    JsonObjectWrapper or None: 

    out_json_object (JsonObjectWrapper):

<a id="unreal.PCGData"></a>