## NiagaraEffectType Objects

```python
class NiagaraEffectType(Object)
```

Contains settings and working data shared among many Niagara systems that share some commonality of type, for example ImpactFX vs EnvironmentalFX.
Main usage of effect types is to control scalability settings for a group of effects, setting visibility and cull reactions on a per-platform basis.

Effect types can also be used for validation, checking that the content passes all the configured validation rule sets.

The effect type is set in Niagara systems in the system properties.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEffectType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_culling_for_local_players`` (bool):  [Read-Write] Controls whether or not culling is allowed for FX that are owned by, attached to or instigated by a locally controlled pawn.
- ``cull_reaction`` (NiagaraCullReaction):  [Read-Write] How effects of this type react when they fail the cull checks.
  Applied to all effects using this effect type and can not be overridden per effect.
- ``emitter_scalability_settings`` (NiagaraEmitterScalabilitySettingsArray):  [Read-Write]
- ``performance_baseline_controller`` (NiagaraBaselineController):  [Read-Write] Controls generation of performance baseline data for this effect type.
- ``significance_handler`` (NiagaraSignificanceHandler):  [Read-Write] Used to determine the relative significance of FX in the scene which is used in other scalability systems such as instance count culling.
- ``system_scalability_settings`` (NiagaraSystemScalabilitySettingsArray):  [Read-Write]
- ``update_frequency`` (NiagaraScalabilityUpdateFrequency):  [Read-Write] How regularly effects of this type are checked for scalability.
- ``validation_rule_sets`` (Array[NiagaraValidationRuleSet]):  [Read-Write] Array of reusable rule sets to apply when checking content. To create your own rules, write a custom class that extends UNiagaraValidationRule.
- ``validation_rules`` (Array[NiagaraValidationRule]):  [Read-Write] A set of rules to apply when checking content. To create your own rules, write a custom class that extends UNiagaraValidationRule.

<a id="unreal.ChaosCache"></a>