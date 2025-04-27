## AssetRenameData Objects

```python
class AssetRenameData(StructBase)
```

Asset Rename Data

**C++ Source:**

- **Module**: AssetTools
- **File**: IAssetTools.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset`` (Object):  [Read-Write] Object being renamed
- ``new_name`` (str):  [Read-Write] New package and asset name, new object path will be PackagePath/NewName.NewName
- ``new_package_path`` (str):  [Read-Write] New path to package without package name, ie /Game/SubDirectory

<a id="unreal.AssetRenameData.__init__"></a>

#### __init__

```python
def __init__(asset: Object = None,
             new_package_path: str = "",
             new_name: str = "") -> None
```

<a id="unreal.AssetRenameData.asset"></a>

#### asset

```python
@property
def asset() -> Object
```

(Object):  [Read-Write] Object being renamed

<a id="unreal.AssetRenameData.asset"></a>

#### asset

```python
@asset.setter
def asset(value: Object) -> None
```

<a id="unreal.AssetRenameData.new_package_path"></a>

#### new_package_path

```python
@property
def new_package_path() -> str
```

(str):  [Read-Write] New path to package without package name, ie /Game/SubDirectory

<a id="unreal.AssetRenameData.new_package_path"></a>

#### new_package_path

```python
@new_package_path.setter
def new_package_path(value: str) -> None
```

<a id="unreal.AssetRenameData.new_name"></a>

#### new_name

```python
@property
def new_name() -> str
```

(str):  [Read-Write] New package and asset name, new object path will be PackagePath/NewName.NewName

<a id="unreal.AssetRenameData.new_name"></a>

#### new_name

```python
@new_name.setter
def new_name(value: str) -> None
```

<a id="unreal.AudioOutputDeviceInfo"></a>