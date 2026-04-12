## CameraLensSettings Objects

```python
class CameraLensSettings(StructBase)
```

#note, this struct has a details customization in CameraLensSettingsCustomization.cpp/h

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``diaphragm_blade_count`` (int32):  [Read-Write] Number of blades of diaphragm.
- ``max_f_stop`` (float):  [Read-Write] Maximum aperture for this lens (e.g. 2.8 for an f/2.8 lens)
- ``max_focal_length`` (float):  [Read-Write] Maximum focal length for this lens
- ``min_f_stop`` (float):  [Read-Write] Minimum aperture for this lens (e.g. 2.8 for an f/2.8 lens)
- ``min_focal_length`` (float):  [Read-Write] Minimum focal length for this lens
- ``minimum_focus_distance`` (float):  [Read-Write] Shortest distance this lens can focus on.
- ``squeeze_factor`` (float):  [Read-Write] Squeeze factor for anamorphic lenses.

<a id="unreal.CameraLensSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(min_focal_length: float = 0.000000,
             max_focal_length: float = 0.000000,
             min_f_stop: float = 0.000000,
             max_f_stop: float = 0.000000,
             minimum_focus_distance: float = 0.000000,
             squeeze_factor: float = 0.000000,
             diaphragm_blade_count: int = 0) -> None
```

<a id="unreal.CameraLensSettings.min_focal_length"></a>

#### min\_focal\_length

```python
@property
def min_focal_length() -> float
```

(float):  [Read-Write] Minimum focal length for this lens

<a id="unreal.CameraLensSettings.min_focal_length"></a>

#### min\_focal\_length

```python
@min_focal_length.setter
def min_focal_length(value: float) -> None
```

<a id="unreal.CameraLensSettings.max_focal_length"></a>

#### max\_focal\_length

```python
@property
def max_focal_length() -> float
```

(float):  [Read-Write] Maximum focal length for this lens

<a id="unreal.CameraLensSettings.max_focal_length"></a>

#### max\_focal\_length

```python
@max_focal_length.setter
def max_focal_length(value: float) -> None
```

<a id="unreal.CameraLensSettings.min_f_stop"></a>

#### min\_f\_stop

```python
@property
def min_f_stop() -> float
```

(float):  [Read-Write] Minimum aperture for this lens (e.g. 2.8 for an f/2.8 lens)

<a id="unreal.CameraLensSettings.min_f_stop"></a>

#### min\_f\_stop

```python
@min_f_stop.setter
def min_f_stop(value: float) -> None
```

<a id="unreal.CameraLensSettings.max_f_stop"></a>

#### max\_f\_stop

```python
@property
def max_f_stop() -> float
```

(float):  [Read-Write] Maximum aperture for this lens (e.g. 2.8 for an f/2.8 lens)

<a id="unreal.CameraLensSettings.max_f_stop"></a>

#### max\_f\_stop

```python
@max_f_stop.setter
def max_f_stop(value: float) -> None
```

<a id="unreal.CameraLensSettings.minimum_focus_distance"></a>

#### minimum\_focus\_distance

```python
@property
def minimum_focus_distance() -> float
```

(float):  [Read-Write] Shortest distance this lens can focus on.

<a id="unreal.CameraLensSettings.minimum_focus_distance"></a>

#### minimum\_focus\_distance

```python
@minimum_focus_distance.setter
def minimum_focus_distance(value: float) -> None
```

<a id="unreal.CameraLensSettings.squeeze_factor"></a>

#### squeeze\_factor

```python
@property
def squeeze_factor() -> float
```

(float):  [Read-Write] Squeeze factor for anamorphic lenses.

<a id="unreal.CameraLensSettings.squeeze_factor"></a>

#### squeeze\_factor

```python
@squeeze_factor.setter
def squeeze_factor(value: float) -> None
```

<a id="unreal.CameraLensSettings.diaphragm_blade_count"></a>

#### diaphragm\_blade\_count

```python
@property
def diaphragm_blade_count() -> int
```

(int32):  [Read-Write] Number of blades of diaphragm.

<a id="unreal.CameraLensSettings.diaphragm_blade_count"></a>

#### diaphragm\_blade\_count

```python
@diaphragm_blade_count.setter
def diaphragm_blade_count(value: int) -> None
```

<a id="unreal.NamedLensPreset"></a>