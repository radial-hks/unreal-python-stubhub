## MovieSceneConditionScope Objects

```python
class MovieSceneConditionScope(EnumBase)
```

* Defines the scope of a particular condition type.
* By default, the condition scope will determine whether conditions need to be re-evaluated for different bindings or entities in the Sequence.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneCondition.h

<a id="unreal.MovieSceneConditionScope.GLOBAL"></a>

#### GLOBAL

0: Condition has the same result regardless of the binding or entity.

<a id="unreal.MovieSceneConditionScope.BINDING"></a>

#### BINDING

1: Condition may have different results for different object bindings.

<a id="unreal.MovieSceneConditionScope.OWNER_OBJECT"></a>

#### OWNER_OBJECT

2: Condition may have different results for each different outer object owner (i.e. track, section) in the Sequence.

<a id="unreal.MovieSceneConditionCheckFrequency"></a>