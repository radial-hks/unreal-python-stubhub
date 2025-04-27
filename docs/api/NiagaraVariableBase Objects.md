## NiagaraVariableBase Objects

```python
class NiagaraVariableBase(StructBase)
```

Niagara Variable Base

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``type_def`` (NiagaraTypeDefinition):  [Read-Write]
  deprecated: Property 'TypeDef' is deprecated.
- ``type_def_handle`` (NiagaraTypeDefinitionHandle):  [Read-Write]

<a id="unreal.NiagaraVariableBase.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraVariableBase.type_def"></a>

#### type_def

```python
@property
def type_def() -> NiagaraTypeDefinition
```

(NiagaraTypeDefinition):  [Read-Write]
deprecated: Property 'TypeDef' is deprecated.

<a id="unreal.NiagaraVariableBase.type_def"></a>

#### type_def

```python
@type_def.setter
def type_def(value: NiagaraTypeDefinition) -> None
```

<a id="unreal.NiagaraVariable"></a>