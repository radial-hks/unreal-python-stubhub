## SphericalDistortionParameters Objects

```python
class SphericalDistortionParameters(StructBase)
```

Spherical lens distortion parameters
All parameters are unitless and represent the coefficients used to undistort a distorted image
Refer to the OpenCV camera calibration documentation for the intended units/usage of these parameters:
https://docs.opencv.org/3.4/d9/d0c/group__calib3d.html

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: SphericalLensModel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``k1`` (float):  [Read-Write] Radial coefficient of the r^2 term
- ``k2`` (float):  [Read-Write] Radial coefficient of the r^4 term
- ``k3`` (float):  [Read-Write] Radial coefficient of the r^6 term
- ``p1`` (float):  [Read-Write] First tangential coefficient
- ``p2`` (float):  [Read-Write] Second tangential coefficient

<a id="unreal.SphericalDistortionParameters.__init__"></a>

#### __init__

```python
def __init__(k1: float = 0.000000,
             k2: float = 0.000000,
             k3: float = 0.000000,
             p1: float = 0.000000,
             p2: float = 0.000000) -> None
```

<a id="unreal.SphericalDistortionParameters.k1"></a>

#### k1

```python
@property
def k1() -> float
```

(float):  [Read-Write] Radial coefficient of the r^2 term

<a id="unreal.SphericalDistortionParameters.k1"></a>

#### k1

```python
@k1.setter
def k1(value: float) -> None
```

<a id="unreal.SphericalDistortionParameters.k2"></a>

#### k2

```python
@property
def k2() -> float
```

(float):  [Read-Write] Radial coefficient of the r^4 term

<a id="unreal.SphericalDistortionParameters.k2"></a>

#### k2

```python
@k2.setter
def k2(value: float) -> None
```

<a id="unreal.SphericalDistortionParameters.k3"></a>

#### k3

```python
@property
def k3() -> float
```

(float):  [Read-Write] Radial coefficient of the r^6 term

<a id="unreal.SphericalDistortionParameters.k3"></a>

#### k3

```python
@k3.setter
def k3(value: float) -> None
```

<a id="unreal.SphericalDistortionParameters.p1"></a>

#### p1

```python
@property
def p1() -> float
```

(float):  [Read-Write] First tangential coefficient

<a id="unreal.SphericalDistortionParameters.p1"></a>

#### p1

```python
@p1.setter
def p1(value: float) -> None
```

<a id="unreal.SphericalDistortionParameters.p2"></a>

#### p2

```python
@property
def p2() -> float
```

(float):  [Read-Write] Second tangential coefficient

<a id="unreal.SphericalDistortionParameters.p2"></a>

#### p2

```python
@p2.setter
def p2(value: float) -> None
```

<a id="unreal.MRMeshConfiguration"></a>