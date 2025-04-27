## RigVMFunction_DebugBoxNoSpace Objects

```python
class RigVMFunction_DebugBoxNoSpace(RigVMFunction_DebugBaseMutable)
```

Draws a box in the viewport

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DebugPrimitives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box`` (Box):  [Read-Write]
- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``thickness`` (float):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugBoxNoSpace.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             box: Box = [[0.000000, 0.000000, 0.000000],
                         [0.000000, 0.000000, 0.000000], False],
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             thickness: float = 0.000000,
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigVMFunction_DebugBoxNoSpace.box"></a>

#### box

```python
@property
def box() -> Box
```

(Box):  [Read-Write]

<a id="unreal.RigVMFunction_DebugBoxNoSpace.box"></a>

#### box

```python
@box.setter
def box(value: Box) -> None
```

<a id="unreal.RigVMFunction_DebugBoxNoSpace.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_DebugBoxNoSpace.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_DebugBoxNoSpace.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugBoxNoSpace.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugBoxNoSpace.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugBoxNoSpace.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugBoxNoSpace.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_DebugBoxNoSpace.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigVMFunction_DebugTransformMutableNoSpace"></a>