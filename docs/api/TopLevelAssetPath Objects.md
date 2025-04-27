## TopLevelAssetPath Objects

```python
class TopLevelAssetPath(StructBase)
```

A struct that can reference a top level asset such as '/Path/To/Package.AssetName'
note: The full C++ class is located here: Engine\Source\Runtime\CoreUObject\Public\UObject\TopLevelAssetPath.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_name`` (Name):  [Read-Write] Name of the asset within the package e.g. 'AssetName'
- ``package_name`` (Name):  [Read-Write] Name of the package containing the asset e.g. /Path/To/Package

<a id="unreal.TopLevelAssetPath.__init__"></a>

#### __init__

```python
def __init__(package_name: str = "", asset_name: str = "") -> None
```

<a id="unreal.TopLevelAssetPath.package_name"></a>

#### package_name

```python
@property
def package_name() -> Name
```

(Name):  [Read-Write] Name of the package containing the asset e.g. /Path/To/Package

<a id="unreal.TopLevelAssetPath.package_name"></a>

#### package_name

```python
@package_name.setter
def package_name(value: Name) -> None
```

<a id="unreal.TopLevelAssetPath.asset_name"></a>

#### asset_name

```python
@property
def asset_name() -> Name
```

(Name):  [Read-Write] Name of the asset within the package e.g. 'AssetName'

<a id="unreal.TopLevelAssetPath.asset_name"></a>

#### asset_name

```python
@asset_name.setter
def asset_name(value: Name) -> None
```

<a id="unreal.SoftObjectPath"></a>