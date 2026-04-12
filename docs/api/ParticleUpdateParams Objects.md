## ParticleUpdateParams Objects

```python
class ParticleUpdateParams(ParamsBase)
```

Particle Update Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ParticlesAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``particle_type`` (str):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]

<a id="unreal.ParticleUpdateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             particle_type: str = "",
             point_entity_eid: str = "",
             coord_z_ref: int = 0) -> None
```

<a id="unreal.ParticleUpdateParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.ParticleUpdateParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.ParticleUpdateParams.particle_type"></a>

#### particle\_type

```python
@property
def particle_type() -> str
```

(str):  [Read-Write]

<a id="unreal.ParticleUpdateParams.particle_type"></a>

#### particle\_type

```python
@particle_type.setter
def particle_type(value: str) -> None
```

<a id="unreal.ParticleUpdateParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.ParticleUpdateParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.ParticleUpdateParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.ParticleUpdateParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.PathStyle"></a>