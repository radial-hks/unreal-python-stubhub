## NiagaraPythonEmitter Objects

```python
class NiagaraPythonEmitter(Object)
```

Wrapper for an emitter stack.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraEditor
- **File**: UpgradeNiagaraScriptResults.h

<a id="unreal.NiagaraPythonEmitter.set_properties"></a>

#### set_properties

```python
def set_properties(data: VersionedNiagaraEmitterData) -> None
```

x.set_properties(data) -> None
sets the new emitter properties

Args:
    data (VersionedNiagaraEmitterData):

<a id="unreal.NiagaraPythonEmitter.has_module"></a>

#### has_module

```python
def has_module(module_name: str) -> bool
```

x.has_module(module_name) -> bool
returns true if the emitter contains a certain module

Args:
    module_name (str): 

Returns:
    bool:

<a id="unreal.NiagaraPythonEmitter.get_properties"></a>

#### get_properties

```python
def get_properties() -> VersionedNiagaraEmitterData
```

x.get_properties() -> VersionedNiagaraEmitterData
returns the emitter properties, such as determinism or interpolated spawning

Returns:
    VersionedNiagaraEmitterData:

<a id="unreal.NiagaraPythonEmitter.get_object"></a>

#### get_object

```python
def get_object() -> NiagaraEmitter
```

x.get_object() -> NiagaraEmitter
Returns the raw underlying object

Returns:
    NiagaraEmitter:

<a id="unreal.NiagaraPythonEmitter.get_modules"></a>

#### get_modules

```python
def get_modules() -> Array[NiagaraPythonModule]
```

x.get_modules() -> Array[NiagaraPythonModule]
returns a list of all modules contained in this emitter

Returns:
    Array[NiagaraPythonModule]:

<a id="unreal.NiagaraPythonEmitter.get_module"></a>

#### get_module

```python
def get_module(module_name: str) -> NiagaraPythonModule
```

x.get_module(module_name) -> NiagaraPythonModule
returns a module by name

Args:
    module_name (str): 

Returns:
    NiagaraPythonModule:

<a id="unreal.UpgradeNiagaraEmitterContext"></a>