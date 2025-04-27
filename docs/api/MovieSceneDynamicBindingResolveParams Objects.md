## MovieSceneDynamicBindingResolveParams Objects

```python
class MovieSceneDynamicBindingResolveParams(StructBase)
```

Optional parameter struct for dynamic binding resolver functions.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneDynamicBinding.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``object_binding_id`` (Guid):  [Read-Write] The ID of the object binding being resolved
- ``root_sequence`` (MovieSceneSequence):  [Read-Write] The root sequence
- ``sequence`` (MovieSceneSequence):  [Read-Write] The sequence that contains the object binding being resolved

<a id="unreal.MovieSceneDynamicBindingResolveParams.__init__"></a>

#### __init__

```python
def __init__(sequence: MovieSceneSequence = None,
             object_binding_id: Guid = [],
             root_sequence: MovieSceneSequence = None) -> None
```

<a id="unreal.MovieSceneDynamicBindingResolveParams.sequence"></a>

#### sequence

```python
@property
def sequence() -> MovieSceneSequence
```

(MovieSceneSequence):  [Read-Write] The sequence that contains the object binding being resolved

<a id="unreal.MovieSceneDynamicBindingResolveParams.sequence"></a>

#### sequence

```python
@sequence.setter
def sequence(value: MovieSceneSequence) -> None
```

<a id="unreal.MovieSceneDynamicBindingResolveParams.object_binding_id"></a>

#### object_binding_id

```python
@property
def object_binding_id() -> Guid
```

(Guid):  [Read-Write] The ID of the object binding being resolved

<a id="unreal.MovieSceneDynamicBindingResolveParams.object_binding_id"></a>

#### object_binding_id

```python
@object_binding_id.setter
def object_binding_id(value: Guid) -> None
```

<a id="unreal.MovieSceneDynamicBindingResolveParams.root_sequence"></a>

#### root_sequence

```python
@property
def root_sequence() -> MovieSceneSequence
```

(MovieSceneSequence):  [Read-Write] The root sequence

<a id="unreal.MovieSceneDynamicBindingResolveParams.root_sequence"></a>

#### root_sequence

```python
@root_sequence.setter
def root_sequence(value: MovieSceneSequence) -> None
```

<a id="unreal.MovieSceneDynamicBindingResolveResult"></a>