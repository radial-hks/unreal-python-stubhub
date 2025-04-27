## RigUnit_Harmonics_TargetItem Objects

```python
class RigUnit_Harmonics_TargetItem(StructBase)
```

Rig Unit Harmonics Target Item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_BoneHarmonics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] The name of the item to drive
- ``ratio`` (float):  [Read-Only] The ratio of where the item sits within the harmonics system.
  Valid values reach from 0.0 to 1.0

<a id="unreal.RigUnit_Harmonics_TargetItem.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             ratio: float = 0.000000) -> None
```

<a id="unreal.RigUnit_Harmonics_TargetItem.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The name of the item to drive

<a id="unreal.RigUnit_Harmonics_TargetItem.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_Harmonics_TargetItem.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Only] The ratio of where the item sits within the harmonics system.
Valid values reach from 0.0 to 1.0

<a id="unreal.RigUnit_BoneHarmonics"></a>