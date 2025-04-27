## RigVM Objects

```python
class RigVM(Object)
```

The RigVM is the main object for evaluating FRigVMByteCode instructions.
It combines the byte code, a list of required function pointers for
execute instructions and required memory in one class.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVM.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_memory_storage_object`` (RigVMMemoryStorage):  [Read-Write] Deprecated 5.4,
  deprecated: Please use DefaultDebugMemoryStorage for compiling and DebugMemoryStorage in the ExtendedExecuteContext for intance execution
- ``literal_memory_storage_object`` (RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
  deprecated: Please, use LiteralMemoryStorage
- ``work_memory_storage_object`` (RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
  deprecated: Please, use DefaultWorkMemoryStorage for compiling and WorkMemoryStorage in the ExtendedExecuteContext for intance execution

<a id="unreal.RigVM.work_memory_storage_object"></a>

#### work_memory_storage_object

```python
@property
def work_memory_storage_object() -> RigVMMemoryStorage
```

(RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
deprecated: Please, use DefaultWorkMemoryStorage for compiling and WorkMemoryStorage in the ExtendedExecuteContext for intance execution

<a id="unreal.RigVM.work_memory_storage_object"></a>

#### work_memory_storage_object

```python
@work_memory_storage_object.setter
def work_memory_storage_object(value: RigVMMemoryStorage) -> None
```

<a id="unreal.RigVM.literal_memory_storage_object"></a>

#### literal_memory_storage_object

```python
@property
def literal_memory_storage_object() -> RigVMMemoryStorage
```

(RigVMMemoryStorage):  [Read-Write] Deprecated 5.4
deprecated: Please, use LiteralMemoryStorage

<a id="unreal.RigVM.literal_memory_storage_object"></a>

#### literal_memory_storage_object

```python
@literal_memory_storage_object.setter
def literal_memory_storage_object(value: RigVMMemoryStorage) -> None
```

<a id="unreal.RigVM.debug_memory_storage_object"></a>

#### debug_memory_storage_object

```python
@property
def debug_memory_storage_object() -> RigVMMemoryStorage
```

(RigVMMemoryStorage):  [Read-Write] Deprecated 5.4,
deprecated: Please use DefaultDebugMemoryStorage for compiling and DebugMemoryStorage in the ExtendedExecuteContext for intance execution

<a id="unreal.RigVM.debug_memory_storage_object"></a>

#### debug_memory_storage_object

```python
@debug_memory_storage_object.setter
def debug_memory_storage_object(value: RigVMMemoryStorage) -> None
```

<a id="unreal.RigVM.set_parameter_value_vector2d"></a>

#### set_parameter_value_vector2d

```python
def set_parameter_value_vector2d(parameter_name: Name,
                                 value: Vector2D,
                                 array_index: int = 0) -> None
```

x.set_parameter_value_vector2d(parameter_name, value, array_index=0) -> None
Set Parameter Value Vector 2D
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (Vector2D): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_vector"></a>

#### set_parameter_value_vector

```python
def set_parameter_value_vector(parameter_name: Name,
                               value: Vector,
                               array_index: int = 0) -> None
```

x.set_parameter_value_vector(parameter_name, value, array_index=0) -> None
Set Parameter Value Vector
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (Vector): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_transform"></a>

#### set_parameter_value_transform

```python
def set_parameter_value_transform(parameter_name: Name,
                                  value: Transform,
                                  array_index: int = 0) -> None
```

x.set_parameter_value_transform(parameter_name, value, array_index=0) -> None
Set Parameter Value Transform
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (Transform): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_string"></a>

#### set_parameter_value_string

```python
def set_parameter_value_string(parameter_name: Name,
                               value: str,
                               array_index: int = 0) -> None
```

x.set_parameter_value_string(parameter_name, value, array_index=0) -> None
Set Parameter Value String
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (str): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_quat"></a>

#### set_parameter_value_quat

```python
def set_parameter_value_quat(parameter_name: Name,
                             value: Quat,
                             array_index: int = 0) -> None
```

x.set_parameter_value_quat(parameter_name, value, array_index=0) -> None
Set Parameter Value Quat
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (Quat): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_name"></a>

#### set_parameter_value_name

```python
def set_parameter_value_name(parameter_name: Name,
                             value: Name,
                             array_index: int = 0) -> None
```

x.set_parameter_value_name(parameter_name, value, array_index=0) -> None
Set Parameter Value Name
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (Name): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_int"></a>

#### set_parameter_value_int

```python
def set_parameter_value_int(parameter_name: Name,
                            value: int,
                            array_index: int = 0) -> None
```

x.set_parameter_value_int(parameter_name, value, array_index=0) -> None
Set Parameter Value Int
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (int32): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_float"></a>

#### set_parameter_value_float

```python
def set_parameter_value_float(parameter_name: Name,
                              value: float,
                              array_index: int = 0) -> None
```

x.set_parameter_value_float(parameter_name, value, array_index=0) -> None
Set Parameter Value Float
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (float): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_double"></a>

#### set_parameter_value_double

```python
def set_parameter_value_double(parameter_name: Name,
                               value: float,
                               array_index: int = 0) -> None
```

x.set_parameter_value_double(parameter_name, value, array_index=0) -> None
Set Parameter Value Double
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (double): 
    array_index (int32):

<a id="unreal.RigVM.set_parameter_value_bool"></a>

#### set_parameter_value_bool

```python
def set_parameter_value_bool(parameter_name: Name,
                             value: bool,
                             array_index: int = 0) -> None
```

x.set_parameter_value_bool(parameter_name, value, array_index=0) -> None
Set Parameter Value Bool
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    value (bool): 
    array_index (int32):

<a id="unreal.RigVM.get_statistics"></a>

#### get_statistics

```python
def get_statistics() -> RigVMStatistics
```

x.get_statistics() -> RigVMStatistics
returns the statistics information
deprecated: Function 'GetStatistics' is deprecated.

Returns:
    RigVMStatistics:

<a id="unreal.RigVM.get_parameter_value_vector2d"></a>

#### get_parameter_value_vector2d

```python
def get_parameter_value_vector2d(parameter_name: Name,
                                 array_index: int = 0) -> Vector2D
```

x.get_parameter_value_vector2d(parameter_name, array_index=0) -> Vector2D
Get Parameter Value Vector 2D
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    Vector2D:

<a id="unreal.RigVM.get_parameter_value_vector"></a>

#### get_parameter_value_vector

```python
def get_parameter_value_vector(parameter_name: Name,
                               array_index: int = 0) -> Vector
```

x.get_parameter_value_vector(parameter_name, array_index=0) -> Vector
Get Parameter Value Vector
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    Vector:

<a id="unreal.RigVM.get_parameter_value_transform"></a>

#### get_parameter_value_transform

```python
def get_parameter_value_transform(parameter_name: Name,
                                  array_index: int = 0) -> Transform
```

x.get_parameter_value_transform(parameter_name, array_index=0) -> Transform
Get Parameter Value Transform
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    Transform:

<a id="unreal.RigVM.get_parameter_value_string"></a>

#### get_parameter_value_string

```python
def get_parameter_value_string(parameter_name: Name,
                               array_index: int = 0) -> str
```

x.get_parameter_value_string(parameter_name, array_index=0) -> str
Get Parameter Value String
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    str:

<a id="unreal.RigVM.get_parameter_value_quat"></a>

#### get_parameter_value_quat

```python
def get_parameter_value_quat(parameter_name: Name,
                             array_index: int = 0) -> Quat
```

x.get_parameter_value_quat(parameter_name, array_index=0) -> Quat
Get Parameter Value Quat
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    Quat:

<a id="unreal.RigVM.get_parameter_value_name"></a>

#### get_parameter_value_name

```python
def get_parameter_value_name(parameter_name: Name,
                             array_index: int = 0) -> Name
```

x.get_parameter_value_name(parameter_name, array_index=0) -> Name
Get Parameter Value Name
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    Name:

<a id="unreal.RigVM.get_parameter_value_int"></a>

#### get_parameter_value_int

```python
def get_parameter_value_int(parameter_name: Name, array_index: int = 0) -> int
```

x.get_parameter_value_int(parameter_name, array_index=0) -> int32
Get Parameter Value Int
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    int32:

<a id="unreal.RigVM.get_parameter_value_float"></a>

#### get_parameter_value_float

```python
def get_parameter_value_float(parameter_name: Name,
                              array_index: int = 0) -> float
```

x.get_parameter_value_float(parameter_name, array_index=0) -> float
Get Parameter Value Float
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    float:

<a id="unreal.RigVM.get_parameter_value_double"></a>

#### get_parameter_value_double

```python
def get_parameter_value_double(parameter_name: Name,
                               array_index: int = 0) -> float
```

x.get_parameter_value_double(parameter_name, array_index=0) -> double
Get Parameter Value Double
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    double:

<a id="unreal.RigVM.get_parameter_value_bool"></a>

#### get_parameter_value_bool

```python
def get_parameter_value_bool(parameter_name: Name,
                             array_index: int = 0) -> bool
```

x.get_parameter_value_bool(parameter_name, array_index=0) -> bool
Get Parameter Value Bool
deprecated: This function has been deprecated and it is no longer supported, please, update your code.

Args:
    parameter_name (Name): 
    array_index (int32): 

Returns:
    bool:

<a id="unreal.RigVM.execute"></a>

#### execute

```python
def execute(
        entry_name: Name = "None") -> Optional[RigVMExtendedExecuteContext]
```

x.execute(entry_name="None") -> RigVMExtendedExecuteContext or None
Execute
deprecated: This function has been deprecated and it is no longer supported.

Args:
    entry_name (Name): 

Returns:
    RigVMExtendedExecuteContext or None: 

    context (RigVMExtendedExecuteContext):

<a id="unreal.NameSpacedUserData"></a>