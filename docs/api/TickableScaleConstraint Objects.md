## TickableScaleConstraint Objects

```python
class TickableScaleConstraint(TickableTransformConstraint)
```

UTickableScaleConstraint

**C++ Source:**

- **Module**: Constraints
- **File**: TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active`` (bool):  [Read-Write]
  todo: documentation.
- ``axis_filter`` (FilterOptionPerAxis):  [Read-Write] Defines which scale axis is constrained.
- ``child_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the child of that constraint.
- ``dynamic_offset`` (bool):  [Read-Write] Should the child be able to change it's offset dynamically.
- ``maintain_offset`` (bool):  [Read-Write] Should that constraint maintain the default offset.
- ``offset_scale`` (Vector):  [Read-Write] Defines the local child's scale offset in the parent space.
- ``parent_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the parent of that constraint.

<a id="unreal.TickableScaleConstraint.offset_scale"></a>

#### offset_scale

```python
@property
def offset_scale() -> Vector
```

(Vector):  [Read-Write] Defines the local child's scale offset in the parent space.

<a id="unreal.TickableScaleConstraint.offset_scale"></a>

#### offset_scale

```python
@offset_scale.setter
def offset_scale(value: Vector) -> None
```

<a id="unreal.TickableScaleConstraint.axis_filter"></a>

#### axis_filter

```python
@property
def axis_filter() -> FilterOptionPerAxis
```

(FilterOptionPerAxis):  [Read-Write] Defines which scale axis is constrained.

<a id="unreal.TickableScaleConstraint.axis_filter"></a>

#### axis_filter

```python
@axis_filter.setter
def axis_filter(value: FilterOptionPerAxis) -> None
```

<a id="unreal.TickableParentConstraint"></a>