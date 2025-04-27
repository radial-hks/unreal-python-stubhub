## PhysicalAnimationComponent Objects

```python
class PhysicalAnimationComponent(ActorComponent)
```

Physical Animation Component

**C++ Source:**

- **Module**: Engine
- **File**: PhysicalAnimationComponent.h

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
- ``strength_multiplyer`` (float):  [Read-Write] Multiplies the strength of any active motors. (can blend from 0-1 for example)

<a id="unreal.PhysicalAnimationComponent.strength_multiplyer"></a>

#### strength_multiplyer

```python
@property
def strength_multiplyer() -> float
```

(float):  [Read-Only] Multiplies the strength of any active motors. (can blend from 0-1 for example)

<a id="unreal.PhysicalAnimationComponent.set_strength_multiplyer"></a>

#### set_strength_multiplyer

```python
def set_strength_multiplyer(strength_multiplyer: float) -> None
```

x.set_strength_multiplyer(strength_multiplyer) -> None
Updates strength multiplyer and any active motors

Args:
    strength_multiplyer (float):

<a id="unreal.PhysicalAnimationComponent.set_skeletal_mesh_component"></a>

#### set_skeletal_mesh_component

```python
def set_skeletal_mesh_component(
        skeletal_mesh_component: SkeletalMeshComponent) -> None
```

x.set_skeletal_mesh_component(skeletal_mesh_component) -> None
Sets the skeletal mesh we are driving through physical animation. Will erase any existing physical animation data.

Args:
    skeletal_mesh_component (SkeletalMeshComponent):

<a id="unreal.PhysicalAnimationComponent.get_body_target_transform"></a>

#### get_body_target_transform

```python
def get_body_target_transform(body_name: Name) -> Transform
```

x.get_body_target_transform(body_name) -> Transform
Returns the target transform for the given body. If physical animation component is not controlling this body, returns its current transform.

Args:
    body_name (Name): 

Returns:
    Transform:

<a id="unreal.PhysicalAnimationComponent.apply_physical_animation_settings_below"></a>

#### apply_physical_animation_settings_below

```python
def apply_physical_animation_settings_below(
        body_name: Name,
        physical_animation_data: PhysicalAnimationData,
        include_self: bool = True) -> None
```

x.apply_physical_animation_settings_below(body_name, physical_animation_data, include_self=True) -> None
Applies the physical animation settings to the body given and all bodies below.

Args:
    body_name (Name): 
    physical_animation_data (PhysicalAnimationData): 
    include_self (bool):

<a id="unreal.PhysicalAnimationComponent.apply_physical_animation_settings"></a>

#### apply_physical_animation_settings

```python
def apply_physical_animation_settings(
        body_name: Name,
        physical_animation_data: PhysicalAnimationData) -> None
```

x.apply_physical_animation_settings(body_name, physical_animation_data) -> None
Applies the physical animation settings to the body given.

Args:
    body_name (Name): 
    physical_animation_data (PhysicalAnimationData):

<a id="unreal.PhysicalAnimationComponent.apply_physical_animation_profile_below"></a>

#### apply_physical_animation_profile_below

```python
def apply_physical_animation_profile_below(
        body_name: Name,
        profile_name: Name,
        include_self: bool = True,
        clear_not_found: bool = False) -> None
```

x.apply_physical_animation_profile_below(body_name, profile_name, include_self=True, clear_not_found=False) -> None
Applies the physical animation profile to the body given and all bodies below.

Args:
    body_name (Name): The body from which we'd like to start applying the physical animation profile. Finds all bodies below in the skeleton hierarchy. None implies all bodies
    profile_name (Name): The physical animation profile we'd like to apply. For each body in the physics asset we search for physical animation settings with this name.
    include_self (bool): Whether to include the provided body name in the list of bodies we act on (useful to ignore for cases where a root has multiple children)
    clear_not_found (bool): If true, bodies without the given profile name will have any existing physical animation settings cleared. If false, bodies without the given profile name are left untouched.

<a id="unreal.PhysicalMaterialMask"></a>