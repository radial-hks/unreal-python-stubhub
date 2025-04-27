## MovieSceneConditionContainer Objects

```python
class MovieSceneConditionContainer(StructBase)
```

* Container struct for instanced UMovieSceneConditions, existing only to allow property type customization for choosing conditions.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition`` (MovieSceneCondition):  [Read-Write]

<a id="unreal.MovieSceneConditionContainer.__init__"></a>

#### __init__

```python
def __init__(condition: MovieSceneCondition = None) -> None
```

<a id="unreal.MovieSceneConditionContainer.condition"></a>

#### condition

```python
@property
def condition() -> MovieSceneCondition
```

(MovieSceneCondition):  [Read-Write]

<a id="unreal.MovieSceneConditionContainer.condition"></a>

#### condition

```python
@condition.setter
def condition(value: MovieSceneCondition) -> None
```

<a id="unreal.MovieSceneBindingResolveResult"></a>