## ShapeChangedEventArgs Objects

```python
class ShapeChangedEventArgs(EventArgsBase)
```

Shape Changed Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpShapeEditorAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``points`` (Array[WdpShapeChangedPointInfo]):  [Read-Write]

<a id="unreal.ShapeChangedEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(points: Array[WdpShapeChangedPointInfo] = []) -> None
```

<a id="unreal.ShapeChangedEventArgs.points"></a>

#### points

```python
@property
def points() -> Array[WdpShapeChangedPointInfo]
```

(Array[WdpShapeChangedPointInfo]):  [Read-Write]

<a id="unreal.ShapeChangedEventArgs.points"></a>

#### points

```python
@points.setter
def points(value: Array[WdpShapeChangedPointInfo]) -> None
```

<a id="unreal.WdpUpdateShapePointsParams"></a>