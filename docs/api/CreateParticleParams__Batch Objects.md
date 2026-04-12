## CreateParticleParams\_Batch Objects

```python
class CreateParticleParams_Batch(ParamsBase)
```

Create Particle Params Batch

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ParticlesAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``batch_params`` (Array[CreateParticlesParams]):  [Read-Write]
- ``default_param`` (CreateParticlesParams):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.CreateParticleParams_Batch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(default_param: CreateParticlesParams = ["alarm", "", 0],
             batch_params: Array[CreateParticlesParams] = []) -> None
```

<a id="unreal.CreateParticleParams_Batch.default_param"></a>

#### default\_param

```python
@property
def default_param() -> CreateParticlesParams
```

(CreateParticlesParams):  [Read-Write]

<a id="unreal.CreateParticleParams_Batch.default_param"></a>

#### default\_param

```python
@default_param.setter
def default_param(value: CreateParticlesParams) -> None
```

<a id="unreal.CreateParticleParams_Batch.batch_params"></a>

#### batch\_params

```python
@property
def batch_params() -> Array[CreateParticlesParams]
```

(Array[CreateParticlesParams]):  [Read-Write]

<a id="unreal.CreateParticleParams_Batch.batch_params"></a>

#### batch\_params

```python
@batch_params.setter
def batch_params(value: Array[CreateParticlesParams]) -> None
```

<a id="unreal.ParticleUpdateParams"></a>