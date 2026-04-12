## GeometryScriptCopyMeshFromComponentOptions Objects

```python
class GeometryScriptCopyMeshFromComponentOptions(StructBase)
```

Geometry Script Copy Mesh from Component Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: SceneUtilityFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``requested_lod`` (GeometryScriptMeshReadLOD):  [Read-Write]
- ``want_instance_colors`` (bool):  [Read-Write] Whether to request per-instance vertex colors (where applicable; applies to RenderData LODs of Static Mesh components)
- ``want_normals`` (bool):  [Read-Write]
- ``want_tangents`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    want_normals: bool = False,
    want_tangents: bool = False,
    want_instance_colors: bool = False,
    requested_lod: GeometryScriptMeshReadLOD = [
        GeometryScriptLODType.MAX_AVAILABLE, 0
    ]
) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.want_normals"></a>

#### want\_normals

```python
@property
def want_normals() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.want_normals"></a>

#### want\_normals

```python
@want_normals.setter
def want_normals(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.want_tangents"></a>

#### want\_tangents

```python
@property
def want_tangents() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.want_tangents"></a>

#### want\_tangents

```python
@want_tangents.setter
def want_tangents(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.want_instance_colors"></a>

#### want\_instance\_colors

```python
@property
def want_instance_colors() -> bool
```

(bool):  [Read-Write] Whether to request per-instance vertex colors (where applicable; applies to RenderData LODs of Static Mesh components)

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.want_instance_colors"></a>

#### want\_instance\_colors

```python
@want_instance_colors.setter
def want_instance_colors(value: bool) -> None
```

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.requested_lod"></a>

#### requested\_lod

```python
@property
def requested_lod() -> GeometryScriptMeshReadLOD
```

(GeometryScriptMeshReadLOD):  [Read-Write]

<a id="unreal.GeometryScriptCopyMeshFromComponentOptions.requested_lod"></a>

#### requested\_lod

```python
@requested_lod.setter
def requested_lod(value: GeometryScriptMeshReadLOD) -> None
```

<a id="unreal.GeometryScriptDetermineMeshOcclusionOptions"></a>