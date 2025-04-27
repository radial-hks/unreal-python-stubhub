## LevelEditorContextMenuContext Objects

```python
class LevelEditorContextMenuContext(Object)
```

Level Editor Context Menu Context

**C++ Source:**

- **Module**: LevelEditor
- **File**: LevelEditorMenuContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``context_type`` (LevelEditorMenuContext):  [Read-Only]
- ``current_selection`` (TypedElementSelectionSet):  [Read-Only]
- ``cursor_world_location`` (Vector):  [Read-Only]
- ``hit_proxy_actor`` (Actor):  [Read-Only] If the ContextType is Viewport this property can be set to the HitProxy actor that triggered the ContextMenu.
- ``selected_components`` (Array[ActorComponent]):  [Read-Only]

<a id="unreal.LevelEditorContextMenuContext.context_type"></a>

#### context_type

```python
@property
def context_type() -> LevelEditorMenuContext
```

(LevelEditorMenuContext):  [Read-Only]

<a id="unreal.LevelEditorContextMenuContext.current_selection"></a>

#### current_selection

```python
@property
def current_selection() -> TypedElementSelectionSet
```

(TypedElementSelectionSet):  [Read-Only]

<a id="unreal.LevelEditorContextMenuContext.cursor_world_location"></a>

#### cursor_world_location

```python
@property
def cursor_world_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.LevelEditorContextMenuContext.selected_components"></a>

#### selected_components

```python
@property
def selected_components() -> Array[ActorComponent]
```

(Array[ActorComponent]):  [Read-Only]

<a id="unreal.LevelEditorContextMenuContext.hit_proxy_actor"></a>

#### hit_proxy_actor

```python
@property
def hit_proxy_actor() -> Actor
```

(Actor):  [Read-Only] If the ContextType is Viewport this property can be set to the HitProxy actor that triggered the ContextMenu.

<a id="unreal.LevelEditorContextMenuContext.get_hit_proxy_element"></a>

#### get_hit_proxy_element

```python
def get_hit_proxy_element() -> ScriptTypedElementHandle
```

x.get_hit_proxy_element() -> ScriptTypedElementHandle
Get Script Hit Proxy Element

Returns:
    ScriptTypedElementHandle:

<a id="unreal.QuickActionMenuContext"></a>