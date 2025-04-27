## SoundModulationDestinationSettings Objects

```python
class SoundModulationDestinationSettings(StructBase)
```

Parameter destination settings allowing modulation control override for parameter destinations opting in to the Modulation System.

**C++ Source:**

- **Module**: Engine
- **File**: SoundModulationDestination.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_modulation`` (bool):  [Read-Write] Whether or not to enable modulation
- ``modulator`` (SoundModulatorBase):  [Read-Write]
  deprecated: Property 'Modulator' is deprecated.
- ``modulators`` (Set[SoundModulatorBase]):  [Read-Write] Set of modulation sources, which provides values to mix with base value.
- ``value`` (float):  [Read-Write] Base value of parameter

<a id="unreal.SoundModulationDestinationSettings.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             modulators: Set[SoundModulatorBase] = []) -> None
```

<a id="unreal.SoundModulationDestinationSettings.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] Base value of parameter

<a id="unreal.SoundModulationDestinationSettings.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.SoundModulationDestinationSettings.modulator"></a>

#### modulator

```python
@property
def modulator() -> SoundModulatorBase
```

(SoundModulatorBase):  [Read-Write]
deprecated: Property 'Modulator' is deprecated.

<a id="unreal.SoundModulationDestinationSettings.modulator"></a>

#### modulator

```python
@modulator.setter
def modulator(value: SoundModulatorBase) -> None
```

<a id="unreal.SoundModulationDestinationSettings.modulators"></a>

#### modulators

```python
@property
def modulators() -> Set[SoundModulatorBase]
```

(Set[SoundModulatorBase]):  [Read-Write] Set of modulation sources, which provides values to mix with base value.

<a id="unreal.SoundModulationDestinationSettings.modulators"></a>

#### modulators

```python
@modulators.setter
def modulators(value: Set[SoundModulatorBase]) -> None
```

<a id="unreal.PassiveSoundMixModifier"></a>