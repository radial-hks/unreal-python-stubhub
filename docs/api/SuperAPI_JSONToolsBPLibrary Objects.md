## SuperAPI_JSONToolsBPLibrary Objects

```python
class SuperAPI_JSONToolsBPLibrary(BlueprintFunctionLibrary)
```

Super API JSONTools BPLibrary

**C++ Source:**

- **Plugin**: SunFunctionLibrary
- **Module**: SuperAPI_JSONTools
- **File**: SuperAPI_JSONToolsBPLibrary.h

<a id="unreal.SuperAPI_JSONToolsBPLibrary.matching_type"></a>

#### matching_type

```python
@classmethod
def matching_type(cls,
                  json: str,
                  type: SuperAPI_JsonType = SuperAPI_JsonType.OBJECT) -> bool
```

X.matching_type(json, type=SuperAPI_JsonType.OBJECT) -> bool
Matching Type

Args:
    json (str): 
    type (SuperAPI_JsonType): 

Returns:
    bool:

<a id="unreal.SuperAPI_JSONToolsBPLibrary.generation_separator"></a>

#### generation_separator

```python
@classmethod
def generation_separator(cls, field_name_array: Array[str]) -> Optional[str]
```

X.generation_separator(field_name_array) -> str or None
Generation Separator

Args:
    field_name_array (Array[str]): 

Returns:
    str or None: 

    field_name (str):

<a id="unreal.SuperAPI_JSONToolsBPLibrary.delete_field"></a>

#### delete_field

```python
@classmethod
def delete_field(cls, json: str, field_name: str) -> Tuple[bool, str, str]
```

X.delete_field(json, field_name) -> (success=bool, info=str, result=str)
Delete Field

Args:
    json (str): 
    field_name (str): 

Returns:
    tuple: 

    success (bool): 

    info (str): 

    result (str):

<a id="unreal.SuperAPI_JSONToolsBPLibrary.analytical_separator"></a>

#### analytical_separator

```python
@classmethod
def analytical_separator(cls, field_name: str) -> Optional[Array[str]]
```

X.analytical_separator(field_name) -> Array[str] or None
Analytical Separator

Args:
    field_name (str): 

Returns:
    Array[str] or None: 

    field_name_array (Array[str]):

<a id="unreal.EditorUtilityObject"></a>