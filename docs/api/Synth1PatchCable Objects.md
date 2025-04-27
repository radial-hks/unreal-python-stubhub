## Synth1PatchCable Objects

```python
class Synth1PatchCable(StructBase)
```

Synth 1Patch Cable

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: EpicSynth1Types.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``depth`` (float):  [Read-Write] The patch depth (how much the modulator modulates the destination)
- ``destination`` (Synth1PatchDestination):  [Read-Write] The patch destination type

<a id="unreal.Synth1PatchCable.__init__"></a>

#### __init__

```python
def __init__(
    depth: float = 0.000000,
    destination: Synth1PatchDestination = Synth1PatchDestination.OSC1_GAIN
) -> None
```

<a id="unreal.Synth1PatchCable.depth"></a>

#### depth

```python
@property
def depth() -> float
```

(float):  [Read-Write] The patch depth (how much the modulator modulates the destination)

<a id="unreal.Synth1PatchCable.depth"></a>

#### depth

```python
@depth.setter
def depth(value: float) -> None
```

<a id="unreal.Synth1PatchCable.destination"></a>

#### destination

```python
@property
def destination() -> Synth1PatchDestination
```

(Synth1PatchDestination):  [Read-Write] The patch destination type

<a id="unreal.Synth1PatchCable.destination"></a>

#### destination

```python
@destination.setter
def destination(value: Synth1PatchDestination) -> None
```

<a id="unreal.PatchId"></a>