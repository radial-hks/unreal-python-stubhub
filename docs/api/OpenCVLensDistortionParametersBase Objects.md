## OpenCVLensDistortionParametersBase Objects

```python
class OpenCVLensDistortionParametersBase(StructBase)
```

Mathematic camera model for lens distortion/undistortion.
Camera matrix =
 | F.X  0  C.x |
 |  0  F.Y C.Y |
 |  0   0   1  |
where F and C are normalized.

**C++ Source:**

- **Plugin**: OpenCV
- **Module**: OpenCVHelper
- **File**: OpenCVHelper.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``c`` (Vector2D):  [Read-Write] Camera matrix's normalized Cx and Cy.
- ``f`` (Vector2D):  [Read-Write] Camera matrix's normalized Fx and Fy.
- ``k1`` (float):  [Read-Write] Radial parameter #1.
- ``k2`` (float):  [Read-Write] Radial parameter #2.
- ``k3`` (float):  [Read-Write] Radial parameter #3.
- ``k4`` (float):  [Read-Write] Radial parameter #4.
- ``k5`` (float):  [Read-Write] Radial parameter #5.
- ``k6`` (float):  [Read-Write] Radial parameter #6.
- ``p1`` (float):  [Read-Write] Tangential parameter #1.
- ``p2`` (float):  [Read-Write] Tangential parameter #2.
- ``use_fisheye_model`` (bool):  [Read-Write] Camera lens needs Fisheye camera model.

<a id="unreal.OpenCVLensDistortionParametersBase.__init__"></a>

#### __init__

```python
def __init__(k1: float = 0.000000,
             k2: float = 0.000000,
             p1: float = 0.000000,
             p2: float = 0.000000,
             k3: float = 0.000000,
             k4: float = 0.000000,
             k5: float = 0.000000,
             k6: float = 0.000000,
             f: Vector2D = [0.000000, 0.000000],
             c: Vector2D = [0.000000, 0.000000],
             use_fisheye_model: bool = False) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.k1"></a>

#### k1

```python
@property
def k1() -> float
```

(float):  [Read-Write] Radial parameter #1.

<a id="unreal.OpenCVLensDistortionParametersBase.k1"></a>

#### k1

```python
@k1.setter
def k1(value: float) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.k2"></a>

#### k2

```python
@property
def k2() -> float
```

(float):  [Read-Write] Radial parameter #2.

<a id="unreal.OpenCVLensDistortionParametersBase.k2"></a>

#### k2

```python
@k2.setter
def k2(value: float) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.p1"></a>

#### p1

```python
@property
def p1() -> float
```

(float):  [Read-Write] Tangential parameter #1.

<a id="unreal.OpenCVLensDistortionParametersBase.p1"></a>

#### p1

```python
@p1.setter
def p1(value: float) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.p2"></a>

#### p2

```python
@property
def p2() -> float
```

(float):  [Read-Write] Tangential parameter #2.

<a id="unreal.OpenCVLensDistortionParametersBase.p2"></a>

#### p2

```python
@p2.setter
def p2(value: float) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.k3"></a>

#### k3

```python
@property
def k3() -> float
```

(float):  [Read-Write] Radial parameter #3.

<a id="unreal.OpenCVLensDistortionParametersBase.k3"></a>

#### k3

```python
@k3.setter
def k3(value: float) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.k4"></a>

#### k4

```python
@property
def k4() -> float
```

(float):  [Read-Write] Radial parameter #4.

<a id="unreal.OpenCVLensDistortionParametersBase.k4"></a>

#### k4

```python
@k4.setter
def k4(value: float) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.k5"></a>

#### k5

```python
@property
def k5() -> float
```

(float):  [Read-Write] Radial parameter #5.

<a id="unreal.OpenCVLensDistortionParametersBase.k5"></a>

#### k5

```python
@k5.setter
def k5(value: float) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.k6"></a>

#### k6

```python
@property
def k6() -> float
```

(float):  [Read-Write] Radial parameter #6.

<a id="unreal.OpenCVLensDistortionParametersBase.k6"></a>

#### k6

```python
@k6.setter
def k6(value: float) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.f"></a>

#### f

```python
@property
def f() -> Vector2D
```

(Vector2D):  [Read-Write] Camera matrix's normalized Fx and Fy.

<a id="unreal.OpenCVLensDistortionParametersBase.f"></a>

#### f

```python
@f.setter
def f(value: Vector2D) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.c"></a>

#### c

```python
@property
def c() -> Vector2D
```

(Vector2D):  [Read-Write] Camera matrix's normalized Cx and Cy.

<a id="unreal.OpenCVLensDistortionParametersBase.c"></a>

#### c

```python
@c.setter
def c(value: Vector2D) -> None
```

<a id="unreal.OpenCVLensDistortionParametersBase.use_fisheye_model"></a>

#### use_fisheye_model

```python
@property
def use_fisheye_model() -> bool
```

(bool):  [Read-Write] Camera lens needs Fisheye camera model.

<a id="unreal.OpenCVLensDistortionParametersBase.use_fisheye_model"></a>

#### use_fisheye_model

```python
@use_fisheye_model.setter
def use_fisheye_model(value: bool) -> None
```

<a id="unreal.ProcMeshTangent"></a>