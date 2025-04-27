## GeometryScriptPointFlatteningOptions Objects

```python
class GeometryScriptPointFlatteningOptions(StructBase)
```

Geometry Script Point Flattening Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: PointSetFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``drop_axis`` (GeometryScriptAxis):  [Read-Write] Which axis to drop when flattening
- ``frame`` (Transform):  [Read-Write] Relative transform to use as a frame of reference. When flattening, the inverse transform will be applied to bring the points into the local space of the frame.

<a id="unreal.GeometryScriptPointFlatteningOptions.__init__"></a>

#### __init__

```python
def __init__(frame: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]],
             drop_axis: GeometryScriptAxis = GeometryScriptAxis.X) -> None
```

<a id="unreal.GeometryScriptPointFlatteningOptions.frame"></a>

#### frame

```python
@property
def frame() -> Transform
```

(Transform):  [Read-Write] Relative transform to use as a frame of reference. When flattening, the inverse transform will be applied to bring the points into the local space of the frame.

<a id="unreal.GeometryScriptPointFlatteningOptions.frame"></a>

#### frame

```python
@frame.setter
def frame(value: Transform) -> None
```

<a id="unreal.GeometryScriptPointFlatteningOptions.drop_axis"></a>

#### drop_axis

```python
@property
def drop_axis() -> GeometryScriptAxis
```

(GeometryScriptAxis):  [Read-Write] Which axis to drop when flattening

<a id="unreal.GeometryScriptPointFlatteningOptions.drop_axis"></a>

#### drop_axis

```python
@drop_axis.setter
def drop_axis(value: GeometryScriptAxis) -> None
```

<a id="unreal.GeometryScriptPolygonOffsetOptions"></a>