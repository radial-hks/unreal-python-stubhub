## NiagaraModuleDependencyScriptConstraint Objects

```python
class NiagaraModuleDependencyScriptConstraint(EnumBase)
```

ENiagara Module Dependency Script Constraint

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraScript.h

<a id="unreal.NiagaraModuleDependencyScriptConstraint.SAME_SCRIPT"></a>

#### SAME_SCRIPT

0: The module providing the dependency must be in the same script e.g. if the module requiring the dependency is in "Particle Spawn" the module providing the dependency must also be in "Particle Spawn".

<a id="unreal.NiagaraModuleDependencyScriptConstraint.ALL_SCRIPTS"></a>

#### ALL_SCRIPTS

1: The module providing the dependency can be in any script as long as it satisfies the dependency type, e.g. if the module requiring the dependency is in "Particle Spawn" the module providing the dependency could be in "Emitter Spawn".

<a id="unreal.ScriptExecutionMode"></a>