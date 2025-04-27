## SpecularProfileStruct Objects

```python
class SpecularProfileStruct(StructBase)
```

struct with all the settings we want in USpecularProfile, separate to make it easer to pass this data around in the engine.

**C++ Source:**

- **Module**: Engine
- **File**: SpecularProfile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``format`` (SpecularProfileFormat):  [Read-Write] Define the texture used as a specular profile
- ``light_color`` (RuntimeCurveLinearColor):  [Read-Write] Define the light facing color
- ``texture`` (Texture2D):  [Read-Write] Define the texture used as a specular profile
- ``view_color`` (RuntimeCurveLinearColor):  [Read-Write] Define the view facing color

<a id="unreal.SpecularProfileStruct.__init__"></a>

#### __init__

```python
def __init__(format: SpecularProfileFormat = SpecularProfileFormat.
             VIEW_LIGHT_VECTOR,
             texture: Texture2D = None) -> None
```

<a id="unreal.SpecularProfileStruct.format"></a>

#### format

```python
@property
def format() -> SpecularProfileFormat
```

(SpecularProfileFormat):  [Read-Only] Define the texture used as a specular profile

<a id="unreal.SpecularProfileStruct.texture"></a>

#### texture

```python
@property
def texture() -> Texture2D
```

(Texture2D):  [Read-Only] Define the texture used as a specular profile

<a id="unreal.SubsurfaceProfileStruct"></a>