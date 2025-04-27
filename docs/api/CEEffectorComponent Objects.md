## CEEffectorComponent Objects

```python
class CEEffectorComponent(SceneComponent)
```

Class used to define an effector

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``channel_data`` (CEClonerEffectorChannelData):  [Read-Only] Transient effector channel data
- ``color`` (LinearColor):  [Read-Write] Affected clones color passed over to material
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enabled`` (bool):  [Read-Write] Is this effector enabled/disabled on linked cloners
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``magnitude`` (float):  [Read-Write] The ratio effect of the effector on clones
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``mode_name`` (Name):  [Read-Write] Name of the shape type to use
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
- ``type_name`` (Name):  [Read-Write] Name of the shape type to use
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``visualizer_component_visible`` (bool):  [Read-Write] Visibility of the components visualizer
- ``visualizer_sprite_visible`` (bool):  [Read-Write] Toggle the sprite to visualize and click on this effector

<a id="unreal.CEEffectorComponent.set_visualizer_sprite_visible"></a>

#### set_visualizer_sprite_visible

```python
def set_visualizer_sprite_visible(visible: bool) -> None
```

x.set_visualizer_sprite_visible(visible) -> None
Set Visualizer Sprite Visible

Args:
    visible (bool):

<a id="unreal.CEEffectorComponent.set_visualizer_component_visible"></a>

#### set_visualizer_component_visible

```python
def set_visualizer_component_visible(visible: bool) -> None
```

x.set_visualizer_component_visible(visible) -> None
Set Visualizer Component Visible

Args:
    visible (bool):

<a id="unreal.CEEffectorComponent.set_type_name"></a>

#### set_type_name

```python
def set_type_name(type_name: Name) -> None
```

x.set_type_name(type_name) -> None
Set Type Name

Args:
    type_name (Name):

<a id="unreal.CEEffectorComponent.set_type_class"></a>

#### set_type_class

```python
def set_type_class(type_class: Class) -> None
```

x.set_type_class(type_class) -> None
Set Type Class

Args:
    type_class (type(Class)):

<a id="unreal.CEEffectorComponent.set_mode_name"></a>

#### set_mode_name

```python
def set_mode_name(mode_name: Name) -> None
```

x.set_mode_name(mode_name) -> None
Set Mode Name

Args:
    mode_name (Name):

<a id="unreal.CEEffectorComponent.set_mode_class"></a>

#### set_mode_class

```python
def set_mode_class(mode_class: Class) -> None
```

x.set_mode_class(mode_class) -> None
Set Mode Class

Args:
    mode_class (type(Class)):

<a id="unreal.CEEffectorComponent.set_magnitude"></a>

#### set_magnitude

```python
def set_magnitude(magnitude: float) -> None
```

x.set_magnitude(magnitude) -> None
Set Magnitude

Args:
    magnitude (float):

<a id="unreal.CEEffectorComponent.set_enabled"></a>

#### set_enabled

```python
def set_enabled(enable: bool) -> None
```

x.set_enabled(enable) -> None
Set Enabled

Args:
    enable (bool):

<a id="unreal.CEEffectorComponent.set_color"></a>

#### set_color

```python
def set_color(color: LinearColor) -> None
```

x.set_color(color) -> None
Set Color

Args:
    color (LinearColor):

<a id="unreal.CEEffectorComponent.get_visualizer_sprite_visible"></a>

#### get_visualizer_sprite_visible

```python
def get_visualizer_sprite_visible() -> bool
```

x.get_visualizer_sprite_visible() -> bool
Get Visualizer Sprite Visible

Returns:
    bool:

<a id="unreal.CEEffectorComponent.get_visualizer_component_visible"></a>

#### get_visualizer_component_visible

```python
def get_visualizer_component_visible() -> bool
```

x.get_visualizer_component_visible() -> bool
Get Visualizer Component Visible

Returns:
    bool:

<a id="unreal.CEEffectorComponent.get_type_name"></a>

#### get_type_name

```python
def get_type_name() -> Name
```

x.get_type_name() -> Name
Get Type Name

Returns:
    Name:

<a id="unreal.CEEffectorComponent.get_type_class"></a>

#### get_type_class

```python
def get_type_class() -> Class
```

x.get_type_class() -> type(Class)
Get Type Class

Returns:
    type(Class):

<a id="unreal.CEEffectorComponent.get_mode_name"></a>

#### get_mode_name

```python
def get_mode_name() -> Name
```

x.get_mode_name() -> Name
Get Mode Name

Returns:
    Name:

<a id="unreal.CEEffectorComponent.get_mode_class"></a>

#### get_mode_class

```python
def get_mode_class() -> Class
```

x.get_mode_class() -> type(Class)
Get Mode Class

Returns:
    type(Class):

<a id="unreal.CEEffectorComponent.get_magnitude"></a>

#### get_magnitude

```python
def get_magnitude() -> float
```

x.get_magnitude() -> float
Get Magnitude

Returns:
    float:

<a id="unreal.CEEffectorComponent.get_extension"></a>

#### get_extension

```python
def get_extension(extension_class: Class) -> CEEffectorExtensionBase
```

x.get_extension(extension_class) -> CEEffectorExtensionBase
Get Extension

Args:
    extension_class (type(Class)): 

Returns:
    CEEffectorExtensionBase:

<a id="unreal.CEEffectorComponent.get_enabled"></a>

#### get_enabled

```python
def get_enabled() -> bool
```

x.get_enabled() -> bool
Get Enabled

Returns:
    bool:

<a id="unreal.CEEffectorComponent.get_color"></a>

#### get_color

```python
def get_color() -> LinearColor
```

x.get_color() -> LinearColor
Get Color

Returns:
    LinearColor:

<a id="unreal.CEEffectorComponent.get_channel_identifier"></a>

#### get_channel_identifier

```python
def get_channel_identifier() -> int
```

x.get_channel_identifier() -> int32
Get the effector channel identifier

Returns:
    int32:

<a id="unreal.CEEffectorComponent.get_active_type"></a>

#### get_active_type

```python
def get_active_type() -> CEEffectorTypeBase
```

x.get_active_type() -> CEEffectorTypeBase
Get Active Type

Returns:
    CEEffectorTypeBase:

<a id="unreal.CEEffectorComponent.get_active_mode"></a>

#### get_active_mode

```python
def get_active_mode() -> CEEffectorModeBase
```

x.get_active_mode() -> CEEffectorModeBase
Get Active Mode

Returns:
    CEEffectorModeBase:

<a id="unreal.CEEffectorComponent.get_active_extensions"></a>

#### get_active_extensions

```python
def get_active_extensions() -> Array[CEEffectorExtensionBase]
```

x.get_active_extensions() -> Array[CEEffectorExtensionBase]
Get Active Extensions

Returns:
    Array[CEEffectorExtensionBase]: 

    out_extensions (Array[CEEffectorExtensionBase]):

<a id="unreal.AvaEffectorComponent"></a>