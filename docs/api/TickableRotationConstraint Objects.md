## TickableRotationConstraint Objects

```python
class TickableRotationConstraint(TickableTransformConstraint)
```

UTickableRotationConstraint

**C++ Source:**

- **Module**: Constraints
- **File**: TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active`` (bool):  [Read-Write]
  todo: documentation.
- ``axis_filter`` (FilterOptionPerAxis):  [Read-Write] Defines which rotation axis is constrained.
- ``child_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the child of that constraint.
- ``dynamic_offset`` (bool):  [Read-Write] Should the child be able to change it's offset dynamically.
- ``maintain_offset`` (bool):  [Read-Write] Should that constraint maintain the default offset.
- ``offset_rotation`` (Quat):  [Read-Write] Defines the local child's rotation offset in the parent space.
- ``parent_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the parent of that constraint.

<a id="unreal.TickableRotationConstraint.offset_rotation"></a>

#### offset_rotation

```python
@property
def offset_rotation() -> Quat
```

(Quat):  [Read-Write] Defines the local child's rotation offset in the parent space.

<a id="unreal.TickableRotationConstraint.offset_rotation"></a>

#### offset_rotation

```python
@offset_rotation.setter
def offset_rotation(value: Quat) -> None
```

<a id="unreal.TickableRotationConstraint.axis_filter"></a>

#### axis_filter

```python
@property
def axis_filter() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write] Defines which rotation axis is constrained.

<a id="unreal.TickableRotationConstraint.axis_filter"></a>

#### axis_filter

```python
@axis_filter.setter
def axis_filter(value: FilterOptionPerAxis) -> None
```

<a id="unreal.TickableScaleConstraint"></a>