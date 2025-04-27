## RigVMFunction_MathQuaternionEquals Objects

```python
class RigVMFunction_MathQuaternionEquals(RigVMFunction_MathQuaternionBase)
```

Returns true if the value A equals B

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Quat):  [Read-Write]
- ``b`` (Quat):  [Read-Write]
- ``result`` (bool):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionEquals.__init__"></a>

#### __init__

```python
def __init__(a: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             b: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             result: bool = False) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionEquals.a"></a>

#### a

```python
@property
def a() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionEquals.a"></a>

#### a

```python
@a.setter
def a(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionEquals.b"></a>

#### b

```python
@property
def b() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionEquals.b"></a>

#### b

```python
@b.setter
def b(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionEquals.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionEquals"></a>