## RigVMFunction_DebugLineNoSpace Objects

```python
class RigVMFunction_DebugLineNoSpace(RigVMFunction_DebugBaseMutable)
```

Draws a line in the viewport given a start and end vector

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DebugLine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (Vector):  [Read-Write]
- ``b`` (Vector):  [Read-Write]
- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``thickness`` (float):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineNoSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             a: Vector = [0.000000, 0.000000, 0.000000],
             b: Vector = [0.000000, 0.000000, 0.000000],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigVMFunction_DebugLineNoSpace.a"></a>

#### a

```python
@property
def a() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineNoSpace.a"></a>

#### a

```python
@a.setter
def a(value: Vector) -> None
```

<a id="unreal.RigVMFunction_DebugLineNoSpace.b"></a>

#### b

```python
@property
def b() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineNoSpace.b"></a>

#### b

```python
@b.setter
def b(value: Vector) -> None
```

<a id="unreal.RigVMFunction_DebugLineNoSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineNoSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_DebugLineNoSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineNoSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugLineNoSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineNoSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugLineNoSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_DebugLineNoSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigVMFunction_DebugLineStripNoSpace"></a>