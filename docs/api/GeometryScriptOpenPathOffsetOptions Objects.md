## GeometryScriptOpenPathOffsetOptions Objects

```python
class GeometryScriptOpenPathOffsetOptions(StructBase)
```

Geometry Script Open Path Offset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PolygonFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_type`` (GeometryScriptPathOffsetEndType):  [Read-Write] How the ends of a path should be closed off
- ``join_type`` (GeometryScriptPolyOffsetJoinType):  [Read-Write] How to join / extend corners between two edges
- ``maximum_steps_per_radian`` (double):  [Read-Write] Maximum vertices per radian for round joins and ends. Only applied if > 0.
- ``miter_limit`` (double):  [Read-Write] if JoinType is Miter, limits how far the miter can extend
- ``steps_per_radian_scale`` (double):  [Read-Write] Scales the default number of vertices (per radian) used for round joins and ends.

<a id="unreal.GeometryScriptOpenPathOffsetOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        join_type:
    GeometryScriptPolyOffsetJoinType = GeometryScriptPolyOffsetJoinType.SQUARE,
        miter_limit: float = 0.000000,
        end_type:
    GeometryScriptPathOffsetEndType = GeometryScriptPathOffsetEndType.BUTT,
        steps_per_radian_scale: float = 0.000000,
        maximum_steps_per_radian: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptOpenPathOffsetOptions.join_type"></a>

#### join\_type

```python
@property
def join_type() -> GeometryScriptPolyOffsetJoinType
```

(GeometryScriptPolyOffsetJoinType):  [Read-Write] How to join / extend corners between two edges

<a id="unreal.GeometryScriptOpenPathOffsetOptions.join_type"></a>

#### join\_type

```python
@join_type.setter
def join_type(value: GeometryScriptPolyOffsetJoinType) -> None
```

<a id="unreal.GeometryScriptOpenPathOffsetOptions.miter_limit"></a>

#### miter\_limit

```python
@property
def miter_limit() -> float
```

(double):  [Read-Write] if JoinType is Miter, limits how far the miter can extend

<a id="unreal.GeometryScriptOpenPathOffsetOptions.miter_limit"></a>

#### miter\_limit

```python
@miter_limit.setter
def miter_limit(value: float) -> None
```

<a id="unreal.GeometryScriptOpenPathOffsetOptions.end_type"></a>

#### end\_type

```python
@property
def end_type() -> GeometryScriptPathOffsetEndType
```

(GeometryScriptPathOffsetEndType):  [Read-Write] How the ends of a path should be closed off

<a id="unreal.GeometryScriptOpenPathOffsetOptions.end_type"></a>

#### end\_type

```python
@end_type.setter
def end_type(value: GeometryScriptPathOffsetEndType) -> None
```

<a id="unreal.GeometryScriptOpenPathOffsetOptions.steps_per_radian_scale"></a>

#### steps\_per\_radian\_scale

```python
@property
def steps_per_radian_scale() -> float
```

(double):  [Read-Write] Scales the default number of vertices (per radian) used for round joins and ends.

<a id="unreal.GeometryScriptOpenPathOffsetOptions.steps_per_radian_scale"></a>

#### steps\_per\_radian\_scale

```python
@steps_per_radian_scale.setter
def steps_per_radian_scale(value: float) -> None
```

<a id="unreal.GeometryScriptOpenPathOffsetOptions.maximum_steps_per_radian"></a>

#### maximum\_steps\_per\_radian

```python
@property
def maximum_steps_per_radian() -> float
```

(double):  [Read-Write] Maximum vertices per radian for round joins and ends. Only applied if > 0.

<a id="unreal.GeometryScriptOpenPathOffsetOptions.maximum_steps_per_radian"></a>

#### maximum\_steps\_per\_radian

```python
@maximum_steps_per_radian.setter
def maximum_steps_per_radian(value: float) -> None
```

<a id="unreal.GeometryScriptSplineSamplingOptions"></a>