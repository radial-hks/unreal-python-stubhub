## MovieGraphRenderLayer Objects

```python
class MovieGraphRenderLayer(Object)
```

Provides a means of assembling modifiers together to generate a desired view of a scene.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

<a id="unreal.MovieGraphRenderLayer.set_render_layer_name"></a>

#### set_render_layer_name

```python
def set_render_layer_name(new_name: Name) -> None
```

x.set_render_layer_name(new_name) -> None
Set Render Layer Name

Args:
    new_name (Name):

<a id="unreal.MovieGraphRenderLayer.revert"></a>

#### revert

```python
def revert() -> None
```

x.revert() -> None
Revert

<a id="unreal.MovieGraphRenderLayer.remove_modifier"></a>

#### remove_modifier

```python
def remove_modifier(modifier: MovieGraphCollectionModifier) -> None
```

x.remove_modifier(modifier) -> None
Remove Modifier

Args:
    modifier (MovieGraphCollectionModifier):

<a id="unreal.MovieGraphRenderLayer.get_render_layer_name"></a>

#### get_render_layer_name

```python
def get_render_layer_name() -> Name
```

x.get_render_layer_name() -> Name
Get Render Layer Name

Returns:
    Name:

<a id="unreal.MovieGraphRenderLayer.get_modifiers"></a>

#### get_modifiers

```python
def get_modifiers() -> Array[MovieGraphCollectionModifier]
```

x.get_modifiers() -> Array[MovieGraphCollectionModifier]
Get Modifiers

Returns:
    Array[MovieGraphCollectionModifier]:

<a id="unreal.MovieGraphRenderLayer.get_collection_by_name"></a>

#### get_collection_by_name

```python
def get_collection_by_name(name: str) -> MovieGraphCollection
```

x.get_collection_by_name(name) -> MovieGraphCollection
Get Collection by Name

Args:
    name (str): 

Returns:
    MovieGraphCollection:

<a id="unreal.MovieGraphRenderLayer.apply"></a>

#### apply

```python
def apply(world: World) -> None
```

x.apply(world) -> None
Apply

Args:
    world (World):

<a id="unreal.MovieGraphRenderLayer.add_modifier"></a>

#### add_modifier

```python
def add_modifier(modifier: MovieGraphCollectionModifier) -> None
```

x.add_modifier(modifier) -> None
Add Modifier

Args:
    modifier (MovieGraphCollectionModifier):

<a id="unreal.MovieGraphRenderLayerSubsystem"></a>