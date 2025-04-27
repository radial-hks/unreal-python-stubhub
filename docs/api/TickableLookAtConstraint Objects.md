## TickableLookAtConstraint Objects

```python
class TickableLookAtConstraint(TickableTransformConstraint)
```

UTickableLookAtConstraint

**C++ Source:**

- **Module**: Constraints
- **File**: TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active`` (bool):  [Read-Write]
  todo: documentation.
- ``axis`` (Vector):  [Read-Write] Defines the aiming axis.
- ``child_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the child of that constraint.
- ``dynamic_offset`` (bool):  [Read-Write] Should the child be able to change it's offset dynamically.
- ``maintain_offset`` (bool):  [Read-Write] Should that constraint maintain the default offset.
- ``parent_trs_handle`` (TransformableHandle):  [Read-Write] The transformable handle representing the parent of that constraint.

<a id="unreal.TickableLookAtConstraint.axis"></a>

#### axis

```python
@property
def axis() -> Vector
```

(Vector):  [Read-Write] Defines the aiming axis.

<a id="unreal.TickableLookAtConstraint.axis"></a>

#### axis

```python
@axis.setter
def axis(value: Vector) -> None
```

<a id="unreal.SubobjectDataBlueprintFunctionLibrary"></a>