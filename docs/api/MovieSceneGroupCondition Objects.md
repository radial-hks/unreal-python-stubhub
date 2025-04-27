## MovieSceneGroupCondition Objects

```python
class MovieSceneGroupCondition(MovieSceneCondition)
```

Condition class that allows the grouping of other conditions using 'and', 'or', or 'xor'.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneGroupCondition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_force_true`` (bool):  [Read-Write] If true, will skip evaluating the condition and always return true. Useful for authoring or debugging.
- ``invert`` (bool):  [Read-Write] If true, inverts the result of the condition check.
- ``operator`` (MovieSceneGroupConditionOperator):  [Read-Write] Which operator to use in evaluating the group condition
- ``sub_conditions`` (Array[MovieSceneConditionContainer]):  [Read-Write] List of sub-conditions to evaluate as part of this condition. Condition results will be combined together using ConditionOperator

<a id="unreal.MovieSceneGroupCondition.operator"></a>

#### operator

```python
@property
def operator() -> MovieSceneGroupConditionOperator
```

(MovieSceneGroupConditionOperator):  [Read-Write] Which operator to use in evaluating the group condition

<a id="unreal.MovieSceneGroupCondition.operator"></a>

#### operator

```python
@operator.setter
def operator(value: MovieSceneGroupConditionOperator) -> None
```

<a id="unreal.MovieSceneGroupCondition.sub_conditions"></a>

#### sub_conditions

```python
@property
def sub_conditions() -> Array[MovieSceneConditionContainer]
```

(Array[MovieSceneConditionContainer]):  [Read-Write] List of sub-conditions to evaluate as part of this condition. Condition results will be combined together using ConditionOperator

<a id="unreal.MovieSceneGroupCondition.sub_conditions"></a>

#### sub_conditions

```python
@sub_conditions.setter
def sub_conditions(value: Array[MovieSceneConditionContainer]) -> None
```

<a id="unreal.MovieSceneTimeWarpSection"></a>