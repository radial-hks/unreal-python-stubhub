## NiagaraSystemScalabilityOverride Objects

```python
class NiagaraSystemScalabilityOverride(NiagaraSystemScalabilitySettings)
```

Niagara System Scalability Override

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEffectType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``budget_scaling`` (NiagaraGlobalBudgetScaling):  [Read-Write] Settings related to scaling down FX based on the current budget usage.
- ``cull_by_distance`` (bool):  [Read-Write] Controls whether distance culling is enabled.
- ``cull_max_instance_count`` (bool):  [Read-Write] Controls whether we should cull systems based on how many instances with the same Effect Type are active.
- ``cull_per_system_max_instance_count`` (bool):  [Read-Write] Controls whether we should cull systems based on how many instances of the system are active.
- ``cull_proxy_mode`` (NiagaraCullProxyMode):  [Read-Write] Controls what, if any, proxy will be used in place of culled systems.
- ``max_distance`` (float):  [Read-Write] Effects of this type are culled beyond this distance.
- ``max_instances`` (int32):  [Read-Write] Effects of this type will be culled when total active instances using this same EffectType exceeds this number.
  If the effect type has a significance handler, instances are sorted by their significance and only the N most significant will be kept. The rest are culled.
  If it does not have a significance handler, instance count culling will be applied at spawn time only. New FX that would exceed the counts are not spawned/activated.
- ``max_system_instances`` (int32):  [Read-Write] Effects of this type will be culled when total active instances of the same NiagaraSystem exceeds this number.
  If the effect type has a significance handler, instances are sorted by their significance and only the N most significant will be kept. The rest are culled.
  If it does not have a significance handler, instance count culling will be applied at spawn time only. New FX that would exceed the counts are not spawned/activated.
- ``max_system_proxies`` (int32):  [Read-Write] Limit on the number of proxies that can be used at once per system.
  While much cheaper than full FX instances, proxies still incur some cost so must have a limit.
  When significance information is available using a significance handler, the most significance proxies will be kept up to this limit.
- ``override_cull_proxy_settings`` (bool):  [Read-Write] Controls whether we override the cull proxy settings.
- ``override_distance_settings`` (bool):  [Read-Write] Controls whether we override the distance culling settings.
- ``override_global_budget_scaling_settings`` (bool):  [Read-Write] Controls whether we override the global budget scaling settings.
- ``override_instance_count_settings`` (bool):  [Read-Write] Controls whether we override the instance count culling settings.
- ``override_per_system_instance_count_settings`` (bool):  [Read-Write] Controls whether we override the per system instance count culling settings.
- ``override_visibility_settings`` (bool):  [Read-Write] Controls whether we override the visibility culling settings.
- ``platforms`` (NiagaraPlatformSet):  [Read-Write] The platforms on which these settings are active (unless overridden).
- ``visibility_culling`` (NiagaraSystemVisibilityCullingSettings):  [Read-Write] Settings controlling how systems are culled by visibility.

<a id="unreal.NiagaraSystemScalabilityOverride.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraScalabilityOverrides"></a>