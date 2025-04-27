## RigVMFunction_MathQuaternionToVectors Objects

```python
class RigVMFunction_MathQuaternionToVectors(RigVMFunction_MathQuaternionBase)
```

Retrieves the forward, right and up vectors of a quaternion

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``forward`` (Vector):  [Read-Write]
- ``right`` (Vector):  [Read-Write]
- ``up`` (Vector):  [Read-Write]
- ``value`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToVectors.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             forward: Vector = [0.000000, 0.000000, 0.000000],
             right: Vector = [0.000000, 0.000000, 0.000000],
             up: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToVectors.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionToVectors.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionToVectors.forward"></a>

#### forward

```python
@property
def forward() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathQuaternionToVectors.right"></a>

#### right

```python
@property
def right() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathQuaternionToVectors.up"></a>

#### up

```python
@property
def up() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigVMFunction_MathQuaternionScale"></a>