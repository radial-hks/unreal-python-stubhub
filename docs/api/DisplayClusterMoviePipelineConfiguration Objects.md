## DisplayClusterMoviePipelineConfiguration Objects

```python
class DisplayClusterMoviePipelineConfiguration(StructBase)
```

Display Cluster Movie Pipeline Configuration

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterMoviePipeline
- **File**: DisplayClusterMoviePipelineSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allowed_viewport_names_list`` (Array[str]):  [Read-Write] Render only viewports from this list.
- ``dc_root_actor`` (DisplayClusterRootActor):  [Read-Write] Reference to Display Cluster Root Actor
  If not set, the first available in the scene will be set.
- ``render_all_viewports`` (bool):  [Read-Write] Render all viewports
- ``use_viewport_resolutions`` (bool):  [Read-Write] Render with nDisplay viewport resolutions.

<a id="unreal.DisplayClusterMoviePipelineConfiguration.__init__"></a>

#### __init__

```python
def __init__(dc_root_actor: DisplayClusterRootActor = None,
             use_viewport_resolutions: bool = False,
             render_all_viewports: bool = False,
             allowed_viewport_names_list: Array[str] = []) -> None
```

<a id="unreal.DisplayClusterMoviePipelineConfiguration.dc_root_actor"></a>

#### dc_root_actor

```python
@property
def dc_root_actor() -> DisplayClusterRootActor
```

(DisplayClusterRootActor):  [Read-Write] Reference to Display Cluster Root Actor
If not set, the first available in the scene will be set.

<a id="unreal.DisplayClusterMoviePipelineConfiguration.dc_root_actor"></a>

#### dc_root_actor

```python
@dc_root_actor.setter
def dc_root_actor(value: DisplayClusterRootActor) -> None
```

<a id="unreal.DisplayClusterMoviePipelineConfiguration.use_viewport_resolutions"></a>

#### use_viewport_resolutions

```python
@property
def use_viewport_resolutions() -> bool
```

(bool):  [Read-Write] Render with nDisplay viewport resolutions.

<a id="unreal.DisplayClusterMoviePipelineConfiguration.use_viewport_resolutions"></a>

#### use_viewport_resolutions

```python
@use_viewport_resolutions.setter
def use_viewport_resolutions(value: bool) -> None
```

<a id="unreal.DisplayClusterMoviePipelineConfiguration.render_all_viewports"></a>

#### render_all_viewports

```python
@property
def render_all_viewports() -> bool
```

(bool):  [Read-Write] Render all viewports

<a id="unreal.DisplayClusterMoviePipelineConfiguration.render_all_viewports"></a>

#### render_all_viewports

```python
@render_all_viewports.setter
def render_all_viewports(value: bool) -> None
```

<a id="unreal.DisplayClusterMoviePipelineConfiguration.allowed_viewport_names_list"></a>

#### allowed_viewport_names_list

```python
@property
def allowed_viewport_names_list() -> Array[str]
```

(Array[str]):  [Read-Write] Render only viewports from this list.

<a id="unreal.DisplayClusterMoviePipelineConfiguration.allowed_viewport_names_list"></a>

#### allowed_viewport_names_list

```python
@allowed_viewport_names_list.setter
def allowed_viewport_names_list(value: Array[str]) -> None
```

<a id="unreal.CollisionResponse"></a>