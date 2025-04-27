## NiagaraModuleDependency Objects

```python
class NiagaraModuleDependency(StructBase)
```

Niagara Module Dependency

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraScript.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (Text):  [Read-Write] Detailed description of the dependency
- ``id`` (Name):  [Read-Write] Specifies the provided id of the required dependent module (e.g. 'ProvidesNormalizedAge')
- ``only_evaluate_in_script_usage`` (int32):  [Read-Write] This property can limit where the dependency is evaluated. By default, the dependency is enforced in all script usages
- ``required_version`` (str):  [Read-Write] Specifies the version constraint that module providing the dependency must fulfill.
  Example usages:
  '1.2' requires the exact version 1.2 of the source script
  '1.2+' requires at least version 1.2, but any higher version is also ok
  '1.2-2.0' requires any version between 1.2 and 2.0
- ``script_constraint`` (NiagaraModuleDependencyScriptConstraint):  [Read-Write] Specifies constraints related to the source script a modules provides as dependency.
- ``type`` (NiagaraModuleDependencyType):  [Read-Write] Whether the dependency belongs before or after this module

<a id="unreal.NiagaraModuleDependency.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraEmitterScriptProperties"></a>