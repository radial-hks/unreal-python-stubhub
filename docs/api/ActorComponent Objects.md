## ActorComponent Objects

```python
class ActorComponent(Object)
```

ActorComponent is the base class for components that define reusable behavior that can be added to different types of Actors.
ActorComponents that have a transform are known as SceneComponents and those that can be rendered are PrimitiveComponents.
see: [ActorComponent](https://docs.unrealengine.com/latest/INT/Programming/UnrealArchitecture/Actors/Components/index.html#actorcomponents)
see: USceneComponent
see: UPrimitiveComponent

**C++ Source:**

- **Module**: Engine
- **File**: ActorComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.ActorComponent.component_tags"></a>

#### component\_tags

```python
@property
def component_tags() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.

<a id="unreal.ActorComponent.component_tags"></a>

#### component\_tags

```python
@component_tags.setter
def component_tags(value: Array[Name]) -> None
```

<a id="unreal.ActorComponent.replicate_using_registered_sub_object_list"></a>

#### replicate\_using\_registered\_sub\_object\_list

```python
@property
def replicate_using_registered_sub_object_list() -> bool
```

(bool):  [Read-Only] When true the replication system will only replicate the registered subobjects list
When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.

<a id="unreal.ActorComponent.replicates"></a>

#### replicates

```python
@property
def replicates() -> bool
```

(bool):  [Read-Only] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.ActorComponent.auto_activate"></a>

#### auto\_activate

```python
@property
def auto_activate() -> bool
```

(bool):  [Read-Only] Whether the component is activated at creation or must be explicitly activated.

<a id="unreal.ActorComponent.is_editor_only"></a>

#### is\_editor\_only

```python
@property
def is_editor_only() -> bool
```

(bool):  [Read-Only] If true, the component will be excluded from non-editor builds

<a id="unreal.ActorComponent.on_component_activated"></a>

#### on\_component\_activated

```python
@property
def on_component_activated() -> ActorComponentActivatedSignature
```

(ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset

<a id="unreal.ActorComponent.on_component_activated"></a>

#### on\_component\_activated

```python
@on_component_activated.setter
def on_component_activated(value: ActorComponentActivatedSignature) -> None
```

<a id="unreal.ActorComponent.on_component_deactivated"></a>

#### on\_component\_deactivated

```python
@property
def on_component_deactivated() -> ActorComponentDeactivateSignature
```

(ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated

<a id="unreal.ActorComponent.on_component_deactivated"></a>

#### on\_component\_deactivated

```python
@on_component_deactivated.setter
def on_component_deactivated(value: ActorComponentDeactivateSignature) -> None
```

<a id="unreal.ActorComponent.toggle_active"></a>

#### toggle\_active

```python
def toggle_active() -> None
```

x.toggle_active() -> None
Toggles the active state of the component

<a id="unreal.ActorComponent.set_tick_group"></a>

#### set\_tick\_group

```python
def set_tick_group(new_tick_group: TickingGroup) -> None
```

x.set_tick_group(new_tick_group) -> None
Changes the ticking group for this component

Args:
    new_tick_group (TickingGroup):

<a id="unreal.ActorComponent.set_tickable_when_paused"></a>

#### set\_tickable\_when\_paused

```python
def set_tickable_when_paused(tickable_when_paused: bool) -> None
```

x.set_tickable_when_paused(tickable_when_paused) -> None
Sets whether this component can tick when paused.

Args:
    tickable_when_paused (bool):

<a id="unreal.ActorComponent.set_is_replicated"></a>

#### set\_is\_replicated

```python
def set_is_replicated(should_replicate: bool) -> None
```

x.set_is_replicated(should_replicate) -> None
Enable or disable replication. This is the equivalent of RemoteRole for actors (only a bool is required for components)

Args:
    should_replicate (bool):

<a id="unreal.ActorComponent.set_component_tick_interval_and_cooldown"></a>

#### set\_component\_tick\_interval\_and\_cooldown

```python
def set_component_tick_interval_and_cooldown(tick_interval: float) -> None
```

x.set_component_tick_interval_and_cooldown(tick_interval) -> None
Sets the tick interval for this component's primary tick function. Does not enable the tick interval. Takes effect imediately.

Args:
    tick_interval (float): The duration between ticks for this component's primary tick function

<a id="unreal.ActorComponent.set_component_tick_interval"></a>

#### set\_component\_tick\_interval

```python
def set_component_tick_interval(tick_interval: float) -> None
```

x.set_component_tick_interval(tick_interval) -> None
Sets the tick interval for this component's primary tick function. Does not enable the tick interval. Takes effect on next tick.

Args:
    tick_interval (float): The duration between ticks for this component's primary tick function

<a id="unreal.ActorComponent.set_component_tick_enabled"></a>

#### set\_component\_tick\_enabled

```python
def set_component_tick_enabled(enabled: bool) -> None
```

x.set_component_tick_enabled(enabled) -> None
Set this component's tick functions to be enabled or disabled. Only has an effect if the function is registered

Args:
    enabled (bool): Whether it should be enabled or not

<a id="unreal.ActorComponent.set_auto_activate"></a>

#### set\_auto\_activate

```python
def set_auto_activate(new_auto_activate: bool) -> None
```

x.set_auto_activate(new_auto_activate) -> None
Sets whether the component should be auto activate or not. Only safe during construction scripts.

Args:
    new_auto_activate (bool): The new auto activate state of the component

<a id="unreal.ActorComponent.set_active"></a>

#### set\_active

```python
def set_active(new_active: bool, reset: bool = False) -> None
```

x.set_active(new_active, reset=False) -> None
Sets whether the component is active or not

Args:
    new_active (bool): The new active state of the component
    reset (bool): Whether the activation should happen even if ShouldActivate returns false.

<a id="unreal.ActorComponent.remove_tick_prerequisite_component"></a>

#### remove\_tick\_prerequisite\_component

```python
def remove_tick_prerequisite_component(
        prerequisite_component: ActorComponent) -> None
```

x.remove_tick_prerequisite_component(prerequisite_component) -> None
Remove tick dependency on PrerequisiteComponent.

Args:
    prerequisite_component (ActorComponent):

<a id="unreal.ActorComponent.remove_tick_prerequisite_actor"></a>

#### remove\_tick\_prerequisite\_actor

```python
def remove_tick_prerequisite_actor(prerequisite_actor: Actor) -> None
```

x.remove_tick_prerequisite_actor(prerequisite_actor) -> None
Remove tick dependency on PrerequisiteActor.

Args:
    prerequisite_actor (Actor):

<a id="unreal.ActorComponent.receive_tick"></a>

#### receive\_tick

```python
def receive_tick(delta_seconds: float) -> None
```

x.receive_tick(delta_seconds) -> None
Event called every frame if tick is enabled

Args:
    delta_seconds (float):

<a id="unreal.ActorComponent.receive_end_play"></a>

#### receive\_end\_play

```python
def receive_end_play(end_play_reason: EndPlayReason) -> None
```

x.receive_end_play(end_play_reason) -> None
Blueprint implementable event for when the component ends play, generally via destruction or its Actor's EndPlay.

Args:
    end_play_reason (EndPlayReason):

<a id="unreal.ActorComponent.receive_uninitialize_component"></a>

#### receive\_uninitialize\_component

```python
def receive_uninitialize_component(end_play_reason: EndPlayReason) -> None
```

deprecated: 'receive_uninitialize_component' was renamed to 'receive_end_play'.

<a id="unreal.ActorComponent.receive_begin_play"></a>

#### receive\_begin\_play

```python
def receive_begin_play() -> None
```

x.receive_begin_play() -> None
Blueprint implementable event for when the component is beginning play, called before its owning actor's BeginPlay
or when the component is dynamically created if the Actor has already BegunPlay.

<a id="unreal.ActorComponent.receive_initialize_component"></a>

#### receive\_initialize\_component

```python
def receive_initialize_component() -> None
```

deprecated: 'receive_initialize_component' was renamed to 'receive_begin_play'.

<a id="unreal.ActorComponent.receive_async_physics_tick"></a>

#### receive\_async\_physics\_tick

```python
def receive_async_physics_tick(delta_seconds: float,
                               sim_seconds: float) -> None
```

x.receive_async_physics_tick(delta_seconds, sim_seconds) -> None
Event called every async physics tick if bAsyncPhysicsTickEnabled is true

Args:
    delta_seconds (float): 
    sim_seconds (float):

<a id="unreal.ActorComponent.destroy_component"></a>

#### destroy\_component

```python
def destroy_component(object: Object) -> None
```

x.destroy_component(object) -> None
Unregister and mark for pending kill a component.  This may not be used to destroy a component that is owned by an actor unless the owning actor is calling the function.

Args:
    object (Object):

<a id="unreal.ActorComponent.is_component_tick_enabled"></a>

#### is\_component\_tick\_enabled

```python
def is_component_tick_enabled() -> bool
```

x.is_component_tick_enabled() -> bool
Returns whether this component has tick enabled or not

Returns:
    bool:

<a id="unreal.ActorComponent.is_being_destroyed"></a>

#### is\_being\_destroyed

```python
def is_being_destroyed() -> bool
```

x.is_being_destroyed() -> bool
Returns whether the component is in the process of being destroyed.

Returns:
    bool:

<a id="unreal.ActorComponent.is_active"></a>

#### is\_active

```python
def is_active() -> bool
```

x.is_active() -> bool
Returns whether the component is active or not

Returns:
    bool: The active state of the component.

<a id="unreal.ActorComponent.get_owner"></a>

#### get\_owner

```python
def get_owner() -> Actor
```

x.get_owner() -> Actor
Follow the Outer chain to get the  AActor  that 'Owns' this component

Returns:
    Actor:

<a id="unreal.ActorComponent.get_component_tick_interval"></a>

#### get\_component\_tick\_interval

```python
def get_component_tick_interval() -> float
```

x.get_component_tick_interval() -> float
Returns the tick interval for this component's primary tick function, which is the frequency in seconds at which it will be executed

Returns:
    float:

<a id="unreal.ActorComponent.deactivate"></a>

#### deactivate

```python
def deactivate() -> None
```

x.deactivate() -> None
Deactivates the SceneComponent.

<a id="unreal.ActorComponent.component_has_tag"></a>

#### component\_has\_tag

```python
def component_has_tag(tag: Name) -> bool
```

x.component_has_tag(tag) -> bool
See if this component contains the supplied tag

Args:
    tag (Name): 

Returns:
    bool:

<a id="unreal.ActorComponent.add_tick_prerequisite_component"></a>

#### add\_tick\_prerequisite\_component

```python
def add_tick_prerequisite_component(
        prerequisite_component: ActorComponent) -> None
```

x.add_tick_prerequisite_component(prerequisite_component) -> None
Make this component tick after PrerequisiteComponent.

Args:
    prerequisite_component (ActorComponent):

<a id="unreal.ActorComponent.add_tick_prerequisite_actor"></a>

#### add\_tick\_prerequisite\_actor

```python
def add_tick_prerequisite_actor(prerequisite_actor: Actor) -> None
```

x.add_tick_prerequisite_actor(prerequisite_actor) -> None
Make this component tick after PrerequisiteActor

Args:
    prerequisite_actor (Actor):

<a id="unreal.ActorComponent.activate"></a>

#### activate

```python
def activate(reset: bool = False) -> None
```

x.activate(reset=False) -> None
Activates the SceneComponent, should be overridden by native child classes.

Args:
    reset (bool): Whether the activation should happen even if ShouldActivate returns false.

<a id="unreal.ActorComponent.has_asset_user_data_of_class"></a>

#### has\_asset\_user\_data\_of\_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.ActorComponent.get_asset_user_data_of_class"></a>

#### get\_asset\_user\_data\_of\_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.ActorComponent.add_asset_user_data_of_class"></a>

#### add\_asset\_user\_data\_of\_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.ActorComponent.acquire_editor_element_handle"></a>

#### acquire\_editor\_element\_handle

```python
def acquire_editor_element_handle(
        allow_create: bool = True) -> ScriptTypedElementHandle
```

x.acquire_editor_element_handle(allow_create=True) -> ScriptTypedElementHandle
K2 Acquire Editor Component Element Handle

Args:
    allow_create (bool): 

Returns:
    ScriptTypedElementHandle:

<a id="unreal.SceneComponent"></a>