## GroomImportOptions Objects

```python
class GroomImportOptions(Object)
```

Groom Import Options

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``conversion_settings`` (GroomConversionSettings):  [Read-Write]
- ``interpolation_settings`` (Array[HairGroupsInterpolation]):  [Read-Only] Interpolation settings per group

<a id="unreal.GroomImportOptions.conversion_settings"></a>

#### conversion_settings

```python
@property
def conversion_settings() -> GroomConversionSettings
```

(GroomConversionSettings):  [Read-Write]

<a id="unreal.GroomImportOptions.conversion_settings"></a>

#### conversion_settings

```python
@conversion_settings.setter
def conversion_settings(value: GroomConversionSettings) -> None
```

<a id="unreal.GroomImportOptions.interpolation_settings"></a>

#### interpolation_settings

```python
@property
def interpolation_settings() -> Array[HairGroupsInterpolation]
```

(Array[HairGroupsInterpolation]):  [Read-Only] Interpolation settings per group

<a id="unreal.GroomHairGroupsPreview"></a>