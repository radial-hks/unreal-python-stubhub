## MigrationLine Objects

```python
class MigrationLine(StructBase)
```

Migration Line

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: ChinaMapTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``particle`` (ParticleSystemComponent):  [Read-Write]
- ``spline`` (SplineMeshComponent):  [Read-Write]

<a id="unreal.MigrationLine.__init__"></a>

#### \_\_init\_\_

```python
def __init__(spline: SplineMeshComponent = None,
             particle: ParticleSystemComponent = None) -> None
```

<a id="unreal.MigrationLine.spline"></a>

#### spline

```python
@property
def spline() -> SplineMeshComponent
```

(SplineMeshComponent):  [Read-Write]

<a id="unreal.MigrationLine.spline"></a>

#### spline

```python
@spline.setter
def spline(value: SplineMeshComponent) -> None
```

<a id="unreal.MigrationLine.particle"></a>

#### particle

```python
@property
def particle() -> ParticleSystemComponent
```

(ParticleSystemComponent):  [Read-Write]

<a id="unreal.MigrationLine.particle"></a>

#### particle

```python
@particle.setter
def particle(value: ParticleSystemComponent) -> None
```

<a id="unreal.Migration"></a>