## MovieSceneScalabilityConditionGroup Objects

```python
class MovieSceneScalabilityConditionGroup(EnumBase)
```

The below is a bit hardcoded to try and match how scalability settings are set up in Scalability.h.
This is because unfortunately scalability settings at their core are not very extensible or data-driven
and so it's difficult to do this in a data driven way. So I've made enums here to make the setup user friendly here,
and then do the mapping in code. If scalability gets re-architected, this will need be to be updated to match.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneScalabilityCondition.h

<a id="unreal.MovieSceneScalabilityConditionGroup.VIEW_DISTANCE"></a>

#### VIEW_DISTANCE

0

<a id="unreal.MovieSceneScalabilityConditionGroup.ANTI_ALIASING"></a>

#### ANTI_ALIASING

1

<a id="unreal.MovieSceneScalabilityConditionGroup.SHADOW"></a>

#### SHADOW

2

<a id="unreal.MovieSceneScalabilityConditionGroup.GLOBAL_ILLUMINATION"></a>

#### GLOBAL_ILLUMINATION

3

<a id="unreal.MovieSceneScalabilityConditionGroup.REFLECTION"></a>

#### REFLECTION

4

<a id="unreal.MovieSceneScalabilityConditionGroup.POST_PROCESS"></a>

#### POST_PROCESS

5

<a id="unreal.MovieSceneScalabilityConditionGroup.TEXTURE"></a>

#### TEXTURE

6

<a id="unreal.MovieSceneScalabilityConditionGroup.EFFECTS"></a>

#### EFFECTS

7

<a id="unreal.MovieSceneScalabilityConditionGroup.FOLIAGE"></a>

#### FOLIAGE

8

<a id="unreal.MovieSceneScalabilityConditionGroup.SHADING"></a>

#### SHADING

9

<a id="unreal.MovieSceneScalabilityConditionGroup.LANDSCAPE"></a>

#### LANDSCAPE

10

<a id="unreal.MovieSceneScalabilityConditionOperator"></a>