## MeterChannelInfo Objects

```python
class MeterChannelInfo(StructBase)
```

Meter Channel Info

**C++ Source:**

- **Plugin**: AudioWidgets
- **Module**: AudioWidgets
- **File**: AudioMeterTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``clipping_value`` (float):  [Read-Write]
- ``meter_value`` (float):  [Read-Write]
- ``peak_value`` (float):  [Read-Write]

<a id="unreal.MeterChannelInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(meter_value: float = 0.000000,
             peak_value: float = 0.000000,
             clipping_value: float = 0.000000) -> None
```

<a id="unreal.MeterChannelInfo.meter_value"></a>

#### meter\_value

```python
@property
def meter_value() -> float
```

(float):  [Read-Write]

<a id="unreal.MeterChannelInfo.meter_value"></a>

#### meter\_value

```python
@meter_value.setter
def meter_value(value: float) -> None
```

<a id="unreal.MeterChannelInfo.peak_value"></a>

#### peak\_value

```python
@property
def peak_value() -> float
```

(float):  [Read-Write]

<a id="unreal.MeterChannelInfo.peak_value"></a>

#### peak\_value

```python
@peak_value.setter
def peak_value(value: float) -> None
```

<a id="unreal.MeterChannelInfo.clipping_value"></a>

#### clipping\_value

```python
@property
def clipping_value() -> float
```

(float):  [Read-Write]

<a id="unreal.MeterChannelInfo.clipping_value"></a>

#### clipping\_value

```python
@clipping_value.setter
def clipping_value(value: float) -> None
```

<a id="unreal.AudioMaterialWidgetStyle"></a>