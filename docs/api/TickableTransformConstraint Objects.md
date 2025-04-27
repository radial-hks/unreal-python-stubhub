## TickableTransformConstraint Objects

```python
class TickableTransformConstraint(TickableConstraint)
```

UTickableTransformConstraint

**C++ Source:**

- **Module**: Constraints
- **File**: TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active`` (bool):  [Read-Write]
  todo: documentation.
- ``child_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the child of that constraint.
- ``dynamic_offset`` (bool):  [Read-Write] Should the child be able to change it's offset dynamically.
- ``maintain_offset`` (bool):  [Read-Write] Should that constraint maintain the default offset.
- ``parent_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the parent of that constraint.

<a id="unreal.TickableTransformConstraint.parent_trs_handle"></a>

#### parent_trs_handle

```python
@property
def parent_trs_handle() -> TransformableHandle
```

(TransformableHandle):  [Read-Write] The transformable handle representing the parent of that constraint.

<a id="unreal.TickableTransformConstraint.parent_trs_handle"></a>

#### parent_trs_handle

```python
@parent_trs_handle.setter
def parent_trs_handle(value: TransformableHandle) -> None
```

<a id="unreal.TickableTransformConstraint.child_trs_handle"></a>

#### child_trs_handle

```python
@property
def child_trs_handle() -> TransformableHandle
```

(TransformableHandle):  [Read-Write] The transformable handle representing the child of that constraint.

<a id="unreal.TickableTransformConstraint.child_trs_handle"></a>

#### child_trs_handle

```python
@child_trs_handle.setter
def child_trs_handle(value: TransformableHandle) -> None
```

<a id="unreal.TickableTransformConstraint.maintain_offset"></a>

#### maintain_offset

```python
@property
def maintain_offset() -> bool
```

(bool):  [Read-Write] Should that constraint maintain the default offset.

<a id="unreal.TickableTransformConstraint.maintain_offset"></a>

#### maintain_offset

```python
@maintain_offset.setter
def maintain_offset(value: bool) -> None
```

<a id="unreal.TickableTransformConstraint.dynamic_offset"></a>

#### dynamic_offset

```python
@property
def dynamic_offset() -> bool
```

(bool):  [Read-Write] Should the child be able to change it's offset dynamically.

<a id="unreal.TickableTransformConstraint.dynamic_offset"></a>

#### dynamic_offset

```python
@dynamic_offset.setter
def dynamic_offset(value: bool) -> None
```

<a id="unreal.TickableTranslationConstraint"></a>