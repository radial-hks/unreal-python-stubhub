## AnamorphicDistortionParameters Objects

```python
class AnamorphicDistortionParameters(StructBase)
```

Lens distortion parameters for the 3DE4 Anamorphic - Standard Degree 4 model
All parameters are unitless and represent the coefficients used to undistort a distorted image
For complete model description, see "tde4_ldm_standard.pdf" from https://www.3dequalizer.com/ in the Lens Distortion Plugin Kit v2.8

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: AnamorphicLensModel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cx02`` (float):  [Read-Write] X coefficient of the r^2 term
- ``cx04`` (float):  [Read-Write] X coefficient of the r^4 term
- ``cx22`` (float):  [Read-Write] X coefficient of the r^2*cos(2*phi) term
- ``cx24`` (float):  [Read-Write] X coefficient of the r^4*cos(2*phi) term
- ``cx44`` (float):  [Read-Write] X coefficient of the r^4*cos(4*phi) term
- ``cy02`` (float):  [Read-Write] Y coefficient of the r^2 term
- ``cy04`` (float):  [Read-Write] Y coefficient of the r^4 term
- ``cy22`` (float):  [Read-Write] Y coefficient of the r^2*cos(2*phi) term
- ``cy24`` (float):  [Read-Write] Y coefficient of the r^4*cos(2*phi) term
- ``cy44`` (float):  [Read-Write] Y coefficient of the r^4*cos(4*phi) term
- ``lens_rotation`` (float):  [Read-Write] Lens Rotation in degrees. Represents mounting inaccuracies (should be small, between -2 and +2 degrees)
- ``pixel_aspect`` (float):  [Read-Write] Anamorphic Squeeze (the ratio of the filmback size to the size of the rasterized image)
- ``squeeze_x`` (float):  [Read-Write] Squeeze Factor (should be small, relatively close to 1.0)
- ``squeeze_y`` (float):  [Read-Write] Squeeze Factor (should be small, relatively close to 1.0)

<a id="unreal.AnamorphicDistortionParameters.__init__"></a>

#### __init__

```python
def __init__(pixel_aspect: float = 0.000000,
             cx02: float = 0.000000,
             cx04: float = 0.000000,
             cx22: float = 0.000000,
             cx24: float = 0.000000,
             cx44: float = 0.000000,
             cy02: float = 0.000000,
             cy04: float = 0.000000,
             cy22: float = 0.000000,
             cy24: float = 0.000000,
             cy44: float = 0.000000,
             squeeze_x: float = 0.000000,
             squeeze_y: float = 0.000000,
             lens_rotation: float = 0.000000) -> None
```

<a id="unreal.AnamorphicDistortionParameters.pixel_aspect"></a>

#### pixel_aspect

```python
@property
def pixel_aspect() -> float
```

(float):  [Read-Write] Anamorphic Squeeze (the ratio of the filmback size to the size of the rasterized image)

<a id="unreal.AnamorphicDistortionParameters.pixel_aspect"></a>

#### pixel_aspect

```python
@pixel_aspect.setter
def pixel_aspect(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cx02"></a>

#### cx02

```python
@property
def cx02() -> float
```

(float):  [Read-Write] X coefficient of the r^2 term

<a id="unreal.AnamorphicDistortionParameters.cx02"></a>

#### cx02

```python
@cx02.setter
def cx02(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cx04"></a>

#### cx04

```python
@property
def cx04() -> float
```

(float):  [Read-Write] X coefficient of the r^4 term

<a id="unreal.AnamorphicDistortionParameters.cx04"></a>

#### cx04

```python
@cx04.setter
def cx04(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cx22"></a>

#### cx22

```python
@property
def cx22() -> float
```

(float):  [Read-Write] X coefficient of the r^2*cos(2*phi) term

<a id="unreal.AnamorphicDistortionParameters.cx22"></a>

#### cx22

```python
@cx22.setter
def cx22(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cx24"></a>

#### cx24

```python
@property
def cx24() -> float
```

(float):  [Read-Write] X coefficient of the r^4*cos(2*phi) term

<a id="unreal.AnamorphicDistortionParameters.cx24"></a>

#### cx24

```python
@cx24.setter
def cx24(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cx44"></a>

#### cx44

```python
@property
def cx44() -> float
```

(float):  [Read-Write] X coefficient of the r^4*cos(4*phi) term

<a id="unreal.AnamorphicDistortionParameters.cx44"></a>

#### cx44

```python
@cx44.setter
def cx44(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cy02"></a>

#### cy02

```python
@property
def cy02() -> float
```

(float):  [Read-Write] Y coefficient of the r^2 term

<a id="unreal.AnamorphicDistortionParameters.cy02"></a>

#### cy02

```python
@cy02.setter
def cy02(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cy04"></a>

#### cy04

```python
@property
def cy04() -> float
```

(float):  [Read-Write] Y coefficient of the r^4 term

<a id="unreal.AnamorphicDistortionParameters.cy04"></a>

#### cy04

```python
@cy04.setter
def cy04(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cy22"></a>

#### cy22

```python
@property
def cy22() -> float
```

(float):  [Read-Write] Y coefficient of the r^2*cos(2*phi) term

<a id="unreal.AnamorphicDistortionParameters.cy22"></a>

#### cy22

```python
@cy22.setter
def cy22(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cy24"></a>

#### cy24

```python
@property
def cy24() -> float
```

(float):  [Read-Write] Y coefficient of the r^4*cos(2*phi) term

<a id="unreal.AnamorphicDistortionParameters.cy24"></a>

#### cy24

```python
@cy24.setter
def cy24(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.cy44"></a>

#### cy44

```python
@property
def cy44() -> float
```

(float):  [Read-Write] Y coefficient of the r^4*cos(4*phi) term

<a id="unreal.AnamorphicDistortionParameters.cy44"></a>

#### cy44

```python
@cy44.setter
def cy44(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.squeeze_x"></a>

#### squeeze_x

```python
@property
def squeeze_x() -> float
```

(float):  [Read-Write] Squeeze Factor (should be small, relatively close to 1.0)

<a id="unreal.AnamorphicDistortionParameters.squeeze_x"></a>

#### squeeze_x

```python
@squeeze_x.setter
def squeeze_x(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.squeeze_y"></a>

#### squeeze_y

```python
@property
def squeeze_y() -> float
```

(float):  [Read-Write] Squeeze Factor (should be small, relatively close to 1.0)

<a id="unreal.AnamorphicDistortionParameters.squeeze_y"></a>

#### squeeze_y

```python
@squeeze_y.setter
def squeeze_y(value: float) -> None
```

<a id="unreal.AnamorphicDistortionParameters.lens_rotation"></a>

#### lens_rotation

```python
@property
def lens_rotation() -> float
```

(float):  [Read-Write] Lens Rotation in degrees. Represents mounting inaccuracies (should be small, between -2 and +2 degrees)

<a id="unreal.AnamorphicDistortionParameters.lens_rotation"></a>

#### lens_rotation

```python
@lens_rotation.setter
def lens_rotation(value: float) -> None
```

<a id="unreal.DistortionCalibrationResult"></a>