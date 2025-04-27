## UpgradeNiagaraScriptResults Objects

```python
class UpgradeNiagaraScriptResults(Object)
```

Wrapper class for passing results back from the version upgrade python script.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraEditor
- **File**: UpgradeNiagaraScriptResults.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cancelled_by_python_error`` (bool):  [Read-Write] Whether the converter process was cancelled due to an unrecoverable error in the python script process.
- ``new_inputs`` (Array[NiagaraPythonScriptModuleInput]):  [Read-Write]
- ``old_inputs`` (Array[NiagaraPythonScriptModuleInput]):  [Read-Write]

<a id="unreal.UpgradeNiagaraScriptResults.cancelled_by_python_error"></a>

#### cancelled_by_python_error

```python
@property
def cancelled_by_python_error() -> bool
```

(bool):  [Read-Write] Whether the converter process was cancelled due to an unrecoverable error in the python script process.

<a id="unreal.UpgradeNiagaraScriptResults.cancelled_by_python_error"></a>

#### cancelled_by_python_error

```python
@cancelled_by_python_error.setter
def cancelled_by_python_error(value: bool) -> None
```

<a id="unreal.UpgradeNiagaraScriptResults.old_inputs"></a>

#### old_inputs

```python
@property
def old_inputs() -> Array[NiagaraPythonScriptModuleInput]
```

(Array[NiagaraPythonScriptModuleInput]):  [Read-Write]

<a id="unreal.UpgradeNiagaraScriptResults.old_inputs"></a>

#### old_inputs

```python
@old_inputs.setter
def old_inputs(value: Array[NiagaraPythonScriptModuleInput]) -> None
```

<a id="unreal.UpgradeNiagaraScriptResults.new_inputs"></a>

#### new_inputs

```python
@property
def new_inputs() -> Array[NiagaraPythonScriptModuleInput]
```

(Array[NiagaraPythonScriptModuleInput]):  [Read-Write]

<a id="unreal.UpgradeNiagaraScriptResults.new_inputs"></a>

#### new_inputs

```python
@new_inputs.setter
def new_inputs(value: Array[NiagaraPythonScriptModuleInput]) -> None
```

<a id="unreal.UpgradeNiagaraScriptResults.set_vec4_input"></a>

#### set_vec4_input

```python
def set_vec4_input(input_name: str, value: Vector4) -> None
```

x.set_vec4_input(input_name, value) -> None
Set Vec 4Input

Args:
    input_name (str): 
    value (Vector4):

<a id="unreal.UpgradeNiagaraScriptResults.set_vec3_input"></a>

#### set_vec3_input

```python
def set_vec3_input(input_name: str, value: Vector) -> None
```

x.set_vec3_input(input_name, value) -> None
Set Vec 3Input

Args:
    input_name (str): 
    value (Vector):

<a id="unreal.UpgradeNiagaraScriptResults.set_vec2_input"></a>

#### set_vec2_input

```python
def set_vec2_input(input_name: str, value: Vector2D) -> None
```

x.set_vec2_input(input_name, value) -> None
Set Vec 2Input

Args:
    input_name (str): 
    value (Vector2D):

<a id="unreal.UpgradeNiagaraScriptResults.set_quat_input"></a>

#### set_quat_input

```python
def set_quat_input(input_name: str, value: Quat) -> None
```

x.set_quat_input(input_name, value) -> None
Set Quat Input

Args:
    input_name (str): 
    value (Quat):

<a id="unreal.UpgradeNiagaraScriptResults.set_new_input"></a>

#### set_new_input

```python
def set_new_input(input_name: str,
                  value: NiagaraPythonScriptModuleInput) -> None
```

x.set_new_input(input_name, value) -> None
Set New Input

Args:
    input_name (str): 
    value (NiagaraPythonScriptModuleInput):

<a id="unreal.UpgradeNiagaraScriptResults.set_linked_input"></a>

#### set_linked_input

```python
def set_linked_input(input_name: str, value: str) -> None
```

x.set_linked_input(input_name, value) -> None
Set Linked Input

Args:
    input_name (str): 
    value (str):

<a id="unreal.UpgradeNiagaraScriptResults.set_int_input"></a>

#### set_int_input

```python
def set_int_input(input_name: str, value: int) -> None
```

x.set_int_input(input_name, value) -> None
Set Int Input

Args:
    input_name (str): 
    value (int32):

<a id="unreal.UpgradeNiagaraScriptResults.set_float_input"></a>

#### set_float_input

```python
def set_float_input(input_name: str, value: float) -> None
```

x.set_float_input(input_name, value) -> None
Set Float Input

Args:
    input_name (str): 
    value (float):

<a id="unreal.UpgradeNiagaraScriptResults.set_enum_input"></a>

#### set_enum_input

```python
def set_enum_input(input_name: str, value: str) -> None
```

x.set_enum_input(input_name, value) -> None
Set Enum Input

Args:
    input_name (str): 
    value (str):

<a id="unreal.UpgradeNiagaraScriptResults.set_color_input"></a>

#### set_color_input

```python
def set_color_input(input_name: str, value: LinearColor) -> None
```

x.set_color_input(input_name, value) -> None
Set Color Input

Args:
    input_name (str): 
    value (LinearColor):

<a id="unreal.UpgradeNiagaraScriptResults.set_bool_input"></a>

#### set_bool_input

```python
def set_bool_input(input_name: str, value: bool) -> None
```

x.set_bool_input(input_name, value) -> None
Set Bool Input

Args:
    input_name (str): 
    value (bool):

<a id="unreal.UpgradeNiagaraScriptResults.reset_to_default"></a>

#### reset_to_default

```python
def reset_to_default(input_name: str) -> None
```

x.reset_to_default(input_name) -> None
Reset to Default

Args:
    input_name (str):

<a id="unreal.UpgradeNiagaraScriptResults.get_old_input"></a>

#### get_old_input

```python
def get_old_input(input_name: str) -> NiagaraPythonScriptModuleInput
```

x.get_old_input(input_name) -> NiagaraPythonScriptModuleInput
Get Old Input

Args:
    input_name (str): 

Returns:
    NiagaraPythonScriptModuleInput:

<a id="unreal.NiagaraPythonModule"></a>