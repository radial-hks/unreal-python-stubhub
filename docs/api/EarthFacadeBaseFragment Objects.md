## EarthFacadeBaseFragment Objects

```python
class EarthFacadeBaseFragment(EarthPropertyFragment)
```

定义立面基础数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFacadeFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] 立面颜色
- ``footprint_offset`` (float):  [Read-Write] 轮廓线偏移距离，正值为放大，负值为缩小
- ``height`` (float):  [Read-Write] 立面高度，单位为米
- ``height_offset`` (float):  [Read-Write] 立面高度偏移值，单位为米
- ``levels`` (int32):  [Read-Write] 立面层数
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthFacadeBaseFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             height: float = 0.000000,
             height_offset: float = 0.000000,
             levels: int = 0,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             footprint_offset: float = 0.000000) -> None
```

<a id="unreal.EarthFacadeBaseFragment.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 立面高度，单位为米

<a id="unreal.EarthFacadeBaseFragment.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.EarthFacadeBaseFragment.height_offset"></a>

#### height\_offset

```python
@property
def height_offset() -> float
```

(float):  [Read-Write] 立面高度偏移值，单位为米

<a id="unreal.EarthFacadeBaseFragment.height_offset"></a>

#### height\_offset

```python
@height_offset.setter
def height_offset(value: float) -> None
```

<a id="unreal.EarthFacadeBaseFragment.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] 立面层数

<a id="unreal.EarthFacadeBaseFragment.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.EarthFacadeBaseFragment.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] 立面颜色

<a id="unreal.EarthFacadeBaseFragment.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.EarthFacadeBaseFragment.footprint_offset"></a>

#### footprint\_offset

```python
@property
def footprint_offset() -> float
```

(float):  [Read-Write] 轮廓线偏移距离，正值为放大，负值为缩小

<a id="unreal.EarthFacadeBaseFragment.footprint_offset"></a>

#### footprint\_offset

```python
@footprint_offset.setter
def footprint_offset(value: float) -> None
```

<a id="unreal.EarthFacadeMeshFragment"></a>