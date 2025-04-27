## StateTreeStateType Objects

```python
class StateTreeStateType(EnumBase)
```

EState Tree State Type

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeTypes.h

<a id="unreal.StateTreeStateType.STATE"></a>

#### STATE

0: A State containing tasks and child states.

<a id="unreal.StateTreeStateType.GROUP"></a>

#### GROUP

1: A State containing just child states.

<a id="unreal.StateTreeStateType.LINKED"></a>

#### LINKED

2: A State that is linked to another state in the tree (the execution continues on the linked state).

<a id="unreal.StateTreeStateType.LINKED_ASSET"></a>

#### LINKED_ASSET

3: A State that is linked to another StateTree asset (the execution continues on the Root state of the linked asset).

<a id="unreal.StateTreeStateType.SUBTREE"></a>

#### SUBTREE

4: A subtree that can be linked to.

<a id="unreal.StateTreeStateSelectionBehavior"></a>