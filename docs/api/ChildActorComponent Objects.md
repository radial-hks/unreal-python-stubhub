## ChildActorComponent Objects

```python
class ChildActorComponent(SceneComponent)
```

A component that spawns an Actor when registered, and destroys it when unregistered.

**C++ Source:**

- **Module**: Engine
- **File**: ChildActorComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``child_actor`` (Actor):  [Read-Write] The actor that we spawned and own
- ``child_actor_class`` (type(Class)):  [Read-Write] The class of Actor to spawn
- ``child_actor_is_transient`` (bool):  [Read-Write] Should the spawned actor be marked as transient?
  note: The spawned actor will also be marked transient if this component or its owner actor are transient, regardless of the state of this flag.
- ``child_actor_template`` (Actor):  [Read-Only] Property to point to the template child actor for details panel purposes
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
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
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.ChildActorComponent.child_actor_class"></a>

#### child_actor_class

```python
@property
def child_actor_class() -> Class
```

(type(Class)):  [Read-Only] The class of Actor to spawn

<a id="unreal.ChildActorComponent.child_actor"></a>

#### child_actor

```python
@property
def child_actor() -> Actor
```

(Actor):  [Read-Only] The actor that we spawned and own

<a id="unreal.ChildActorComponent.set_child_actor_class"></a>

#### set_child_actor_class

```python
def set_child_actor_class(class_: Class) -> None
```

x.set_child_actor_class(class_) -> None
Sets the class to use for the child actor.
If called on a template component (owned by a CDO), the properties of any existing child actor template will be copied as best possible to the template.
If called on a component instance in a world (and the class is changing), the created ChildActor will use the class defaults as template.

Args:
    class_ (type(Class)): The Actor subclass to spawn as a child actor

<a id="unreal.AutoRTFMTestChildActorComponent"></a>