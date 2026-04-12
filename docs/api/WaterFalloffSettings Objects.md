## WaterFalloffSettings Objects

```python
class WaterFalloffSettings(StructBase)
```

Water Falloff Settings

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterFalloffSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``edge_offset`` (float):  [Read-Write]
- ``falloff_angle`` (float):  [Read-Write]
- ``falloff_mode`` (WaterBrushFalloffMode):  [Read-Write]
- ``falloff_width`` (float):  [Read-Write]
- ``z_offset`` (float):  [Read-Write]

<a id="unreal.WaterFalloffSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(falloff_mode: WaterBrushFalloffMode = WaterBrushFalloffMode.ANGLE,
             falloff_angle: float = 0.000000,
             falloff_width: float = 0.000000,
             edge_offset: float = 0.000000,
             z_offset: float = 0.000000) -> None
```

<a id="unreal.WaterFalloffSettings.falloff_mode"></a>

#### falloff\_mode

```python
@property
def falloff_mode() -> WaterBrushFalloffMode
```

(WaterBrushFalloffMode):  [Read-Write]

<a id="unreal.WaterFalloffSettings.falloff_mode"></a>

#### falloff\_mode

```python
@falloff_mode.setter
def falloff_mode(value: WaterBrushFalloffMode) -> None
```

<a id="unreal.WaterFalloffSettings.falloff_angle"></a>

#### falloff\_angle

```python
@property
def falloff_angle() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterFalloffSettings.falloff_angle"></a>

#### falloff\_angle

```python
@falloff_angle.setter
def falloff_angle(value: float) -> None
```

<a id="unreal.WaterFalloffSettings.falloff_width"></a>

#### falloff\_width

```python
@property
def falloff_width() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterFalloffSettings.falloff_width"></a>

#### falloff\_width

```python
@falloff_width.setter
def falloff_width(value: float) -> None
```

<a id="unreal.WaterFalloffSettings.edge_offset"></a>

#### edge\_offset

```python
@property
def edge_offset() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterFalloffSettings.edge_offset"></a>

#### edge\_offset

```python
@edge_offset.setter
def edge_offset(value: float) -> None
```

<a id="unreal.WaterFalloffSettings.z_offset"></a>

#### z\_offset

```python
@property
def z_offset() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterFalloffSettings.z_offset"></a>

#### z\_offset

```python
@z_offset.setter
def z_offset(value: float) -> None
```

<a id="unreal.WaterBrushEffectCurves"></a>