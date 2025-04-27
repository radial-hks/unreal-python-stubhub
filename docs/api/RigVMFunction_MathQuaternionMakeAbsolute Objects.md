## RigVMFunction_MathQuaternionMakeAbsolute Objects

```python
class RigVMFunction_MathQuaternionMakeAbsolute(RigVMFunction_MathQuaternionBase
                                               )
```

Returns the absolute global transform within a parent's transform

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_MathQuaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``global_`` (Quat):  [Read-Write]
- ``local`` (Quat):  [Read-Write]
- ``parent`` (Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionMakeAbsolute.__init__"></a>

#### __init__

```python
def __init__(local: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             parent: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             global_: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMakeAbsolute.local"></a>

#### local

```python
@property
def local() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionMakeAbsolute.local"></a>

#### local

```python
@local.setter
def local(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMakeAbsolute.parent"></a>

#### parent

```python
@property
def parent() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigVMFunction_MathQuaternionMakeAbsolute.parent"></a>

#### parent

```python
@parent.setter
def parent(value: Quat) -> None
```

<a id="unreal.RigVMFunction_MathQuaternionMakeAbsolute.global_"></a>

#### global_

```python
@property
def global_() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_MathQuaternionMakeAbsolute"></a>