## PCGLoadAlembicBPData Objects

```python
class PCGLoadAlembicBPData(StructBase)
```

PCGLoad Alembic BPData

**C++ Source:**

- **Plugin**: PCGExternalDataInterop
- **Module**: PCGExternalDataInteropEditor
- **File**: PCGLoadAlembic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alembic_file_path`` (FilePath):  [Read-Write]
- ``attribute_mapping`` (Map[str, PCGAttributePropertyInputSelector]):  [Read-Write]
- ``conversion_flip_handedness`` (bool):  [Read-Write] Flips rotation direction (W), useful together with swizzling
- ``conversion_settings`` (AbcConversionSettings):  [Read-Write] Conversion settings that will be applied on the transform only

<a id="unreal.PCGLoadAlembicBPData.__init__"></a>

#### __init__

```python
def __init__(
    conversion_settings: AbcConversionSettings = [
        AbcConversionPreset.MAYA, False, True, [1.000000, -1.000000, 1.000000],
        [90.000000, 0.000000, 0.000000]
    ],
    conversion_flip_handedness: bool = False,
    attribute_mapping: Map[str,
                           PCGAttributePropertyInputSelector] = {}) -> None
```

<a id="unreal.PCGLoadAlembicBPData.conversion_settings"></a>

#### conversion_settings

```python
@property
def conversion_settings() -> AbcConversionSettings
```

(AbcConversionSettings):  [Read-Write] Conversion settings that will be applied on the transform only

<a id="unreal.PCGLoadAlembicBPData.conversion_settings"></a>

#### conversion_settings

```python
@conversion_settings.setter
def conversion_settings(value: AbcConversionSettings) -> None
```

<a id="unreal.PCGLoadAlembicBPData.conversion_flip_handedness"></a>

#### conversion_flip_handedness

```python
@property
def conversion_flip_handedness() -> bool
```

(bool):  [Read-Write] Flips rotation direction (W), useful together with swizzling

<a id="unreal.PCGLoadAlembicBPData.conversion_flip_handedness"></a>

#### conversion_flip_handedness

```python
@conversion_flip_handedness.setter
def conversion_flip_handedness(value: bool) -> None
```

<a id="unreal.PCGLoadAlembicBPData.attribute_mapping"></a>

#### attribute_mapping

```python
@property
def attribute_mapping() -> Map[str, PCGAttributePropertyInputSelector]
```

(Map[str, PCGAttributePropertyInputSelector]):  [Read-Write]

<a id="unreal.PCGLoadAlembicBPData.attribute_mapping"></a>

#### attribute_mapping

```python
@attribute_mapping.setter
def attribute_mapping(
        value: Map[str, PCGAttributePropertyInputSelector]) -> None
```

<a id="unreal.PCGLoadAlembicBPData.setup_from_standard"></a>

#### setup_from_standard

```python
def setup_from_standard(setup: PCGLoadAlembicStandardSetup) -> None
```

x.setup_from_standard(setup) -> None
Setup from Standard

Args:
    setup (PCGLoadAlembicStandardSetup):

<a id="unreal.AppleImageUtilsImageConversionResult"></a>