## DatasmithContentLibrary Objects

```python
class DatasmithContentLibrary(BlueprintFunctionLibrary)
```

Datasmith Content Blueprint Library

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithContentBlueprintLibrary.h

<a id="unreal.DatasmithContentLibrary.get_datasmith_user_data_values_for_key"></a>

#### get_datasmith_user_data_values_for_key

```python
@classmethod
def get_datasmith_user_data_values_for_key(
        cls,
        object: Object,
        key: Name,
        partial_match_key: bool = False) -> Array[str]
```

X.get_datasmith_user_data_values_for_key(object, key, partial_match_key=False) -> Array[str]
Get the values of the given key for the Datasmith User Data of the given object.

Args:
    object (Object): The Object from which to retrieve the Datasmith User Data.
    key (Name): The key to find in the Datasmith User Data.
    partial_match_key (bool): If true, check for contains, rather than exact match.

Returns:
    Array[str]: The string value associated with the given key

<a id="unreal.DatasmithContentLibrary.get_datasmith_user_data_value_for_key"></a>

#### get_datasmith_user_data_value_for_key

```python
@classmethod
def get_datasmith_user_data_value_for_key(
        cls,
        object: Object,
        key: Name,
        partial_match_key: bool = False) -> str
```

X.get_datasmith_user_data_value_for_key(object, key, partial_match_key=False) -> str
Get the value of the given key for the Datasmith User Data of the given object.

Args:
    object (Object): The Object from which to retrieve the Datasmith User Data.
    key (Name): The key to find in the Datasmith User Data.
    partial_match_key (bool): 

Returns:
    str: The string value associated with the given key

<a id="unreal.DatasmithContentLibrary.get_datasmith_user_data_keys_and_values_for_value"></a>

#### get_datasmith_user_data_keys_and_values_for_value

```python
@classmethod
def get_datasmith_user_data_keys_and_values_for_value(
        cls, object: Object,
        string_to_match: str) -> Tuple[Array[Name], Array[str]]
```

X.get_datasmith_user_data_keys_and_values_for_value(object, string_to_match) -> (out_keys=Array[Name], out_values=Array[str])
Get the keys and values for which the associated value contains the string to match for the Datasmith User Data of the given object.

Args:
    object (Object): The Object from which to retrieve the Datasmith User Data.
    string_to_match (str): The string to match in the values.

Returns:
    tuple: 

    out_keys (Array[Name]): Output array of keys for which the associated values contain the string to match.

    out_values (Array[str]): Output array of values associated to the keys.

<a id="unreal.DatasmithContentLibrary.get_datasmith_user_data"></a>

#### get_datasmith_user_data

```python
@classmethod
def get_datasmith_user_data(cls, object: Object) -> DatasmithUserData
```

X.get_datasmith_user_data(object) -> DatasmithUserData
Get the Datasmith User Data of a given object

Args:
    object (Object): The Object from which to retrieve the Datasmith User Data.

Returns:
    DatasmithUserData: The Datasmith User Data if it exists; nullptr, otherwise

<a id="unreal.DatasmithContentLibrary.get_all_objects_and_values_for_key"></a>

#### get_all_objects_and_values_for_key

```python
@classmethod
def get_all_objects_and_values_for_key(
        cls, key: Name,
        object_class: Class) -> Tuple[Array[Object], Array[str]]
```

X.get_all_objects_and_values_for_key(key, object_class) -> (out_objects=Array[Object], out_values=Array[str])
Find all loaded objects of the given type that have a Datasmith User Data that contains the given key and their associated values.
This is a slow operation, so editor only.

Args:
    key (Name): The key to find in the Datasmith User Data.
    object_class (type(Class)): Class of the object on which to filter, if specificed; otherwise there's no filtering

Returns:
    tuple: 

    out_objects (Array[Object]): Output array of objects for which the Datasmith User Data match the given key.

    out_values (Array[str]): Output array of values associated with each object in OutObjects.

<a id="unreal.DatasmithContentLibrary.get_all_datasmith_user_data"></a>

#### get_all_datasmith_user_data

```python
@classmethod
def get_all_datasmith_user_data(
        cls, object_class: Class) -> Array[DatasmithUserData]
```

X.get_all_datasmith_user_data(object_class) -> Array[DatasmithUserData]
Find all Datasmith User Data of loaded objects of the given type.
This is a slow operation, so editor only.

Args:
    object_class (type(Class)): Class of the object on which to filter, if specificed; otherwise there's no filtering

Returns:
    Array[DatasmithUserData]: 

    out_user_data (Array[DatasmithUserData]): Output array of Datasmith User Data.

<a id="unreal.DatasmithImportedSequencesActor"></a>