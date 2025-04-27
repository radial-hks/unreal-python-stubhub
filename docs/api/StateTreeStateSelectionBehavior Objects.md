## StateTreeStateSelectionBehavior Objects

```python
class StateTreeStateSelectionBehavior(EnumBase)
```

EState Tree State Selection Behavior

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeTypes.h

<a id="unreal.StateTreeStateSelectionBehavior.NONE"></a>

#### NONE

0: The State cannot be directly selected.

<a id="unreal.StateTreeStateSelectionBehavior.TRY_ENTER_STATE"></a>

#### TRY_ENTER_STATE

1: When state is considered for selection, it is selected even if it has child states.

<a id="unreal.StateTreeStateSelectionBehavior.TRY_SELECT_CHILDREN_IN_ORDER"></a>

#### TRY_SELECT_CHILDREN_IN_ORDER

2: When state is considered for selection, try to select the first child state (in order they appear in the child list). If no child states are present, behaves like SelectState.

<a id="unreal.StateTreeStateSelectionBehavior.TRY_SELECT_CHILDREN_AT_RANDOM"></a>

#### TRY_SELECT_CHILDREN_AT_RANDOM

3: When state is considered for selection, shuffle the order of child states and try to select the first one. If no child states are present, behaves like SelectState.

<a id="unreal.StateTreeStateSelectionBehavior.TRY_SELECT_CHILDREN_WITH_HIGHEST_UTILITY"></a>

#### TRY_SELECT_CHILDREN_WITH_HIGHEST_UTILITY

4: When state is considered for selection, try to select the child state with highest utility score. If there is a tie, it will try to select in order.

<a id="unreal.StateTreeStateSelectionBehavior.TRY_SELECT_CHILDREN_AT_RANDOM_WEIGHTED_BY_UTILITY"></a>

#### TRY_SELECT_CHILDREN_AT_RANDOM_WEIGHTED_BY_UTILITY

5: When state is considered for selection, randomly pick one of its child states. The probability of selecting each child state is its normalized utility score

<a id="unreal.StateTreeStateSelectionBehavior.TRY_FOLLOW_TRANSITIONS"></a>

#### TRY_FOLLOW_TRANSITIONS

6: When state is considered for selection, try to trigger the transitions instead.

<a id="unreal.SubmixEffectConvolutionReverbBlockSize"></a>