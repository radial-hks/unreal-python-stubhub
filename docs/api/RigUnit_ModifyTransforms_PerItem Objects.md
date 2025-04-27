## RigUnit_ModifyTransforms_PerItem Objects

```python
class RigUnit_ModifyTransforms_PerItem(StructBase)
```

Rig Unit Modify Transforms Per Item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ModifyTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] The item to set the transform for.
- ``transform`` (Transform):  [Read-Write] The transform value to set for the given Bone.

<a id="unreal.RigUnit_ModifyTransforms_PerItem.__init__"></a>

#### __init__

```python
def __init__(
    item: RigElementKey = [RigElementType.NONE, "None"],
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_ModifyTransforms_PerItem.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] The item to set the transform for.

<a id="unreal.RigUnit_ModifyTransforms_PerItem.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ModifyTransforms_PerItem.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] The transform value to set for the given Bone.

<a id="unreal.RigUnit_ModifyTransforms_PerItem.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.RigUnit_ModifyTransforms"></a>