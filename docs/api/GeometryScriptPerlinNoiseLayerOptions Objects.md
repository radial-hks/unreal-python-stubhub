## GeometryScriptPerlinNoiseLayerOptions Objects

```python
class GeometryScriptPerlinNoiseLayerOptions(StructBase)
```

Geometry Script Perlin Noise Layer Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDeformFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frequency`` (float):  [Read-Write]
- ``frequency_shift`` (Vector):  [Read-Write]
- ``magnitude`` (float):  [Read-Write]
- ``random_seed`` (int32):  [Read-Write]

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.__init__"></a>

#### __init__

```python
def __init__(magnitude: float = 0.000000,
             frequency: float = 0.000000,
             frequency_shift: Vector = [0.000000, 0.000000, 0.000000],
             random_seed: int = 0) -> None
```

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.magnitude"></a>

#### magnitude

```python
@property
def magnitude() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.magnitude"></a>

#### magnitude

```python
@magnitude.setter
def magnitude(value: float) -> None
```

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.frequency_shift"></a>

#### frequency_shift

```python
@property
def frequency_shift() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.frequency_shift"></a>

#### frequency_shift

```python
@frequency_shift.setter
def frequency_shift(value: Vector) -> None
```

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.random_seed"></a>

#### random_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Write]

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions.random_seed"></a>

#### random_seed

```python
@random_seed.setter
def random_seed(value: int) -> None
```

<a id="unreal.GeometryScriptMathWarpOptions"></a>