## HairGeometrySettings Objects

```python
class HairGeometrySettings(StructBase)
```

Hair Geometry Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetRendering.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hair_root_scale`` (float):  [Read-Write] Scale the hair width at the root
- ``hair_tip_scale`` (float):  [Read-Write] Scale the hair width at the tip
- ``hair_width`` (float):  [Read-Write] Hair width (in centimeters)
- ``hair_width_override`` (bool):  [Read-Write]

<a id="unreal.HairGeometrySettings.__init__"></a>

#### __init__

```python
def __init__(hair_width: float = 0.000000,
             hair_width_override: bool = False,
             hair_root_scale: float = 0.000000,
             hair_tip_scale: float = 0.000000) -> None
```

<a id="unreal.HairGeometrySettings.hair_width"></a>

#### hair_width

```python
@property
def hair_width() -> float
```

(float):  [Read-Write] Hair width (in centimeters)

<a id="unreal.HairGeometrySettings.hair_width"></a>

#### hair_width

```python
@hair_width.setter
def hair_width(value: float) -> None
```

<a id="unreal.HairGeometrySettings.hair_width_override"></a>

#### hair_width_override

```python
@property
def hair_width_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.HairGeometrySettings.hair_width_override"></a>

#### hair_width_override

```python
@hair_width_override.setter
def hair_width_override(value: bool) -> None
```

<a id="unreal.HairGeometrySettings.hair_root_scale"></a>

#### hair_root_scale

```python
@property
def hair_root_scale() -> float
```

(float):  [Read-Write] Scale the hair width at the root

<a id="unreal.HairGeometrySettings.hair_root_scale"></a>

#### hair_root_scale

```python
@hair_root_scale.setter
def hair_root_scale(value: float) -> None
```

<a id="unreal.HairGeometrySettings.hair_tip_scale"></a>

#### hair_tip_scale

```python
@property
def hair_tip_scale() -> float
```

(float):  [Read-Write] Scale the hair width at the tip

<a id="unreal.HairGeometrySettings.hair_tip_scale"></a>

#### hair_tip_scale

```python
@hair_tip_scale.setter
def hair_tip_scale(value: float) -> None
```

<a id="unreal.HairShadowSettings"></a>