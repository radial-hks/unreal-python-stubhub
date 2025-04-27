## TypedElementWorldInterface Objects

```python
class TypedElementWorldInterface(Interface)
```

Typed Element World Interface

**C++ Source:**

- **Module**: Engine
- **File**: TypedElementWorldInterface.h

<a id="unreal.TypedElementWorldInterface.set_world_transform"></a>

#### set_world_transform

```python
def set_world_transform(element_handle: ScriptTypedElementHandle,
                        transform: Transform) -> bool
```

x.set_world_transform(element_handle, transform) -> bool
Attempt to set the transform of this element within its owner world.

Args:
    element_handle (ScriptTypedElementHandle): 
    transform (Transform): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.set_relative_transform"></a>

#### set_relative_transform

```python
def set_relative_transform(element_handle: ScriptTypedElementHandle,
                           transform: Transform) -> bool
```

x.set_relative_transform(element_handle, transform) -> bool
Attempt to set the transform of this element relative to its parent.

Args:
    element_handle (ScriptTypedElementHandle): 
    transform (Transform): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.set_pivot_offset"></a>

#### set_pivot_offset

```python
def set_pivot_offset(element_handle: ScriptTypedElementHandle,
                     pivot_offset: Vector) -> bool
```

x.set_pivot_offset(element_handle, pivot_offset) -> bool
Attempt to set the local space offset of this element that should be added to its pivot location.

Args:
    element_handle (ScriptTypedElementHandle): 
    pivot_offset (Vector): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.promote_element"></a>

#### promote_element

```python
def promote_element(element_handle: ScriptTypedElementHandle,
                    override_world: World = None) -> ScriptTypedElementHandle
```

x.promote_element(element_handle, override_world=None) -> ScriptTypedElementHandle
Promote an element when possible
Generally available when the element is a lighter representation of another element.
Like an instance for example.

Args:
    element_handle (ScriptTypedElementHandle): 
    override_world (World): Override the world in which the promotion might create new elements. Leave it to null to use the world from the handle.

Returns:
    ScriptTypedElementHandle:

<a id="unreal.TypedElementWorldInterface.notify_movement_started"></a>

#### notify_movement_started

```python
def notify_movement_started(element_handle: ScriptTypedElementHandle) -> None
```

x.notify_movement_started(element_handle) -> None
Notify that this element is about to be moved.

Args:
    element_handle (ScriptTypedElementHandle):

<a id="unreal.TypedElementWorldInterface.notify_movement_ongoing"></a>

#### notify_movement_ongoing

```python
def notify_movement_ongoing(element_handle: ScriptTypedElementHandle) -> None
```

x.notify_movement_ongoing(element_handle) -> None
Notify that this element is currently being moved.

Args:
    element_handle (ScriptTypedElementHandle):

<a id="unreal.TypedElementWorldInterface.notify_movement_ended"></a>

#### notify_movement_ended

```python
def notify_movement_ended(element_handle: ScriptTypedElementHandle) -> None
```

x.notify_movement_ended(element_handle) -> None
Notify that this element is done being moved.

Args:
    element_handle (ScriptTypedElementHandle):

<a id="unreal.TypedElementWorldInterface.is_template_element"></a>

#### is_template_element

```python
def is_template_element(element_handle: ScriptTypedElementHandle) -> bool
```

x.is_template_element(element_handle) -> bool
Is this element considered a template within its world (eg, a CDO or archetype).

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.get_world_transform"></a>

#### get_world_transform

```python
def get_world_transform(
        element_handle: ScriptTypedElementHandle) -> Optional[Transform]
```

x.get_world_transform(element_handle) -> Transform or None
Get the transform of this element within its owner world, if any.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    Transform or None: 

    out_transform (Transform):

<a id="unreal.TypedElementWorldInterface.get_relative_transform"></a>

#### get_relative_transform

```python
def get_relative_transform(
        element_handle: ScriptTypedElementHandle) -> Optional[Transform]
```

x.get_relative_transform(element_handle) -> Transform or None
Get the transform of this element relative to its parent, if any.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    Transform or None: 

    out_transform (Transform):

<a id="unreal.TypedElementWorldInterface.get_pivot_offset"></a>

#### get_pivot_offset

```python
def get_pivot_offset(
        element_handle: ScriptTypedElementHandle) -> Optional[Vector]
```

x.get_pivot_offset(element_handle) -> Vector or None
Get the local space offset of this element that should be added to its pivot location, if any.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    Vector or None: 

    out_pivot_offset (Vector):

<a id="unreal.TypedElementWorldInterface.get_owner_world"></a>

#### get_owner_world

```python
def get_owner_world(element_handle: ScriptTypedElementHandle) -> World
```

x.get_owner_world(element_handle) -> World
Get the owner world associated with this element, if any.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    World:

<a id="unreal.TypedElementWorldInterface.get_owner_level"></a>

#### get_owner_level

```python
def get_owner_level(element_handle: ScriptTypedElementHandle) -> Level
```

x.get_owner_level(element_handle) -> Level
Get the owner level associated with this element, if any.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    Level:

<a id="unreal.TypedElementWorldInterface.get_bounds"></a>

#### get_bounds

```python
def get_bounds(
        element_handle: ScriptTypedElementHandle) -> Optional[BoxSphereBounds]
```

x.get_bounds(element_handle) -> BoxSphereBounds or None
Get the bounds of this element, if any.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    BoxSphereBounds or None: 

    out_bounds (BoxSphereBounds):

<a id="unreal.TypedElementWorldInterface.duplicate_element"></a>

#### duplicate_element

```python
def duplicate_element(element_handle: ScriptTypedElementHandle, world: World,
                      location_offset: Vector) -> ScriptTypedElementHandle
```

x.duplicate_element(element_handle, world, location_offset) -> ScriptTypedElementHandle
Duplicate the given element.
note: Default version calls DuplicateElements with a single element.

Args:
    element_handle (ScriptTypedElementHandle): 
    world (World): 
    location_offset (Vector): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.TypedElementWorldInterface.delete_element"></a>

#### delete_element

```python
def delete_element(element_handle: ScriptTypedElementHandle, world: World,
                   selection_set: TypedElementSelectionSet,
                   deletion_options: TypedElementDeletionOptions) -> bool
```

x.delete_element(element_handle, world, selection_set, deletion_options) -> bool
Delete the given element.
note: Default version calls DeleteElements with a single element.

Args:
    element_handle (ScriptTypedElementHandle): 
    world (World): 
    selection_set (TypedElementSelectionSet): 
    deletion_options (TypedElementDeletionOptions): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.can_scale_element"></a>

#### can_scale_element

```python
def can_scale_element(element_handle: ScriptTypedElementHandle) -> bool
```

x.can_scale_element(element_handle) -> bool
Can the given element be scaled?

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.can_promote_element"></a>

#### can_promote_element

```python
def can_promote_element(element_handle: ScriptTypedElementHandle) -> bool
```

x.can_promote_element(element_handle) -> bool
Can the element be promoted
Generally available when the element is a lighter representation of another element.
Like an instance for example.

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.can_move_element"></a>

#### can_move_element

```python
def can_move_element(element_handle: ScriptTypedElementHandle,
                     world_type: TypedElementWorldType) -> bool
```

x.can_move_element(element_handle, world_type) -> bool
Can the given element be moved within the world?

Args:
    element_handle (ScriptTypedElementHandle): 
    world_type (TypedElementWorldType): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.can_edit_element"></a>

#### can_edit_element

```python
def can_edit_element(element_handle: ScriptTypedElementHandle) -> bool
```

x.can_edit_element(element_handle) -> bool
Can this element actually be edited in the world?

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.can_duplicate_element"></a>

#### can_duplicate_element

```python
def can_duplicate_element(element_handle: ScriptTypedElementHandle) -> bool
```

x.can_duplicate_element(element_handle) -> bool
Can the given element be duplicated?

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.TypedElementWorldInterface.can_delete_element"></a>

#### can_delete_element

```python
def can_delete_element(element_handle: ScriptTypedElementHandle) -> bool
```

x.can_delete_element(element_handle) -> bool
Can the given element be deleted?

Args:
    element_handle (ScriptTypedElementHandle): 

Returns:
    bool:

<a id="unreal.CancellableAsyncAction"></a>