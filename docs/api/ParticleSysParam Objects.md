## ParticleSysParam Objects

```python
class ParticleSysParam(StructBase)
```

Struct used for a particular named instance parameter for this ParticleSystemComponent.

**C++ Source:**

- **Module**: Engine
- **File**: ParticleSystemComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor`` (Actor):  [Read-Write]
- ``color`` (Color):  [Read-Write]
- ``material`` (MaterialInterface):  [Read-Write]
- ``name`` (Name):  [Read-Write] The name of the parameter
- ``param_type`` (ParticleSysParamType):  [Read-Write] The type of parameters
  PSPT_None       - There is no data type
  PSPT_Scalar     - Use the scalar value
  PSPT_ScalarRand - Select a scalar value in the range [Scalar_Low..Scalar)
  PSPT_Vector     - Use the vector value
  PSPT_VectorRand - Select a vector value in the range [Vector_Low..Vector)
  PSPT_Color      - Use the color value
  PSPT_Actor      - Use the actor value
  PSPT_Material   - Use the material value
  PSPT_VectorUnitRand - Select a random unit vector and scale along the range [Vector_Low..Vector)
- ``scalar`` (float):  [Read-Write]
- ``scalar_low`` (float):  [Read-Write]
- ``vector`` (Vector):  [Read-Write]
- ``vector_low`` (Vector):  [Read-Write]

<a id="unreal.ParticleSysParam.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             param_type: ParticleSysParamType = ParticleSysParamType.PSPT_NONE,
             scalar: float = 0.000000,
             scalar_low: float = 0.000000,
             vector: Vector = [0.000000, 0.000000, 0.000000],
             vector_low: Vector = [0.000000, 0.000000, 0.000000],
             color: Color = [0, 0, 0, 0],
             actor: Actor = None,
             material: MaterialInterface = None) -> None
```

<a id="unreal.ParticleSysParam.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] The name of the parameter

<a id="unreal.ParticleSysParam.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.ParticleSysParam.param_type"></a>

#### param_type

```python
@property
def param_type() -> ParticleSysParamType
```

(ParticleSysParamType):  [Read-Write] The type of parameters
PSPT_None       - There is no data type
PSPT_Scalar     - Use the scalar value
PSPT_ScalarRand - Select a scalar value in the range [Scalar_Low..Scalar)
PSPT_Vector     - Use the vector value
PSPT_VectorRand - Select a vector value in the range [Vector_Low..Vector)
PSPT_Color      - Use the color value
PSPT_Actor      - Use the actor value
PSPT_Material   - Use the material value
PSPT_VectorUnitRand - Select a random unit vector and scale along the range [Vector_Low..Vector)

<a id="unreal.ParticleSysParam.param_type"></a>

#### param_type

```python
@param_type.setter
def param_type(value: ParticleSysParamType) -> None
```

<a id="unreal.ParticleSysParam.scalar"></a>

#### scalar

```python
@property
def scalar() -> float
```

(float):  [Read-Write]

<a id="unreal.ParticleSysParam.scalar"></a>

#### scalar

```python
@scalar.setter
def scalar(value: float) -> None
```

<a id="unreal.ParticleSysParam.scalar_low"></a>

#### scalar_low

```python
@property
def scalar_low() -> float
```

(float):  [Read-Write]

<a id="unreal.ParticleSysParam.scalar_low"></a>

#### scalar_low

```python
@scalar_low.setter
def scalar_low(value: float) -> None
```

<a id="unreal.ParticleSysParam.vector"></a>

#### vector

```python
@property
def vector() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.ParticleSysParam.vector"></a>

#### vector

```python
@vector.setter
def vector(value: Vector) -> None
```

<a id="unreal.ParticleSysParam.vector_low"></a>

#### vector_low

```python
@property
def vector_low() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.ParticleSysParam.vector_low"></a>

#### vector_low

```python
@vector_low.setter
def vector_low(value: Vector) -> None
```

<a id="unreal.ParticleSysParam.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write]

<a id="unreal.ParticleSysParam.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.ParticleSysParam.actor"></a>

#### actor

```python
@property
def actor() -> Actor
```

(Actor):  [Read-Write]

<a id="unreal.ParticleSysParam.actor"></a>

#### actor

```python
@actor.setter
def actor(value: Actor) -> None
```

<a id="unreal.ParticleSysParam.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.ParticleSysParam.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.FXSystemSpawnParameters"></a>