## MovieSceneSubSectionFlags Objects

```python
class MovieSceneSubSectionFlags(EnumBase)
```

Flag structure that can be applied to any sub-section allowing control over various
behaviors for the nested sub-sequence.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSectionParameters.h

<a id="unreal.MovieSceneSubSectionFlags.NONE"></a>

#### NONE

0

<a id="unreal.MovieSceneSubSectionFlags.OVERRIDE_KEEP_STATE"></a>

#### OVERRIDE_KEEP_STATE

1: When set, everything within the sub-section (including further sub-sections) should be keep-state. Mutually exclusive with OverrideRestoreState.

<a id="unreal.MovieSceneSubSectionFlags.OVERRIDE_RESTORE_STATE"></a>

#### OVERRIDE_RESTORE_STATE

2: When set, everything within the sub-section (including further sub-sections) should be restore-state. Mutually exclusive with OverrideKeepState.

<a id="unreal.MovieSceneSubSectionFlags.IGNORE_HIERARCHICAL_BIAS"></a>

#### IGNORE_HIERARCHICAL_BIAS

4: Everything inside this sub-sequence should ignore hierarchical bias and always be relevant

<a id="unreal.MovieSceneSubSectionFlags.BLEND_HIERARCHICAL_BIAS"></a>

#### BLEND_HIERARCHICAL_BIAS

8: Blend this sub sequence's hierarchical bias level using a higher -> lower override. Values from higher biases will override those in lower biases until a combined weight of 1 is reached.

<a id="unreal.MovieSceneSubSectionFlags.ANY_RESTORE_STATE_OVERRIDE"></a>

#### ANY_RESTORE_STATE_OVERRIDE

3

<a id="unreal.MovieSceneCompletionModeOverride"></a>