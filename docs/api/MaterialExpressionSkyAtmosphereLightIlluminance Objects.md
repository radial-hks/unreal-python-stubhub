## MaterialExpressionSkyAtmosphereLightIlluminance Objects

```python
class MaterialExpressionSkyAtmosphereLightIlluminance(MaterialExpression)
```

Material Expression Sky Atmosphere Light Illuminance

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionSkyAtmosphereLightIlluminance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``light_index`` (int32):  [Read-Write] Index of the atmosphere light to sample.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``world_position_origin_type`` (PositionOrigin):  [Read-Write] Defines the reference space for the WorldPosition input.

<a id="unreal.MaterialExpressionSkyAtmosphereLightIlluminance.light_index"></a>

#### light_index

```python
@property
def light_index() -> int
```

(int32):  [Read-Write] Index of the atmosphere light to sample.

<a id="unreal.MaterialExpressionSkyAtmosphereLightIlluminance.light_index"></a>

#### light_index

```python
@light_index.setter
def light_index(value: int) -> None
```

<a id="unreal.MaterialExpressionSkyAtmosphereLightIlluminanceOnGround"></a>