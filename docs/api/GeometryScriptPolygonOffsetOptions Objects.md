## GeometryScriptPolygonOffsetOptions Objects

```python
class GeometryScriptPolygonOffsetOptions(StructBase)
```

Geometry Script Polygon Offset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PolygonFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``join_type`` (GeometryScriptPolyOffsetJoinType):  [Read-Write] How to join / extend corners between two edges
- ``maximum_steps_per_radian`` (double):  [Read-Write] Maximum vertices per radian for round joins. Only applied if > 0.
- ``miter_limit`` (double):  [Read-Write] if JoinType is Miter, limits how far the miter can extend
- ``offset_both_sides`` (bool):  [Read-Write] Whether to apply the offset to both sides of the polygon, i.e. adding an inner hole to any polygon. If false, the offset is only applied to one side.
- ``steps_per_radian_scale`` (double):  [Read-Write] Scales the default number of vertices (per radian) used for round joins.

<a id="unreal.GeometryScriptPolygonOffsetOptions.__init__"></a>

#### __init__

```python
def __init__(
        join_type:
    GeometryScriptPolyOffsetJoinType = GeometryScriptPolyOffsetJoinType.SQUARE,
        miter_limit: float = 0.000000,
        offset_both_sides: bool = False,
        steps_per_radian_scale: float = 0.000000,
        maximum_steps_per_radian: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptPolygonOffsetOptions.join_type"></a>

#### join_type

```python
@property
def join_type() -> GeometryScriptPolyOffsetJoinType
```

(GeometryScriptPolyOffsetJoinType):  [Read-Write] How to join / extend corners between two edges

<a id="unreal.GeometryScriptPolygonOffsetOptions.join_type"></a>

#### join_type

```python
@join_type.setter
def join_type(value: GeometryScriptPolyOffsetJoinType) -> None
```

<a id="unreal.GeometryScriptPolygonOffsetOptions.miter_limit"></a>

#### miter_limit

```python
@property
def miter_limit() -> float
```

(double):  [Read-Write] if JoinType is Miter, limits how far the miter can extend

<a id="unreal.GeometryScriptPolygonOffsetOptions.miter_limit"></a>

#### miter_limit

```python
@miter_limit.setter
def miter_limit(value: float) -> None
```

<a id="unreal.GeometryScriptPolygonOffsetOptions.offset_both_sides"></a>

#### offset_both_sides

```python
@property
def offset_both_sides() -> bool
```

(bool):  [Read-Write] Whether to apply the offset to both sides of the polygon, i.e. adding an inner hole to any polygon. If false, the offset is only applied to one side.

<a id="unreal.GeometryScriptPolygonOffsetOptions.offset_both_sides"></a>

#### offset_both_sides

```python
@offset_both_sides.setter
def offset_both_sides(value: bool) -> None
```

<a id="unreal.GeometryScriptPolygonOffsetOptions.steps_per_radian_scale"></a>

#### steps_per_radian_scale

```python
@property
def steps_per_radian_scale() -> float
```

(double):  [Read-Write] Scales the default number of vertices (per radian) used for round joins.

<a id="unreal.GeometryScriptPolygonOffsetOptions.steps_per_radian_scale"></a>

#### steps_per_radian_scale

```python
@steps_per_radian_scale.setter
def steps_per_radian_scale(value: float) -> None
```

<a id="unreal.GeometryScriptPolygonOffsetOptions.maximum_steps_per_radian"></a>

#### maximum_steps_per_radian

```python
@property
def maximum_steps_per_radian() -> float
```

(double):  [Read-Write] Maximum vertices per radian for round joins. Only applied if > 0.

<a id="unreal.GeometryScriptPolygonOffsetOptions.maximum_steps_per_radian"></a>

#### maximum_steps_per_radian

```python
@maximum_steps_per_radian.setter
def maximum_steps_per_radian(value: float) -> None
```

<a id="unreal.GeometryScriptOpenPathOffsetOptions"></a>