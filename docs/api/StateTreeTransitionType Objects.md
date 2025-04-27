## StateTreeTransitionType Objects

```python
class StateTreeTransitionType(EnumBase)
```

Transitions behavior.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeTypes.h

<a id="unreal.StateTreeTransitionType.NONE"></a>

#### NONE

0: No transition will take place.

<a id="unreal.StateTreeTransitionType.SUCCEEDED"></a>

#### SUCCEEDED

1: Stop State Tree or sub-tree and mark execution succeeded.

<a id="unreal.StateTreeTransitionType.FAILED"></a>

#### FAILED

2: Stop State Tree or sub-tree and mark execution failed.

<a id="unreal.StateTreeTransitionType.GOTO_STATE"></a>

#### GOTO_STATE

3: Transition to the specified state.

<a id="unreal.StateTreeTransitionType.NEXT_STATE"></a>

#### NEXT_STATE

4: Transition to the next sibling state.

<a id="unreal.StateTreeTransitionType.NEXT_SELECTABLE_STATE"></a>

#### NEXT_SELECTABLE_STATE

5: Transition to the next selectable sibling state

<a id="unreal.StateTreeTransitionType.NOT_SET"></a>

#### NOT_SET

6

<a id="unreal.AvaMarkDirection"></a>