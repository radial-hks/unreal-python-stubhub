## GeometryScriptRenderCaptureCamerasForBoxOptions Objects

```python
class GeometryScriptRenderCaptureCamerasForBoxOptions(StructBase)
```

Geometry Script Render Capture Cameras for Box Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``extra_view_from_positions`` (Array[Vector]):  [Read-Write] Extra positions from which to deduce view directions on the box center (located at (0,0,0))
- ``field_of_view_degrees`` (double):  [Read-Write]
- ``resolution`` (int32):  [Read-Write] The pixel resolution of render capture photos, this value is used for width and height
- ``view_from_box_faces`` (bool):  [Read-Write] Enable 6 directions corresponding to views from box face centers to the box center
- ``view_from_lower_corners`` (bool):  [Read-Write] Enable 4 directions corresponding to views from box lower corners to the box center
- ``view_from_lower_edges`` (bool):  [Read-Write] Enable 4 directions corresponding to views from box lower edges centers to the box center
- ``view_from_side_edges`` (bool):  [Read-Write] Enable 4 directions corresponding to views from box side edges centers to the box center
- ``view_from_upper_corners`` (bool):  [Read-Write] Enable 4 directions corresponding to views from box upper corners to the box center
- ``view_from_upper_edges`` (bool):  [Read-Write] Enable 4 directions corresponding to views from box upper edges centers to the box center

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.__init__"></a>

#### __init__

```python
def __init__(resolution: int = 0,
             field_of_view_degrees: float = 0.000000,
             view_from_box_faces: bool = False,
             view_from_upper_corners: bool = False,
             view_from_lower_corners: bool = False,
             view_from_upper_edges: bool = False,
             view_from_lower_edges: bool = False,
             view_from_side_edges: bool = False,
             extra_view_from_positions: Array[Vector] = []) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.resolution"></a>

#### resolution

```python
@property
def resolution() -> int
```

(int32):  [Read-Write] The pixel resolution of render capture photos, this value is used for width and height

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: int) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.field_of_view_degrees"></a>

#### field_of_view_degrees

```python
@property
def field_of_view_degrees() -> float
```

(double):  [Read-Write]

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.field_of_view_degrees"></a>

#### field_of_view_degrees

```python
@field_of_view_degrees.setter
def field_of_view_degrees(value: float) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_box_faces"></a>

#### view_from_box_faces

```python
@property
def view_from_box_faces() -> bool
```

(bool):  [Read-Write] Enable 6 directions corresponding to views from box face centers to the box center

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_box_faces"></a>

#### view_from_box_faces

```python
@view_from_box_faces.setter
def view_from_box_faces(value: bool) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_upper_corners"></a>

#### view_from_upper_corners

```python
@property
def view_from_upper_corners() -> bool
```

(bool):  [Read-Write] Enable 4 directions corresponding to views from box upper corners to the box center

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_upper_corners"></a>

#### view_from_upper_corners

```python
@view_from_upper_corners.setter
def view_from_upper_corners(value: bool) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_lower_corners"></a>

#### view_from_lower_corners

```python
@property
def view_from_lower_corners() -> bool
```

(bool):  [Read-Write] Enable 4 directions corresponding to views from box lower corners to the box center

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_lower_corners"></a>

#### view_from_lower_corners

```python
@view_from_lower_corners.setter
def view_from_lower_corners(value: bool) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_upper_edges"></a>

#### view_from_upper_edges

```python
@property
def view_from_upper_edges() -> bool
```

(bool):  [Read-Write] Enable 4 directions corresponding to views from box upper edges centers to the box center

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_upper_edges"></a>

#### view_from_upper_edges

```python
@view_from_upper_edges.setter
def view_from_upper_edges(value: bool) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_lower_edges"></a>

#### view_from_lower_edges

```python
@property
def view_from_lower_edges() -> bool
```

(bool):  [Read-Write] Enable 4 directions corresponding to views from box lower edges centers to the box center

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_lower_edges"></a>

#### view_from_lower_edges

```python
@view_from_lower_edges.setter
def view_from_lower_edges(value: bool) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_side_edges"></a>

#### view_from_side_edges

```python
@property
def view_from_side_edges() -> bool
```

(bool):  [Read-Write] Enable 4 directions corresponding to views from box side edges centers to the box center

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.view_from_side_edges"></a>

#### view_from_side_edges

```python
@view_from_side_edges.setter
def view_from_side_edges(value: bool) -> None
```

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.extra_view_from_positions"></a>

#### extra_view_from_positions

```python
@property
def extra_view_from_positions() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] Extra positions from which to deduce view directions on the box center (located at (0,0,0))

<a id="unreal.GeometryScriptRenderCaptureCamerasForBoxOptions.extra_view_from_positions"></a>

#### extra_view_from_positions

```python
@extra_view_from_positions.setter
def extra_view_from_positions(value: Array[Vector]) -> None
```

<a id="unreal.GeometryScriptDebugMessage"></a>