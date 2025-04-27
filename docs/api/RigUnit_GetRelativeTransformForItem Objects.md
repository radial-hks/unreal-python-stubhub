## RigUnit_GetRelativeTransformForItem Objects

```python
class RigUnit_GetRelativeTransformForItem(RigUnit)
```

GetRelativeTransform is used to retrieve a single transform from a hierarchy in the space of another transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetRelativeTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write] The child item to retrieve the transform for
- ``child_initial`` (bool):  [Read-Write] Defines if the child's transform should be retrieved as current (false) or initial (true).
  Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.
- ``parent`` (RigElementKey):  [Read-Write] The parent item to use.
  The child transform will be retrieve in the space of the parent.
- ``parent_initial`` (bool):  [Read-Write] Defines if the parent's transform should be retrieved as current (false) or initial (true).
  Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.
- ``relative_transform`` (Transform):  [Read-Write] The transform of the given child item relative to the provided parent

<a id="unreal.RigUnit_GetRelativeTransformForItem.__init__"></a>

#### __init__

```python
def __init__(
    child: RigElementKey = [RigElementType.NONE, "None"],
    child_initial: bool = False,
    parent: RigElementKey = [RigElementType.NONE, "None"],
    parent_initial: bool = False,
    relative_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_GetRelativeTransformForItem.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] The child item to retrieve the transform for

<a id="unreal.RigUnit_GetRelativeTransformForItem.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_GetRelativeTransformForItem.child_initial"></a>

#### child_initial

```python
@property
def child_initial() -> bool
```

(bool):  [Read-Write] Defines if the child's transform should be retrieved as current (false) or initial (true).
Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.

<a id="unreal.RigUnit_GetRelativeTransformForItem.child_initial"></a>

#### child_initial

```python
@child_initial.setter
def child_initial(value: bool) -> None
```

<a id="unreal.RigUnit_GetRelativeTransformForItem.parent"></a>

#### parent

```python
@property
def parent() -> RigElementKey
```

(RigElementKey):  [Read-Write] The parent item to use.
The child transform will be retrieve in the space of the parent.

<a id="unreal.RigUnit_GetRelativeTransformForItem.parent"></a>

#### parent

```python
@parent.setter
def parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_GetRelativeTransformForItem.parent_initial"></a>

#### parent_initial

```python
@property
def parent_initial() -> bool
```

(bool):  [Read-Write] Defines if the parent's transform should be retrieved as current (false) or initial (true).
Initial transforms for bones and other elements in the hierarchy represent the reference pose's value.

<a id="unreal.RigUnit_GetRelativeTransformForItem.parent_initial"></a>

#### parent_initial

```python
@parent_initial.setter
def parent_initial(value: bool) -> None
```

<a id="unreal.RigUnit_GetRelativeTransformForItem.relative_transform"></a>

#### relative_transform

```python
@property
def relative_transform() -> Transform
```

(Transform):  [Read-Only] The transform of the given child item relative to the provided parent

<a id="unreal.RigUnit_GetSpaceTransform"></a>