## PhysicsHandleComponent Objects

```python
class PhysicsHandleComponent(ActorComponent)
```

Utility object for moving physics objects around.

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsHandleComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angular_damping`` (float):  [Read-Write] Angular damping of the handle spring
- ``angular_stiffness`` (float):  [Read-Write] Angular stiffness of the handle spring
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``interpolate_target`` (bool):  [Read-Write]
- ``interpolation_speed`` (float):  [Read-Write] How quickly we interpolate the physics target transform
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``linear_damping`` (float):  [Read-Write] Linear damping of the handle spring.
- ``linear_stiffness`` (float):  [Read-Write] Linear stiffness of the handle spring
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``soft_angular_constraint`` (bool):  [Read-Write]
- ``soft_linear_constraint`` (bool):  [Read-Write]

<a id="unreal.PhysicsHandleComponent.soft_angular_constraint"></a>

#### soft_angular_constraint

```python
@property
def soft_angular_constraint() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PhysicsHandleComponent.soft_linear_constraint"></a>

#### soft_linear_constraint

```python
@property
def soft_linear_constraint() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PhysicsHandleComponent.interpolate_target"></a>

#### interpolate_target

```python
@property
def interpolate_target() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PhysicsHandleComponent.interpolate_target"></a>

#### interpolate_target

```python
@interpolate_target.setter
def interpolate_target(value: bool) -> None
```

<a id="unreal.PhysicsHandleComponent.linear_damping"></a>

#### linear_damping

```python
@property
def linear_damping() -> float
```

(float):  [Read-Only] Linear damping of the handle spring.

<a id="unreal.PhysicsHandleComponent.linear_stiffness"></a>

#### linear_stiffness

```python
@property
def linear_stiffness() -> float
```

(float):  [Read-Only] Linear stiffness of the handle spring

<a id="unreal.PhysicsHandleComponent.angular_damping"></a>

#### angular_damping

```python
@property
def angular_damping() -> float
```

(float):  [Read-Only] Angular damping of the handle spring

<a id="unreal.PhysicsHandleComponent.angular_stiffness"></a>

#### angular_stiffness

```python
@property
def angular_stiffness() -> float
```

(float):  [Read-Only] Angular stiffness of the handle spring

<a id="unreal.PhysicsHandleComponent.interpolation_speed"></a>

#### interpolation_speed

```python
@property
def interpolation_speed() -> float
```

(float):  [Read-Only] How quickly we interpolate the physics target transform

<a id="unreal.PhysicsHandleComponent.set_target_rotation"></a>

#### set_target_rotation

```python
def set_target_rotation(new_rotation: Rotator) -> None
```

x.set_target_rotation(new_rotation) -> None
Set the target rotation

Args:
    new_rotation (Rotator):

<a id="unreal.PhysicsHandleComponent.set_target_location_and_rotation"></a>

#### set_target_location_and_rotation

```python
def set_target_location_and_rotation(new_location: Vector,
                                     new_rotation: Rotator) -> None
```

x.set_target_location_and_rotation(new_location, new_rotation) -> None
Set target location and rotation

Args:
    new_location (Vector): 
    new_rotation (Rotator):

<a id="unreal.PhysicsHandleComponent.set_target_location"></a>

#### set_target_location

```python
def set_target_location(new_location: Vector) -> None
```

x.set_target_location(new_location) -> None
Set the target location

Args:
    new_location (Vector):

<a id="unreal.PhysicsHandleComponent.set_linear_stiffness"></a>

#### set_linear_stiffness

```python
def set_linear_stiffness(new_linear_stiffness: float) -> None
```

x.set_linear_stiffness(new_linear_stiffness) -> None
Set linear stiffness

Args:
    new_linear_stiffness (float):

<a id="unreal.PhysicsHandleComponent.set_linear_damping"></a>

#### set_linear_damping

```python
def set_linear_damping(new_linear_damping: float) -> None
```

x.set_linear_damping(new_linear_damping) -> None
Set linear damping

Args:
    new_linear_damping (float):

<a id="unreal.PhysicsHandleComponent.set_interpolation_speed"></a>

#### set_interpolation_speed

```python
def set_interpolation_speed(new_interpolation_speed: float) -> None
```

x.set_interpolation_speed(new_interpolation_speed) -> None
Set interpolation speed

Args:
    new_interpolation_speed (float):

<a id="unreal.PhysicsHandleComponent.set_angular_stiffness"></a>

#### set_angular_stiffness

```python
def set_angular_stiffness(new_angular_stiffness: float) -> None
```

x.set_angular_stiffness(new_angular_stiffness) -> None
Set angular stiffness

Args:
    new_angular_stiffness (float):

<a id="unreal.PhysicsHandleComponent.set_angular_damping"></a>

#### set_angular_damping

```python
def set_angular_damping(new_angular_damping: float) -> None
```

x.set_angular_damping(new_angular_damping) -> None
Set angular damping

Args:
    new_angular_damping (float):

<a id="unreal.PhysicsHandleComponent.release_component"></a>

#### release_component

```python
def release_component() -> None
```

x.release_component() -> None
Release the currently held component

<a id="unreal.PhysicsHandleComponent.grab_component_at_location_with_rotation"></a>

#### grab_component_at_location_with_rotation

```python
def grab_component_at_location_with_rotation(component: PrimitiveComponent,
                                             bone_name: Name, location: Vector,
                                             rotation: Rotator) -> None
```

x.grab_component_at_location_with_rotation(component, bone_name, location, rotation) -> None
Grab the specified component at a given location and rotation. Constrains rotation.

Args:
    component (PrimitiveComponent): 
    bone_name (Name): 
    location (Vector): 
    rotation (Rotator):

<a id="unreal.PhysicsHandleComponent.grab_component_at_location"></a>

#### grab_component_at_location

```python
def grab_component_at_location(component: PrimitiveComponent, bone_name: Name,
                               grab_location: Vector) -> None
```

x.grab_component_at_location(component, bone_name, grab_location) -> None
Grab the specified component at a given location. Does NOT constraint rotation which means the handle will pivot about GrabLocation.

Args:
    component (PrimitiveComponent): 
    bone_name (Name): 
    grab_location (Vector):

<a id="unreal.PhysicsHandleComponent.grab_component"></a>

#### grab_component

```python
def grab_component(component: PrimitiveComponent, bone_name: Name,
                   grab_location: Vector, constrain_rotation: bool) -> None
```

x.grab_component(component, bone_name, grab_location, constrain_rotation) -> None
Grab Component
deprecated: Please use GrabComponentAtLocation or GrabComponentAtLocationWithRotation

Args:
    component (PrimitiveComponent): 
    bone_name (Name): 
    grab_location (Vector): 
    constrain_rotation (bool):

<a id="unreal.PhysicsHandleComponent.get_target_location_and_rotation"></a>

#### get_target_location_and_rotation

```python
def get_target_location_and_rotation() -> Tuple[Vector, Rotator]
```

x.get_target_location_and_rotation() -> (target_location=Vector, target_rotation=Rotator)
Get the current location and rotation

Returns:
    tuple: 

    target_location (Vector): 

    target_rotation (Rotator):

<a id="unreal.PhysicsHandleComponent.get_grabbed_component"></a>

#### get_grabbed_component

```python
def get_grabbed_component() -> PrimitiveComponent
```

x.get_grabbed_component() -> PrimitiveComponent
Returns the currently grabbed component, or null if nothing is grabbed.

Returns:
    PrimitiveComponent:

<a id="unreal.RB_Handle"></a>