## NiagaraSimCache Objects

```python
class NiagaraSimCache(Object)
```

Recording of multiple frames of simulation data from a running Niagara system.
Can be used to play back the captured recording or to inspect the captured data for debug purposes.
Depending on the capture settings, not all attributes from the simulation are present in the cache.

To capture a cache, either
(1) use the baker tool in the system editor,
(2) use the Niagara component cache track in sequencer or
(3) manually capture a running system with the "CaptureNiagaraSimCache" Blueprint functions

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSimCache.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_guid`` (Guid):  [Read-Only]
- ``duration_seconds`` (float):  [Read-Only]
- ``soft_niagara_system`` (NiagaraSystem):  [Read-Only]
- ``start_seconds`` (float):  [Read-Only]

<a id="unreal.NiagaraSimCache.read_vector_attribute"></a>

#### read_vector_attribute

```python
def read_vector_attribute(attribute_name: Name,
                          emitter_name: Name,
                          frame_index: int = 0) -> Array[Vector]
```

x.read_vector_attribute(attribute_name, emitter_name, frame_index=0) -> Array[Vector]
Reads Niagara Vec3 attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[Vector]: 

    out_values (Array[Vector]):

<a id="unreal.NiagaraSimCache.read_vector4_attribute"></a>

#### read_vector4_attribute

```python
def read_vector4_attribute(attribute_name: Name,
                           emitter_name: Name,
                           frame_index: int = 0) -> Array[Vector4]
```

x.read_vector4_attribute(attribute_name, emitter_name, frame_index=0) -> Array[Vector4]
Reads Niagara Vec4 attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[Vector4]: 

    out_values (Array[Vector4]):

<a id="unreal.NiagaraSimCache.read_vector2_attribute"></a>

#### read_vector2_attribute

```python
def read_vector2_attribute(attribute_name: Name,
                           emitter_name: Name,
                           frame_index: int = 0) -> Array[Vector2D]
```

x.read_vector2_attribute(attribute_name, emitter_name, frame_index=0) -> Array[Vector2D]
Reads Niagara Vec2 attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[Vector2D]: 

    out_values (Array[Vector2D]):

<a id="unreal.NiagaraSimCache.read_quat_attribute_with_rebase"></a>

#### read_quat_attribute_with_rebase

```python
def read_quat_attribute_with_rebase(quat: Quat,
                                    attribute_name: Name = "MeshOrientation",
                                    emitter_name: Name = "None",
                                    frame_index: int = 0) -> Array[Quat]
```

x.read_quat_attribute_with_rebase(quat, attribute_name="MeshOrientation", emitter_name="None", frame_index=0) -> Array[Quat]
Reads Niagara Quaternion attributes by name from the cache frame and appends them into the OutValues array.
Only attributes that in the rebase list will be transform into the provided Quat space.  Therefore the cache
must be captured with rebasing enabled to have any impact.
EmitterName - If left blank will return the system simulation attributes.

Args:
    quat (Quat): 
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[Quat]: 

    out_values (Array[Quat]):

<a id="unreal.NiagaraSimCache.read_quat_attribute"></a>

#### read_quat_attribute

```python
def read_quat_attribute(attribute_name: Name = "MeshOrientation",
                        emitter_name: Name = "None",
                        local_space_to_world: bool = True,
                        frame_index: int = 0) -> Array[Quat]
```

x.read_quat_attribute(attribute_name="MeshOrientation", emitter_name="None", local_space_to_world=True, frame_index=0) -> Array[Quat]
Reads Niagara Quaternion attributes by name from the cache frame and appends them into the OutValues array.
Local space emitters provide data at local rotation unless bLocalSpaceToWorld is true.
EmitterName - If left blank will return the system simulation attributes.
LocalSpaceToWorld - Caches are always stored in the emitters space, i.e. local or world space.  You can set this to false if you want the local Quat rather than the world Quat.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    local_space_to_world (bool): 
    frame_index (int32): 

Returns:
    Array[Quat]: 

    out_values (Array[Quat]):

<a id="unreal.NiagaraSimCache.read_position_attribute_with_rebase"></a>

#### read_position_attribute_with_rebase

```python
def read_position_attribute_with_rebase(transform: Transform,
                                        attribute_name: Name = "Position",
                                        emitter_name: Name = "None",
                                        frame_index: int = 0) -> Array[Vector]
```

x.read_position_attribute_with_rebase(transform, attribute_name="Position", emitter_name="None", frame_index=0) -> Array[Vector]
Reads Niagara Position attributes by name from the cache frame and appends them into the OutValues array.
All attributes read with this method will be re-based from the captured space into the provided transform space,
this will occur even if the cache was not captured with re-basing enabled.
EmitterName - If left blank will return the system simulation attributes.

Args:
    transform (Transform): 
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[Vector]: 

    out_values (Array[Vector]):

<a id="unreal.NiagaraSimCache.read_position_attribute"></a>

#### read_position_attribute

```python
def read_position_attribute(attribute_name: Name = "Position",
                            emitter_name: Name = "None",
                            local_space_to_world: bool = True,
                            frame_index: int = 0) -> Array[Vector]
```

x.read_position_attribute(attribute_name="Position", emitter_name="None", local_space_to_world=True, frame_index=0) -> Array[Vector]
Reads Niagara Position attributes by name from the cache frame and appends them into the OutValues array.
Local space emitters provide data at local locations unless bLocalSpaceToWorld is true.
EmitterName - If left blank will return the system simulation attributes.
LocalSpaceToWorld - Caches are always stored in the emitters space, i.e. local or world space.  You can set this to false if you want the local position rather than the world position.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    local_space_to_world (bool): 
    frame_index (int32): 

Returns:
    Array[Vector]: 

    out_values (Array[Vector]):

<a id="unreal.NiagaraSimCache.read_int_attribute"></a>

#### read_int_attribute

```python
def read_int_attribute(attribute_name: Name,
                       emitter_name: Name,
                       frame_index: int = 0) -> Array[int]
```

x.read_int_attribute(attribute_name, emitter_name, frame_index=0) -> Array[int32]
Reads Niagara int attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[int32]: 

    out_values (Array[int32]):

<a id="unreal.NiagaraSimCache.read_id_attribute"></a>

#### read_id_attribute

```python
def read_id_attribute(attribute_name: Name,
                      emitter_name: Name,
                      frame_index: int = 0) -> Array[NiagaraID]
```

x.read_id_attribute(attribute_name, emitter_name, frame_index=0) -> Array[NiagaraID]
Reads Niagara ID attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[NiagaraID]: 

    out_values (Array[NiagaraID]):

<a id="unreal.NiagaraSimCache.read_float_attribute"></a>

#### read_float_attribute

```python
def read_float_attribute(attribute_name: Name,
                         emitter_name: Name,
                         frame_index: int = 0) -> Array[float]
```

x.read_float_attribute(attribute_name, emitter_name, frame_index=0) -> Array[float]
Reads Niagara float attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[float]: 

    out_values (Array[float]):

<a id="unreal.NiagaraSimCache.read_data_interface_as"></a>

#### read_data_interface_as

```python
def read_data_interface_as(requested_type: Class,
                           attribute_name: Name,
                           frame_index: int = 0) -> Object
```

x.read_data_interface_as(requested_type, attribute_name, frame_index=0) -> Object
Reads data interface data from the cache as the requested type.
This method will return nullptr if the attribute does not exists or the requests type is not supported by the storage type.

Args:
    requested_type (type(Class)): 
    attribute_name (Name): 
    frame_index (int32): 

Returns:
    Object:

<a id="unreal.NiagaraSimCache.read_color_attribute"></a>

#### read_color_attribute

```python
def read_color_attribute(attribute_name: Name = "Color",
                         emitter_name: Name = "None",
                         frame_index: int = 0) -> Array[LinearColor]
```

x.read_color_attribute(attribute_name="Color", emitter_name="None", frame_index=0) -> Array[LinearColor]
Reads Niagara Color attributes by name from the cache frame and appends them into the OutValues array.
EmitterName - If left blank will return the system simulation attributes.

Args:
    attribute_name (Name): 
    emitter_name (Name): 
    frame_index (int32): 

Returns:
    Array[LinearColor]: 

    out_values (Array[LinearColor]):

<a id="unreal.NiagaraSimCache.is_empty"></a>

#### is_empty

```python
def is_empty() -> bool
```

x.is_empty() -> bool
An empty cache contains no frame data and can not be used

Returns:
    bool:

<a id="unreal.NiagaraSimCache.is_cache_valid"></a>

#### is_cache_valid

```python
def is_cache_valid() -> bool
```

x.is_cache_valid() -> bool
A valid cache is one that contains at least 1 frames worth of data.

Returns:
    bool:

<a id="unreal.NiagaraSimCache.get_start_seconds"></a>

#### get_start_seconds

```python
def get_start_seconds() -> float
```

x.get_start_seconds() -> float
Get the time the simulation was at when recorded.

Returns:
    float:

<a id="unreal.NiagaraSimCache.get_num_frames"></a>

#### get_num_frames

```python
def get_num_frames() -> int
```

x.get_num_frames() -> int32
Get number of frames stored in the cache.

Returns:
    int32:

<a id="unreal.NiagaraSimCache.get_num_emitters"></a>

#### get_num_emitters

```python
def get_num_emitters() -> int
```

x.get_num_emitters() -> int32
Get number of emitters stored inside the cache.

Returns:
    int32:

<a id="unreal.NiagaraSimCache.get_emitter_names"></a>

#### get_emitter_names

```python
def get_emitter_names() -> Array[Name]
```

x.get_emitter_names() -> Array[Name]
Returns a list of emitters we have captured in the SimCache.

Returns:
    Array[Name]:

<a id="unreal.NiagaraSimCache.get_emitter_name"></a>

#### get_emitter_name

```python
def get_emitter_name(emitter_index: int) -> Name
```

x.get_emitter_name(emitter_index) -> Name
Get the emitter name at the provided index.

Args:
    emitter_index (int32): 

Returns:
    Name:

<a id="unreal.NiagaraSimCache.get_attribute_capture_mode"></a>

#### get_attribute_capture_mode

```python
def get_attribute_capture_mode() -> NiagaraSimCacheAttributeCaptureMode
```

x.get_attribute_capture_mode() -> NiagaraSimCacheAttributeCaptureMode
How were the attributes captured for this sim cache.

Returns:
    NiagaraSimCacheAttributeCaptureMode:

<a id="unreal.AsyncNiagaraCaptureSimCache"></a>