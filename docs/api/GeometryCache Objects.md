## GeometryCache Objects

```python
class GeometryCache(Object)
```

A Geometry Cache is a piece/set of geometry that consists of individual Mesh/Transformation samples.
In contrast with Static Meshes they can have their vertices animated in certain ways. *

**C++ Source:**

- **Plugin**: GeometryCache
- **Module**: GeometryCache
- **File**: GeometryCache.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only] Importing data and options used for this Geometry cache object
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``end_frame`` (int32):  [Read-Write]
- ``material_slot_names`` (Array[Name]):  [Read-Write]
- ``materials`` (Array[MaterialInterface]):  [Read-Write]
- ``start_frame`` (int32):  [Read-Write]
- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering
- ``tracks`` (Array[GeometryCacheTrack]):  [Read-Only] GeometryCache track defining the samples/geometry data for this GeomCache instance

<a id="unreal.GeometryCache.materials"></a>

#### materials

```python
@property
def materials() -> Array[MaterialInterface]
```

(Array[MaterialInterface]):  [Read-Write]

<a id="unreal.GeometryCache.materials"></a>

#### materials

```python
@materials.setter
def materials(value: Array[MaterialInterface]) -> None
```

<a id="unreal.GeometryCache.material_slot_names"></a>

#### material_slot_names

```python
@property
def material_slot_names() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.GeometryCache.material_slot_names"></a>

#### material_slot_names

```python
@material_slot_names.setter
def material_slot_names(value: Array[Name]) -> None
```

<a id="unreal.GeometryCache.start_frame"></a>

#### start_frame

```python
@property
def start_frame() -> int
```

(int32):  [Read-Only]

<a id="unreal.GeometryCache.end_frame"></a>

#### end_frame

```python
@property
def end_frame() -> int
```

(int32):  [Read-Only]

<a id="unreal.GeometryCache.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.GeometryCache.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.GeometryCache.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.GeometryCacheActor"></a>