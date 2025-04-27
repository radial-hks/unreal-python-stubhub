## RigVMFunction_MathTransformToVectors Objects

```python
class RigVMFunction_MathTransformToVectors(RigVMFunction_MathTransformBase)
```

Retrieves the forward, right and up vectors of a transform's quaternion

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``forward`` (Vector):  [Read-Write]
- ``right`` (Vector):  [Read-Write]
- ``up`` (Vector):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformToVectors.__init__"></a>

#### __init__

```python
def __init__(value: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]],
             forward: Vector = [0.000000, 0.000000, 0.000000],
             right: Vector = [0.000000, 0.000000, 0.000000],
             up: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathTransformToVectors.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_MathTransformToVectors.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.RigVMFunction_MathTransformToVectors.forward"></a>

#### forward

```python
@property
def forward() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathTransformToVectors.right"></a>

#### right

```python
@property
def right() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathTransformToVectors.up"></a>

#### up

```python
@property
def up() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathTransformMul"></a>