## AssetData Objects

```python
class AssetData(StructBase)
```

A struct to hold important information about an assets found by the Asset Registry
This struct is transient and should never be serialized

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_class`` (Name):  [Read-Write] The name of the asset's class
  deprecated: Short asset class name must be converted to full asset pathname. Use AssetClassPath instead.
- ``asset_class_path`` (TopLevelAssetPath):  [Read-Write] The path name of the asset's class
- ``asset_name`` (Name):  [Read-Write] The name of the asset without the package
- ``package_name`` (Name):  [Read-Write] The name of the package in which the asset is found, this is the full long package name such as /Game/Path/Package
- ``package_path`` (Name):  [Read-Write] The path to the package in which the asset is found, this is /Game/Path with the Package stripped off

<a id="unreal.AssetData.__init__"></a>

#### __init__

```python
def __init__(package_name: Name = "None",
             package_path: Name = "None",
             asset_name: Name = "None",
             asset_class_path: TopLevelAssetPath = [""]) -> None
```

<a id="unreal.AssetData.package_name"></a>

#### package_name

```python
@property
def package_name() -> Name
```

(Name):  [Read-Only] The name of the package in which the asset is found, this is the full long package name such as /Game/Path/Package

<a id="unreal.AssetData.package_path"></a>

#### package_path

```python
@property
def package_path() -> Name
```

(Name):  [Read-Only] The path to the package in which the asset is found, this is /Game/Path with the Package stripped off

<a id="unreal.AssetData.asset_name"></a>

#### asset_name

```python
@property
def asset_name() -> Name
```

(Name):  [Read-Only] The name of the asset without the package

<a id="unreal.AssetData.asset_class"></a>

#### asset_class

```python
@property
def asset_class() -> Name
```

(Name):  [Read-Only] The name of the asset's class
deprecated: Short asset class name must be converted to full asset pathname. Use AssetClassPath instead.

<a id="unreal.AssetData.asset_class_path"></a>

#### asset_class_path

```python
@property
def asset_class_path() -> TopLevelAssetPath
```

(TopLevelAssetPath):  [Read-Only] The path name of the asset's class

<a id="unreal.AssetData.to_soft_object_path"></a>

#### to_soft_object_path

```python
def to_soft_object_path() -> SoftObjectPath
```

x.to_soft_object_path() -> SoftObjectPath
Convert to a SoftObjectPath for loading

Returns:
    SoftObjectPath:

<a id="unreal.AssetData.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool
Checks to see if this AssetData refers to an asset or is NULL

Returns:
    bool:

<a id="unreal.AssetData.is_u_asset"></a>

#### is_u_asset

```python
def is_u_asset() -> bool
```

x.is_u_asset() -> bool
Returns true if this is the primary asset in a package, true for maps and assets but false for secondary objects like class redirectors

Returns:
    bool:

<a id="unreal.AssetData.is_redirector"></a>

#### is_redirector

```python
def is_redirector() -> bool
```

x.is_redirector() -> bool
Returns true if the this asset is a redirector.

Returns:
    bool:

<a id="unreal.AssetData.is_asset_loaded"></a>

#### is_asset_loaded

```python
def is_asset_loaded() -> bool
```

x.is_asset_loaded() -> bool
Returns true if the asset is loaded

Returns:
    bool:

<a id="unreal.AssetData.get_tag_value"></a>

#### get_tag_value

```python
def get_tag_value(tag_name: Name) -> Optional[str]
```

x.get_tag_value(tag_name) -> str or None
Gets the value associated with the given tag as a string

Args:
    tag_name (Name): 

Returns:
    str or None: 

    out_tag_value (str):

<a id="unreal.AssetData.get_full_name"></a>

#### get_full_name

```python
def get_full_name() -> str
```

x.get_full_name() -> str
Returns the full name for the asset in the form: Class ObjectPath

Returns:
    str:

<a id="unreal.AssetData.get_export_text_name"></a>

#### get_export_text_name

```python
def get_export_text_name() -> str
```

x.get_export_text_name() -> str
Returns the name for the asset in the form: Class'ObjectPath'

Returns:
    str:

<a id="unreal.AssetData.get_class"></a>

#### get_class

```python
def get_class() -> Class
```

x.get_class() -> type(Class)
Get Class

Returns:
    type(Class):

<a id="unreal.AssetData.get_asset"></a>

#### get_asset

```python
def get_asset() -> Object
```

x.get_asset() -> Object
Returns the asset UObject if it is loaded or loads the asset if it is unloaded then returns the result

Returns:
    Object:

<a id="unreal.AssetData.find_asset_native_class"></a>

#### find_asset_native_class

```python
def find_asset_native_class() -> Class
```

x.find_asset_native_class() -> type(Class)
Returns the first native class of the asset type that can be found.  Normally this is just the FAssetData::GetClass(),
however if the class is a blueprint generated class it may not be loaded.  In which case GetAncestorClassNames will
be used to find the first native super class.  This can be slow if temporary caching mode is not on.

Returns:
    type(Class):

<a id="unreal.Guid"></a>