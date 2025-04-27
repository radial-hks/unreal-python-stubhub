## BasicParticleData Objects

```python
class BasicParticleData(StructBase)
```

Basic Particle Data

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraDataInterfaceExport.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``position`` (Vector):  [Read-Write]
- ``size`` (float):  [Read-Write]
- ``velocity`` (Vector):  [Read-Write]

<a id="unreal.BasicParticleData.__init__"></a>

#### __init__

```python
def __init__(position: Vector = [0.000000, 0.000000, 0.000000],
             size: float = 0.000000,
             velocity: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.BasicParticleData.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.BasicParticleData.size"></a>

#### size

```python
@property
def size() -> float
```

(float):  [Read-Only]

<a id="unreal.BasicParticleData.velocity"></a>

#### velocity

```python
@property
def velocity() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.VersionedNiagaraEmitterData"></a>