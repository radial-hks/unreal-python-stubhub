## GeometryScriptRecomputeUVsOptions Objects

```python
class GeometryScriptRecomputeUVsOptions(StructBase)
```

Geometry Script Recompute UVs Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshUVFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_align_islands_with_axes`` (bool):  [Read-Write]
- ``exp_map_options`` (GeometryScriptExpMapUVOptions):  [Read-Write]
- ``group_layer`` (GeometryScriptGroupLayer):  [Read-Write]
- ``island_source`` (GeometryScriptUVIslandSource):  [Read-Write]
- ``method`` (GeometryScriptUVFlattenMethod):  [Read-Write]
- ``spectral_conformal_options`` (GeometryScriptSpectralConformalUVOptions):  [Read-Write]

<a id="unreal.GeometryScriptRecomputeUVsOptions.__init__"></a>

#### __init__

```python
def __init__(
        method: GeometryScriptUVFlattenMethod = GeometryScriptUVFlattenMethod.
    EXP_MAP,
        island_source:
    GeometryScriptUVIslandSource = GeometryScriptUVIslandSource.POLY_GROUPS,
        exp_map_options: GeometryScriptExpMapUVOptions = [0, 0.250000],
        spectral_conformal_options: GeometryScriptSpectralConformalUVOptions = [
            True
        ],
        group_layer: GeometryScriptGroupLayer = [True, 0],
        auto_align_islands_with_axes: bool = False) -> None
```

<a id="unreal.GeometryScriptRecomputeUVsOptions.method"></a>

#### method

```python
@property
def method() -> GeometryScriptUVFlattenMethod
```

(GeometryScriptUVFlattenMethod):  [Read-Write]

<a id="unreal.GeometryScriptRecomputeUVsOptions.method"></a>

#### method

```python
@method.setter
def method(value: GeometryScriptUVFlattenMethod) -> None
```

<a id="unreal.GeometryScriptRecomputeUVsOptions.island_source"></a>

#### island_source

```python
@property
def island_source() -> GeometryScriptUVIslandSource
```

(GeometryScriptUVIslandSource):  [Read-Write]

<a id="unreal.GeometryScriptRecomputeUVsOptions.island_source"></a>

#### island_source

```python
@island_source.setter
def island_source(value: GeometryScriptUVIslandSource) -> None
```

<a id="unreal.GeometryScriptRecomputeUVsOptions.exp_map_options"></a>

#### exp_map_options

```python
@property
def exp_map_options() -> GeometryScriptExpMapUVOptions
```

(GeometryScriptExpMapUVOptions):  [Read-Write]

<a id="unreal.GeometryScriptRecomputeUVsOptions.exp_map_options"></a>

#### exp_map_options

```python
@exp_map_options.setter
def exp_map_options(value: GeometryScriptExpMapUVOptions) -> None
```

<a id="unreal.GeometryScriptRecomputeUVsOptions.spectral_conformal_options"></a>

#### spectral_conformal_options

```python
@property
def spectral_conformal_options() -> GeometryScriptSpectralConformalUVOptions
```

(GeometryScriptSpectralConformalUVOptions):  [Read-Write]

<a id="unreal.GeometryScriptRecomputeUVsOptions.spectral_conformal_options"></a>

#### spectral_conformal_options

```python
@spectral_conformal_options.setter
def spectral_conformal_options(
        value: GeometryScriptSpectralConformalUVOptions) -> None
```

<a id="unreal.GeometryScriptRecomputeUVsOptions.group_layer"></a>

#### group_layer

```python
@property
def group_layer() -> GeometryScriptGroupLayer
```

(GeometryScriptGroupLayer):  [Read-Write]

<a id="unreal.GeometryScriptRecomputeUVsOptions.group_layer"></a>

#### group_layer

```python
@group_layer.setter
def group_layer(value: GeometryScriptGroupLayer) -> None
```

<a id="unreal.GeometryScriptRecomputeUVsOptions.auto_align_islands_with_axes"></a>

#### auto_align_islands_with_axes

```python
@property
def auto_align_islands_with_axes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptRecomputeUVsOptions.auto_align_islands_with_axes"></a>

#### auto_align_islands_with_axes

```python
@auto_align_islands_with_axes.setter
def auto_align_islands_with_axes(value: bool) -> None
```

<a id="unreal.GeometryScriptPatchBuilderOptions"></a>