## EarthWaterColorPreset Objects

```python
class EarthWaterColorPreset(StructBase)
```

Earth Water Color Preset

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRenderTarget2DFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absorption_color`` (LinearColor):  [Read-Write]
- ``behind_color`` (LinearColor):  [Read-Write]
- ``clarity`` (float):  [Read-Write]
- ``overlay_color`` (LinearColor):  [Read-Write]
- ``phase_g`` (float):  [Read-Write]
- ``scattering_color`` (LinearColor):  [Read-Write]

<a id="unreal.EarthWaterColorPreset.__init__"></a>

#### \_\_init\_\_

```python
def __init__(scattering_color: LinearColor = [
    0.000000, 0.000000, 0.000000, 0.000000
],
             absorption_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             behind_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             overlay_color: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             clarity: float = 0.000000,
             phase_g: float = 0.000000) -> None
```

<a id="unreal.EarthWaterColorPreset.scattering_color"></a>

#### scattering\_color

```python
@property
def scattering_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.EarthWaterColorPreset.scattering_color"></a>

#### scattering\_color

```python
@scattering_color.setter
def scattering_color(value: LinearColor) -> None
```

<a id="unreal.EarthWaterColorPreset.absorption_color"></a>

#### absorption\_color

```python
@property
def absorption_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.EarthWaterColorPreset.absorption_color"></a>

#### absorption\_color

```python
@absorption_color.setter
def absorption_color(value: LinearColor) -> None
```

<a id="unreal.EarthWaterColorPreset.behind_color"></a>

#### behind\_color

```python
@property
def behind_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.EarthWaterColorPreset.behind_color"></a>

#### behind\_color

```python
@behind_color.setter
def behind_color(value: LinearColor) -> None
```

<a id="unreal.EarthWaterColorPreset.overlay_color"></a>

#### overlay\_color

```python
@property
def overlay_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.EarthWaterColorPreset.overlay_color"></a>

#### overlay\_color

```python
@overlay_color.setter
def overlay_color(value: LinearColor) -> None
```

<a id="unreal.EarthWaterColorPreset.clarity"></a>

#### clarity

```python
@property
def clarity() -> float
```

(float):  [Read-Write]

<a id="unreal.EarthWaterColorPreset.clarity"></a>

#### clarity

```python
@clarity.setter
def clarity(value: float) -> None
```

<a id="unreal.EarthWaterColorPreset.phase_g"></a>

#### phase\_g

```python
@property
def phase_g() -> float
```

(float):  [Read-Write]

<a id="unreal.EarthWaterColorPreset.phase_g"></a>

#### phase\_g

```python
@phase_g.setter
def phase_g(value: float) -> None
```

<a id="unreal.EarthRenderTarget2DFragment"></a>