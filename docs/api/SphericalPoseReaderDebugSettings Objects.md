## SphericalPoseReaderDebugSettings Objects

```python
class SphericalPoseReaderDebugSettings(StructBase)
```

Spherical Pose Reader Debug Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SphericalPoseReader.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_scale`` (float):  [Read-Write]
- ``debug_segments`` (int32):  [Read-Write]
- ``debug_thickness`` (float):  [Read-Write]
- ``draw2d`` (bool):  [Read-Write]
- ``draw_debug`` (bool):  [Read-Write]
- ``draw_local_axes`` (bool):  [Read-Write]

<a id="unreal.SphericalPoseReaderDebugSettings.__init__"></a>

#### __init__

```python
def __init__(draw_debug: bool = False,
             draw2d: bool = False,
             draw_local_axes: bool = False,
             debug_scale: float = 0.000000,
             debug_segments: int = 0,
             debug_thickness: float = 0.000000) -> None
```

<a id="unreal.SphericalPoseReaderDebugSettings.draw_debug"></a>

#### draw_debug

```python
@property
def draw_debug() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SphericalPoseReaderDebugSettings.draw_debug"></a>

#### draw_debug

```python
@draw_debug.setter
def draw_debug(value: bool) -> None
```

<a id="unreal.SphericalPoseReaderDebugSettings.draw2d"></a>

#### draw2d

```python
@property
def draw2d() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SphericalPoseReaderDebugSettings.draw2d"></a>

#### draw2d

```python
@draw2d.setter
def draw2d(value: bool) -> None
```

<a id="unreal.SphericalPoseReaderDebugSettings.draw_local_axes"></a>

#### draw_local_axes

```python
@property
def draw_local_axes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SphericalPoseReaderDebugSettings.draw_local_axes"></a>

#### draw_local_axes

```python
@draw_local_axes.setter
def draw_local_axes(value: bool) -> None
```

<a id="unreal.SphericalPoseReaderDebugSettings.debug_scale"></a>

#### debug_scale

```python
@property
def debug_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.SphericalPoseReaderDebugSettings.debug_scale"></a>

#### debug_scale

```python
@debug_scale.setter
def debug_scale(value: float) -> None
```

<a id="unreal.SphericalPoseReaderDebugSettings.debug_segments"></a>

#### debug_segments

```python
@property
def debug_segments() -> int
```

(int32):  [Read-Write]

<a id="unreal.SphericalPoseReaderDebugSettings.debug_segments"></a>

#### debug_segments

```python
@debug_segments.setter
def debug_segments(value: int) -> None
```

<a id="unreal.SphericalPoseReaderDebugSettings.debug_thickness"></a>

#### debug_thickness

```python
@property
def debug_thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.SphericalPoseReaderDebugSettings.debug_thickness"></a>

#### debug_thickness

```python
@debug_thickness.setter
def debug_thickness(value: float) -> None
```

<a id="unreal.RigUnit_SphericalPoseReader"></a>