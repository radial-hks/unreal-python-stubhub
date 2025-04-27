## VOscillator Objects

```python
class VOscillator(StructBase)
```

Defines FVector oscillation.

**C++ Source:**

- **Plugin**: EngineCameras
- **Module**: EngineCameras
- **File**: LegacyCameraShake.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``x`` (FOscillator):  [Read-Write] Oscillation in the X axis.
- ``y`` (FOscillator):  [Read-Write] Oscillation in the Y axis.
- ``z`` (FOscillator):  [Read-Write] Oscillation in the Z axis.

<a id="unreal.VOscillator.__init__"></a>

#### __init__

```python
def __init__(
    x: FOscillator = [0.000000, 0.000000, OscillatorWaveform.SINE_WAVE],
    y: FOscillator = [0.000000, 0.000000, OscillatorWaveform.SINE_WAVE],
    z: FOscillator = [0.000000, 0.000000,
                      OscillatorWaveform.SINE_WAVE]) -> None
```

<a id="unreal.VOscillator.x"></a>

#### x

```python
@property
def x() -> FOscillator
```

(FOscillator):  [Read-Write] Oscillation in the X axis.

<a id="unreal.VOscillator.x"></a>

#### x

```python
@x.setter
def x(value: FOscillator) -> None
```

<a id="unreal.VOscillator.y"></a>

#### y

```python
@property
def y() -> FOscillator
```

(FOscillator):  [Read-Write] Oscillation in the Y axis.

<a id="unreal.VOscillator.y"></a>

#### y

```python
@y.setter
def y(value: FOscillator) -> None
```

<a id="unreal.VOscillator.z"></a>

#### z

```python
@property
def z() -> FOscillator
```

(FOscillator):  [Read-Write] Oscillation in the Z axis.

<a id="unreal.VOscillator.z"></a>

#### z

```python
@z.setter
def z(value: FOscillator) -> None
```

<a id="unreal.CameraAnimationParams"></a>