## RigUnit\_ProjectTransformToNewParent Objects

```python
class RigUnit_ProjectTransformToNewParent(RigUnit)
```

Gets the relative offset between the child and the old parent, then multiplies by new parent's transform.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_ProjectTransformToNewParent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``child`` (RigElementKey):  [Read-Write] The element to project between parents
- ``child_initial`` (bool):  [Read-Write] If set to true the child will be retrieved in its initial transform
- ``new_parent`` (RigElementKey):  [Read-Write] The new parent of the child.
- ``new_parent_initial`` (bool):  [Read-Write] If set to true the new parent will be retrieved in its initial transform
- ``old_parent`` (RigElementKey):  [Read-Write] The original parent of the child.
  Can be an actual parent in the hierarchy or any other
  item you want to use to compute to offset against.
- ``old_parent_initial`` (bool):  [Read-Write] If set to true the old parent will be retrieved in its initial transform
- ``transform`` (Transform):  [Read-Write] The resulting transform

<a id="unreal.RigUnit_ProjectTransformToNewParent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    child: RigElementKey = [RigElementType.NONE, "None"],
    child_initial: bool = False,
    old_parent: RigElementKey = [RigElementType.NONE, "None"],
    old_parent_initial: bool = False,
    new_parent: RigElementKey = [RigElementType.NONE, "None"],
    new_parent_initial: bool = False,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigUnit_ProjectTransformToNewParent.child"></a>

#### child

```python
@property
def child() -> RigElementKey
```

(RigElementKey):  [Read-Write] The element to project between parents

<a id="unreal.RigUnit_ProjectTransformToNewParent.child"></a>

#### child

```python
@child.setter
def child(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ProjectTransformToNewParent.child_initial"></a>

#### child\_initial

```python
@property
def child_initial() -> bool
```

(bool):  [Read-Write] If set to true the child will be retrieved in its initial transform

<a id="unreal.RigUnit_ProjectTransformToNewParent.child_initial"></a>

#### child\_initial

```python
@child_initial.setter
def child_initial(value: bool) -> None
```

<a id="unreal.RigUnit_ProjectTransformToNewParent.old_parent"></a>

#### old\_parent

```python
@property
def old_parent() -> RigElementKey
```

(RigElementKey):  [Read-Write] The original parent of the child.
Can be an actual parent in the hierarchy or any other
item you want to use to compute to offset against.

<a id="unreal.RigUnit_ProjectTransformToNewParent.old_parent"></a>

#### old\_parent

```python
@old_parent.setter
def old_parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ProjectTransformToNewParent.old_parent_initial"></a>

#### old\_parent\_initial

```python
@property
def old_parent_initial() -> bool
```

(bool):  [Read-Write] If set to true the old parent will be retrieved in its initial transform

<a id="unreal.RigUnit_ProjectTransformToNewParent.old_parent_initial"></a>

#### old\_parent\_initial

```python
@old_parent_initial.setter
def old_parent_initial(value: bool) -> None
```

<a id="unreal.RigUnit_ProjectTransformToNewParent.new_parent"></a>

#### new\_parent

```python
@property
def new_parent() -> RigElementKey
```

(RigElementKey):  [Read-Write] The new parent of the child.

<a id="unreal.RigUnit_ProjectTransformToNewParent.new_parent"></a>

#### new\_parent

```python
@new_parent.setter
def new_parent(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ProjectTransformToNewParent.new_parent_initial"></a>

#### new\_parent\_initial

```python
@property
def new_parent_initial() -> bool
```

(bool):  [Read-Write] If set to true the new parent will be retrieved in its initial transform

<a id="unreal.RigUnit_ProjectTransformToNewParent.new_parent_initial"></a>

#### new\_parent\_initial

```python
@new_parent_initial.setter
def new_parent_initial(value: bool) -> None
```

<a id="unreal.RigUnit_ProjectTransformToNewParent.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only] The resulting transform

<a id="unreal.RigUnit_PropagateTransform"></a>