## UrbanStaticMeshBlueprintLibrary Objects

```python
class UrbanStaticMeshBlueprintLibrary(BlueprintFunctionLibrary)
```

Urban Static Mesh Blueprint Library

**C++ Source:**

- **Plugin**: AesBuilder
- **Module**: UrbanEntityBuilder
- **File**: UrbanStaticMeshBlueprintLibrary.h

<a id="unreal.UrbanStaticMeshBlueprintLibrary.set_static_mesh_asset_user_data_material_simplification_for_key"></a>

#### set\_static\_mesh\_asset\_user\_data\_material\_simplification\_for\_key

```python
@classmethod
def set_static_mesh_asset_user_data_material_simplification_for_key(
        cls, object: Object, key: SoftObjectPath, value: str) -> bool
```

X.set_static_mesh_asset_user_data_material_simplification_for_key(object, key, value) -> bool
Set Static Mesh Asset User Data Material Simplification for Key

Args:
    object (Object): 
    key (SoftObjectPath): 
    value (str): 

Returns:
    bool:

<a id="unreal.UrbanStaticMeshBlueprintLibrary.set_static_mesh_asset_user_data_material_color_for_key"></a>

#### set\_static\_mesh\_asset\_user\_data\_material\_color\_for\_key

```python
@classmethod
def set_static_mesh_asset_user_data_material_color_for_key(
        cls, object: Object, key: SoftObjectPath, value: LinearColor) -> bool
```

X.set_static_mesh_asset_user_data_material_color_for_key(object, key, value) -> bool
Set Static Mesh Asset User Data Material Color for Key

Args:
    object (Object): 
    key (SoftObjectPath): 
    value (LinearColor): 

Returns:
    bool:

<a id="unreal.UrbanStaticMeshBlueprintLibrary.get_static_mesh_user_data_material_simplification_for_key"></a>

#### get\_static\_mesh\_user\_data\_material\_simplification\_for\_key

```python
@classmethod
def get_static_mesh_user_data_material_simplification_for_key(
        cls, object: Object, key: SoftObjectPath) -> str
```

X.get_static_mesh_user_data_material_simplification_for_key(object, key) -> str
Get the value of the given key for material simplification in the Urban Static Mesh User Data of the given object.

Args:
    object (Object): The Object from which to retrieve the Datasmith User Data.
    key (SoftObjectPath): The key to find in the Datasmith User Data.

Returns:
    str: The string value associated with the given key

<a id="unreal.UrbanStaticMeshBlueprintLibrary.get_static_mesh_user_data_material_color_for_key"></a>

#### get\_static\_mesh\_user\_data\_material\_color\_for\_key

```python
@classmethod
def get_static_mesh_user_data_material_color_for_key(
        cls, object: Object, key: SoftObjectPath) -> LinearColor
```

X.get_static_mesh_user_data_material_color_for_key(object, key) -> LinearColor
Get the value of the given key for material color in the Urban Static Mesh User Data of the given object.

Args:
    object (Object): The Object from which to retrieve the Datasmith User Data.
    key (SoftObjectPath): The key to find in the Datasmith User Data.

Returns:
    LinearColor: The string value associated with the given key

<a id="unreal.UrbanStaticMeshBlueprintLibrary.get_static_mesh_user_data_keys_and_values_for_value"></a>

#### get\_static\_mesh\_user\_data\_keys\_and\_values\_for\_value

```python
@classmethod
def get_static_mesh_user_data_keys_and_values_for_value(
    cls, object: Object, color_to_match: LinearColor
) -> Tuple[Array[SoftObjectPath], Array[LinearColor]]
```

X.get_static_mesh_user_data_keys_and_values_for_value(object, color_to_match) -> (out_keys=Array[SoftObjectPath], out_values=Array[LinearColor])
Get the keys and values for which the associated value contains the string to match for the Urban Static Mesh User Data of the given object.

Args:
    object (Object): The Object from which to retrieve the Datasmith User Data.
    color_to_match (LinearColor): 

Returns:
    tuple: 

    out_keys (Array[SoftObjectPath]): Output array of keys for which the associated values contain the string to match.

    out_values (Array[LinearColor]): Output array of values associated to the keys.

<a id="unreal.UrbanStaticMeshBlueprintLibrary.get_static_mesh_user_data"></a>

#### get\_static\_mesh\_user\_data

```python
@classmethod
def get_static_mesh_user_data(cls,
                              object: Object) -> UrbanStaticMeshAssetUserData
```

X.get_static_mesh_user_data(object) -> UrbanStaticMeshAssetUserData
Get the Urban Static Mesh User Data of a given object

Args:
    object (Object): The Object from which to retrieve the Datasmith User Data.

Returns:
    UrbanStaticMeshAssetUserData: The Datasmith User Data if it exists; nullptr, otherwise

<a id="unreal.UrbanStaticMeshBlueprintLibrary.get_all_static_mesh_user_data"></a>

#### get\_all\_static\_mesh\_user\_data

```python
@classmethod
def get_all_static_mesh_user_data(
        cls, object_class: Class) -> Array[UrbanStaticMeshAssetUserData]
```

X.get_all_static_mesh_user_data(object_class) -> Array[UrbanStaticMeshAssetUserData]
Find all Urban Static Mesh User Data of loaded objects of the given type.
This is a slow operation, so editor only.

Args:
    object_class (type(Class)): Class of the object on which to filter, if specificed; otherwise there's no filtering

Returns:
    Array[UrbanStaticMeshAssetUserData]: 

    out_user_data (Array[UrbanStaticMeshAssetUserData]): Output array of Datasmith User Data.

<a id="unreal.UrbanEntityEditorScene"></a>