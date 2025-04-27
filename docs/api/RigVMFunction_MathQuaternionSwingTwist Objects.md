## RigVMFunction_MathQuaternionSwingTwist Objects

```python
class RigVMFunction_MathQuaternionSwingTwist(RigVMFunction_MathQuaternionBase)
```

Computes the swing and twist components of a quaternion

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``input`` (Quat):  [Read-Write]
- ``swing`` (Quat):  [Read-Write]
- ``twist`` (Quat):  [Read-Write]
- ``twist_axis`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSwingTwist.__init__"></a>

#### __init__

```python
def __init__(input: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             twist_axis: Vector = [0.000000, 0.000000, 0.000000],
             swing: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             twist: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSwingTwist.input"></a>

#### input

```python
@property
def input() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSwingTwist.input"></a>

#### input

```python
@input.setter
def input(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSwingTwist.twist_axis"></a>

#### twist_axis

```python
@property
def twist_axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSwingTwist.twist_axis"></a>

#### twist_axis

```python
@twist_axis.setter
def twist_axis(value: Vector) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSwingTwist.swing"></a>

#### swing

```python
@property
def swing() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigVMFunction_MathQuaternionSwingTwist.twist"></a>

#### twist

```python
@property
def twist() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionSwingTwist"></a>