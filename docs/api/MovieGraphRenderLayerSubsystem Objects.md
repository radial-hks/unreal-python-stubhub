## MovieGraphRenderLayerSubsystem Objects

```python
class MovieGraphRenderLayerSubsystem(WorldSubsystem)
```

The primary means of controlling render layers in MRQ. Render layers can be added/registered with the subsystem, then
made active in order to view them. Collections and modifiers can also be viewed, but they do not need to be added to
the subsystem ahead of time.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

<a id="unreal.MovieGraphRenderLayerSubsystem.set_active_render_layer_by_obj"></a>

#### set_active_render_layer_by_obj

```python
def set_active_render_layer_by_obj(
        render_layer: MovieGraphRenderLayer) -> None
```

x.set_active_render_layer_by_obj(render_layer) -> None
Applies the given layer. The layer does not need to have been registered with AddRenderLayer().

Args:
    render_layer (MovieGraphRenderLayer):

<a id="unreal.MovieGraphRenderLayerSubsystem.set_active_render_layer_by_name"></a>

#### set_active_render_layer_by_name

```python
def set_active_render_layer_by_name(render_layer_name: Name) -> None
```

x.set_active_render_layer_by_name(render_layer_name) -> None
Applies the layer with the given name. The layer needs to have been registered with AddRenderLayer().

Args:
    render_layer_name (Name):

<a id="unreal.MovieGraphRenderLayerSubsystem.reset"></a>

#### reset

```python
def reset() -> None
```

x.reset() -> None
Clear out all tracked render layers and collections.

<a id="unreal.MovieGraphRenderLayerSubsystem.remove_render_layer"></a>

#### remove_render_layer

```python
def remove_render_layer(render_layer_name: str) -> None
```

x.remove_render_layer(render_layer_name) -> None
Removes the render layer with the given name. After removal it can no longer be made active with SetActiveRenderLayerBy*().

Args:
    render_layer_name (str):

<a id="unreal.MovieGraphRenderLayerSubsystem.get_render_layers"></a>

#### get_render_layers

```python
def get_render_layers() -> Array[MovieGraphRenderLayer]
```

x.get_render_layers() -> Array[MovieGraphRenderLayer]
Gets all render layers which are currently tracked by the system.

Returns:
    Array[MovieGraphRenderLayer]:

<a id="unreal.MovieGraphRenderLayerSubsystem.get_from_world"></a>

#### get_from_world

```python
@classmethod
def get_from_world(cls, world: World) -> MovieGraphRenderLayerSubsystem
```

X.get_from_world(world) -> MovieGraphRenderLayerSubsystem
Get this subsystem for a specific world. Handy for use from Python.

Args:
    world (World): 

Returns:
    MovieGraphRenderLayerSubsystem:

<a id="unreal.MovieGraphRenderLayerSubsystem.get_active_render_layer"></a>

#### get_active_render_layer

```python
def get_active_render_layer() -> MovieGraphRenderLayer
```

x.get_active_render_layer() -> MovieGraphRenderLayer
Gets the currently active render layer (the layer with its modifiers applied).

Returns:
    MovieGraphRenderLayer:

<a id="unreal.MovieGraphRenderLayerSubsystem.clear_active_render_layer"></a>

#### clear_active_render_layer

```python
def clear_active_render_layer() -> None
```

x.clear_active_render_layer() -> None
Clears the currently active render layer and reverts its modifiers.

<a id="unreal.MovieGraphRenderLayerSubsystem.add_render_layer"></a>

#### add_render_layer

```python
def add_render_layer(render_layer: MovieGraphRenderLayer) -> bool
```

x.add_render_layer(render_layer) -> bool
Adds a render layer to the system, which can later be made active by SetActiveRenderLayer*(). Returns true
if the layer was added successfully, else false.

Args:
    render_layer (MovieGraphRenderLayer): 

Returns:
    bool:

<a id="unreal.MovieGraphSamplingMethodNode"></a>