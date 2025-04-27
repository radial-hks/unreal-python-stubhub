## RigVMFunction_MathTransformTransformVector Objects

```python
class RigVMFunction_MathTransformTransformVector(
        RigVMFunction_MathTransformBase)
```

Multiplies a given vector (location) by the transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``transform`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformTransformVector.__init__"></a>

#### __init__

```python
def __init__(transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             location: Vector = [0.000000, 0.000000, 0.000000],
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathTransformTransformVector.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformTransformVector.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformTransformVector.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformTransformVector.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathTransformTransformVector.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_MathTransformTransformVector"></a>