## RigVMFunction_MathQuaternionScaleV2 Objects

```python
class RigVMFunction_MathQuaternionScaleV2(RigVMFunction_MathQuaternionBase)
```

Scales a quaternion's angle

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``factor`` (float):  [Read-Write]
- ``result`` (Quat):  [Read-Write]
- ``value`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionScaleV2.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             factor: float = 0.000000,
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionScaleV2.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionScaleV2.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionScaleV2.factor"></a>

#### factor

```python
@property
def factor() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionScaleV2.factor"></a>

#### factor

```python
@factor.setter
def factor(value: float) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionScaleV2.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionScaleV2"></a>