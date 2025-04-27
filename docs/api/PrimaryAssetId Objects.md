## PrimaryAssetId Objects

```python
class PrimaryAssetId(StructBase)
```

This identifies an object as a "primary" asset that can be searched for by the AssetManager and used in various tools
note: The full C++ class is located here: Engine\Source\Runtime\CoreUObject\Public\UObject\PrimaryAssetId.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``primary_asset_name`` (Name):  [Read-Write] The Name of this object, by default its short name
- ``primary_asset_type`` (PrimaryAssetType):  [Read-Write] The Type of this object, by default its base class's name

<a id="unreal.PrimaryAssetId.__init__"></a>

#### __init__

```python
def __init__(primary_asset_type: PrimaryAssetType = ["None"],
             primary_asset_name: Name = "None") -> None
```

<a id="unreal.PrimaryAssetId.primary_asset_type"></a>

#### primary_asset_type

```python
@property
def primary_asset_type() -> PrimaryAssetType
```

(PrimaryAssetType):  [Read-Write] The Type of this object, by default its base class's name

<a id="unreal.PrimaryAssetId.primary_asset_type"></a>

#### primary_asset_type

```python
@primary_asset_type.setter
def primary_asset_type(value: PrimaryAssetType) -> None
```

<a id="unreal.PrimaryAssetId.primary_asset_name"></a>

#### primary_asset_name

```python
@property
def primary_asset_name() -> Name
```

(Name):  [Read-Write] The Name of this object, by default its short name

<a id="unreal.PrimaryAssetId.primary_asset_name"></a>

#### primary_asset_name

```python
@primary_asset_name.setter
def primary_asset_name(value: Name) -> None
```

<a id="unreal.PrimaryAssetId.unload"></a>

#### unload

```python
def unload() -> None
```

x.unload() -> None
Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

<a id="unreal.PrimaryAssetId.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Returns true if the Primary Asset Id is valid

Returns:
    bool:

<a id="unreal.PrimaryAssetId.get_soft_object_reference"></a>

#### get_soft_object_reference

```python
def get_soft_object_reference() -> Object
```

x.get_soft_object_reference() -> Object
Returns the Object Id associated with a Primary Asset Id, this works even if the asset is not loaded

Returns:
    Object:

<a id="unreal.PrimaryAssetId.get_soft_class_reference"></a>

#### get_soft_class_reference

```python
def get_soft_class_reference() -> Class
```

x.get_soft_class_reference() -> Class
Returns the Blueprint Class Id associated with a Primary Asset Id, this works even if the asset is not loaded

Returns:
    Class:

<a id="unreal.PrimaryAssetId.get_object"></a>

#### get_object

```python
def get_object() -> Object
```

x.get_object() -> Object
Returns the Object associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

Returns:
    Object:

<a id="unreal.PrimaryAssetId.get_current_bundle_state"></a>

#### get_current_bundle_state

```python
def get_current_bundle_state(
        force_current_state: bool) -> Optional[Array[Name]]
```

x.get_current_bundle_state(force_current_state) -> Array[Name] or None
Returns the list of loaded bundles for a given Primary Asset. This will return false if the asset is not loaded at all.
If ForceCurrentState is true it will return the current state even if a load is in process

Args:
    force_current_state (bool): 

Returns:
    Array[Name] or None: 

    out_bundles (Array[Name]):

<a id="unreal.PrimaryAssetId.get_class"></a>

#### get_class

```python
def get_class() -> Class
```

x.get_class() -> type(Class)
Returns the Blueprint Class associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

Returns:
    type(Class):

<a id="unreal.PrimaryAssetId.to_string"></a>

#### to_string

```python
def to_string() -> str
```

x.to_string() -> str
Converts a Primary Asset Id to a string. The other direction is not provided because it cannot be validated

Returns:
    str:

<a id="unreal.PrimaryAssetId.__bool__"></a>

#### __bool__

```python
def __bool__() -> bool
```

Returns true if the Primary Asset Id is valid

<a id="unreal.PrimaryAssetId.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``PrimaryAssetId`` Returns true if the values are equal (A == B)

<a id="unreal.PrimaryAssetId.__ne__"></a>

#### __ne__

```python
def __ne__(other: object) -> bool
```

**Overloads:**

- ``PrimaryAssetId`` Returns true if the values are not equal (A != B)

<a id="unreal.PrimaryAssetType"></a>