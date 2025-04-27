## MovieSceneReplaceableActorBinding_BPBase Objects

```python
class MovieSceneReplaceableActorBinding_BPBase(MovieSceneReplaceableBindingBase
                                               )
```

Base class for Custom Replaceable Binding classes implemented by Blueprints

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneReplaceableActorBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``binding_type_pretty_name`` (Text):  [Read-Write] Name to show in Sequencer for the custom binding type.
- ``binding_type_tooltip`` (Text):  [Read-Write] Tooltip to show in Sequencer for the custom binding type.
- ``custom_binding_priority`` (int32):  [Read-Write] Priority with which to consider this binding type over others when considering binding an object to Sequencer.
  As a guideline, a priority of BaseEnginePriority will ensure that engine types(such as Spawnable Actor, Replaceable Actor) will
  be higher priority than your custom binding, and so your binding type will not automatically be created(but may be converted to manually).
  A priority of BaseCustomPriority and higher will ensure that your binding type is considered more highly than engine types,
  so if your binding type's 'SupportsBindingCreationFromObject' returns true for an object, your binding type will be created by default
  rather than an engine type.
- ``preview_spawnable`` (MovieSceneSpawnableBindingBase):  [Read-Only] Optional Editor-only preview object
- ``preview_spawnable_type`` (type(Class)):  [Read-Write] Preview Spawnable Type to use for this replaceable

<a id="unreal.MovieSceneReplaceableActorBinding_BPBase.binding_type_pretty_name"></a>

#### binding_type_pretty_name

```python
@property
def binding_type_pretty_name() -> Text
```

(Text):  [Read-Only] Name to show in Sequencer for the custom binding type.

<a id="unreal.MovieSceneReplaceableActorBinding_BPBase.binding_type_tooltip"></a>

#### binding_type_tooltip

```python
@property
def binding_type_tooltip() -> Text
```

(Text):  [Read-Only] Tooltip to show in Sequencer for the custom binding type.

<a id="unreal.MovieSceneReplaceableActorBinding_BPBase.custom_binding_priority"></a>

#### custom_binding_priority

```python
@property
def custom_binding_priority() -> int
```

(int32):  [Read-Only] Priority with which to consider this binding type over others when considering binding an object to Sequencer.
As a guideline, a priority of BaseEnginePriority will ensure that engine types(such as Spawnable Actor, Replaceable Actor) will
be higher priority than your custom binding, and so your binding type will not automatically be created(but may be converted to manually).
A priority of BaseCustomPriority and higher will ensure that your binding type is considered more highly than engine types,
so if your binding type's 'SupportsBindingCreationFromObject' returns true for an object, your binding type will be created by default
rather than an engine type.

<a id="unreal.MovieSceneReplaceableActorBinding_BPBase.preview_spawnable_type"></a>

#### preview_spawnable_type

```python
@property
def preview_spawnable_type() -> Class
```

(type(Class)):  [Read-Only] Preview Spawnable Type to use for this replaceable

<a id="unreal.MovieSceneReplaceableActorBinding_BPBase.bp_supports_binding_creation_from_object"></a>

#### bp_supports_binding_creation_from_object

```python
def bp_supports_binding_creation_from_object(source_object: Object) -> bool
```

x.bp_supports_binding_creation_from_object(source_object) -> bool
Called on the binding to determine whether this binding type supports creating a binding from the passed in object.

Args:
    source_object (Object): 

Returns:
    bool:

<a id="unreal.MovieSceneReplaceableActorBinding_BPBase.bp_resolve_runtime_binding"></a>

#### bp_resolve_runtime_binding

```python
def bp_resolve_runtime_binding(
    resolve_context: MovieSceneBindingResolveContext
) -> MovieSceneBindingResolveResult
```

x.bp_resolve_runtime_binding(resolve_context) -> MovieSceneBindingResolveResult
* Must be implemented. Called during non-editor/runtime to resolve the binding dynamically. In editor worlds/Sequencer will instead use the PreviewSpawnable binding to spawn a preview object.
* If no object is returned, Sequencer's BindingOverrides can still be used to dynamically bind the object.

Args:
    resolve_context (MovieSceneBindingResolveContext): 

Returns:
    MovieSceneBindingResolveResult:

<a id="unreal.MovieSceneReplaceableActorBinding_BPBase.bp_init_replaceable_binding"></a>

#### bp_init_replaceable_binding

```python
def bp_init_replaceable_binding(source_object: Object,
                                owner_movie_scene: MovieScene) -> None
```

x.bp_init_replaceable_binding(source_object, owner_movie_scene) -> None
Called after binding creation to allow the replaceable to initialize any data members from the source object.

Args:
    source_object (Object): 
    owner_movie_scene (MovieScene):

<a id="unreal.MovieSceneReplaceableDirectorBlueprintBinding"></a>