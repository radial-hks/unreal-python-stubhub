## AvaGizmoComponent Objects

```python
class AvaGizmoComponent(ActorComponent)
```

Add to an actor to indicate it's used as a Gizmo.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: Avalanche
- **File**: AvaGizmoComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_to_child_actors`` (bool):  [Read-Write] Whether the settings apply to child actors or not.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``cast_shadow`` (bool):  [Read-Write] Controls whether the primitive component should cast a shadow or not.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``draw_wireframe`` (bool):  [Read-Write] Currently only applies to dynamic meshes.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``is_gizmo_enabled`` (bool):  [Read-Write] Whether "gizmo mode" is enabled.
- ``is_hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_visible_in_editor`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``material`` (MaterialInterface):  [Read-Write] Material that overrides all others attached to the parent actor, if specified.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``render_depth`` (bool):  [Read-Write] Whether to render to the depth buffer.
- ``render_in_main_pass`` (bool):  [Read-Write] Whether to render in the main pass.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``set_stencil`` (bool):  [Read-Write] Whether to render to the custom depth/stencil buffer.
- ``stencil_id`` (uint8):  [Read-Write] The custom stencil id, if applicable.
- ``wireframe_color`` (LinearColor):  [Read-Write] The color of the wireframe when drawn.

<a id="unreal.AvaGizmoComponent.is_gizmo_enabled"></a>

#### is_gizmo_enabled

```python
@property
def is_gizmo_enabled() -> bool
```

(bool):  [Read-Write] Whether "gizmo mode" is enabled.

<a id="unreal.AvaGizmoComponent.is_gizmo_enabled"></a>

#### is_gizmo_enabled

```python
@is_gizmo_enabled.setter
def is_gizmo_enabled(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.apply_to_child_actors"></a>

#### apply_to_child_actors

```python
@property
def apply_to_child_actors() -> bool
```

(bool):  [Read-Write] Whether the settings apply to child actors or not.

<a id="unreal.AvaGizmoComponent.apply_to_child_actors"></a>

#### apply_to_child_actors

```python
@apply_to_child_actors.setter
def apply_to_child_actors(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] Material that overrides all others attached to the parent actor, if specified.

<a id="unreal.AvaGizmoComponent.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.AvaGizmoComponent.cast_shadow"></a>

#### cast_shadow

```python
@property
def cast_shadow() -> bool
```

(bool):  [Read-Write] Controls whether the primitive component should cast a shadow or not.

<a id="unreal.AvaGizmoComponent.cast_shadow"></a>

#### cast_shadow

```python
@cast_shadow.setter
def cast_shadow(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.is_visible_in_editor"></a>

#### is_visible_in_editor

```python
@property
def is_visible_in_editor() -> bool
```

(bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.AvaGizmoComponent.is_visible_in_editor"></a>

#### is_visible_in_editor

```python
@is_visible_in_editor.setter
def is_visible_in_editor(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.is_hidden_in_game"></a>

#### is_hidden_in_game

```python
@property
def is_hidden_in_game() -> bool
```

(bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.

<a id="unreal.AvaGizmoComponent.is_hidden_in_game"></a>

#### is_hidden_in_game

```python
@is_hidden_in_game.setter
def is_hidden_in_game(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.render_in_main_pass"></a>

#### render_in_main_pass

```python
@property
def render_in_main_pass() -> bool
```

(bool):  [Read-Write] Whether to render in the main pass.

<a id="unreal.AvaGizmoComponent.render_in_main_pass"></a>

#### render_in_main_pass

```python
@render_in_main_pass.setter
def render_in_main_pass(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.render_depth"></a>

#### render_depth

```python
@property
def render_depth() -> bool
```

(bool):  [Read-Write] Whether to render to the depth buffer.

<a id="unreal.AvaGizmoComponent.render_depth"></a>

#### render_depth

```python
@render_depth.setter
def render_depth(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.draw_wireframe"></a>

#### draw_wireframe

```python
@property
def draw_wireframe() -> bool
```

(bool):  [Read-Write] Currently only applies to dynamic meshes.

<a id="unreal.AvaGizmoComponent.draw_wireframe"></a>

#### draw_wireframe

```python
@draw_wireframe.setter
def draw_wireframe(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.wireframe_color"></a>

#### wireframe_color

```python
@property
def wireframe_color() -> LinearColor
```

(LinearColor):  [Read-Write] The color of the wireframe when drawn.

<a id="unreal.AvaGizmoComponent.wireframe_color"></a>

#### wireframe_color

```python
@wireframe_color.setter
def wireframe_color(value: LinearColor) -> None
```

<a id="unreal.AvaGizmoComponent.set_stencil"></a>

#### set_stencil

```python
@property
def set_stencil() -> bool
```

(bool):  [Read-Write] Whether to render to the custom depth/stencil buffer.

<a id="unreal.AvaGizmoComponent.set_stencil"></a>

#### set_stencil

```python
@set_stencil.setter
def set_stencil(value: bool) -> None
```

<a id="unreal.AvaGizmoComponent.stencil_id"></a>

#### stencil_id

```python
@property
def stencil_id() -> int
```

(uint8):  [Read-Write] The custom stencil id, if applicable.

<a id="unreal.AvaGizmoComponent.stencil_id"></a>

#### stencil_id

```python
@stencil_id.setter
def stencil_id(value: int) -> None
```

<a id="unreal.AvaNullActor"></a>