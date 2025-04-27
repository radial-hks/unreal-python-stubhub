## DatasmithStaticMeshImportOptions Objects

```python
class DatasmithStaticMeshImportOptions(StructBase)
```

Datasmith Static Mesh Import Options

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``generate_lightmap_u_vs`` (bool):  [Read-Write]
- ``max_lightmap_resolution`` (DatasmithImportLightmapMax):  [Read-Write] Maximum resolution for auto-generated lightmap UVs
- ``min_lightmap_resolution`` (DatasmithImportLightmapMin):  [Read-Write] Minimum resolution for auto-generated lightmap UVs
- ``remove_degenerates`` (bool):  [Read-Write]

<a id="unreal.DatasmithStaticMeshImportOptions.__init__"></a>

#### __init__

```python
def __init__(
        min_lightmap_resolution:
    DatasmithImportLightmapMin = DatasmithImportLightmapMin.LIGHTMAP_16,
        max_lightmap_resolution:
    DatasmithImportLightmapMax = DatasmithImportLightmapMax.LIGHTMAP_64,
        generate_lightmap_u_vs: bool = False,
        remove_degenerates: bool = False) -> None
```

<a id="unreal.DatasmithStaticMeshImportOptions.min_lightmap_resolution"></a>

#### min_lightmap_resolution

```python
@property
def min_lightmap_resolution() -> DatasmithImportLightmapMin
```

(DatasmithImportLightmapMin):  [Read-Write] Minimum resolution for auto-generated lightmap UVs

<a id="unreal.DatasmithStaticMeshImportOptions.min_lightmap_resolution"></a>

#### min_lightmap_resolution

```python
@min_lightmap_resolution.setter
def min_lightmap_resolution(value: DatasmithImportLightmapMin) -> None
```

<a id="unreal.DatasmithStaticMeshImportOptions.max_lightmap_resolution"></a>

#### max_lightmap_resolution

```python
@property
def max_lightmap_resolution() -> DatasmithImportLightmapMax
```

(DatasmithImportLightmapMax):  [Read-Write] Maximum resolution for auto-generated lightmap UVs

<a id="unreal.DatasmithStaticMeshImportOptions.max_lightmap_resolution"></a>

#### max_lightmap_resolution

```python
@max_lightmap_resolution.setter
def max_lightmap_resolution(value: DatasmithImportLightmapMax) -> None
```

<a id="unreal.DatasmithStaticMeshImportOptions.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@property
def generate_lightmap_u_vs() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DatasmithStaticMeshImportOptions.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@generate_lightmap_u_vs.setter
def generate_lightmap_u_vs(value: bool) -> None
```

<a id="unreal.DatasmithStaticMeshImportOptions.remove_degenerates"></a>

#### remove_degenerates

```python
@property
def remove_degenerates() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DatasmithStaticMeshImportOptions.remove_degenerates"></a>

#### remove_degenerates

```python
@remove_degenerates.setter
def remove_degenerates(value: bool) -> None
```

<a id="unreal.DatasmithReimportOptions"></a>