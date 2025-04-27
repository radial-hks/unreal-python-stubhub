## CameraFilmbackSettings Objects

```python
class CameraFilmbackSettings(StructBase)
```

#note, this struct has a details customization in CameraFilmbackSettingsCustomization.cpp/h

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``sensor_aspect_ratio`` (float):  [Read-Only] Read-only. Computed from Sensor dimensions.
- ``sensor_height`` (float):  [Read-Write] Vertical size of filmback or digital sensor, in mm.
- ``sensor_horizontal_offset`` (float):  [Read-Write] Horizontal offset of the filmback, in mm.
- ``sensor_vertical_offset`` (float):  [Read-Write] Vertical offset of the filmback, in mm.
- ``sensor_width`` (float):  [Read-Write] Horizontal size of filmback or digital sensor, in mm.

<a id="unreal.CameraFilmbackSettings.__init__"></a>

#### __init__

```python
def __init__(sensor_width: float = 0.000000,
             sensor_height: float = 0.000000,
             sensor_horizontal_offset: float = 0.000000,
             sensor_vertical_offset: float = 0.000000,
             sensor_aspect_ratio: float = 0.000000) -> None
```

<a id="unreal.CameraFilmbackSettings.sensor_width"></a>

#### sensor_width

```python
@property
def sensor_width() -> float
```

(float):  [Read-Write] Horizontal size of filmback or digital sensor, in mm.

<a id="unreal.CameraFilmbackSettings.sensor_width"></a>

#### sensor_width

```python
@sensor_width.setter
def sensor_width(value: float) -> None
```

<a id="unreal.CameraFilmbackSettings.sensor_height"></a>

#### sensor_height

```python
@property
def sensor_height() -> float
```

(float):  [Read-Write] Vertical size of filmback or digital sensor, in mm.

<a id="unreal.CameraFilmbackSettings.sensor_height"></a>

#### sensor_height

```python
@sensor_height.setter
def sensor_height(value: float) -> None
```

<a id="unreal.CameraFilmbackSettings.sensor_horizontal_offset"></a>

#### sensor_horizontal_offset

```python
@property
def sensor_horizontal_offset() -> float
```

(float):  [Read-Write] Horizontal offset of the filmback, in mm.

<a id="unreal.CameraFilmbackSettings.sensor_horizontal_offset"></a>

#### sensor_horizontal_offset

```python
@sensor_horizontal_offset.setter
def sensor_horizontal_offset(value: float) -> None
```

<a id="unreal.CameraFilmbackSettings.sensor_vertical_offset"></a>

#### sensor_vertical_offset

```python
@property
def sensor_vertical_offset() -> float
```

(float):  [Read-Write] Vertical offset of the filmback, in mm.

<a id="unreal.CameraFilmbackSettings.sensor_vertical_offset"></a>

#### sensor_vertical_offset

```python
@sensor_vertical_offset.setter
def sensor_vertical_offset(value: float) -> None
```

<a id="unreal.CameraFilmbackSettings.sensor_aspect_ratio"></a>

#### sensor_aspect_ratio

```python
@property
def sensor_aspect_ratio() -> float
```

(float):  [Read-Only] Read-only. Computed from Sensor dimensions.

<a id="unreal.NamedFilmbackPreset"></a>