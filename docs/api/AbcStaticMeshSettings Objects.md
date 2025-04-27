## AbcStaticMeshSettings Objects

```python
class AbcStaticMeshSettings(StructBase)
```

Abc Static Mesh Settings

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``generate_lightmap_u_vs`` (bool):  [Read-Write] Flag for whether or not lightmap UVs should be generated
- ``merge_meshes`` (bool):  [Read-Write] Whether or not to merge the static meshes on import (remember this can cause problems with overlapping UV-sets)
- ``propagate_matrix_transformations`` (bool):  [Read-Write] This will, if applicable, apply matrix transformations to the meshes

<a id="unreal.AbcStaticMeshSettings.__init__"></a>

#### __init__

```python
def __init__(merge_meshes: bool = False,
             propagate_matrix_transformations: bool = False,
             generate_lightmap_u_vs: bool = False) -> None
```

<a id="unreal.AbcStaticMeshSettings.merge_meshes"></a>

#### merge_meshes

```python
@property
def merge_meshes() -> bool
```

(bool):  [Read-Write] Whether or not to merge the static meshes on import (remember this can cause problems with overlapping UV-sets)

<a id="unreal.AbcStaticMeshSettings.merge_meshes"></a>

#### merge_meshes

```python
@merge_meshes.setter
def merge_meshes(value: bool) -> None
```

<a id="unreal.AbcStaticMeshSettings.propagate_matrix_transformations"></a>

#### propagate_matrix_transformations

```python
@property
def propagate_matrix_transformations() -> bool
```

(bool):  [Read-Write] This will, if applicable, apply matrix transformations to the meshes

<a id="unreal.AbcStaticMeshSettings.propagate_matrix_transformations"></a>

#### propagate_matrix_transformations

```python
@propagate_matrix_transformations.setter
def propagate_matrix_transformations(value: bool) -> None
```

<a id="unreal.AbcStaticMeshSettings.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@property
def generate_lightmap_u_vs() -> bool
```

(bool):  [Read-Write] Flag for whether or not lightmap UVs should be generated

<a id="unreal.AbcStaticMeshSettings.generate_lightmap_u_vs"></a>

#### generate_lightmap_u_vs

```python
@generate_lightmap_u_vs.setter
def generate_lightmap_u_vs(value: bool) -> None
```

<a id="unreal.AbcConversionSettings"></a>