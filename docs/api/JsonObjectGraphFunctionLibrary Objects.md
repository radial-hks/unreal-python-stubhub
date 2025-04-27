## JsonObjectGraphFunctionLibrary Objects

```python
class JsonObjectGraphFunctionLibrary(BlueprintFunctionLibrary)
```

Json Object Graph Function Library

**C++ Source:**

- **Module**: Kismet
- **File**: JsonObjectGraphFunctionLibrary.h

<a id="unreal.JsonObjectGraphFunctionLibrary.write_package_to_temp_file"></a>

#### write_package_to_temp_file

```python
@classmethod
def write_package_to_temp_file(cls, object: Object, label: str,
                               options: JsonStringifyOptions) -> str
```

X.write_package_to_temp_file(object, label, options) -> str
! EXPERIMENTAL !

Writes all objects in the provided object's package to a temporary file
using the JsonObjectGraph format.

Args:
    object (Object): The object whose package will be written to the file
    label (str): A label to disambiguate the temporary file
    options (JsonStringifyOptions): Options controlling the written format

Returns:
    str: 

    out_filename (str): The filename written, empty if no file written

<a id="unreal.JsonObjectGraphFunctionLibrary.write_blueprint_class_to_temp_file"></a>

#### write_blueprint_class_to_temp_file

```python
@classmethod
def write_blueprint_class_to_temp_file(cls, bp: Blueprint, label: str,
                                       options: JsonStringifyOptions) -> str
```

X.write_blueprint_class_to_temp_file(bp, label, options) -> str
! EXPERIMENTAL !

Writes only the provided blueprint's Class and CDO to a temporary file
using the JsonObjectGraph format. Always excludes editor only data.

Args:
    bp (Blueprint): The blueprint to write to a file
    label (str): A label to disambiguate the temporary file
    options (JsonStringifyOptions): 

Returns:
    str: 

    out_filename (str): The filename written, empty if no file written

<a id="unreal.JsonObjectGraphFunctionLibrary.stringify"></a>

#### stringify

```python
@classmethod
def stringify(cls, root_objects: Array[Object],
              options: JsonStringifyOptions) -> str
```

X.stringify(root_objects, options) -> str
! EXPERIMENTAL !

Writes the provided objects to a string output, using the JsonObjectGraph format. Reachable
nested objects will be included automatically. Objects not within a root should be included in
RootObjects if they want to be deeply represented in the result string

Examples of invocation from python:
 Print an object:
     print( unreal.JsonObjectGraphFunctionLibrary.stringify([object], tuple()) )
 Print a list objects:
     print( unreal.JsonObjectGraphFunctionLibrary.stringify(objects, tuple()) )
 Print an object's entire package:
     print( unreal.JsonObjectGraphFunctionLibrary.stringify([unreal.EditorAssetLibrary.get_package_for_object(object)], tuple()) )

Args:
    root_objects (Array[Object]): The objects to write at the root level
    options (JsonStringifyOptions): Options controlling the written format

Returns:
    str: 

    result_string (str): The objects stringified

<a id="unreal.AssetEditorContextInterface"></a>