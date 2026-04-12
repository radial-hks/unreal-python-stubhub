## glTFRuntimeAnimationCurve Objects

```python
class glTFRuntimeAnimationCurve(CurveBase)
```

Gl TFRuntime Animation Curve

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeAnimationCurve.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only]
- ``gl_tf_curve_animation_duration`` (float):  [Read-Only]
- ``gl_tf_curve_animation_index`` (int32):  [Read-Only]
- ``gl_tf_curve_animation_name`` (str):  [Read-Only]

<a id="unreal.glTFRuntimeAnimationCurve.gl_tf_curve_animation_name"></a>

#### gl\_tf\_curve\_animation\_name

```python
@property
def gl_tf_curve_animation_name() -> str
```

(str):  [Read-Only]

<a id="unreal.glTFRuntimeAnimationCurve.gl_tf_curve_animation_index"></a>

#### gl\_tf\_curve\_animation\_index

```python
@property
def gl_tf_curve_animation_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.glTFRuntimeAnimationCurve.gl_tf_curve_animation_duration"></a>

#### gl\_tf\_curve\_animation\_duration

```python
@property
def gl_tf_curve_animation_duration() -> float
```

(float):  [Read-Only]

<a id="unreal.glTFRuntimeAnimationCurve.get_transform_value"></a>

#### get\_transform\_value

```python
def get_transform_value(time: float) -> Transform
```

x.get_transform_value(time) -> Transform
Evaluate this float curve at the specified time

Args:
    time (float): 

Returns:
    Transform:

<a id="unreal.glTFRuntimeAsset"></a>