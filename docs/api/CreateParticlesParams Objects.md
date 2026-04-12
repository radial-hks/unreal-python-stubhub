## CreateParticlesParams Objects

```python
class CreateParticlesParams(StructBase)
```

Create Particles Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ParticlesAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``particle_type`` (str):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]

<a id="unreal.CreateParticlesParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(particle_type: str = "",
             point_entity_eid: str = "",
             coord_z_ref: int = 0) -> None
```

<a id="unreal.CreateParticlesParams.particle_type"></a>

#### particle\_type

```python
@property
def particle_type() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateParticlesParams.particle_type"></a>

#### particle\_type

```python
@particle_type.setter
def particle_type(value: str) -> None
```

<a id="unreal.CreateParticlesParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateParticlesParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.CreateParticlesParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.CreateParticlesParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreateParticleParams_Batch"></a>