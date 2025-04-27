## RigVMFunction_MathQuaternionNotEquals Objects

```python
class RigVMFunction_MathQuaternionNotEquals(RigVMFunction_MathQuaternionBase)
```

Returns true if the value A does not equal B

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Quat):  [Read-Write]
- ``b`` (Quat):  [Read-Write]
- ``result`` (bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionNotEquals.__init__"></a>

#### __init__

```python
def __init__(a: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             b: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionNotEquals.a"></a>

#### a

```python
@property
def a() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionNotEquals.a"></a>

#### a

```python
@a.setter
def a(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionNotEquals.b"></a>

#### b

```python
@property
def b() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionNotEquals.b"></a>

#### b

```python
@b.setter
def b(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionNotEquals.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionNotEquals"></a>