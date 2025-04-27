## NiagaraDataChannelReader Objects

```python
class NiagaraDataChannelReader(Object)
```

Initial simple API for reading and writing data in a data channel from game code / BP.
Likely to be replaced in the near future with a custom BP node and a helper struct.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataChannelAccessor.h

<a id="unreal.NiagaraDataChannelReader.read_vector4"></a>

#### read_vector4

```python
def read_vector4(var_name: Name, index: int) -> Tuple[Vector4, bool]
```

x.read_vector4(var_name, index) -> (Vector4, is_valid=bool)
Read Vector 4

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_vector2d"></a>

#### read_vector2d

```python
def read_vector2d(var_name: Name, index: int) -> Tuple[Vector2D, bool]
```

x.read_vector2d(var_name, index) -> (Vector2D, is_valid=bool)
Read Vector 2D

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_vector"></a>

#### read_vector

```python
def read_vector(var_name: Name, index: int) -> Tuple[Vector, bool]
```

x.read_vector(var_name, index) -> (Vector, is_valid=bool)
Read Vector

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_spawn_info"></a>

#### read_spawn_info

```python
def read_spawn_info(var_name: Name,
                    index: int) -> Tuple[NiagaraSpawnInfo, bool]
```

x.read_spawn_info(var_name, index) -> (NiagaraSpawnInfo, is_valid=bool)
Read Spawn Info

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_quat"></a>

#### read_quat

```python
def read_quat(var_name: Name, index: int) -> Tuple[Quat, bool]
```

x.read_quat(var_name, index) -> (Quat, is_valid=bool)
Read Quat

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_position"></a>

#### read_position

```python
def read_position(var_name: Name, index: int) -> Tuple[Vector, bool]
```

x.read_position(var_name, index) -> (Vector, is_valid=bool)
Read Position

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_linear_color"></a>

#### read_linear_color

```python
def read_linear_color(var_name: Name, index: int) -> Tuple[LinearColor, bool]
```

x.read_linear_color(var_name, index) -> (LinearColor, is_valid=bool)
Read Linear Color

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_int"></a>

#### read_int

```python
def read_int(var_name: Name, index: int) -> Tuple[int, bool]
```

x.read_int(var_name, index) -> (int32, is_valid=bool)
Read Int

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_id"></a>

#### read_id

```python
def read_id(var_name: Name, index: int) -> Tuple[NiagaraID, bool]
```

x.read_id(var_name, index) -> (NiagaraID, is_valid=bool)
Read ID

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_float"></a>

#### read_float

```python
def read_float(var_name: Name, index: int) -> Tuple[float, bool]
```

x.read_float(var_name, index) -> (double, is_valid=bool)
Read Float

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_enum"></a>

#### read_enum

```python
def read_enum(var_name: Name, index: int) -> Tuple[int, bool]
```

x.read_enum(var_name, index) -> (uint8, is_valid=bool)
Read Enum

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.read_bool"></a>

#### read_bool

```python
def read_bool(var_name: Name, index: int) -> Optional[bool]
```

x.read_bool(var_name, index) -> bool or None
Read Bool

Args:
    var_name (Name): 
    index (int32): 

Returns:
    bool or None: 

    is_valid (bool):

<a id="unreal.NiagaraDataChannelReader.num"></a>

#### num

```python
def num() -> int
```

x.num() -> int32
Num

Returns:
    int32:

<a id="unreal.NiagaraDataChannelReader.init_access"></a>

#### init_access

```python
def init_access(search_params: NiagaraDataChannelSearchParameters,
                read_prev_frame_data: bool) -> bool
```

x.init_access(search_params, read_prev_frame_data) -> bool
Call before each access to the data channel to grab the correct data to read.

Args:
    search_params (NiagaraDataChannelSearchParameters): 
    read_prev_frame_data (bool): 

Returns:
    bool:

<a id="unreal.NiagaraDataChannelWriter"></a>