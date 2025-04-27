## NiagaraDataInterfaceArrayFunctionLibrary Objects

```python
class NiagaraDataInterfaceArrayFunctionLibrary(BlueprintFunctionLibrary)
```

C++ and Blueprint library for accessing array types

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceArrayFunctionLibrary.h

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector_value"></a>

#### set_niagara_array_vector_value

```python
@classmethod
def set_niagara_array_vector_value(cls, niagara_system: NiagaraComponent,
                                   override_name: Name, index: int,
                                   value: Vector, size_to_fit: bool) -> None
```

X.set_niagara_array_vector_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array FVector.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (Vector): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector4_value"></a>

#### set_niagara_array_vector4_value

```python
@classmethod
def set_niagara_array_vector4_value(cls, niagara_system: NiagaraComponent,
                                    override_name: Name, index: int,
                                    value: Vector4, size_to_fit: bool) -> None
```

X.set_niagara_array_vector4_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array FVector4.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (Vector4): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector4"></a>

#### set_niagara_array_vector4

```python
@classmethod
def set_niagara_array_vector4(cls, niagara_system: NiagaraComponent,
                              override_name: Name,
                              array_data: Array[Vector4]) -> None
```

X.set_niagara_array_vector4(niagara_system, override_name, array_data) -> None
Sets Niagara Array FVector4 Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[Vector4]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector2d_value"></a>

#### set_niagara_array_vector2d_value

```python
@classmethod
def set_niagara_array_vector2d_value(cls, niagara_system: NiagaraComponent,
                                     override_name: Name, index: int,
                                     value: Vector2D,
                                     size_to_fit: bool) -> None
```

X.set_niagara_array_vector2d_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array FVector2D.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (Vector2D): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector2d"></a>

#### set_niagara_array_vector2d

```python
@classmethod
def set_niagara_array_vector2d(cls, niagara_system: NiagaraComponent,
                               override_name: Name,
                               array_data: Array[Vector2D]) -> None
```

X.set_niagara_array_vector2d(niagara_system, override_name, array_data) -> None
Sets Niagara Array FVector2D Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[Vector2D]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_vector"></a>

#### set_niagara_array_vector

```python
@classmethod
def set_niagara_array_vector(cls, niagara_system: NiagaraComponent,
                             override_name: Name,
                             array_data: Array[Vector]) -> None
```

X.set_niagara_array_vector(niagara_system, override_name, array_data) -> None
Sets Niagara Array FVector Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[Vector]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_u_int8_value"></a>

#### set_niagara_array_u_int8_value

```python
@classmethod
def set_niagara_array_u_int8_value(cls, niagara_system: NiagaraComponent,
                                   override_name: Name, index: int, value: int,
                                   size_to_fit: bool) -> None
```

X.set_niagara_array_u_int8_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array UInt8.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (int32): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_u_int8"></a>

#### set_niagara_array_u_int8

```python
@classmethod
def set_niagara_array_u_int8(cls, niagara_system: NiagaraComponent,
                             override_name: Name,
                             array_data: Array[int]) -> None
```

X.set_niagara_array_u_int8(niagara_system, override_name, array_data) -> None
Sets Niagara Array UInt8 Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[int32]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_quat_value"></a>

#### set_niagara_array_quat_value

```python
@classmethod
def set_niagara_array_quat_value(cls, niagara_system: NiagaraComponent,
                                 override_name: Name, index: int, value: Quat,
                                 size_to_fit: bool) -> None
```

X.set_niagara_array_quat_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array FQuat.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (Quat): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_quat"></a>

#### set_niagara_array_quat

```python
@classmethod
def set_niagara_array_quat(cls, niagara_system: NiagaraComponent,
                           override_name: Name,
                           array_data: Array[Quat]) -> None
```

X.set_niagara_array_quat(niagara_system, override_name, array_data) -> None
Sets Niagara Array FQuat Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[Quat]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_position_value"></a>

#### set_niagara_array_position_value

```python
@classmethod
def set_niagara_array_position_value(cls, niagara_system: NiagaraComponent,
                                     override_name: Name, index: int,
                                     value: Vector, size_to_fit: bool) -> None
```

X.set_niagara_array_position_value(niagara_system, override_name, index, value, size_to_fit) -> None
Set Niagara Array Position Value

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (Vector): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_position"></a>

#### set_niagara_array_position

```python
@classmethod
def set_niagara_array_position(cls, niagara_system: NiagaraComponent,
                               override_name: Name,
                               array_data: Array[Vector]) -> None
```

X.set_niagara_array_position(niagara_system, override_name, array_data) -> None
Sets Niagara Array FVector Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[Vector]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_matrix_value"></a>

#### set_niagara_array_matrix_value

```python
@classmethod
def set_niagara_array_matrix_value(cls,
                                   niagara_system: NiagaraComponent,
                                   override_name: Name,
                                   index: int,
                                   value: Matrix,
                                   size_to_fit: bool,
                                   apply_lwc_rebase: bool = True) -> None
```

X.set_niagara_array_matrix_value(niagara_system, override_name, index, value, size_to_fit, apply_lwc_rebase=True) -> None
Sets a single value within a Niagara Array FMatrix.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (Matrix): 
    size_to_fit (bool): 
    apply_lwc_rebase (bool): When enabled the matrix translation will have the simulation tile offset subtracted from it

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_matrix"></a>

#### set_niagara_array_matrix

```python
@classmethod
def set_niagara_array_matrix(cls,
                             niagara_system: NiagaraComponent,
                             override_name: Name,
                             array_data: Array[Matrix],
                             apply_lwc_rebase: bool = True) -> None
```

X.set_niagara_array_matrix(niagara_system, override_name, array_data, apply_lwc_rebase=True) -> None
Sets Niagara Array FMatrix Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[Matrix]): 
    apply_lwc_rebase (bool): When enabled the matrix translation will have the simulation tile offset subtracted from it

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_int32_value"></a>

#### set_niagara_array_int32_value

```python
@classmethod
def set_niagara_array_int32_value(cls, niagara_system: NiagaraComponent,
                                  override_name: Name, index: int, value: int,
                                  size_to_fit: bool) -> None
```

X.set_niagara_array_int32_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array Int32.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (int32): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_int32"></a>

#### set_niagara_array_int32

```python
@classmethod
def set_niagara_array_int32(cls, niagara_system: NiagaraComponent,
                            override_name: Name,
                            array_data: Array[int]) -> None
```

X.set_niagara_array_int32(niagara_system, override_name, array_data) -> None
Sets Niagara Array Int32 Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[int32]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_float_value"></a>

#### set_niagara_array_float_value

```python
@classmethod
def set_niagara_array_float_value(cls, niagara_system: NiagaraComponent,
                                  override_name: Name, index: int,
                                  value: float, size_to_fit: bool) -> None
```

X.set_niagara_array_float_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array Float.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (float): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_float"></a>

#### set_niagara_array_float

```python
@classmethod
def set_niagara_array_float(cls, niagara_system: NiagaraComponent,
                            override_name: Name,
                            array_data: Array[float]) -> None
```

X.set_niagara_array_float(niagara_system, override_name, array_data) -> None
Sets Niagara Array Float Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[float]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_color_value"></a>

#### set_niagara_array_color_value

```python
@classmethod
def set_niagara_array_color_value(cls, niagara_system: NiagaraComponent,
                                  override_name: Name, index: int,
                                  value: LinearColor,
                                  size_to_fit: bool) -> None
```

X.set_niagara_array_color_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array FLinearColor.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (LinearColor): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_color"></a>

#### set_niagara_array_color

```python
@classmethod
def set_niagara_array_color(cls, niagara_system: NiagaraComponent,
                            override_name: Name,
                            array_data: Array[LinearColor]) -> None
```

X.set_niagara_array_color(niagara_system, override_name, array_data) -> None
Sets Niagara Array FLinearColor Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[LinearColor]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_bool_value"></a>

#### set_niagara_array_bool_value

```python
@classmethod
def set_niagara_array_bool_value(cls, niagara_system: NiagaraComponent,
                                 override_name: Name, index: int, value: bool,
                                 size_to_fit: bool) -> None
```

X.set_niagara_array_bool_value(niagara_system, override_name, index, value, size_to_fit) -> None
Sets a single value within a Niagara Array Bool.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    value (bool): 
    size_to_fit (bool):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.set_niagara_array_bool"></a>

#### set_niagara_array_bool

```python
@classmethod
def set_niagara_array_bool(cls, niagara_system: NiagaraComponent,
                           override_name: Name,
                           array_data: Array[bool]) -> None
```

X.set_niagara_array_bool(niagara_system, override_name, array_data) -> None
Sets Niagara Array Bool Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    array_data (Array[bool]):

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector_value"></a>

#### get_niagara_array_vector_value

```python
@classmethod
def get_niagara_array_vector_value(cls, niagara_system: NiagaraComponent,
                                   override_name: Name, index: int) -> Vector
```

X.get_niagara_array_vector_value(niagara_system, override_name, index) -> Vector
Gets a single value within a Niagara Array FVector.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    Vector:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector4_value"></a>

#### get_niagara_array_vector4_value

```python
@classmethod
def get_niagara_array_vector4_value(cls, niagara_system: NiagaraComponent,
                                    override_name: Name,
                                    index: int) -> Vector4
```

X.get_niagara_array_vector4_value(niagara_system, override_name, index) -> Vector4
Gets a single value within a Niagara Array FVector4.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    Vector4:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector4"></a>

#### get_niagara_array_vector4

```python
@classmethod
def get_niagara_array_vector4(cls, niagara_system: NiagaraComponent,
                              override_name: Name) -> Array[Vector4]
```

X.get_niagara_array_vector4(niagara_system, override_name) -> Array[Vector4]
Gets a copy of Niagara FVector4 Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[Vector4]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector2d_value"></a>

#### get_niagara_array_vector2d_value

```python
@classmethod
def get_niagara_array_vector2d_value(cls, niagara_system: NiagaraComponent,
                                     override_name: Name,
                                     index: int) -> Vector2D
```

X.get_niagara_array_vector2d_value(niagara_system, override_name, index) -> Vector2D
Gets a single value within a Niagara Array FVector2D.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    Vector2D:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector2d"></a>

#### get_niagara_array_vector2d

```python
@classmethod
def get_niagara_array_vector2d(cls, niagara_system: NiagaraComponent,
                               override_name: Name) -> Array[Vector2D]
```

X.get_niagara_array_vector2d(niagara_system, override_name) -> Array[Vector2D]
Gets a copy of Niagara FVector2D Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[Vector2D]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_vector"></a>

#### get_niagara_array_vector

```python
@classmethod
def get_niagara_array_vector(cls, niagara_system: NiagaraComponent,
                             override_name: Name) -> Array[Vector]
```

X.get_niagara_array_vector(niagara_system, override_name) -> Array[Vector]
Gets a copy of Niagara FVector Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[Vector]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_u_int8_value"></a>

#### get_niagara_array_u_int8_value

```python
@classmethod
def get_niagara_array_u_int8_value(cls, niagara_system: NiagaraComponent,
                                   override_name: Name, index: int) -> int
```

X.get_niagara_array_u_int8_value(niagara_system, override_name, index) -> int32
Gets a single value within a Niagara Array UInt8.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    int32:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_u_int8"></a>

#### get_niagara_array_u_int8

```python
@classmethod
def get_niagara_array_u_int8(cls, niagara_system: NiagaraComponent,
                             override_name: Name) -> Array[int]
```

X.get_niagara_array_u_int8(niagara_system, override_name) -> Array[int32]
Gets a copy of Niagara UInt8 Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[int32]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_quat_value"></a>

#### get_niagara_array_quat_value

```python
@classmethod
def get_niagara_array_quat_value(cls, niagara_system: NiagaraComponent,
                                 override_name: Name, index: int) -> Quat
```

X.get_niagara_array_quat_value(niagara_system, override_name, index) -> Quat
Gets a single value within a Niagara Array FQuat.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    Quat:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_quat"></a>

#### get_niagara_array_quat

```python
@classmethod
def get_niagara_array_quat(cls, niagara_system: NiagaraComponent,
                           override_name: Name) -> Array[Quat]
```

X.get_niagara_array_quat(niagara_system, override_name) -> Array[Quat]
Gets a copy of Niagara FQuat Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[Quat]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_position_value"></a>

#### get_niagara_array_position_value

```python
@classmethod
def get_niagara_array_position_value(cls, niagara_system: NiagaraComponent,
                                     override_name: Name,
                                     index: int) -> Vector
```

X.get_niagara_array_position_value(niagara_system, override_name, index) -> Vector
Gets a single value within a Niagara Array Position.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    Vector:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_position"></a>

#### get_niagara_array_position

```python
@classmethod
def get_niagara_array_position(cls, niagara_system: NiagaraComponent,
                               override_name: Name) -> Array[Vector]
```

X.get_niagara_array_position(niagara_system, override_name) -> Array[Vector]
Gets a copy of Niagara Position Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[Vector]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_matrix_value"></a>

#### get_niagara_array_matrix_value

```python
@classmethod
def get_niagara_array_matrix_value(cls,
                                   niagara_system: NiagaraComponent,
                                   override_name: Name,
                                   index: int,
                                   apply_lwc_rebase: bool = True) -> Matrix
```

X.get_niagara_array_matrix_value(niagara_system, override_name, index, apply_lwc_rebase=True) -> Matrix
Gets a single value within a Niagara Array FMatrix.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 
    apply_lwc_rebase (bool): When enabled the matrix translation will have the simulation tile offset added to it

Returns:
    Matrix:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_matrix"></a>

#### get_niagara_array_matrix

```python
@classmethod
def get_niagara_array_matrix(cls,
                             niagara_system: NiagaraComponent,
                             override_name: Name,
                             apply_lwc_rebase: bool = True) -> Array[Matrix]
```

X.get_niagara_array_matrix(niagara_system, override_name, apply_lwc_rebase=True) -> Array[Matrix]
Gets a copy of Niagara FMatrix Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    apply_lwc_rebase (bool): When enabled the matrix translation will have the simulation tile offset added to it

Returns:
    Array[Matrix]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_int32_value"></a>

#### get_niagara_array_int32_value

```python
@classmethod
def get_niagara_array_int32_value(cls, niagara_system: NiagaraComponent,
                                  override_name: Name, index: int) -> int
```

X.get_niagara_array_int32_value(niagara_system, override_name, index) -> int32
Gets a single value within a Niagara Array Int32.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    int32:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_int32"></a>

#### get_niagara_array_int32

```python
@classmethod
def get_niagara_array_int32(cls, niagara_system: NiagaraComponent,
                            override_name: Name) -> Array[int]
```

X.get_niagara_array_int32(niagara_system, override_name) -> Array[int32]
Gets a copy of Niagara Int32 Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[int32]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_float_value"></a>

#### get_niagara_array_float_value

```python
@classmethod
def get_niagara_array_float_value(cls, niagara_system: NiagaraComponent,
                                  override_name: Name, index: int) -> float
```

X.get_niagara_array_float_value(niagara_system, override_name, index) -> float
Gets a single value within a Niagara Array Float.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    float:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_float"></a>

#### get_niagara_array_float

```python
@classmethod
def get_niagara_array_float(cls, niagara_system: NiagaraComponent,
                            override_name: Name) -> Array[float]
```

X.get_niagara_array_float(niagara_system, override_name) -> Array[float]
Gets a copy of Niagara Float Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[float]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_color_value"></a>

#### get_niagara_array_color_value

```python
@classmethod
def get_niagara_array_color_value(cls, niagara_system: NiagaraComponent,
                                  override_name: Name,
                                  index: int) -> LinearColor
```

X.get_niagara_array_color_value(niagara_system, override_name, index) -> LinearColor
Gets a single value within a Niagara Array FLinearColor.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    LinearColor:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_color"></a>

#### get_niagara_array_color

```python
@classmethod
def get_niagara_array_color(cls, niagara_system: NiagaraComponent,
                            override_name: Name) -> Array[LinearColor]
```

X.get_niagara_array_color(niagara_system, override_name) -> Array[LinearColor]
Gets a copy of Niagara FLinearColor Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[LinearColor]:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_bool_value"></a>

#### get_niagara_array_bool_value

```python
@classmethod
def get_niagara_array_bool_value(cls, niagara_system: NiagaraComponent,
                                 override_name: Name, index: int) -> bool
```

X.get_niagara_array_bool_value(niagara_system, override_name, index) -> bool
Gets a single value within a Niagara Array Bool.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 
    index (int32): 

Returns:
    bool:

<a id="unreal.NiagaraDataInterfaceArrayFunctionLibrary.get_niagara_array_bool"></a>

#### get_niagara_array_bool

```python
@classmethod
def get_niagara_array_bool(cls, niagara_system: NiagaraComponent,
                           override_name: Name) -> Array[bool]
```

X.get_niagara_array_bool(niagara_system, override_name) -> Array[bool]
Gets a copy of Niagara Bool Data.

Args:
    niagara_system (NiagaraComponent): 
    override_name (Name): 

Returns:
    Array[bool]:

<a id="unreal.NiagaraDataInterfaceArrayInt32"></a>