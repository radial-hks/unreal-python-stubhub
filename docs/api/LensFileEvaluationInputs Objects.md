## LensFileEvaluationInputs Objects

```python
class LensFileEvaluationInputs(StructBase)
```

Lens File Evaluation Inputs

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensFile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filmback`` (CameraFilmbackSettings):  [Read-Write]
- ``focus`` (float):  [Read-Write]
- ``iris`` (float):  [Read-Write]
- ``is_valid`` (bool):  [Read-Write]
- ``zoom`` (float):  [Read-Write]

<a id="unreal.LensFileEvaluationInputs.__init__"></a>

#### __init__

```python
def __init__(focus: float = 0.000000,
             iris: float = 0.000000,
             zoom: float = 0.000000,
             filmback: CameraFilmbackSettings = [
                 24.889999, 18.670000, 0.000000, 0.000000, 1.330000
             ],
             is_valid: bool = False) -> None
```

<a id="unreal.LensFileEvaluationInputs.focus"></a>

#### focus

```python
@property
def focus() -> float
```

(float):  [Read-Write]

<a id="unreal.LensFileEvaluationInputs.focus"></a>

#### focus

```python
@focus.setter
def focus(value: float) -> None
```

<a id="unreal.LensFileEvaluationInputs.iris"></a>

#### iris

```python
@property
def iris() -> float
```

(float):  [Read-Write]

<a id="unreal.LensFileEvaluationInputs.iris"></a>

#### iris

```python
@iris.setter
def iris(value: float) -> None
```

<a id="unreal.LensFileEvaluationInputs.zoom"></a>

#### zoom

```python
@property
def zoom() -> float
```

(float):  [Read-Write]

<a id="unreal.LensFileEvaluationInputs.zoom"></a>

#### zoom

```python
@zoom.setter
def zoom(value: float) -> None
```

<a id="unreal.LensFileEvaluationInputs.filmback"></a>

#### filmback

```python
@property
def filmback() -> CameraFilmbackSettings
```

(CameraFilmbackSettings):  [Read-Write]

<a id="unreal.LensFileEvaluationInputs.filmback"></a>

#### filmback

```python
@filmback.setter
def filmback(value: CameraFilmbackSettings) -> None
```

<a id="unreal.LensFileEvaluationInputs.is_valid"></a>

#### is_valid

```python
@property
def is_valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.SphericalDistortionParameters"></a>