## PhysicsSpringComponent Objects

```python
class PhysicsSpringComponent(SceneComponent)
```

Note: this component is still work in progress. Uses raycast springs for simple vehicle forces
   Used with objects that have physics to create a spring down the X direction
   ie. point X in the direction you want generate spring.

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsSpringComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``ignore_self`` (bool):  [Read-Write] If true, the spring will ignore all components in its own actor
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``spring_channel`` (CollisionChannel):  [Read-Write] Strength of thrust force applied to the base object.
- ``spring_compression`` (float):  [Read-Write] The current compression of the spring. A spring at rest will have SpringCompression 0.
- ``spring_damping`` (float):  [Read-Write] Specifies how quickly the spring can absorb energy of a body. The higher the damping the less oscillation
- ``spring_length_at_rest`` (float):  [Read-Write] Determines how long the spring will be along the X-axis at rest. The spring will apply 0 force on a body when it's at rest.
- ``spring_radius`` (float):  [Read-Write] Determines the radius of the spring.
- ``spring_stiffness`` (float):  [Read-Write] Specifies how much strength the spring has. The higher the SpringStiffness the more force the spring can push on a body with.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.PhysicsSpringComponent.spring_stiffness"></a>

#### spring_stiffness

```python
@property
def spring_stiffness() -> float
```

(float):  [Read-Write] Specifies how much strength the spring has. The higher the SpringStiffness the more force the spring can push on a body with.

<a id="unreal.PhysicsSpringComponent.spring_stiffness"></a>

#### spring_stiffness

```python
@spring_stiffness.setter
def spring_stiffness(value: float) -> None
```

<a id="unreal.PhysicsSpringComponent.spring_damping"></a>

#### spring_damping

```python
@property
def spring_damping() -> float
```

(float):  [Read-Write] Specifies how quickly the spring can absorb energy of a body. The higher the damping the less oscillation

<a id="unreal.PhysicsSpringComponent.spring_damping"></a>

#### spring_damping

```python
@spring_damping.setter
def spring_damping(value: float) -> None
```

<a id="unreal.PhysicsSpringComponent.spring_length_at_rest"></a>

#### spring_length_at_rest

```python
@property
def spring_length_at_rest() -> float
```

(float):  [Read-Write] Determines how long the spring will be along the X-axis at rest. The spring will apply 0 force on a body when it's at rest.

<a id="unreal.PhysicsSpringComponent.spring_length_at_rest"></a>

#### spring_length_at_rest

```python
@spring_length_at_rest.setter
def spring_length_at_rest(value: float) -> None
```

<a id="unreal.PhysicsSpringComponent.spring_radius"></a>

#### spring_radius

```python
@property
def spring_radius() -> float
```

(float):  [Read-Write] Determines the radius of the spring.

<a id="unreal.PhysicsSpringComponent.spring_radius"></a>

#### spring_radius

```python
@spring_radius.setter
def spring_radius(value: float) -> None
```

<a id="unreal.PhysicsSpringComponent.spring_channel"></a>

#### spring_channel

```python
@property
def spring_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write] Strength of thrust force applied to the base object.

<a id="unreal.PhysicsSpringComponent.spring_channel"></a>

#### spring_channel

```python
@spring_channel.setter
def spring_channel(value: CollisionChannel) -> None
```

<a id="unreal.PhysicsSpringComponent.ignore_self"></a>

#### ignore_self

```python
@property
def ignore_self() -> bool
```

(bool):  [Read-Write] If true, the spring will ignore all components in its own actor

<a id="unreal.PhysicsSpringComponent.ignore_self"></a>

#### ignore_self

```python
@ignore_self.setter
def ignore_self(value: bool) -> None
```

<a id="unreal.PhysicsSpringComponent.spring_compression"></a>

#### spring_compression

```python
@property
def spring_compression() -> float
```

(float):  [Read-Only] The current compression of the spring. A spring at rest will have SpringCompression 0.

<a id="unreal.PhysicsSpringComponent.get_spring_resting_point"></a>

#### get_spring_resting_point

```python
def get_spring_resting_point() -> Vector
```

x.get_spring_resting_point() -> Vector
Returns the spring resting point in world space.

Returns:
    Vector:

<a id="unreal.PhysicsSpringComponent.get_spring_direction"></a>

#### get_spring_direction

```python
def get_spring_direction() -> Vector
```

x.get_spring_direction() -> Vector
Returns the spring direction from start to resting point

Returns:
    Vector:

<a id="unreal.PhysicsSpringComponent.get_spring_current_end_point"></a>

#### get_spring_current_end_point

```python
def get_spring_current_end_point() -> Vector
```

x.get_spring_current_end_point() -> Vector
Returns the spring current end point in world space.

Returns:
    Vector:

<a id="unreal.PhysicsSpringComponent.get_normalized_compression_scalar"></a>

#### get_normalized_compression_scalar

```python
def get_normalized_compression_scalar() -> float
```

x.get_normalized_compression_scalar() -> float
Returns the spring compression as a normalized scalar along spring direction.
0 implies spring is at rest
1 implies fully compressed

Returns:
    float:

<a id="unreal.PhysicsThreadLibrary"></a>