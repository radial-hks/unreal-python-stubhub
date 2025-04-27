## OptionalMovieSceneBlendType Objects

```python
class OptionalMovieSceneBlendType(StructBase)
```

Optional blend type structure

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneBlendType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_type`` (MovieSceneBlendType):  [Read-Write] The actual blend type
- ``is_valid`` (bool):  [Read-Write] Boolean indicating whether BlendType is valid

<a id="unreal.OptionalMovieSceneBlendType.__init__"></a>

#### __init__

```python
def __init__(blend_type: MovieSceneBlendType = 0,
             is_valid: bool = False) -> None
```

<a id="unreal.OptionalMovieSceneBlendType.blend_type"></a>

#### blend_type

```python
@property
def blend_type() -> MovieSceneBlendType
```

(MovieSceneBlendType):  [Read-Only] The actual blend type

<a id="unreal.OptionalMovieSceneBlendType.is_valid"></a>

#### is_valid

```python
@property
def is_valid() -> bool
```

(bool):  [Read-Only] Boolean indicating whether BlendType is valid

<a id="unreal.MovieSceneMarkedFrame"></a>