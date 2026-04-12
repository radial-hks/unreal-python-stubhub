## GroomHairGroupPreview Objects

```python
class GroomHairGroupPreview(StructBase)
```

Groom Hair Group Preview

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_count`` (int32):  [Read-Only]
- ``group_id`` (int32):  [Read-Only]
- ``group_name`` (Name):  [Read-Only]
- ``guide_count`` (int32):  [Read-Only]
- ``interpolation_settings`` (HairGroupsInterpolation):  [Read-Write]

<a id="unreal.GroomHairGroupPreview.__init__"></a>

#### \_\_init\_\_

```python
def __init__(group_name: Name = "None",
             group_id: int = 0,
             curve_count: int = 0,
             guide_count: int = 0,
             interpolation_settings: HairGroupsInterpolation = []) -> None
```

<a id="unreal.GroomHairGroupPreview.group_name"></a>

#### group\_name

```python
@property
def group_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.GroomHairGroupPreview.group_id"></a>

#### group\_id

```python
@property
def group_id() -> int
```

(int32):  [Read-Only]

<a id="unreal.GroomHairGroupPreview.curve_count"></a>

#### curve\_count

```python
@property
def curve_count() -> int
```

(int32):  [Read-Only]

<a id="unreal.GroomHairGroupPreview.guide_count"></a>

#### guide\_count

```python
@property
def guide_count() -> int
```

(int32):  [Read-Only]

<a id="unreal.GroomHairGroupPreview.interpolation_settings"></a>

#### interpolation\_settings

```python
@property
def interpolation_settings() -> HairGroupsInterpolation
```

(HairGroupsInterpolation):  [Read-Write]

<a id="unreal.GroomHairGroupPreview.interpolation_settings"></a>

#### interpolation\_settings

```python
@interpolation_settings.setter
def interpolation_settings(value: HairGroupsInterpolation) -> None
```

<a id="unreal.GroomBuildSettings"></a>