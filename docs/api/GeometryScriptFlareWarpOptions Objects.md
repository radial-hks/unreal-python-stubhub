## GeometryScriptFlareWarpOptions Objects

```python
class GeometryScriptFlareWarpOptions(StructBase)
```

Geometry Script Flare Warp Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDeformFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flare_type`` (GeometryScriptFlareType):  [Read-Write] Determines the profile used as a displacement
- ``lower_extent`` (float):  [Read-Write] Lower extent used when bSymmetricExtents = false
- ``symmetric_extents`` (bool):  [Read-Write] Symmetric extents are [-BendExtent,BendExtent], if disabled, then [-LowerExtent,BendExtent] is used

<a id="unreal.GeometryScriptFlareWarpOptions.__init__"></a>

#### __init__

```python
def __init__(
    symmetric_extents: bool = False,
    lower_extent: float = 0.000000,
    flare_type: GeometryScriptFlareType = GeometryScriptFlareType.SIN_MODE
) -> None
```

<a id="unreal.GeometryScriptFlareWarpOptions.symmetric_extents"></a>

#### symmetric_extents

```python
@property
def symmetric_extents() -> bool
```

(bool):  [Read-Write] Symmetric extents are [-BendExtent,BendExtent], if disabled, then [-LowerExtent,BendExtent] is used

<a id="unreal.GeometryScriptFlareWarpOptions.symmetric_extents"></a>

#### symmetric_extents

```python
@symmetric_extents.setter
def symmetric_extents(value: bool) -> None
```

<a id="unreal.GeometryScriptFlareWarpOptions.lower_extent"></a>

#### lower_extent

```python
@property
def lower_extent() -> float
```

(float):  [Read-Write] Lower extent used when bSymmetricExtents = false

<a id="unreal.GeometryScriptFlareWarpOptions.lower_extent"></a>

#### lower_extent

```python
@lower_extent.setter
def lower_extent(value: float) -> None
```

<a id="unreal.GeometryScriptFlareWarpOptions.flare_type"></a>

#### flare_type

```python
@property
def flare_type() -> GeometryScriptFlareType
```

(GeometryScriptFlareType):  [Read-Write] Determines the profile used as a displacement

<a id="unreal.GeometryScriptFlareWarpOptions.flare_type"></a>

#### flare_type

```python
@flare_type.setter
def flare_type(value: GeometryScriptFlareType) -> None
```

<a id="unreal.GeometryScriptPerlinNoiseLayerOptions"></a>