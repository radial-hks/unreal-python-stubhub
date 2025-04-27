## CurveLinearColor Objects

```python
class CurveLinearColor(CurveBase)
```

Curve Linear Color

**C++ Source:**

- **Module**: Engine
- **File**: CurveLinearColor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``adjust_brightness`` (float):  [Read-Write]
- ``adjust_brightness_curve`` (float):  [Read-Write]
- ``adjust_hue`` (float):  [Read-Write] Properties for adjusting the color of the gradient
- ``adjust_max_alpha`` (float):  [Read-Write]
- ``adjust_min_alpha`` (float):  [Read-Write]
- ``adjust_saturation`` (float):  [Read-Write]
- ``adjust_vibrance`` (float):  [Read-Write]
- ``asset_import_data`` (AssetImportData):  [Read-Only]

<a id="unreal.CurveLinearColor.get_unadjusted_linear_color_value"></a>

#### get_unadjusted_linear_color_value

```python
def get_unadjusted_linear_color_value(time: float) -> LinearColor
```

x.get_unadjusted_linear_color_value(time) -> LinearColor
Get Unadjusted Linear Color Value

Args:
    time (float): 

Returns:
    LinearColor:

<a id="unreal.CurveLinearColor.get_linear_color_value"></a>

#### get_linear_color_value

```python
def get_linear_color_value(time: float) -> LinearColor
```

x.get_linear_color_value(time) -> LinearColor
Get Linear Color Value

Args:
    time (float): 

Returns:
    LinearColor:

<a id="unreal.CurveLinearColor.get_clamped_linear_color_value"></a>

#### get_clamped_linear_color_value

```python
def get_clamped_linear_color_value(time: float) -> LinearColor
```

x.get_clamped_linear_color_value(time) -> LinearColor
Get Clamped Linear Color Value

Args:
    time (float): 

Returns:
    LinearColor:

<a id="unreal.CurveLinearColorAtlas"></a>