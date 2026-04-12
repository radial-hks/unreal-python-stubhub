## AesAssetChildMetaData Objects

```python
class AesAssetChildMetaData(StructBase)
```

子资产元数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesAssetCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control_type`` (AesAssetTransformControlType):  [Read-Write] 子资产控制类型
- ``height`` (float):  [Read-Write] 子资产高度
- ``length`` (float):  [Read-Write] 子资产长度
- ``meta_data`` (AesAssetMetaData):  [Read-Write] 子资产元数据
- ``position`` (Vector3f):  [Read-Write] 子资产坐标偏移
- ``random_list`` (Array[SoftObjectPath]):  [Read-Write] 子资产随机列表，用于猜测流程和子资产元数据为空时
- ``rotation`` (Rotator3f):  [Read-Write] 子资产旋转
- ``scale`` (Vector3f):  [Read-Write] 子资产缩放
- ``tags`` (Array[Name]):  [Read-Write] 子资产自定义标签
- ``transform`` (Transform3f):  [Read-Write] 子资产变换
- ``use_bounds`` (bool):  [Read-Write] 是否启用子资产包围盒
- ``use_parent_curves_data`` (bool):  [Read-Write] 是否使用父资产的样条线数据
- ``width`` (float):  [Read-Write] 子资产宽度

<a id="unreal.AesAssetChildMetaData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(meta_data: AesAssetMetaData = [
    "None", 0, 0, "None", False, {}, "", [""]
],
             use_bounds: bool = False,
             use_parent_curves_data: bool = False,
             control_type:
             AesAssetTransformControlType = AesAssetTransformControlType.SCALE,
             length: float = 0.000000,
             width: float = 0.000000,
             height: float = 0.000000,
             scale: Vector3f = [0.000000, 0.000000, 0.000000],
             position: Vector3f = [0.000000, 0.000000, 0.000000],
             rotation: Rotator3f = [0.000000, 0.000000, 0.000000],
             transform: Transform3f = [[0.000000, 0.000000, 0.000000],
                                       [-0.000000, 0.000000, 0.000000],
                                       [1.000000, 1.000000, 1.000000]],
             random_list: Array[SoftObjectPath] = [],
             tags: Array[Name] = []) -> None
```

<a id="unreal.AesAssetChildMetaData.meta_data"></a>

#### meta\_data

```python
@property
def meta_data() -> AesAssetMetaData
```

(AesAssetMetaData):  [Read-Write] 子资产元数据

<a id="unreal.AesAssetChildMetaData.meta_data"></a>

#### meta\_data

```python
@meta_data.setter
def meta_data(value: AesAssetMetaData) -> None
```

<a id="unreal.AesAssetChildMetaData.use_bounds"></a>

#### use\_bounds

```python
@property
def use_bounds() -> bool
```

(bool):  [Read-Write] 是否启用子资产包围盒

<a id="unreal.AesAssetChildMetaData.use_bounds"></a>

#### use\_bounds

```python
@use_bounds.setter
def use_bounds(value: bool) -> None
```

<a id="unreal.AesAssetChildMetaData.use_parent_curves_data"></a>

#### use\_parent\_curves\_data

```python
@property
def use_parent_curves_data() -> bool
```

(bool):  [Read-Write] 是否使用父资产的样条线数据

<a id="unreal.AesAssetChildMetaData.use_parent_curves_data"></a>

#### use\_parent\_curves\_data

```python
@use_parent_curves_data.setter
def use_parent_curves_data(value: bool) -> None
```

<a id="unreal.AesAssetChildMetaData.control_type"></a>

#### control\_type

```python
@property
def control_type() -> AesAssetTransformControlType
```

(AesAssetTransformControlType):  [Read-Write] 子资产控制类型

<a id="unreal.AesAssetChildMetaData.control_type"></a>

#### control\_type

```python
@control_type.setter
def control_type(value: AesAssetTransformControlType) -> None
```

<a id="unreal.AesAssetChildMetaData.length"></a>

#### length

```python
@property
def length() -> float
```

(float):  [Read-Write] 子资产长度

<a id="unreal.AesAssetChildMetaData.length"></a>

#### length

```python
@length.setter
def length(value: float) -> None
```

<a id="unreal.AesAssetChildMetaData.width"></a>

#### width

```python
@property
def width() -> float
```

(float):  [Read-Write] 子资产宽度

<a id="unreal.AesAssetChildMetaData.width"></a>

#### width

```python
@width.setter
def width(value: float) -> None
```

<a id="unreal.AesAssetChildMetaData.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 子资产高度

<a id="unreal.AesAssetChildMetaData.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesAssetChildMetaData.scale"></a>

#### scale

```python
@property
def scale() -> Vector3f
```

(Vector3f):  [Read-Write] 子资产缩放

<a id="unreal.AesAssetChildMetaData.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector3f) -> None
```

<a id="unreal.AesAssetChildMetaData.position"></a>

#### position

```python
@property
def position() -> Vector3f
```

(Vector3f):  [Read-Write] 子资产坐标偏移

<a id="unreal.AesAssetChildMetaData.position"></a>

#### position

```python
@position.setter
def position(value: Vector3f) -> None
```

<a id="unreal.AesAssetChildMetaData.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator3f
```

(Rotator3f):  [Read-Write] 子资产旋转

<a id="unreal.AesAssetChildMetaData.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator3f) -> None
```

<a id="unreal.AesAssetChildMetaData.transform"></a>

#### transform

```python
@property
def transform() -> Transform3f
```

(Transform3f):  [Read-Write] 子资产变换

<a id="unreal.AesAssetChildMetaData.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform3f) -> None
```

<a id="unreal.AesAssetChildMetaData.random_list"></a>

#### random\_list

```python
@property
def random_list() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 子资产随机列表，用于猜测流程和子资产元数据为空时

<a id="unreal.AesAssetChildMetaData.random_list"></a>

#### random\_list

```python
@random_list.setter
def random_list(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.AesAssetChildMetaData.tags"></a>

#### tags

```python
@property
def tags() -> Array[Name]
```

(Array[Name]):  [Read-Write] 子资产自定义标签

<a id="unreal.AesAssetChildMetaData.tags"></a>

#### tags

```python
@tags.setter
def tags(value: Array[Name]) -> None
```

<a id="unreal.AesAssetData"></a>