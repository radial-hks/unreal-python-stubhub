## DataTablePointInfoBase Objects

```python
class DataTablePointInfoBase(StructBase)
```

Base struct for point info wrapper which holds focus and zoom
Child classes should hold the point info itself

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``focus`` (float):  [Read-Write] Point Focus Value
- ``zoom`` (float):  [Read-Write] Point Zoom Value

<a id="unreal.DataTablePointInfoBase.__init__"></a>

#### __init__

```python
def __init__(focus: float = 0.000000, zoom: float = 0.000000) -> None
```

<a id="unreal.DataTablePointInfoBase.focus"></a>

#### focus

```python
@property
def focus() -> float
```

(float):  [Read-Write] Point Focus Value

<a id="unreal.DataTablePointInfoBase.focus"></a>

#### focus

```python
@focus.setter
def focus(value: float) -> None
```

<a id="unreal.DataTablePointInfoBase.zoom"></a>

#### zoom

```python
@property
def zoom() -> float
```

(float):  [Read-Write] Point Zoom Value

<a id="unreal.DataTablePointInfoBase.zoom"></a>

#### zoom

```python
@zoom.setter
def zoom(value: float) -> None
```

<a id="unreal.DistortionPointInfo"></a>