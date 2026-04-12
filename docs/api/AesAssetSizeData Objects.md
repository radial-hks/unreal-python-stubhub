## AesAssetSizeData Objects

```python
class AesAssetSizeData(StructBase)
```

资产尺寸数据基类

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds`` (Box3f):  [Read-Write] 资产包围盒大小
- ``custom_bounds`` (bool):  [Read-Write] 资产是否使用自定义包围盒大小
- ``transform`` (Transform3f):  [Read-Write] 资产变换

<a id="unreal.AesAssetSizeData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(transform: Transform3f = [[0.000000, 0.000000, 0.000000],
                                       [-0.000000, 0.000000, 0.000000],
                                       [1.000000, 1.000000, 1.000000]],
             custom_bounds: bool = False,
             bounds: Box3f = []) -> None
```

<a id="unreal.AesAssetSizeData.transform"></a>

#### transform

```python
@property
def transform() -> Transform3f
```

(Transform3f):  [Read-Write] 资产变换

<a id="unreal.AesAssetSizeData.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform3f) -> None
```

<a id="unreal.AesAssetSizeData.custom_bounds"></a>

#### custom\_bounds

```python
@property
def custom_bounds() -> bool
```

(bool):  [Read-Write] 资产是否使用自定义包围盒大小

<a id="unreal.AesAssetSizeData.custom_bounds"></a>

#### custom\_bounds

```python
@custom_bounds.setter
def custom_bounds(value: bool) -> None
```

<a id="unreal.AesAssetSizeData.bounds"></a>

#### bounds

```python
@property
def bounds() -> Box3f
```

(Box3f):  [Read-Write] 资产包围盒大小

<a id="unreal.AesAssetSizeData.bounds"></a>

#### bounds

```python
@bounds.setter
def bounds(value: Box3f) -> None
```

<a id="unreal.AesAssetCollisionData"></a>