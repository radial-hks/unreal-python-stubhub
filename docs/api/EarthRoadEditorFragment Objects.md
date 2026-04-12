## EarthRoadEditorFragment Objects

```python
class EarthRoadEditorFragment(EarthPropertyFragment)
```

Earth Road Editor Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chamfer_corner`` (bool):  [Read-Write] 点是否倒角
- ``chamfer_length`` (float):  [Read-Write] 切角长度
- ``lane_width`` (float):  [Read-Write] 单车道宽度
- ``lanes`` (IntPoint):  [Read-Write] 左右车道数
- ``level`` (int32):  [Read-Write] 道路Level
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthRoadEditorFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             level: int = 0,
             lanes: IntPoint = [0, 0],
             lane_width: float = 0.000000,
             chamfer_corner: bool = False,
             chamfer_length: float = 0.000000) -> None
```

<a id="unreal.EarthRoadEditorFragment.level"></a>

#### level

```python
@property
def level() -> int
```

(int32):  [Read-Write] 道路Level

<a id="unreal.EarthRoadEditorFragment.level"></a>

#### level

```python
@level.setter
def level(value: int) -> None
```

<a id="unreal.EarthRoadEditorFragment.lanes"></a>

#### lanes

```python
@property
def lanes() -> IntPoint
```

(IntPoint):  [Read-Write] 左右车道数

<a id="unreal.EarthRoadEditorFragment.lanes"></a>

#### lanes

```python
@lanes.setter
def lanes(value: IntPoint) -> None
```

<a id="unreal.EarthRoadEditorFragment.lane_width"></a>

#### lane\_width

```python
@property
def lane_width() -> float
```

(float):  [Read-Write] 单车道宽度

<a id="unreal.EarthRoadEditorFragment.lane_width"></a>

#### lane\_width

```python
@lane_width.setter
def lane_width(value: float) -> None
```

<a id="unreal.EarthRoadEditorFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@property
def chamfer_corner() -> bool
```

(bool):  [Read-Write] 点是否倒角

<a id="unreal.EarthRoadEditorFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@chamfer_corner.setter
def chamfer_corner(value: bool) -> None
```

<a id="unreal.EarthRoadEditorFragment.chamfer_length"></a>

#### chamfer\_length

```python
@property
def chamfer_length() -> float
```

(float):  [Read-Write] 切角长度

<a id="unreal.EarthRoadEditorFragment.chamfer_length"></a>

#### chamfer\_length

```python
@chamfer_length.setter
def chamfer_length(value: float) -> None
```

<a id="unreal.EarthRoadModifierEditorFragment"></a>