## AvaMaterialParameterMap Objects

```python
class AvaMaterialParameterMap(StructBase)
```

Ava Material Parameter Map

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaMaterialParameterModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``scalar_parameters`` (Map[Name, float]):  [Read-Write]
- ``texture_parameters`` (Map[Name, Texture]):  [Read-Write]
- ``vector_parameters`` (Map[Name, LinearColor]):  [Read-Write]

<a id="unreal.AvaMaterialParameterMap.__init__"></a>

#### __init__

```python
def __init__(scalar_parameters: Map[Name, float] = {},
             vector_parameters: Map[Name, LinearColor] = {},
             texture_parameters: Map[Name, Texture] = {}) -> None
```

<a id="unreal.AvaMaterialParameterMap.scalar_parameters"></a>

#### scalar_parameters

```python
@property
def scalar_parameters() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write]

<a id="unreal.AvaMaterialParameterMap.scalar_parameters"></a>

#### scalar_parameters

```python
@scalar_parameters.setter
def scalar_parameters(value: Map[Name, float]) -> None
```

<a id="unreal.AvaMaterialParameterMap.vector_parameters"></a>

#### vector_parameters

```python
@property
def vector_parameters() -> Map[Name, LinearColor]
```

(Map[Name, LinearColor]):  [Read-Write]

<a id="unreal.AvaMaterialParameterMap.vector_parameters"></a>

#### vector_parameters

```python
@vector_parameters.setter
def vector_parameters(value: Map[Name, LinearColor]) -> None
```

<a id="unreal.AvaMaterialParameterMap.texture_parameters"></a>

#### texture_parameters

```python
@property
def texture_parameters() -> Map[Name, Texture]
```

(Map[Name, Texture]):  [Read-Write]

<a id="unreal.AvaMaterialParameterMap.texture_parameters"></a>

#### texture_parameters

```python
@texture_parameters.setter
def texture_parameters(value: Map[Name, Texture]) -> None
```

<a id="unreal.Vector2b"></a>