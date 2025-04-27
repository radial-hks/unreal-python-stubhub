## DistanceFieldToTextureSettings Objects

```python
class DistanceFieldToTextureSettings(StructBase)
```

Distance Field to Texture Settings

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: VolumeTextureBakeFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``offset`` (float):  [Read-Write] Offset values by this amount before writing them to the texture (after applying Scale)
- ``scale`` (float):  [Read-Write] Scale values by this amount before writing them to the texture

<a id="unreal.DistanceFieldToTextureSettings.__init__"></a>

#### __init__

```python
def __init__(scale: float = 0.000000, offset: float = 0.000000) -> None
```

<a id="unreal.DistanceFieldToTextureSettings.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write] Scale values by this amount before writing them to the texture

<a id="unreal.DistanceFieldToTextureSettings.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.DistanceFieldToTextureSettings.offset"></a>

#### offset

```python
@property
def offset() -> float
```

(float):  [Read-Write] Offset values by this amount before writing them to the texture (after applying Scale)

<a id="unreal.DistanceFieldToTextureSettings.offset"></a>

#### offset

```python
@offset.setter
def offset(value: float) -> None
```

<a id="unreal.LocationServicesData"></a>