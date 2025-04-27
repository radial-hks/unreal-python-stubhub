## RigVMFunction_VisualDebugVector Objects

```python
class RigVMFunction_VisualDebugVector(RigVMFunction_DebugBase)
```

Rig VMFunction Visual Debug Vector

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_VisualDebug.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_space`` (Name):  [Read-Write]
- ``color`` (LinearColor):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``mode`` (RigUnitVisualDebugPointMode):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugVector.__init__"></a>

#### __init__

```python
def __init__(
        value: Vector = [0.000000, 0.000000, 0.000000],
        enabled: bool = False,
        mode: RigUnitVisualDebugPointMode = RigUnitVisualDebugPointMode.POINT,
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        thickness: float = 0.000000,
        scale: float = 0.000000,
        bone_space: Name = "None") -> None
```

<a id="unreal.RigVMFunction_VisualDebugVector.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugVector.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_VisualDebugVector.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugVector.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigVMFunction_VisualDebugVector.mode"></a>

#### mode

```python
@property
def mode() -> RigUnitVisualDebugPointMode
```

(RigUnitVisualDebugPointMode):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugVector.mode"></a>

#### mode

```python
@mode.setter
def mode(value: RigUnitVisualDebugPointMode) -> None
```

<a id="unreal.RigVMFunction_VisualDebugVector.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugVector.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.RigVMFunction_VisualDebugVector.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugVector.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigVMFunction_VisualDebugVector.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugVector.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigVMFunction_VisualDebugVector.bone_space"></a>

#### bone_space

```python
@property
def bone_space() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigVMFunction_VisualDebugVector.bone_space"></a>

#### bone_space

```python
@bone_space.setter
def bone_space(value: Name) -> None
```

<a id="unreal.RigVMFunction_VisualDebugVectorNoSpace"></a>