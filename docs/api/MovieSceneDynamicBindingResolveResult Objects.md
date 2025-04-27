## MovieSceneDynamicBindingResolveResult Objects

```python
class MovieSceneDynamicBindingResolveResult(StructBase)
```

Movie Scene Dynamic Binding Resolve Result

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneDynamicBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_possessed_object`` (bool):  [Read-Write] Whether the resolved object is external to the sequence

  This property is ignored for possessables, who are always treated as external.
  When resolving a spawnable, setting this to true will not destroy the object
  when the spawnable track ends, or the sequence finishes.
- ``object`` (Object):  [Read-Write] The resolved object

<a id="unreal.MovieSceneDynamicBindingResolveResult.__init__"></a>

#### __init__

```python
def __init__(object: Object = None, is_possessed_object: bool = False) -> None
```

<a id="unreal.MovieSceneDynamicBindingResolveResult.object"></a>

#### object

```python
@property
def object() -> Object
```

(Object):  [Read-Write] The resolved object

<a id="unreal.MovieSceneDynamicBindingResolveResult.object"></a>

#### object

```python
@object.setter
def object(value: Object) -> None
```

<a id="unreal.MovieSceneDynamicBindingResolveResult.is_possessed_object"></a>

#### is_possessed_object

```python
@property
def is_possessed_object() -> bool
```

(bool):  [Read-Write] Whether the resolved object is external to the sequence

This property is ignored for possessables, who are always treated as external.
When resolving a spawnable, setting this to true will not destroy the object
when the spawnable track ends, or the sequence finishes.

<a id="unreal.MovieSceneDynamicBindingResolveResult.is_possessed_object"></a>

#### is_possessed_object

```python
@is_possessed_object.setter
def is_possessed_object(value: bool) -> None
```

<a id="unreal.MovieSceneTimecodeSource"></a>