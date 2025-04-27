## StateTreeDataSourceType Objects

```python
class StateTreeDataSourceType(EnumBase)
```

Data type the FStateTreeDataHandle is pointing at.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeTypes.h

<a id="unreal.StateTreeDataSourceType.GLOBAL_INSTANCE_DATA"></a>

#### GLOBAL_INSTANCE_DATA

1: Global Tasks, Evaluators

<a id="unreal.StateTreeDataSourceType.GLOBAL_INSTANCE_DATA_OBJECT"></a>

#### GLOBAL_INSTANCE_DATA_OBJECT

2: Global Tasks, Evaluators

<a id="unreal.StateTreeDataSourceType.ACTIVE_INSTANCE_DATA"></a>

#### ACTIVE_INSTANCE_DATA

3: Active State Tasks

<a id="unreal.StateTreeDataSourceType.ACTIVE_INSTANCE_DATA_OBJECT"></a>

#### ACTIVE_INSTANCE_DATA_OBJECT

4: Active State Tasks

<a id="unreal.StateTreeDataSourceType.SHARED_INSTANCE_DATA"></a>

#### SHARED_INSTANCE_DATA

5: Conditions and Considerations

<a id="unreal.StateTreeDataSourceType.SHARED_INSTANCE_DATA_OBJECT"></a>

#### SHARED_INSTANCE_DATA_OBJECT

6: Conditions and Considerations

<a id="unreal.StateTreeDataSourceType.CONTEXT_DATA"></a>

#### CONTEXT_DATA

7: Context Data, Tree Parameters

<a id="unreal.StateTreeDataSourceType.EXTERNAL_DATA"></a>

#### EXTERNAL_DATA

8: External Data required by the nodes.

<a id="unreal.StateTreeDataSourceType.GLOBAL_PARAMETER_DATA"></a>

#### GLOBAL_PARAMETER_DATA

9: Global parameters

<a id="unreal.StateTreeDataSourceType.SUBTREE_PARAMETER_DATA"></a>

#### SUBTREE_PARAMETER_DATA

10: Parameters for subtree (may resolve to a linked state's parameters or default params)

<a id="unreal.StateTreeDataSourceType.STATE_PARAMETER_DATA"></a>

#### STATE_PARAMETER_DATA

11: Parameters for regular and linked states

<a id="unreal.StateTreeDataSourceType.TRANSITION_EVENT"></a>

#### TRANSITION_EVENT

12: Event used in transition.

<a id="unreal.StateTreeDataSourceType.STATE_EVENT"></a>

#### STATE_EVENT

13: Event used in state selection.

<a id="unreal.ActorModifierCoreEnableReason"></a>