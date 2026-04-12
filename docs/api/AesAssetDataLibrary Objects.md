## AesAssetDataLibrary Objects

```python
class AesAssetDataLibrary(TableRowBase)
```

资产数据库基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_table`` (SoftObjectPath):  [Read-Write]
- ``type`` (AesAssetType):  [Read-Write] 资产类型

<a id="unreal.AesAssetDataLibrary.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: AesAssetType = AesAssetType.OBJECT,
             data_table: SoftObjectPath = [""]) -> None
```

<a id="unreal.AesAssetDataLibrary.type"></a>

#### type

```python
@property
def type() -> AesAssetType
```

(AesAssetType):  [Read-Only] 资产类型

<a id="unreal.AesAssetDataLibrary.data_table"></a>

#### data\_table

```python
@property
def data_table() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write]

<a id="unreal.AesAssetDataLibrary.data_table"></a>

#### data\_table

```python
@data_table.setter
def data_table(value: SoftObjectPath) -> None
```

<a id="unreal.AesMeshData"></a>