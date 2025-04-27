## AnimNode_ModifyCurve Objects

```python
class AnimNode_ModifyCurve(AnimNode_Base)
```

Easy way to modify curve values on a pose

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_ModifyCurve.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write]
- ``apply_mode`` (ModifyCurveApplyMode):  [Read-Write]
- ``curve_map`` (Map[Name, float]):  [Read-Write]
- ``curve_values`` (Array[float]):  [Read-Write]
- ``source_pose`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_ModifyCurve.__init__"></a>

#### __init__

```python
def __init__(
        source_pose: PoseLink = [],
        curve_map: Map[Name, float] = {},
        curve_values: Array[float] = [],
        alpha: float = 0.000000,
        apply_mode: ModifyCurveApplyMode = ModifyCurveApplyMode.ADD) -> None
```

<a id="unreal.AnimNode_ModifyCurve.source_pose"></a>

#### source_pose

```python
@property
def source_pose() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_ModifyCurve.source_pose"></a>

#### source_pose

```python
@source_pose.setter
def source_pose(value: PoseLink) -> None
```

<a id="unreal.AnimNode_ModifyCurve.curve_map"></a>

#### curve_map

```python
@property
def curve_map() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write]

<a id="unreal.AnimNode_ModifyCurve.curve_map"></a>

#### curve_map

```python
@curve_map.setter
def curve_map(value: Map[Name, float]) -> None
```

<a id="unreal.AnimNode_ModifyCurve.curve_values"></a>

#### curve_values

```python
@property
def curve_values() -> Array[float]
```

(Array[float]):  [Read-Write]

<a id="unreal.AnimNode_ModifyCurve.curve_values"></a>

#### curve_values

```python
@curve_values.setter
def curve_values(value: Array[float]) -> None
```

<a id="unreal.AnimNode_ModifyCurve.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_ModifyCurve.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.AnimNode_ModifyCurve.apply_mode"></a>

#### apply_mode

```python
@property
def apply_mode() -> ModifyCurveApplyMode
```

(ModifyCurveApplyMode):  [Read-Write]

<a id="unreal.AnimNode_ModifyCurve.apply_mode"></a>

#### apply_mode

```python
@apply_mode.setter
def apply_mode(value: ModifyCurveApplyMode) -> None
```

<a id="unreal.AnimNode_MultiWayBlend"></a>