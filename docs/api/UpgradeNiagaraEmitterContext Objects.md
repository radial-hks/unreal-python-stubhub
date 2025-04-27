## UpgradeNiagaraEmitterContext Objects

```python
class UpgradeNiagaraEmitterContext(Object)
```

Wrapper class for passing results back from the version upgrade python script.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraEditor
- **File**: UpgradeNiagaraScriptResults.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cancelled_by_python_error`` (bool):  [Read-Write] Whether the converter process was cancelled due to an unrecoverable error in the python script process.
- ``new_emitter`` (NiagaraPythonEmitter):  [Read-Write]
- ``old_emitter`` (NiagaraPythonEmitter):  [Read-Write]

<a id="unreal.UpgradeNiagaraEmitterContext.cancelled_by_python_error"></a>

#### cancelled_by_python_error

```python
@property
def cancelled_by_python_error() -> bool
```

(bool):  [Read-Write] Whether the converter process was cancelled due to an unrecoverable error in the python script process.

<a id="unreal.UpgradeNiagaraEmitterContext.cancelled_by_python_error"></a>

#### cancelled_by_python_error

```python
@cancelled_by_python_error.setter
def cancelled_by_python_error(value: bool) -> None
```

<a id="unreal.UpgradeNiagaraEmitterContext.old_emitter"></a>

#### old_emitter

```python
@property
def old_emitter() -> NiagaraPythonEmitter
```

(NiagaraPythonEmitter):  [Read-Write]

<a id="unreal.UpgradeNiagaraEmitterContext.old_emitter"></a>

#### old_emitter

```python
@old_emitter.setter
def old_emitter(value: NiagaraPythonEmitter) -> None
```

<a id="unreal.UpgradeNiagaraEmitterContext.new_emitter"></a>

#### new_emitter

```python
@property
def new_emitter() -> NiagaraPythonEmitter
```

(NiagaraPythonEmitter):  [Read-Write]

<a id="unreal.UpgradeNiagaraEmitterContext.new_emitter"></a>

#### new_emitter

```python
@new_emitter.setter
def new_emitter(value: NiagaraPythonEmitter) -> None
```

<a id="unreal.VolumeCacheFactory"></a>