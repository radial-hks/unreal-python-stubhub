## RigPreferredEulerAngles Objects

```python
class RigPreferredEulerAngles(StructBase)
```

Rig Preferred Euler Angles

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``current`` (Vector):  [Read-Write]
- ``initial`` (Vector):  [Read-Write]
- ``rotation_order`` (EulerRotationOrder):  [Read-Write]

<a id="unreal.RigPreferredEulerAngles.__init__"></a>

#### __init__

```python
def __init__(rotation_order: EulerRotationOrder = EulerRotationOrder.XYZ,
             current: Vector = [0.000000, 0.000000, 0.000000],
             initial: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigPreferredEulerAngles.rotation_order"></a>

#### rotation_order

```python
@property
def rotation_order() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Only]

<a id="unreal.RigPreferredEulerAngles.current"></a>

#### current

```python
@property
def current() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigPreferredEulerAngles.initial"></a>

#### initial

```python
@property
def initial() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigControlSettings"></a>