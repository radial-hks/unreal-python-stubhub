## ViewportWorldInteraction Objects

```python
class ViewportWorldInteraction(EditorWorldExtension)
```

Viewport World Interaction

**C++ Source:**

- **Module**: ViewportInteraction
- **File**: ViewportWorldInteraction.h

<a id="unreal.ViewportWorldInteraction.set_world_to_meters_scale"></a>

#### set_world_to_meters_scale

```python
def set_world_to_meters_scale(
        new_world_to_meters_scale: float,
        compensate_room_world_scale: bool = False) -> None
```

x.set_world_to_meters_scale(new_world_to_meters_scale, compensate_room_world_scale=False) -> None
Sets GNewWorldToMetersScale

Args:
    new_world_to_meters_scale (float): 
    compensate_room_world_scale (bool):

<a id="unreal.ViewportWorldInteraction.set_room_transform_for_next_frame"></a>

#### set_room_transform_for_next_frame

```python
def set_room_transform_for_next_frame(new_room_transform: Transform) -> None
```

x.set_room_transform_for_next_frame(new_room_transform) -> None
Set Room Transform for Next Frame

Args:
    new_room_transform (Transform):

<a id="unreal.ViewportWorldInteraction.set_head_transform"></a>

#### set_head_transform

```python
def set_head_transform(new_head_transform: Transform) -> None
```

x.set_head_transform(new_head_transform) -> None
Sets a new transform for the room so that the HMD is aligned to the new transform.
              The Head is kept level to the ground and only rotated on the yaw

Args:
    new_head_transform (Transform):

<a id="unreal.ViewportWorldInteraction.remove_interactor"></a>

#### remove_interactor

```python
def remove_interactor(interactor: ViewportInteractor) -> None
```

x.remove_interactor(interactor) -> None
Removes interactor from the worldinteraction and removes the interactor from its paired interactor if any

Args:
    interactor (ViewportInteractor):

<a id="unreal.ViewportWorldInteraction.get_world_scale_factor"></a>

#### get_world_scale_factor

```python
def get_world_scale_factor() -> float
```

x.get_world_scale_factor() -> float
Gets the world scale factor, which can be multiplied by a scale vector to convert to room space

Returns:
    float:

<a id="unreal.ViewportWorldInteraction.get_transform_gizmo_actor"></a>

#### get_transform_gizmo_actor

```python
def get_transform_gizmo_actor() -> BaseTransformGizmo
```

x.get_transform_gizmo_actor() -> BaseTransformGizmo
Gets the transform gizmo actor, or returns null if we currently don't have one

Returns:
    BaseTransformGizmo:

<a id="unreal.ViewportWorldInteraction.get_room_transform"></a>

#### get_room_transform

```python
def get_room_transform() -> Transform
```

x.get_room_transform() -> Transform
Gets the world space transform of the calibrated VR room origin.  When using a seated VR device, this will feel like the
      camera's world transform (before any HMD positional or rotation adjustments are applied.)

Returns:
    Transform:

<a id="unreal.ViewportWorldInteraction.get_room_space_head_transform"></a>

#### get_room_space_head_transform

```python
def get_room_space_head_transform() -> Transform
```

x.get_room_space_head_transform() -> Transform
Gets the transform of the viewport / user's HMD in room space

Returns:
    Transform:

<a id="unreal.ViewportWorldInteraction.get_interactors"></a>

#### get_interactors

```python
def get_interactors() -> Array[ViewportInteractor]
```

x.get_interactors() -> Array[ViewportInteractor]
Gets all the interactors

Returns:
    Array[ViewportInteractor]:

<a id="unreal.ViewportWorldInteraction.get_head_transform"></a>

#### get_head_transform

```python
def get_head_transform() -> Transform
```

x.get_head_transform() -> Transform
Gets the transform of the viewport / user's HMD in world space

Returns:
    Transform:

<a id="unreal.ViewportWorldInteraction.add_interactor"></a>

#### add_interactor

```python
def add_interactor(interactor: ViewportInteractor) -> None
```

x.add_interactor(interactor) -> None
Adds interactor to the worldinteraction

Args:
    interactor (ViewportInteractor):

<a id="unreal.ViewportWorldInteraction.add_actor_to_exclude_from_hit_tests"></a>

#### add_actor_to_exclude_from_hit_tests

```python
def add_actor_to_exclude_from_hit_tests(
        actor_to_exclude_from_hit_tests: Actor) -> None
```

x.add_actor_to_exclude_from_hit_tests(actor_to_exclude_from_hit_tests) -> None
Adds an actor to the list of actors to never allow an interactor to hit in the scene.  No selection.  No hover.
There's no need to remove actors from this list.  They'll expire from it automatically when destroyed.

Args:
    actor_to_exclude_from_hit_tests (Actor): The actor that should be forever excluded from hit tests

<a id="unreal.GizmoHandleGroup"></a>