## SourceEffectMotionFilterSettings Objects

```python
class SourceEffectMotionFilterSettings(StructBase)
```

FSourceEffectMotionFilterSettings
This is the source effect's setting struct.

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SourceEffectMotionFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dry_volume_db`` (float):  [Read-Write] Dry volume pass-through in dB.
- ``filter_a_settings`` (SourceEffectIndividualFilterSettings):  [Read-Write] Initial settings for Filter A
- ``filter_b_settings`` (SourceEffectIndividualFilterSettings):  [Read-Write] Initial settings for Filter B
- ``modulation_mappings`` (Map[SourceEffectMotionFilterModDestination, SourceEffectMotionFilterModulationSettings]):  [Read-Write] Modulation Mappings
- ``motion_filter_mix`` (float):  [Read-Write] Filter Mix controls the amount of each filter in the signal where -1.0f outputs Only Filter A, 0.0f is an equal balance between Filter A and B, and 1.0f outputs only Filter B. How this blend works depends on the Topology.
- ``motion_filter_topology`` (SourceEffectMotionFilterTopology):  [Read-Write] In Serial Mode, Filter A will process then Filter B will process; in Parallel mode, Filter A and Filter B will process the dry input seprately, then be mixed together afterward.

<a id="unreal.SourceEffectMotionFilterSettings.__init__"></a>

#### __init__

```python
def __init__(
        motion_filter_topology:
    SourceEffectMotionFilterTopology = SourceEffectMotionFilterTopology.
    SERIAL_MODE,
        motion_filter_mix: float = 0.000000,
        filter_a_settings: SourceEffectIndividualFilterSettings = [
            SourceEffectMotionFilterCircuit.LADDER,
            SourceEffectMotionFilterType.LOW_PASS, 800.000000, 2.000000
        ],
        filter_b_settings: SourceEffectIndividualFilterSettings = [
            SourceEffectMotionFilterCircuit.LADDER,
            SourceEffectMotionFilterType.LOW_PASS, 800.000000, 2.000000
        ],
        modulation_mappings: Map[
            SourceEffectMotionFilterModDestination,
            SourceEffectMotionFilterModulationSettings] = {},
        dry_volume_db: float = 0.000000) -> None
```

<a id="unreal.SourceEffectMotionFilterSettings.motion_filter_topology"></a>

#### motion_filter_topology

```python
@property
def motion_filter_topology() -> SourceEffectMotionFilterTopology
```

(SourceEffectMotionFilterTopology):  [Read-Write] In Serial Mode, Filter A will process then Filter B will process; in Parallel mode, Filter A and Filter B will process the dry input seprately, then be mixed together afterward.

<a id="unreal.SourceEffectMotionFilterSettings.motion_filter_topology"></a>

#### motion_filter_topology

```python
@motion_filter_topology.setter
def motion_filter_topology(value: SourceEffectMotionFilterTopology) -> None
```

<a id="unreal.SourceEffectMotionFilterSettings.motion_filter_mix"></a>

#### motion_filter_mix

```python
@property
def motion_filter_mix() -> float
```

(float):  [Read-Write] Filter Mix controls the amount of each filter in the signal where -1.0f outputs Only Filter A, 0.0f is an equal balance between Filter A and B, and 1.0f outputs only Filter B. How this blend works depends on the Topology.

<a id="unreal.SourceEffectMotionFilterSettings.motion_filter_mix"></a>

#### motion_filter_mix

```python
@motion_filter_mix.setter
def motion_filter_mix(value: float) -> None
```

<a id="unreal.SourceEffectMotionFilterSettings.filter_a_settings"></a>

#### filter_a_settings

```python
@property
def filter_a_settings() -> SourceEffectIndividualFilterSettings
```

(SourceEffectIndividualFilterSettings):  [Read-Write] Initial settings for Filter A

<a id="unreal.SourceEffectMotionFilterSettings.filter_a_settings"></a>

#### filter_a_settings

```python
@filter_a_settings.setter
def filter_a_settings(value: SourceEffectIndividualFilterSettings) -> None
```

<a id="unreal.SourceEffectMotionFilterSettings.filter_b_settings"></a>

#### filter_b_settings

```python
@property
def filter_b_settings() -> SourceEffectIndividualFilterSettings
```

(SourceEffectIndividualFilterSettings):  [Read-Write] Initial settings for Filter B

<a id="unreal.SourceEffectMotionFilterSettings.filter_b_settings"></a>

#### filter_b_settings

```python
@filter_b_settings.setter
def filter_b_settings(value: SourceEffectIndividualFilterSettings) -> None
```

<a id="unreal.SourceEffectMotionFilterSettings.modulation_mappings"></a>

#### modulation_mappings

```python
@property
def modulation_mappings() -> Map[SourceEffectMotionFilterModDestination,
                                 SourceEffectMotionFilterModulationSettings]
```

(Map[SourceEffectMotionFilterModDestination, SourceEffectMotionFilterModulationSettings]):  [Read-Write] Modulation Mappings

<a id="unreal.SourceEffectMotionFilterSettings.modulation_mappings"></a>

#### modulation_mappings

```python
@modulation_mappings.setter
def modulation_mappings(
    value: Map[SourceEffectMotionFilterModDestination,
               SourceEffectMotionFilterModulationSettings]
) -> None
```

<a id="unreal.SourceEffectMotionFilterSettings.dry_volume_db"></a>

#### dry_volume_db

```python
@property
def dry_volume_db() -> float
```

(float):  [Read-Write] Dry volume pass-through in dB.

<a id="unreal.SourceEffectMotionFilterSettings.dry_volume_db"></a>

#### dry_volume_db

```python
@dry_volume_db.setter
def dry_volume_db(value: float) -> None
```

<a id="unreal.SourceEffectPannerSettings"></a>