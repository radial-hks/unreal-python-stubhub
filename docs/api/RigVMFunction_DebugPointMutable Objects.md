## RigVMFunction_DebugPointMutable Objects

```python
class RigVMFunction_DebugPointMutable(RigVMFunction_DebugBaseMutable)
```

Rig VMFunction Debug Point Mutable

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_DebugPoint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Only]
- ``execute_context`` (RigVMExecuteContext):  [Read-Write] * This property is used to chain multiple mutable nodes together
- ``mode`` (RigUnitDebugPointMode):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``space`` (Name):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``vector`` (Vector):  [Read-Write]
- ``world_offset`` (Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugPointMutable.__init__"></a>

#### __init__

```python
def __init__(execute_context: RigVMExecuteContext = [],
             vector: Vector = [0.000000, 0.000000, 0.000000],
             mode: RigUnitDebugPointMode = RigUnitDebugPointMode.POINT,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             scale: float = 0.000000,
             thickness: float = 0.000000,
             space: Name = "None",
             world_offset: Transform = [[0.000000, 0.000000, 0.000000],
                                        [-0.000000, 0.000000, 0.000000],
                                        [1.000000, 1.000000, 1.000000]],
             enabled: bool = False) -> None
```

<a id="unreal.RigVMFunction_DebugPointMutable.vector"></a>

#### vector

```python
@property
def vector() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_DebugPointMutable.vector"></a>

#### vector

```python
@vector.setter
def vector(value: Vector) -> None
```

<a id="unreal.RigVMFunction_DebugPointMutable.mode"></a>

#### mode

```python
@property
def mode() -> RigUnitDebugPointMode
```

(RigUnitDebugPointMode):  [Read-Write]

<a id="unreal.RigVMFunction_DebugPointMutable.mode"></a>

#### mode

```python
@mode.setter
def mode(value: RigUnitDebugPointMode) -> None
```

<a id="unreal.RigVMFunction_DebugPointMutable.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_DebugPointMutable.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_DebugPointMutable.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugPointMutable.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugPointMutable.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_DebugPointMutable.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_DebugPointMutable.space"></a>

#### space

```python
@property
def space() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_DebugPointMutable.space"></a>

#### space

```python
@space.setter
def space(value: Name) -> None
```

<a id="unreal.RigVMFunction_DebugPointMutable.world_offset"></a>

#### world_offset

```python
@property
def world_offset() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RigVMFunction_DebugPointMutable.world_offset"></a>

#### world_offset

```python
@world_offset.setter
def world_offset(value: Transform) -> None
```

<a id="unreal.RigVMFunction_DebugPointMutable.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_DebugPointMutable"></a>