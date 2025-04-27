## MovieSceneBindingResolveContext Objects

```python
class MovieSceneBindingResolveContext(StructBase)
```

* Blueprint-specific resolution context for custom bindings.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneCustomBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``binding`` (MovieSceneBindingProxy):  [Read-Write] Binding for the bound object currently evaluating this condition if applicable (BindingId will be invalid for conditions on global tracks/sections).
- ``world_context`` (Object):  [Read-Write] The world context

<a id="unreal.MovieSceneBindingResolveContext.__init__"></a>

#### __init__

```python
def __init__(world_context: Object = None,
             binding: MovieSceneBindingProxy = [[], None]) -> None
```

<a id="unreal.MovieSceneBindingResolveContext.world_context"></a>

#### world_context

```python
@property
def world_context() -> Object
```

(Object):  [Read-Write] The world context

<a id="unreal.MovieSceneBindingResolveContext.world_context"></a>

#### world_context

```python
@world_context.setter
def world_context(value: Object) -> None
```

<a id="unreal.MovieSceneBindingResolveContext.binding"></a>

#### binding

```python
@property
def binding() -> MovieSceneBindingProxy
```

(MovieSceneBindingProxy):  [Read-Write] Binding for the bound object currently evaluating this condition if applicable (BindingId will be invalid for conditions on global tracks/sections).

<a id="unreal.MovieSceneBindingResolveContext.binding"></a>

#### binding

```python
@binding.setter
def binding(value: MovieSceneBindingProxy) -> None
```

<a id="unreal.MovieSceneSectionParameters"></a>