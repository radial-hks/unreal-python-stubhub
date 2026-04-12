## AesRoofAssetTagData Objects

```python
class AesRoofAssetTagData(StructBase)
```

屋顶资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesRoofAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gable_material`` (AesMaterialData):  [Read-Write] 山墙材质
- ``height`` (float):  [Read-Write] 屋顶高度
- ``levels`` (int32):  [Read-Write] 屋顶楼层数
- ``roof_color`` (Color):  [Read-Write] 屋顶颜色
- ``roof_material`` (AesMaterialData):  [Read-Write] 屋顶材质
- ``roof_shape`` (RoofShape):  [Read-Write] 屋顶形态
- ``slope`` (float):  [Read-Write] 屋顶坡度

<a id="unreal.AesRoofAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(roof_shape: RoofShape = RoofShape.FLAT,
             height: float = 0.000000,
             levels: int = 0,
             roof_color: Color = [0, 0, 0, 0],
             roof_material: AesMaterialData = [[""], -1, 1200.000000],
             gable_material: AesMaterialData = [[""], -1, 1200.000000],
             slope: float = 0.000000) -> None
```

<a id="unreal.AesRoofAssetTagData.roof_shape"></a>

#### roof\_shape

```python
@property
def roof_shape() -> RoofShape
```

(RoofShape):  [Read-Write] 屋顶形态

<a id="unreal.AesRoofAssetTagData.roof_shape"></a>

#### roof\_shape

```python
@roof_shape.setter
def roof_shape(value: RoofShape) -> None
```

<a id="unreal.AesRoofAssetTagData.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 屋顶高度

<a id="unreal.AesRoofAssetTagData.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesRoofAssetTagData.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] 屋顶楼层数

<a id="unreal.AesRoofAssetTagData.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.AesRoofAssetTagData.roof_color"></a>

#### roof\_color

```python
@property
def roof_color() -> Color
```

(Color):  [Read-Write] 屋顶颜色

<a id="unreal.AesRoofAssetTagData.roof_color"></a>

#### roof\_color

```python
@roof_color.setter
def roof_color(value: Color) -> None
```

<a id="unreal.AesRoofAssetTagData.roof_material"></a>

#### roof\_material

```python
@property
def roof_material() -> AesMaterialData
```

(AesMaterialData):  [Read-Write] 屋顶材质

<a id="unreal.AesRoofAssetTagData.roof_material"></a>

#### roof\_material

```python
@roof_material.setter
def roof_material(value: AesMaterialData) -> None
```

<a id="unreal.AesRoofAssetTagData.gable_material"></a>

#### gable\_material

```python
@property
def gable_material() -> AesMaterialData
```

(AesMaterialData):  [Read-Write] 山墙材质

<a id="unreal.AesRoofAssetTagData.gable_material"></a>

#### gable\_material

```python
@gable_material.setter
def gable_material(value: AesMaterialData) -> None
```

<a id="unreal.AesRoofAssetTagData.slope"></a>

#### slope

```python
@property
def slope() -> float
```

(float):  [Read-Write] 屋顶坡度

<a id="unreal.AesRoofAssetTagData.slope"></a>

#### slope

```python
@slope.setter
def slope(value: float) -> None
```

<a id="unreal.AesRoofAssetData"></a>