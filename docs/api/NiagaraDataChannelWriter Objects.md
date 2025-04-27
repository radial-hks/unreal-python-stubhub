## NiagaraDataChannelWriter Objects

```python
class NiagaraDataChannelWriter(Object)
```

Niagara Data Channel Writer

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataChannelAccessor.h

<a id="unreal.NiagaraDataChannelWriter.write_vector4"></a>

#### write_vector4

```python
def write_vector4(var_name: Name, index: int, data: Vector4) -> None
```

x.write_vector4(var_name, index, data) -> None
Write Vector 4

Args:
    var_name (Name): 
    index (int32): 
    data (Vector4):

<a id="unreal.NiagaraDataChannelWriter.write_vector2d"></a>

#### write_vector2d

```python
def write_vector2d(var_name: Name, index: int, data: Vector2D) -> None
```

x.write_vector2d(var_name, index, data) -> None
Write Vector 2D

Args:
    var_name (Name): 
    index (int32): 
    data (Vector2D):

<a id="unreal.NiagaraDataChannelWriter.write_vector"></a>

#### write_vector

```python
def write_vector(var_name: Name, index: int, data: Vector) -> None
```

x.write_vector(var_name, index, data) -> None
Write Vector

Args:
    var_name (Name): 
    index (int32): 
    data (Vector):

<a id="unreal.NiagaraDataChannelWriter.write_spawn_info"></a>

#### write_spawn_info

```python
def write_spawn_info(var_name: Name, index: int,
                     data: NiagaraSpawnInfo) -> None
```

x.write_spawn_info(var_name, index, data) -> None
Write Spawn Info

Args:
    var_name (Name): 
    index (int32): 
    data (NiagaraSpawnInfo):

<a id="unreal.NiagaraDataChannelWriter.write_quat"></a>

#### write_quat

```python
def write_quat(var_name: Name, index: int, data: Quat) -> None
```

x.write_quat(var_name, index, data) -> None
Write Quat

Args:
    var_name (Name): 
    index (int32): 
    data (Quat):

<a id="unreal.NiagaraDataChannelWriter.write_position"></a>

#### write_position

```python
def write_position(var_name: Name, index: int, data: Vector) -> None
```

x.write_position(var_name, index, data) -> None
Write Position

Args:
    var_name (Name): 
    index (int32): 
    data (Vector):

<a id="unreal.NiagaraDataChannelWriter.write_linear_color"></a>

#### write_linear_color

```python
def write_linear_color(var_name: Name, index: int, data: LinearColor) -> None
```

x.write_linear_color(var_name, index, data) -> None
Write Linear Color

Args:
    var_name (Name): 
    index (int32): 
    data (LinearColor):

<a id="unreal.NiagaraDataChannelWriter.write_int"></a>

#### write_int

```python
def write_int(var_name: Name, index: int, data: int) -> None
```

x.write_int(var_name, index, data) -> None
Write Int

Args:
    var_name (Name): 
    index (int32): 
    data (int32):

<a id="unreal.NiagaraDataChannelWriter.write_id"></a>

#### write_id

```python
def write_id(var_name: Name, index: int, data: NiagaraID) -> None
```

x.write_id(var_name, index, data) -> None
Write ID

Args:
    var_name (Name): 
    index (int32): 
    data (NiagaraID):

<a id="unreal.NiagaraDataChannelWriter.write_float"></a>

#### write_float

```python
def write_float(var_name: Name, index: int, data: float) -> None
```

x.write_float(var_name, index, data) -> None
Write Float

Args:
    var_name (Name): 
    index (int32): 
    data (double):

<a id="unreal.NiagaraDataChannelWriter.write_enum"></a>

#### write_enum

```python
def write_enum(var_name: Name, index: int, data: int) -> None
```

x.write_enum(var_name, index, data) -> None
Write Enum

Args:
    var_name (Name): 
    index (int32): 
    data (uint8):

<a id="unreal.NiagaraDataChannelWriter.write_bool"></a>

#### write_bool

```python
def write_bool(var_name: Name, index: int, data: bool) -> None
```

x.write_bool(var_name, index, data) -> None
Write Bool

Args:
    var_name (Name): 
    index (int32): 
    data (bool):

<a id="unreal.NiagaraDataChannelWriter.num"></a>

#### num

```python
def num() -> int
```

x.num() -> int32
Num

Returns:
    int32:

<a id="unreal.NiagaraDataChannelWriter.init_write"></a>

#### init_write

```python
def init_write(search_params: NiagaraDataChannelSearchParameters,
               count: int,
               visible_to_game: bool = True,
               visible_to_cpu: bool = True,
               visible_to_gpu: bool = True,
               debug_source: str = ...) -> bool
```

x.init_write(search_params, count, visible_to_game=True, visible_to_cpu=True, visible_to_gpu=True, debug_source) -> bool
Call before each batch of writes to allocate the data we'll be writing to.

Args:
    search_params (NiagaraDataChannelSearchParameters): 
    count (int32): 
    visible_to_game (bool): 
    visible_to_cpu (bool): 
    visible_to_gpu (bool): 
    debug_source (str): 

Returns:
    bool:

<a id="unreal.NiagaraDataChannelHandler"></a>