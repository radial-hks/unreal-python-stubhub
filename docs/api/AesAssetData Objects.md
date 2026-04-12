## AesAssetData Objects

```python
class AesAssetData(TableRowBase)
```

资产数据基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 自定义子资产引用列表
- ``collision_data`` (AesAssetCollisionData):  [Read-Write] 资产碰撞数据
- ``meta_data`` (AesAssetMetaData):  [Read-Write] 资产元数据
- ``size_data`` (AesAssetSizeData):  [Read-Write] 资产尺寸数据

<a id="unreal.AesAssetData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(meta_data: AesAssetMetaData = [
    "None", 0, 0, "None", False, {}, "", [""]
],
             size_data: AesAssetSizeData = [[[0.000000, 0.000000, 0.000000],
                                             [-0.000000, 0.000000, 0.000000],
                                             [1.000000, 1.000000, 1.000000]],
                                            False, []],
             collision_data: AesAssetCollisionData = [
                 AesAssetCollisionType.NONE,
                 ["/Script/AesRenderResource.AesCollisionComponent"]
             ],
             child_assets: Array[AesAssetChildMetaData] = []) -> None
```

<a id="unreal.AesAssetData.meta_data"></a>

#### meta\_data

```python
@property
def meta_data() -> AesAssetMetaData
```

(AesAssetMetaData):  [Read-Write] 资产元数据

<a id="unreal.AesAssetData.meta_data"></a>

#### meta\_data

```python
@meta_data.setter
def meta_data(value: AesAssetMetaData) -> None
```

<a id="unreal.AesAssetData.size_data"></a>

#### size\_data

```python
@property
def size_data() -> AesAssetSizeData
```

(AesAssetSizeData):  [Read-Write] 资产尺寸数据

<a id="unreal.AesAssetData.size_data"></a>

#### size\_data

```python
@size_data.setter
def size_data(value: AesAssetSizeData) -> None
```

<a id="unreal.AesAssetData.collision_data"></a>

#### collision\_data

```python
@property
def collision_data() -> AesAssetCollisionData
```

(AesAssetCollisionData):  [Read-Write] 资产碰撞数据

<a id="unreal.AesAssetData.collision_data"></a>

#### collision\_data

```python
@collision_data.setter
def collision_data(value: AesAssetCollisionData) -> None
```

<a id="unreal.AesAssetData.child_assets"></a>

#### child\_assets

```python
@property
def child_assets() -> Array[AesAssetChildMetaData]
```

(Array[AesAssetChildMetaData]):  [Read-Write] 自定义子资产引用列表

<a id="unreal.AesAssetData.child_assets"></a>

#### child\_assets

```python
@child_assets.setter
def child_assets(value: Array[AesAssetChildMetaData]) -> None
```

<a id="unreal.AesAssetDataLibrary"></a>