## RigVMFunction_MathQuaternionMakeRelative Objects

```python
class RigVMFunction_MathQuaternionMakeRelative(RigVMFunction_MathQuaternionBase
                                               )
```

Returns the relative local transform within a parent's transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (Quat):  [Read-Write]
- ``local`` (Quat):  [Read-Write]
- ``parent`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionMakeRelative.__init__"></a>

#### __init__

```python
def __init__(global_: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             parent: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             local: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMakeRelative.global_"></a>

#### global_

```python
@property
def global_() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionMakeRelative.global_"></a>

#### global_

```python
@global_.setter
def global_(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMakeRelative.parent"></a>

#### parent

```python
@property
def parent() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionMakeRelative.parent"></a>

#### parent

```python
@parent.setter
def parent(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMakeRelative.local"></a>

#### local

```python
@property
def local() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionMakeRelative"></a>