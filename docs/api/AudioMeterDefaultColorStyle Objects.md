## AudioMeterDefaultColorStyle Objects

```python
class AudioMeterDefaultColorStyle(SlateWidgetStyle)
```

Audio Meter Default Color Style

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMeter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``meter_background_color`` (LinearColor):  [Read-Write]
- ``meter_clipping_color`` (LinearColor):  [Read-Write]
- ``meter_peak_color`` (LinearColor):  [Read-Write]
- ``meter_scale_color`` (LinearColor):  [Read-Write]
- ``meter_scale_label_color`` (LinearColor):  [Read-Write]
- ``meter_value_color`` (LinearColor):  [Read-Write]

<a id="unreal.AudioMeterDefaultColorStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    meter_background_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    meter_value_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    meter_peak_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    meter_clipping_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ],
    meter_scale_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    meter_scale_label_color: LinearColor = [
        0.000000, 0.000000, 0.000000, 0.000000
    ]
) -> None
```

<a id="unreal.AudioMeterDefaultColorStyle.meter_background_color"></a>

#### meter\_background\_color

```python
@property
def meter_background_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMeterDefaultColorStyle.meter_background_color"></a>

#### meter\_background\_color

```python
@meter_background_color.setter
def meter_background_color(value: LinearColor) -> None
```

<a id="unreal.AudioMeterDefaultColorStyle.meter_value_color"></a>

#### meter\_value\_color

```python
@property
def meter_value_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMeterDefaultColorStyle.meter_value_color"></a>

#### meter\_value\_color

```python
@meter_value_color.setter
def meter_value_color(value: LinearColor) -> None
```

<a id="unreal.AudioMeterDefaultColorStyle.meter_peak_color"></a>

#### meter\_peak\_color

```python
@property
def meter_peak_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMeterDefaultColorStyle.meter_peak_color"></a>

#### meter\_peak\_color

```python
@meter_peak_color.setter
def meter_peak_color(value: LinearColor) -> None
```

<a id="unreal.AudioMeterDefaultColorStyle.meter_clipping_color"></a>

#### meter\_clipping\_color

```python
@property
def meter_clipping_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMeterDefaultColorStyle.meter_clipping_color"></a>

#### meter\_clipping\_color

```python
@meter_clipping_color.setter
def meter_clipping_color(value: LinearColor) -> None
```

<a id="unreal.AudioMeterDefaultColorStyle.meter_scale_color"></a>

#### meter\_scale\_color

```python
@property
def meter_scale_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMeterDefaultColorStyle.meter_scale_color"></a>

#### meter\_scale\_color

```python
@meter_scale_color.setter
def meter_scale_color(value: LinearColor) -> None
```

<a id="unreal.AudioMeterDefaultColorStyle.meter_scale_label_color"></a>

#### meter\_scale\_label\_color

```python
@property
def meter_scale_label_color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.AudioMeterDefaultColorStyle.meter_scale_label_color"></a>

#### meter\_scale\_label\_color

```python
@meter_scale_label_color.setter
def meter_scale_label_color(value: LinearColor) -> None
```

<a id="unreal.AudioSpectrumPlotStyle"></a>