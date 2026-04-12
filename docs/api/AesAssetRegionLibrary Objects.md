## AesAssetRegionLibrary Objects

```python
class AesAssetRegionLibrary(StructBase)
```

区域资产库

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_libraries`` (Array[AesAssetLibrary]):  [Read-Write] 区域资产库列表
- ``name`` (Name):  [Read-Write] 区域名称
- ``outlines`` (Array[AesAssetRegionOutline]):  [Read-Write] 区域轮廓线列表
- ``quad_keys`` (Array[Name]):  [Read-Write] 区域所在地块编号列表

<a id="unreal.AesAssetRegionLibrary.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: Name = "None",
             quad_keys: Array[Name] = [],
             outlines: Array[AesAssetRegionOutline] = [],
             asset_libraries: Array[AesAssetLibrary] = []) -> None
```

<a id="unreal.AesAssetRegionLibrary.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] 区域名称

<a id="unreal.AesAssetRegionLibrary.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.AesAssetRegionLibrary.quad_keys"></a>

#### quad\_keys

```python
@property
def quad_keys() -> Array[Name]
```

(Array[Name]):  [Read-Write] 区域所在地块编号列表

<a id="unreal.AesAssetRegionLibrary.quad_keys"></a>

#### quad\_keys

```python
@quad_keys.setter
def quad_keys(value: Array[Name]) -> None
```

<a id="unreal.AesAssetRegionLibrary.outlines"></a>

#### outlines

```python
@property
def outlines() -> Array[AesAssetRegionOutline]
```

(Array[AesAssetRegionOutline]):  [Read-Write] 区域轮廓线列表

<a id="unreal.AesAssetRegionLibrary.outlines"></a>

#### outlines

```python
@outlines.setter
def outlines(value: Array[AesAssetRegionOutline]) -> None
```

<a id="unreal.AesAssetRegionLibrary.asset_libraries"></a>

#### asset\_libraries

```python
@property
def asset_libraries() -> Array[AesAssetLibrary]
```

(Array[AesAssetLibrary]):  [Read-Write] 区域资产库列表

<a id="unreal.AesAssetRegionLibrary.asset_libraries"></a>

#### asset\_libraries

```python
@asset_libraries.setter
def asset_libraries(value: Array[AesAssetLibrary]) -> None
```

<a id="unreal.AesClusterAssetData"></a>