## PCGGraphParametersHelpers Objects

```python
class PCGGraphParametersHelpers(BlueprintFunctionLibrary)
```

Blueprint Library to get or set graph parameters on graphs and graph instances

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGraphParametersHelpers.h

<a id="unreal.PCGGraphParametersHelpers.set_vector_parameter"></a>

#### set_vector_parameter

```python
@classmethod
def set_vector_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                         value: Vector) -> None
```

X.set_vector_parameter(graph_interface, name, value) -> None
Set Vector Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Vector):

<a id="unreal.PCGGraphParametersHelpers.set_vector4_parameter"></a>

#### set_vector4_parameter

```python
@classmethod
def set_vector4_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                          value: Vector4) -> None
```

X.set_vector4_parameter(graph_interface, name, value) -> None
Set Vector 4Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Vector4):

<a id="unreal.PCGGraphParametersHelpers.set_vector2d_parameter"></a>

#### set_vector2d_parameter

```python
@classmethod
def set_vector2d_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                           value: Vector2D) -> None
```

X.set_vector2d_parameter(graph_interface, name, value) -> None
Set Vector 2DParameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Vector2D):

<a id="unreal.PCGGraphParametersHelpers.set_transform_parameter"></a>

#### set_transform_parameter

```python
@classmethod
def set_transform_parameter(cls, graph_interface: PCGGraphInterface,
                            name: Name, value: Transform) -> None
```

X.set_transform_parameter(graph_interface, name, value) -> None
Set Transform Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Transform):

<a id="unreal.PCGGraphParametersHelpers.set_string_parameter"></a>

#### set_string_parameter

```python
@classmethod
def set_string_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                         value: str) -> None
```

X.set_string_parameter(graph_interface, name, value) -> None
Set String Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (str):

<a id="unreal.PCGGraphParametersHelpers.set_soft_object_path_parameter"></a>

#### set_soft_object_path_parameter

```python
@classmethod
def set_soft_object_path_parameter(cls, graph_interface: PCGGraphInterface,
                                   name: Name, value: SoftObjectPath) -> None
```

X.set_soft_object_path_parameter(graph_interface, name, value) -> None
Set Soft Object Path Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (SoftObjectPath):

<a id="unreal.PCGGraphParametersHelpers.set_soft_object_parameter"></a>

#### set_soft_object_parameter

```python
@classmethod
def set_soft_object_parameter(cls, graph_interface: PCGGraphInterface,
                              name: Name, value: Object) -> None
```

X.set_soft_object_parameter(graph_interface, name, value) -> None
Set Soft Object Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Object):

<a id="unreal.PCGGraphParametersHelpers.set_soft_class_parameter"></a>

#### set_soft_class_parameter

```python
@classmethod
def set_soft_class_parameter(cls, graph_interface: PCGGraphInterface,
                             name: Name, value: Class) -> None
```

X.set_soft_class_parameter(graph_interface, name, value) -> None
Set Soft Class Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Class):

<a id="unreal.PCGGraphParametersHelpers.set_rotator_parameter"></a>

#### set_rotator_parameter

```python
@classmethod
def set_rotator_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                          value: Rotator) -> None
```

X.set_rotator_parameter(graph_interface, name, value) -> None
Set Rotator Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Rotator):

<a id="unreal.PCGGraphParametersHelpers.set_quaternion_parameter"></a>

#### set_quaternion_parameter

```python
@classmethod
def set_quaternion_parameter(cls, graph_interface: PCGGraphInterface,
                             name: Name, value: Quat) -> None
```

X.set_quaternion_parameter(graph_interface, name, value) -> None
Set Quaternion Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Quat):

<a id="unreal.PCGGraphParametersHelpers.set_object_parameter"></a>

#### set_object_parameter

```python
@classmethod
def set_object_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                         value: Object) -> None
```

X.set_object_parameter(graph_interface, name, value) -> None
Set Object Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Object):

<a id="unreal.PCGGraphParametersHelpers.set_name_parameter"></a>

#### set_name_parameter

```python
@classmethod
def set_name_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                       value: Name) -> None
```

X.set_name_parameter(graph_interface, name, value) -> None
Set Name Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (Name):

<a id="unreal.PCGGraphParametersHelpers.set_int64_parameter"></a>

#### set_int64_parameter

```python
@classmethod
def set_int64_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                        value: int) -> None
```

X.set_int64_parameter(graph_interface, name, value) -> None
Set Int 64Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (int64):

<a id="unreal.PCGGraphParametersHelpers.set_int32_parameter"></a>

#### set_int32_parameter

```python
@classmethod
def set_int32_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                        value: int) -> None
```

X.set_int32_parameter(graph_interface, name, value) -> None
Set Int 32Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (int32):

<a id="unreal.PCGGraphParametersHelpers.set_float_parameter"></a>

#### set_float_parameter

```python
@classmethod
def set_float_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                        value: float) -> None
```

X.set_float_parameter(graph_interface, name, value) -> None
Setters

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (float):

<a id="unreal.PCGGraphParametersHelpers.set_enum_parameter"></a>

#### set_enum_parameter

```python
@classmethod
def set_enum_parameter(cls,
                       graph_interface: PCGGraphInterface,
                       name: Name,
                       value: int,
                       enum: Enum = None) -> None
```

X.set_enum_parameter(graph_interface, name, value, enum=None) -> None
Set Enum Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (uint8): 
    enum (Enum):

<a id="unreal.PCGGraphParametersHelpers.set_double_parameter"></a>

#### set_double_parameter

```python
@classmethod
def set_double_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                         value: float) -> None
```

X.set_double_parameter(graph_interface, name, value) -> None
Set Double Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (double):

<a id="unreal.PCGGraphParametersHelpers.set_class_parameter"></a>

#### set_class_parameter

```python
@classmethod
def set_class_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                        value: Class) -> None
```

X.set_class_parameter(graph_interface, name, value) -> None
Set Class Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (type(Class)):

<a id="unreal.PCGGraphParametersHelpers.set_byte_parameter"></a>

#### set_byte_parameter

```python
@classmethod
def set_byte_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                       value: int) -> None
```

X.set_byte_parameter(graph_interface, name, value) -> None
Set Byte Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (uint8):

<a id="unreal.PCGGraphParametersHelpers.set_bool_parameter"></a>

#### set_bool_parameter

```python
@classmethod
def set_bool_parameter(cls, graph_interface: PCGGraphInterface, name: Name,
                       value: bool) -> None
```

X.set_bool_parameter(graph_interface, name, value) -> None
Set Bool Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 
    value (bool):

<a id="unreal.PCGGraphParametersHelpers.is_overridden"></a>

#### is_overridden

```python
@classmethod
def is_overridden(cls, graph_interface: PCGGraphInterface, name: Name) -> bool
```

X.is_overridden(graph_interface, name) -> bool
Is Overridden

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    bool:

<a id="unreal.PCGGraphParametersHelpers.get_vector_parameter"></a>

#### get_vector_parameter

```python
@classmethod
def get_vector_parameter(cls, graph_interface: PCGGraphInterface,
                         name: Name) -> Vector
```

X.get_vector_parameter(graph_interface, name) -> Vector
Get Vector Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Vector:

<a id="unreal.PCGGraphParametersHelpers.get_vector4_parameter"></a>

#### get_vector4_parameter

```python
@classmethod
def get_vector4_parameter(cls, graph_interface: PCGGraphInterface,
                          name: Name) -> Vector4
```

X.get_vector4_parameter(graph_interface, name) -> Vector4
Get Vector 4Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Vector4:

<a id="unreal.PCGGraphParametersHelpers.get_vector2d_parameter"></a>

#### get_vector2d_parameter

```python
@classmethod
def get_vector2d_parameter(cls, graph_interface: PCGGraphInterface,
                           name: Name) -> Vector2D
```

X.get_vector2d_parameter(graph_interface, name) -> Vector2D
Get Vector 2DParameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Vector2D:

<a id="unreal.PCGGraphParametersHelpers.get_transform_parameter"></a>

#### get_transform_parameter

```python
@classmethod
def get_transform_parameter(cls, graph_interface: PCGGraphInterface,
                            name: Name) -> Transform
```

X.get_transform_parameter(graph_interface, name) -> Transform
Get Transform Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Transform:

<a id="unreal.PCGGraphParametersHelpers.get_string_parameter"></a>

#### get_string_parameter

```python
@classmethod
def get_string_parameter(cls, graph_interface: PCGGraphInterface,
                         name: Name) -> str
```

X.get_string_parameter(graph_interface, name) -> str
Get String Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    str:

<a id="unreal.PCGGraphParametersHelpers.get_soft_object_path_parameter"></a>

#### get_soft_object_path_parameter

```python
@classmethod
def get_soft_object_path_parameter(cls, graph_interface: PCGGraphInterface,
                                   name: Name) -> SoftObjectPath
```

X.get_soft_object_path_parameter(graph_interface, name) -> SoftObjectPath
Get Soft Object Path Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    SoftObjectPath:

<a id="unreal.PCGGraphParametersHelpers.get_soft_object_parameter"></a>

#### get_soft_object_parameter

```python
@classmethod
def get_soft_object_parameter(cls, graph_interface: PCGGraphInterface,
                              name: Name) -> Object
```

X.get_soft_object_parameter(graph_interface, name) -> Object
Get Soft Object Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Object:

<a id="unreal.PCGGraphParametersHelpers.get_soft_class_parameter"></a>

#### get_soft_class_parameter

```python
@classmethod
def get_soft_class_parameter(cls, graph_interface: PCGGraphInterface,
                             name: Name) -> Class
```

X.get_soft_class_parameter(graph_interface, name) -> Class
Get Soft Class Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Class:

<a id="unreal.PCGGraphParametersHelpers.get_rotator_parameter"></a>

#### get_rotator_parameter

```python
@classmethod
def get_rotator_parameter(cls, graph_interface: PCGGraphInterface,
                          name: Name) -> Rotator
```

X.get_rotator_parameter(graph_interface, name) -> Rotator
Get Rotator Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Rotator:

<a id="unreal.PCGGraphParametersHelpers.get_quaternion_parameter"></a>

#### get_quaternion_parameter

```python
@classmethod
def get_quaternion_parameter(cls, graph_interface: PCGGraphInterface,
                             name: Name) -> Quat
```

X.get_quaternion_parameter(graph_interface, name) -> Quat
Get Quaternion Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Quat:

<a id="unreal.PCGGraphParametersHelpers.get_object_parameter"></a>

#### get_object_parameter

```python
@classmethod
def get_object_parameter(cls, graph_interface: PCGGraphInterface,
                         name: Name) -> Object
```

X.get_object_parameter(graph_interface, name) -> Object
Get Object Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Object:

<a id="unreal.PCGGraphParametersHelpers.get_name_parameter"></a>

#### get_name_parameter

```python
@classmethod
def get_name_parameter(cls, graph_interface: PCGGraphInterface,
                       name: Name) -> Name
```

X.get_name_parameter(graph_interface, name) -> Name
Get Name Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    Name:

<a id="unreal.PCGGraphParametersHelpers.get_int64_parameter"></a>

#### get_int64_parameter

```python
@classmethod
def get_int64_parameter(cls, graph_interface: PCGGraphInterface,
                        name: Name) -> int
```

X.get_int64_parameter(graph_interface, name) -> int64
Get Int 64Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    int64:

<a id="unreal.PCGGraphParametersHelpers.get_int32_parameter"></a>

#### get_int32_parameter

```python
@classmethod
def get_int32_parameter(cls, graph_interface: PCGGraphInterface,
                        name: Name) -> int
```

X.get_int32_parameter(graph_interface, name) -> int32
Get Int 32Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    int32:

<a id="unreal.PCGGraphParametersHelpers.get_float_parameter"></a>

#### get_float_parameter

```python
@classmethod
def get_float_parameter(cls, graph_interface: PCGGraphInterface,
                        name: Name) -> float
```

X.get_float_parameter(graph_interface, name) -> float
Getters

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    float:

<a id="unreal.PCGGraphParametersHelpers.get_enum_parameter"></a>

#### get_enum_parameter

```python
@classmethod
def get_enum_parameter(cls, graph_interface: PCGGraphInterface,
                       name: Name) -> int
```

X.get_enum_parameter(graph_interface, name) -> uint8
Get Enum Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    uint8:

<a id="unreal.PCGGraphParametersHelpers.get_double_parameter"></a>

#### get_double_parameter

```python
@classmethod
def get_double_parameter(cls, graph_interface: PCGGraphInterface,
                         name: Name) -> float
```

X.get_double_parameter(graph_interface, name) -> double
Get Double Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    double:

<a id="unreal.PCGGraphParametersHelpers.get_class_parameter"></a>

#### get_class_parameter

```python
@classmethod
def get_class_parameter(cls, graph_interface: PCGGraphInterface,
                        name: Name) -> Class
```

X.get_class_parameter(graph_interface, name) -> type(Class)
Get Class Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    type(Class):

<a id="unreal.PCGGraphParametersHelpers.get_byte_parameter"></a>

#### get_byte_parameter

```python
@classmethod
def get_byte_parameter(cls, graph_interface: PCGGraphInterface,
                       name: Name) -> int
```

X.get_byte_parameter(graph_interface, name) -> uint8
Get Byte Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    uint8:

<a id="unreal.PCGGraphParametersHelpers.get_bool_parameter"></a>

#### get_bool_parameter

```python
@classmethod
def get_bool_parameter(cls, graph_interface: PCGGraphInterface,
                       name: Name) -> bool
```

X.get_bool_parameter(graph_interface, name) -> bool
Get Bool Parameter

Args:
    graph_interface (PCGGraphInterface): 
    name (Name): 

Returns:
    bool:

<a id="unreal.PCGHiGenGridSizeSettings"></a>