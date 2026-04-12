## AesAssetMetaData Objects

```python
class AesAssetMetaData(StructBase)
```

资产元数据基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id`` (int64):  [Read-Only] 资产Id
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 资产LOD设置，针对不同的资产最大LOD级别X，需设置资产在LOD级别Y使用，若为空，则资产在每一个LOD级别都使用
- ``name`` (Name):  [Read-Write] 资产名称
- ``source`` (Name):  [Read-Only] 资产库来源
- ``static_asset`` (bool):  [Read-Write] 是否为静态资产
- ``thumbnail`` (SoftObjectPath):  [Read-Write] 资产缩略图
- ``tips`` (str):  [Read-Write] 资产说明
- ``type`` (AesAssetType):  [Read-Only] 资产类型

<a id="unreal.AesAssetMetaData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: Name = "None",
             type: AesAssetType = AesAssetType.OBJECT,
             id: int = 0,
             source: Name = "None",
             static_asset: bool = False,
             lod_config: Map[int, int] = {},
             tips: str = "",
             thumbnail: SoftObjectPath = [""]) -> None
```

<a id="unreal.AesAssetMetaData.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] 资产名称

<a id="unreal.AesAssetMetaData.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.AesAssetMetaData.type"></a>

#### type

```python
@property
def type() -> AesAssetType
```

(AesAssetType):  [Read-Only] 资产类型

<a id="unreal.AesAssetMetaData.id"></a>

#### id

```python
@property
def id() -> int
```

(int64):  [Read-Only] 资产Id

<a id="unreal.AesAssetMetaData.source"></a>

#### source

```python
@property
def source() -> Name
```

(Name):  [Read-Only] 资产库来源

<a id="unreal.AesAssetMetaData.static_asset"></a>

#### static\_asset

```python
@property
def static_asset() -> bool
```

(bool):  [Read-Write] 是否为静态资产

<a id="unreal.AesAssetMetaData.static_asset"></a>

#### static\_asset

```python
@static_asset.setter
def static_asset(value: bool) -> None
```

<a id="unreal.AesAssetMetaData.lod_config"></a>

#### lod\_config

```python
@property
def lod_config() -> Map[int, int]
```

(Map[int32, int32]):  [Read-Write] 资产LOD设置，针对不同的资产最大LOD级别X，需设置资产在LOD级别Y使用，若为空，则资产在每一个LOD级别都使用

<a id="unreal.AesAssetMetaData.lod_config"></a>

#### lod\_config

```python
@lod_config.setter
def lod_config(value: Map[int, int]) -> None
```

<a id="unreal.AesAssetMetaData.tips"></a>

#### tips

```python
@property
def tips() -> str
```

(str):  [Read-Write] 资产说明

<a id="unreal.AesAssetMetaData.tips"></a>

#### tips

```python
@tips.setter
def tips(value: str) -> None
```

<a id="unreal.AesAssetMetaData.thumbnail"></a>

#### thumbnail

```python
@property
def thumbnail() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 资产缩略图

<a id="unreal.AesAssetMetaData.thumbnail"></a>

#### thumbnail

```python
@thumbnail.setter
def thumbnail(value: SoftObjectPath) -> None
```

<a id="unreal.AesAssetSizeData"></a>