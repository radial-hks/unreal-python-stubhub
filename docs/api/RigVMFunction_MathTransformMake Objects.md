## RigVMFunction_MathTransformMake Objects

```python
class RigVMFunction_MathTransformMake(RigVMFunction_MathTransformBase)
```

Makes a transform from its components

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``result`` (Transform):  [Read-Write]
- ``rotation`` (Quat):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``translation`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformMake.__init__"></a>

#### __init__

```python
def __init__(
    translation: Vector = [0.000000, 0.000000, 0.000000],
    rotation: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
    scale: Vector = [0.000000, 0.000000, 0.000000],
    result: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigVMFunction_MathTransformMake.translation"></a>

#### translation

```python
@property
def translation() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformMake.translation"></a>

#### translation

```python
@translation.setter
def translation(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathTransformMake.rotation"></a>

#### rotation

```python
@property
def rotation() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformMake.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathTransformMake.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformMake.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathTransformMake.result"></a>

#### result

```python
@property
def result() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_MathTransformMake"></a>