## MovieSceneCondition Objects

```python
class MovieSceneCondition(MovieSceneSignedObject)
```

Abstract condition class. Conditions can be applied to sections, tracks, and track rows to determine whether or not they are evaluated at runtime.
This allows developers to create Sequences with dynamic behavior based on gameplay state, local player state, player hardware, etc.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_force_true`` (bool):  [Read-Write] If true, will skip evaluating the condition and always return true. Useful for authoring or debugging.
- ``invert`` (bool):  [Read-Write] If true, inverts the result of the condition check.

<a id="unreal.MovieSceneCondition.editor_force_true"></a>

#### editor_force_true

```python
@property
def editor_force_true() -> bool
```

(bool):  [Read-Write] If true, will skip evaluating the condition and always return true. Useful for authoring or debugging.

<a id="unreal.MovieSceneCondition.editor_force_true"></a>

#### editor_force_true

```python
@editor_force_true.setter
def editor_force_true(value: bool) -> None
```

<a id="unreal.MovieSceneCondition.invert"></a>

#### invert

```python
@property
def invert() -> bool
```

(bool):  [Read-Write] If true, inverts the result of the condition check.

<a id="unreal.MovieSceneCondition.invert"></a>

#### invert

```python
@invert.setter
def invert(value: bool) -> None
```

<a id="unreal.MovieSceneCondition.bp_get_scope"></a>

#### bp_get_scope

```python
def bp_get_scope() -> MovieSceneConditionScope
```

x.bp_get_scope() -> MovieSceneConditionScope
Returns the scope of the condition, which determines whether the condition needs to be re-evaluated for different bindings or entities in the Sequence.

Returns:
    MovieSceneConditionScope:

<a id="unreal.MovieSceneCondition.bp_get_check_frequency"></a>

#### bp_get_check_frequency

```python
def bp_get_check_frequency() -> MovieSceneConditionCheckFrequency
```

x.bp_get_check_frequency() -> MovieSceneConditionCheckFrequency
Returns the check frequency of the condition, which determines whether the condition result can change during playback and needs to get re-evaluated.

Returns:
    MovieSceneConditionCheckFrequency:

<a id="unreal.MovieSceneCondition.bp_evaluate_condition"></a>

#### bp_evaluate_condition

```python
def bp_evaluate_condition(
        condition_context: MovieSceneConditionContext) -> bool
```

x.bp_evaluate_condition(condition_context) -> bool
Override to implement your condition.

Args:
    condition_context (MovieSceneConditionContext): 

Returns:
    bool:

<a id="unreal.MovieSceneDirectorBlueprintCondition"></a>