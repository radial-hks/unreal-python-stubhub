## WaterCurveSettings Objects

```python
class WaterCurveSettings(StructBase)
```

Water Curve Settings

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: WaterCurveSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_depth`` (float):  [Read-Write]
- ``channel_edge_offset`` (float):  [Read-Write]
- ``curve_ramp_width`` (float):  [Read-Write]
- ``elevation_curve_asset`` (CurveFloat):  [Read-Write]
- ``use_curve_channel`` (bool):  [Read-Write]

<a id="unreal.WaterCurveSettings.__init__"></a>

#### __init__

```python
def __init__(use_curve_channel: bool = False,
             elevation_curve_asset: CurveFloat = None,
             channel_edge_offset: float = 0.000000,
             channel_depth: float = 0.000000,
             curve_ramp_width: float = 0.000000) -> None
```

<a id="unreal.WaterCurveSettings.use_curve_channel"></a>

#### use_curve_channel

```python
@property
def use_curve_channel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WaterCurveSettings.use_curve_channel"></a>

#### use_curve_channel

```python
@use_curve_channel.setter
def use_curve_channel(value: bool) -> None
```

<a id="unreal.WaterCurveSettings.elevation_curve_asset"></a>

#### elevation_curve_asset

```python
@property
def elevation_curve_asset() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.WaterCurveSettings.elevation_curve_asset"></a>

#### elevation_curve_asset

```python
@elevation_curve_asset.setter
def elevation_curve_asset(value: CurveFloat) -> None
```

<a id="unreal.WaterCurveSettings.channel_edge_offset"></a>

#### channel_edge_offset

```python
@property
def channel_edge_offset() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterCurveSettings.channel_edge_offset"></a>

#### channel_edge_offset

```python
@channel_edge_offset.setter
def channel_edge_offset(value: float) -> None
```

<a id="unreal.WaterCurveSettings.channel_depth"></a>

#### channel_depth

```python
@property
def channel_depth() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterCurveSettings.channel_depth"></a>

#### channel_depth

```python
@channel_depth.setter
def channel_depth(value: float) -> None
```

<a id="unreal.WaterCurveSettings.curve_ramp_width"></a>

#### curve_ramp_width

```python
@property
def curve_ramp_width() -> float
```

(float):  [Read-Write]

<a id="unreal.WaterCurveSettings.curve_ramp_width"></a>

#### curve_ramp_width

```python
@curve_ramp_width.setter
def curve_ramp_width(value: float) -> None
```

<a id="unreal.GerstnerWave"></a>