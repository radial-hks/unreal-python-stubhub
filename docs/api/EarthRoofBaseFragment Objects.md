## EarthRoofBaseFragment Objects

```python
class EarthRoofBaseFragment(EarthEntityFragment)
```

定义屋顶基础数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoofFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] 屋顶颜色
- ``over_hang`` (float):  [Read-Write] 挑檐长度
- ``roof_material`` (EarthMaterialInfo):  [Read-Write] 屋顶材质
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthRoofBaseFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    over_hang: float = 0.000000,
    roof_material: EarthMaterialInfo = [
        "None", None, 0, False, 255, [0.000000, 0.000000], 0.000000, [0, 0]
    ]
) -> None
```

<a id="unreal.EarthRoofBaseFragment.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] 屋顶颜色

<a id="unreal.EarthRoofBaseFragment.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.EarthRoofBaseFragment.over_hang"></a>

#### over\_hang

```python
@property
def over_hang() -> float
```

(float):  [Read-Write] 挑檐长度

<a id="unreal.EarthRoofBaseFragment.over_hang"></a>

#### over\_hang

```python
@over_hang.setter
def over_hang(value: float) -> None
```

<a id="unreal.EarthRoofBaseFragment.roof_material"></a>

#### roof\_material

```python
@property
def roof_material() -> EarthMaterialInfo
```

(EarthMaterialInfo):  [Read-Write] 屋顶材质

<a id="unreal.EarthRoofBaseFragment.roof_material"></a>

#### roof\_material

```python
@roof_material.setter
def roof_material(value: EarthMaterialInfo) -> None
```

<a id="unreal.EarthFlatRoofFragment"></a>