## GeometryScriptCreateNewStaticMeshAssetOptions Objects

```python
class GeometryScriptCreateNewStaticMeshAssetOptions(StructBase)
```

Geometry Script Create New Static Mesh Asset Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingEditor
- **File**: CreateNewAssetUtilityFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_mode`` (CollisionTraceFlag):  [Read-Write]
- ``enable_collision`` (bool):  [Read-Write]
- ``enable_nanite`` (bool):  [Read-Write]
- ``enable_recompute_normals`` (bool):  [Read-Write]
- ``enable_recompute_tangents`` (bool):  [Read-Write]
- ``nanite_proxy_triangle_percent`` (float):  [Read-Write] Replaced NaniteProxyTrianglePercent with usage of Engine FMeshNaniteSettings, use NaniteSettings property instead
- ``nanite_settings`` (MeshNaniteSettings):  [Read-Write] Nanite settings to set on new StaticMesh Asset
- ``use_original_vertex_order`` (bool):  [Read-Write] Use the original vertex order found in the source data. This is useful if the inbound mesh was originally non-manifold, and needs to keep
  the non-manifold structure when re-created.

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.__init__"></a>

#### __init__

```python
def __init__(enable_recompute_normals: bool = False,
             enable_recompute_tangents: bool = False,
             enable_nanite: bool = False,
             nanite_settings: MeshNaniteSettings = [
                 False, False, False, True, -2147483648, -1, -1, 1.000000,
                 0.000000, NaniteFallbackTarget.AUTO, 1.000000, 1.000000,
                 0.000000, 0
             ],
             nanite_proxy_triangle_percent: float = 0.000000,
             enable_collision: bool = False,
             collision_mode: CollisionTraceFlag = CollisionTraceFlag.
             CTF_USE_DEFAULT,
             use_original_vertex_order: bool = False) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_recompute_normals"></a>

#### enable_recompute_normals

```python
@property
def enable_recompute_normals() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_recompute_normals"></a>

#### enable_recompute_normals

```python
@enable_recompute_normals.setter
def enable_recompute_normals(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_recompute_tangents"></a>

#### enable_recompute_tangents

```python
@property
def enable_recompute_tangents() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_recompute_tangents"></a>

#### enable_recompute_tangents

```python
@enable_recompute_tangents.setter
def enable_recompute_tangents(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_nanite"></a>

#### enable_nanite

```python
@property
def enable_nanite() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_nanite"></a>

#### enable_nanite

```python
@enable_nanite.setter
def enable_nanite(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.nanite_settings"></a>

#### nanite_settings

```python
@property
def nanite_settings() -> MeshNaniteSettings
```

(MeshNaniteSettings):  [Read-Write] Nanite settings to set on new StaticMesh Asset

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.nanite_settings"></a>

#### nanite_settings

```python
@nanite_settings.setter
def nanite_settings(value: MeshNaniteSettings) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.nanite_proxy_triangle_percent"></a>

#### nanite_proxy_triangle_percent

```python
@property
def nanite_proxy_triangle_percent() -> float
```

(float):  [Read-Write] Replaced NaniteProxyTrianglePercent with usage of Engine FMeshNaniteSettings, use NaniteSettings property instead

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.nanite_proxy_triangle_percent"></a>

#### nanite_proxy_triangle_percent

```python
@nanite_proxy_triangle_percent.setter
def nanite_proxy_triangle_percent(value: float) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_collision"></a>

#### enable_collision

```python
@property
def enable_collision() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.enable_collision"></a>

#### enable_collision

```python
@enable_collision.setter
def enable_collision(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.collision_mode"></a>

#### collision_mode

```python
@property
def collision_mode() -> CollisionTraceFlag
```

(CollisionTraceFlag):  [Read-Write]

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.collision_mode"></a>

#### collision_mode

```python
@collision_mode.setter
def collision_mode(value: CollisionTraceFlag) -> None
```

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.use_original_vertex_order"></a>

#### use_original_vertex_order

```python
@property
def use_original_vertex_order() -> bool
```

(bool):  [Read-Write] Use the original vertex order found in the source data. This is useful if the inbound mesh was originally non-manifold, and needs to keep
the non-manifold structure when re-created.

<a id="unreal.GeometryScriptCreateNewStaticMeshAssetOptions.use_original_vertex_order"></a>

#### use_original_vertex_order

```python
@use_original_vertex_order.setter
def use_original_vertex_order(value: bool) -> None
```

<a id="unreal.GeometryScriptCreateNewSkeletalMeshAssetOptions"></a>