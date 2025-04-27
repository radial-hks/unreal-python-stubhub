## TickableParentConstraint Objects

```python
class TickableParentConstraint(TickableTransformConstraint)
```

UTickableParentConstraint

**C++ Source:**

- **Module**: Constraints
- **File**: TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active`` (bool):  [Read-Write]
  todo: documentation.
- ``child_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the child of that constraint.
- ``dynamic_offset`` (bool):  [Read-Write] Should the child be able to change it's offset dynamically.
- ``maintain_offset`` (bool):  [Read-Write] Should that constraint maintain the default offset.
- ``offset_transform`` (Transform):  [Read-Write] Defines the local child's transform offset in the parent space.
- ``parent_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the parent of that constraint.
- ``scaling`` (bool):  [Read-Write] Defines whether we propagate the parent scale.
- ``transform_filter`` (TransformFilter):  [Read-Write] Defines which translation/rotation/scale axis are constrained.

<a id="unreal.TickableParentConstraint.offset_transform"></a>

#### offset_transform

```python
@property
def offset_transform() -> Transform
```

(Transform):  [Read-Write] Defines the local child's transform offset in the parent space.

<a id="unreal.TickableParentConstraint.offset_transform"></a>

#### offset_transform

```python
@offset_transform.setter
def offset_transform(value: Transform) -> None
```

<a id="unreal.TickableParentConstraint.scaling"></a>

#### scaling

```python
@property
def scaling() -> bool
```

(bool):  [Read-Write] Defines whether we propagate the parent scale.

<a id="unreal.TickableParentConstraint.scaling"></a>

#### scaling

```python
@scaling.setter
def scaling(value: bool) -> None
```

<a id="unreal.TickableParentConstraint.transform_filter"></a>

#### transform_filter

```python
@property
def transform_filter() -> TransformFilter
```

(TransformFilter):  [Read-Write] Defines which translation/rotation/scale axis are constrained.

<a id="unreal.TickableParentConstraint.transform_filter"></a>

#### transform_filter

```python
@transform_filter.setter
def transform_filter(value: TransformFilter) -> None
```

<a id="unreal.TickableLookAtConstraint"></a>