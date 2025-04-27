## NiagaraParameterStore Objects

```python
class NiagaraParameterStore(StructBase)
```

Base storage class for Niagara parameter values.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraParameterStore.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``parameter_offsets`` (Map[NiagaraVariable, int32]):  [Read-Write] Map from parameter defs to their offset in the data table or the data interface. TODO: Separate out into a layout and instance class to reduce duplicated data for this?
  deprecated: Property 'ParameterOffsets' is deprecated.

<a id="unreal.NiagaraParameterStore.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraParameterStore.parameter_offsets"></a>

#### parameter_offsets

```python
@property
def parameter_offsets() -> Map[NiagaraVariable, int]
```

(Map[NiagaraVariable, int32]):  [Read-Write] Map from parameter defs to their offset in the data table or the data interface. TODO: Separate out into a layout and instance class to reduce duplicated data for this?
deprecated: Property 'ParameterOffsets' is deprecated.

<a id="unreal.NiagaraParameterStore.parameter_offsets"></a>

#### parameter_offsets

```python
@parameter_offsets.setter
def parameter_offsets(value: Map[NiagaraVariable, int]) -> None
```

<a id="unreal.NiagaraEventScriptProperties"></a>