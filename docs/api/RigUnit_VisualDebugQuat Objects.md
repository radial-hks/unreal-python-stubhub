## RigUnit_VisualDebugQuat Objects

```python
class RigUnit_VisualDebugQuat(RigUnit_DebugBase)
```

Rig Unit Visual Debug Quat

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_VisualDebug.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_space`` (Name):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``scale`` (float):  [Read-Write]
- ``thickness`` (float):  [Read-Write]
- ``value`` (Quat):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugQuat.__init__"></a>

#### __init__

```python
def __init__(value: Quat = [0.000000, 0.000000, 0.000000, 1.000000],
             enabled: bool = False,
             thickness: float = 0.000000,
             scale: float = 0.000000,
             bone_space: Name = "None") -> None
```

<a id="unreal.RigUnit_VisualDebugQuat.value"></a>

#### value

```python
@property
def value() -> Quat
```

(Quat):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugQuat.value"></a>

#### value

```python
@value.setter
def value(value: Quat) -> None
```

<a id="unreal.RigUnit_VisualDebugQuat.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugQuat.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.RigUnit_VisualDebugQuat.thickness"></a>

#### thickness

```python
@property
def thickness() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugQuat.thickness"></a>

#### thickness

```python
@thickness.setter
def thickness(value: float) -> None
```

<a id="unreal.RigUnit_VisualDebugQuat.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugQuat.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.RigUnit_VisualDebugQuat.bone_space"></a>

#### bone_space

```python
@property
def bone_space() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_VisualDebugQuat.bone_space"></a>

#### bone_space

```python
@bone_space.setter
def bone_space(value: Name) -> None
```

<a id="unreal.RigUnit_VisualDebugQuatItemSpace"></a>