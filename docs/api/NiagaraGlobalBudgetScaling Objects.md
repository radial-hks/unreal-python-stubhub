## NiagaraGlobalBudgetScaling Objects

```python
class NiagaraGlobalBudgetScaling(StructBase)
```

Niagara Global Budget Scaling

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEffectType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cull_by_global_budget`` (bool):  [Read-Write] Controls whether global budget based culling is enabled.
- ``max_distance_scale_by_global_budget_use`` (NiagaraLinearRamp):  [Read-Write] When enabled, MaxDistance is scaled down by the global budget use based on this curve. Allows us to cull more aggressively when performance is poor.
- ``max_global_budget_usage`` (float):  [Read-Write] Effects will be culled if the global budget usage exceeds this fraction. A global budget usage of 1.0 means current global FX workload has reached it's max budget. Budgets are set by CVars under FX.Budget...
- ``max_instance_count_scale_by_global_budget_use`` (NiagaraLinearRamp):  [Read-Write] When enabled, Max Effect Type Instances is scaled down by the global budget use based on this curve. Allows us to cull more aggressively when performance is poor.
- ``max_system_instance_count_scale_by_global_budget_use`` (NiagaraLinearRamp):  [Read-Write] When enabled, Max System Instances is scaled down by the global budget use based on this curve. Allows us to cull more aggressively when performance is poor.
- ``scale_max_distance_by_global_budget_use`` (bool):  [Read-Write] Controls whether we scale down the MaxDistance based on the global budget use. Allows us to increase aggression of culling when performance is poor.
- ``scale_max_instance_count_by_global_budget_use`` (bool):  [Read-Write] Controls whether we scale down the system instance counts by global budget usage. Allows us to increase aggression of culling when performance is poor.
- ``scale_system_instance_count_by_global_budget_use`` (bool):  [Read-Write] Controls whether we scale down the effect type instance counts by global budget usage. Allows us to increase aggression of culling when performance is poor.

<a id="unreal.NiagaraGlobalBudgetScaling.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MediaIOConnection"></a>