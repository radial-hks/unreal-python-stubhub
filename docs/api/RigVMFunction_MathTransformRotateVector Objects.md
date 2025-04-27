## RigVMFunction_MathTransformRotateVector Objects

```python
class RigVMFunction_MathTransformRotateVector(RigVMFunction_MathTransformBase)
```

Rotates a given vector (direction) by the transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Vector):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]
- ``vector`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformRotateVector.__init__"></a>

#### __init__

```python
def __init__(transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             vector: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathTransformRotateVector.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformRotateVector.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformRotateVector.vector"></a>

#### vector

```python
@property
def vector() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformRotateVector.vector"></a>

#### vector

```python
@vector.setter
def vector(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathTransformRotateVector.direction"></a>

#### direction

```python
@property
def direction() -> Vector
```

deprecated: 'direction' was renamed to 'vector'.

<a id="unreal.RigVMFunction_MathTransformRotateVector.direction"></a>

#### direction

```python
@direction.setter
def direction(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathTransformRotateVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathTransformRotateVector"></a>