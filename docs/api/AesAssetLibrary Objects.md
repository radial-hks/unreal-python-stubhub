## AesAssetLibrary Objects

```python
class AesAssetLibrary(StructBase)
```

资产库数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``library_path`` (SoftObjectPath):  [Read-Write] 资产库路径
- ``name`` (Name):  [Read-Write] 资产库名称
- ``tags`` (Map[Name, Name]):  [Read-Write] 资产库标签
- ``type`` (AesAssetType):  [Read-Write] 资产库类型
- ``weight`` (float):  [Read-Write] 资产库权重

<a id="unreal.AesAssetLibrary.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: Name = "None",
             type: AesAssetType = AesAssetType.OBJECT,
             library_path: SoftObjectPath = [""],
             tags: Map[Name, Name] = {},
             weight: float = 0.000000) -> None
```

<a id="unreal.AesAssetLibrary.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] 资产库名称

<a id="unreal.AesAssetLibrary.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.AesAssetLibrary.type"></a>

#### type

```python
@property
def type() -> AesAssetType
```

(AesAssetType):  [Read-Only] 资产库类型

<a id="unreal.AesAssetLibrary.library_path"></a>

#### library\_path

```python
@property
def library_path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 资产库路径

<a id="unreal.AesAssetLibrary.library_path"></a>

#### library\_path

```python
@library_path.setter
def library_path(value: SoftObjectPath) -> None
```

<a id="unreal.AesAssetLibrary.tags"></a>

#### tags

```python
@property
def tags() -> Map[Name, Name]
```

(Map[Name, Name]):  [Read-Only] 资产库标签

<a id="unreal.AesAssetLibrary.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] 资产库权重

<a id="unreal.AesAssetLibrary.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.AesAssetRegionOutline"></a>