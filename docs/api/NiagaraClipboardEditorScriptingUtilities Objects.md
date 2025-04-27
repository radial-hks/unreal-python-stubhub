## NiagaraClipboardEditorScriptingUtilities Objects

```python
class NiagaraClipboardEditorScriptingUtilities(Object)
```

Niagara Clipboard Editor Scripting Utilities

**C++ Source:**

- **Plugin**: Niagara
- **Module**: NiagaraEditor
- **File**: NiagaraClipboard.h

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.try_set_local_value_as_int"></a>

#### try_set_local_value_as_int

```python
@classmethod
def try_set_local_value_as_int(cls,
                               input: NiagaraClipboardFunctionInput,
                               value: int,
                               loose_typing: bool = True) -> bool
```

X.try_set_local_value_as_int(input, value, loose_typing=True) -> bool
Try Set Local Value as Int

Args:
    input (NiagaraClipboardFunctionInput): 
    value (int32): 
    loose_typing (bool): 

Returns:
    bool: 

    out_succeeded (bool):

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.try_get_local_value_as_int"></a>

#### try_get_local_value_as_int

```python
@classmethod
def try_get_local_value_as_int(
        cls, input: NiagaraClipboardFunctionInput) -> Tuple[bool, int]
```

X.try_get_local_value_as_int(input) -> (out_succeeded=bool, out_value=int32)
Try Get Local Value as Int

Args:
    input (NiagaraClipboardFunctionInput): 

Returns:
    tuple: 

    out_succeeded (bool): 

    out_value (int32):

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.try_get_local_value_as_float"></a>

#### try_get_local_value_as_float

```python
@classmethod
def try_get_local_value_as_float(
        cls, input: NiagaraClipboardFunctionInput) -> Tuple[bool, float]
```

X.try_get_local_value_as_float(input) -> (out_succeeded=bool, out_value=float)
Try Get Local Value as Float

Args:
    input (NiagaraClipboardFunctionInput): 

Returns:
    tuple: 

    out_succeeded (bool): 

    out_value (float):

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.try_get_input_by_name"></a>

#### try_get_input_by_name

```python
@classmethod
def try_get_input_by_name(
        cls, inputs: Array[NiagaraClipboardFunctionInput],
        input_name: Name) -> Tuple[bool, NiagaraClipboardFunctionInput]
```

X.try_get_input_by_name(inputs, input_name) -> (out_succeeded=bool, out_input=NiagaraClipboardFunctionInput)
Try Get Input by Name

Args:
    inputs (Array[NiagaraClipboardFunctionInput]): 
    input_name (Name): 

Returns:
    tuple: 

    out_succeeded (bool): 

    out_input (NiagaraClipboardFunctionInput):

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.get_type_name"></a>

#### get_type_name

```python
@classmethod
def get_type_name(cls, input: NiagaraClipboardFunctionInput) -> Name
```

X.get_type_name(input) -> Name
Get Type Name

Args:
    input (NiagaraClipboardFunctionInput): 

Returns:
    Name:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_vec3_local_value_input"></a>

#### create_vec3_local_value_input

```python
@classmethod
def create_vec3_local_value_input(
        cls, outer: Object, input_name: Name, has_edit_condition: bool,
        edit_condition_value: bool,
        vec3_value: Vector) -> NiagaraClipboardFunctionInput
```

X.create_vec3_local_value_input(outer, input_name, has_edit_condition, edit_condition_value, vec3_value) -> NiagaraClipboardFunctionInput
Create Vec 3Local Value Input

Args:
    outer (Object): 
    input_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    vec3_value (Vector): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_vec2_local_value_input"></a>

#### create_vec2_local_value_input

```python
@classmethod
def create_vec2_local_value_input(
        cls, outer: Object, input_name: Name, has_edit_condition: bool,
        edit_condition_value: bool,
        vec2_value: Vector2D) -> NiagaraClipboardFunctionInput
```

X.create_vec2_local_value_input(outer, input_name, has_edit_condition, edit_condition_value, vec2_value) -> NiagaraClipboardFunctionInput
Create Vec 2Local Value Input

Args:
    outer (Object): 
    input_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    vec2_value (Vector2D): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_struct_local_value_input"></a>

#### create_struct_local_value_input

```python
@classmethod
def create_struct_local_value_input(
        cls, outer: Object, input_name: Name, has_edit_condition: bool,
        edit_condition_value: bool,
        struct_value: UserDefinedStruct) -> NiagaraClipboardFunctionInput
```

X.create_struct_local_value_input(outer, input_name, has_edit_condition, edit_condition_value, struct_value) -> NiagaraClipboardFunctionInput
Create Struct Local Value Input

Args:
    outer (Object): 
    input_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    struct_value (UserDefinedStruct): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_linked_value_input"></a>

#### create_linked_value_input

```python
@classmethod
def create_linked_value_input(
        cls, outer: Object, input_name: Name, input_type_name: Name,
        has_edit_condition: bool, edit_condition_value: bool,
        linked_value: Name) -> NiagaraClipboardFunctionInput
```

X.create_linked_value_input(outer, input_name, input_type_name, has_edit_condition, edit_condition_value, linked_value) -> NiagaraClipboardFunctionInput
Create Linked Value Input

Args:
    outer (Object): 
    input_name (Name): 
    input_type_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    linked_value (Name): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_int_local_value_input"></a>

#### create_int_local_value_input

```python
@classmethod
def create_int_local_value_input(
        cls, outer: Object, input_name: Name, has_edit_condition: bool,
        edit_condition_value: bool,
        local_value: int) -> NiagaraClipboardFunctionInput
```

X.create_int_local_value_input(outer, input_name, has_edit_condition, edit_condition_value, local_value) -> NiagaraClipboardFunctionInput
Create Int Local Value Input

Args:
    outer (Object): 
    input_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    local_value (int32): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_float_local_value_input"></a>

#### create_float_local_value_input

```python
@classmethod
def create_float_local_value_input(
        cls, outer: Object, input_name: Name, has_edit_condition: bool,
        edit_condition_value: bool,
        local_value: float) -> NiagaraClipboardFunctionInput
```

X.create_float_local_value_input(outer, input_name, has_edit_condition, edit_condition_value, local_value) -> NiagaraClipboardFunctionInput
Create Float Local Value Input

Args:
    outer (Object): 
    input_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    local_value (float): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_expression_value_input"></a>

#### create_expression_value_input

```python
@classmethod
def create_expression_value_input(
        cls, outer: Object, input_name: Name, input_type_name: Name,
        has_edit_condition: bool, edit_condition_value: bool,
        expression_value: str) -> NiagaraClipboardFunctionInput
```

X.create_expression_value_input(outer, input_name, input_type_name, has_edit_condition, edit_condition_value, expression_value) -> NiagaraClipboardFunctionInput
Create Expression Value Input

Args:
    outer (Object): 
    input_name (Name): 
    input_type_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    expression_value (str): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_enum_local_value_input"></a>

#### create_enum_local_value_input

```python
@classmethod
def create_enum_local_value_input(
        cls, outer: Object, input_name: Name, has_edit_condition: bool,
        edit_codition_value: bool, enum_type: UserDefinedEnum,
        enum_value: int) -> NiagaraClipboardFunctionInput
```

X.create_enum_local_value_input(outer, input_name, has_edit_condition, edit_codition_value, enum_type, enum_value) -> NiagaraClipboardFunctionInput
Create Enum Local Value Input

Args:
    outer (Object): 
    input_name (Name): 
    has_edit_condition (bool): 
    edit_codition_value (bool): 
    enum_type (UserDefinedEnum): 
    enum_value (int32): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_dynamic_value_input"></a>

#### create_dynamic_value_input

```python
@classmethod
def create_dynamic_value_input(
        cls, outer: Object, input_name: Name, input_type_name: Name,
        has_edit_condition: bool, edit_condition_value: bool,
        dynamic_value_name: str,
        dynamic_value: NiagaraScript) -> NiagaraClipboardFunctionInput
```

X.create_dynamic_value_input(outer, input_name, input_type_name, has_edit_condition, edit_condition_value, dynamic_value_name, dynamic_value) -> NiagaraClipboardFunctionInput
Create Dynamic Value Input

Args:
    outer (Object): 
    input_name (Name): 
    input_type_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    dynamic_value_name (str): 
    dynamic_value (NiagaraScript): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_data_value_input"></a>

#### create_data_value_input

```python
@classmethod
def create_data_value_input(
        cls, outer: Object, input_name: Name, has_edit_condition: bool,
        edit_condition_value: bool,
        data_value: NiagaraDataInterface) -> NiagaraClipboardFunctionInput
```

X.create_data_value_input(outer, input_name, has_edit_condition, edit_condition_value, data_value) -> NiagaraClipboardFunctionInput
Create Data Value Input

Args:
    outer (Object): 
    input_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    data_value (NiagaraDataInterface): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraClipboardEditorScriptingUtilities.create_bool_local_value_input"></a>

#### create_bool_local_value_input

```python
@classmethod
def create_bool_local_value_input(
        cls, outer: Object, input_name: Name, has_edit_condition: bool,
        edit_condition_value: bool,
        bool_value: bool) -> NiagaraClipboardFunctionInput
```

X.create_bool_local_value_input(outer, input_name, has_edit_condition, edit_condition_value, bool_value) -> NiagaraClipboardFunctionInput
Create Bool Local Value Input

Args:
    outer (Object): 
    input_name (Name): 
    has_edit_condition (bool): 
    edit_condition_value (bool): 
    bool_value (bool): 

Returns:
    NiagaraClipboardFunctionInput:

<a id="unreal.NiagaraEffectTypeFactoryNew"></a>