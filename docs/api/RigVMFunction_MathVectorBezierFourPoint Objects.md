## RigVMFunction_MathVectorBezierFourPoint Objects

```python
class RigVMFunction_MathVectorBezierFourPoint(RigVMFunction_MathVectorBase)
```

Returns the 4 point bezier interpolation

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathVector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bezier`` (RigVMFourPointBezier):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``t`` (float):  [Read-Write]
- ``tangent`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorBezierFourPoint.__init__"></a>

#### __init__

```python
def __init__(bezier: RigVMFourPointBezier = [],
             t: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000],
             tangent: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathVectorBezierFourPoint.bezier"></a>

#### bezier

```python
@property
def bezier() -> RigVMFourPointBezier
```

(RigVMFourPointBezier):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorBezierFourPoint.bezier"></a>

#### bezier

```python
@bezier.setter
def bezier(value: RigVMFourPointBezier) -> None
```

<a id="unreal.RigVMFunction_MathVectorBezierFourPoint.t"></a>

#### t

```python
@property
def t() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathVectorBezierFourPoint.t"></a>

#### t

```python
@t.setter
def t(value: float) -> None
```

<a id="unreal.RigVMFunction_MathVectorBezierFourPoint.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathVectorBezierFourPoint.tangent"></a>

#### tangent

```python
@property
def tangent() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathVectorBezierFourPoint"></a>