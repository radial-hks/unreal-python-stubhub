## RigVMFunction_MathQuaternionSelectBool Objects

```python
class RigVMFunction_MathQuaternionSelectBool(RigVMFunction_MathQuaternionBase)
```

Return one of the two values based on the condition

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition`` (bool):  [Read-Write]
- ``if_false`` (Quat):  [Read-Write]
- ``if_true`` (Quat):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSelectBool.__init__"></a>

#### __init__

```python
def __init__(condition: bool = False,
             if_true: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             if_false: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSelectBool.condition"></a>

#### condition

```python
@property
def condition() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSelectBool.condition"></a>

#### condition

```python
@condition.setter
def condition(value: bool) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSelectBool.if_true"></a>

#### if_true

```python
@property
def if_true() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSelectBool.if_true"></a>

#### if_true

```python
@if_true.setter
def if_true(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSelectBool.if_false"></a>

#### if_false

```python
@property
def if_false() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionSelectBool.if_false"></a>

#### if_false

```python
@if_false.setter
def if_false(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionSelectBool.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionSelectBool"></a>