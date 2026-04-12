## InteriorSettings Objects

```python
class InteriorSettings(StructBase)
```

Struct encapsulating settings for interior areas.

**C++ Source:**

- **Module**: Engine
- **File**: AudioVolume.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``exterior_lpf`` (float):  [Read-Write] The desired LPF frequency cutoff in hertz of sounds outside the volume when the player is inside the volume
- ``exterior_lpf_time`` (float):  [Read-Write] The time over which to interpolate from the current LPF to the desired LPF of sounds outside the volume when the player enters the volume
- ``exterior_time`` (float):  [Read-Write] The time over which to interpolate from the current volume to the desired volume of sounds outside the volume when the player enters the volume
- ``exterior_volume`` (float):  [Read-Write] The desired volume of sounds outside the volume when the player is inside the volume
- ``interior_lpf`` (float):  [Read-Write] The desired LPF frequency cutoff in hertz of sounds inside the volume when the player is outside the volume
- ``interior_lpf_time`` (float):  [Read-Write] The time over which to interpolate from the current LPF to the desired LPF of sounds inside the volume when the player exits the volume
- ``interior_time`` (float):  [Read-Write] The time over which to interpolate from the current volume to the desired volume of sounds inside the volume when the player exits the volume
- ``interior_volume`` (float):  [Read-Write] The desired volume of sounds inside the volume when the player is outside the volume

<a id="unreal.InteriorSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(exterior_volume: float = 0.000000,
             exterior_time: float = 0.000000,
             exterior_lpf: float = 0.000000,
             exterior_lpf_time: float = 0.000000,
             interior_volume: float = 0.000000,
             interior_time: float = 0.000000,
             interior_lpf: float = 0.000000,
             interior_lpf_time: float = 0.000000) -> None
```

<a id="unreal.InteriorSettings.exterior_volume"></a>

#### exterior\_volume

```python
@property
def exterior_volume() -> float
```

(float):  [Read-Write] The desired volume of sounds outside the volume when the player is inside the volume

<a id="unreal.InteriorSettings.exterior_volume"></a>

#### exterior\_volume

```python
@exterior_volume.setter
def exterior_volume(value: float) -> None
```

<a id="unreal.InteriorSettings.exterior_time"></a>

#### exterior\_time

```python
@property
def exterior_time() -> float
```

(float):  [Read-Write] The time over which to interpolate from the current volume to the desired volume of sounds outside the volume when the player enters the volume

<a id="unreal.InteriorSettings.exterior_time"></a>

#### exterior\_time

```python
@exterior_time.setter
def exterior_time(value: float) -> None
```

<a id="unreal.InteriorSettings.exterior_lpf"></a>

#### exterior\_lpf

```python
@property
def exterior_lpf() -> float
```

(float):  [Read-Write] The desired LPF frequency cutoff in hertz of sounds outside the volume when the player is inside the volume

<a id="unreal.InteriorSettings.exterior_lpf"></a>

#### exterior\_lpf

```python
@exterior_lpf.setter
def exterior_lpf(value: float) -> None
```

<a id="unreal.InteriorSettings.exterior_lpf_time"></a>

#### exterior\_lpf\_time

```python
@property
def exterior_lpf_time() -> float
```

(float):  [Read-Write] The time over which to interpolate from the current LPF to the desired LPF of sounds outside the volume when the player enters the volume

<a id="unreal.InteriorSettings.exterior_lpf_time"></a>

#### exterior\_lpf\_time

```python
@exterior_lpf_time.setter
def exterior_lpf_time(value: float) -> None
```

<a id="unreal.InteriorSettings.interior_volume"></a>

#### interior\_volume

```python
@property
def interior_volume() -> float
```

(float):  [Read-Write] The desired volume of sounds inside the volume when the player is outside the volume

<a id="unreal.InteriorSettings.interior_volume"></a>

#### interior\_volume

```python
@interior_volume.setter
def interior_volume(value: float) -> None
```

<a id="unreal.InteriorSettings.interior_time"></a>

#### interior\_time

```python
@property
def interior_time() -> float
```

(float):  [Read-Write] The time over which to interpolate from the current volume to the desired volume of sounds inside the volume when the player exits the volume

<a id="unreal.InteriorSettings.interior_time"></a>

#### interior\_time

```python
@interior_time.setter
def interior_time(value: float) -> None
```

<a id="unreal.InteriorSettings.interior_lpf"></a>

#### interior\_lpf

```python
@property
def interior_lpf() -> float
```

(float):  [Read-Write] The desired LPF frequency cutoff in hertz of sounds inside the volume when the player is outside the volume

<a id="unreal.InteriorSettings.interior_lpf"></a>

#### interior\_lpf

```python
@interior_lpf.setter
def interior_lpf(value: float) -> None
```

<a id="unreal.InteriorSettings.interior_lpf_time"></a>

#### interior\_lpf\_time

```python
@property
def interior_lpf_time() -> float
```

(float):  [Read-Write] The time over which to interpolate from the current LPF to the desired LPF of sounds inside the volume when the player exits the volume

<a id="unreal.InteriorSettings.interior_lpf_time"></a>

#### interior\_lpf\_time

```python
@interior_lpf_time.setter
def interior_lpf_time(value: float) -> None
```

<a id="unreal.CameraLensInterfaceClassSupport"></a>