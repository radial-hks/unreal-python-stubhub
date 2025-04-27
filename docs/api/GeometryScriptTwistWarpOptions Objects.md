## GeometryScriptTwistWarpOptions Objects

```python
class GeometryScriptTwistWarpOptions(StructBase)
```

Geometry Script Twist Warp Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshDeformFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bidirectional`` (bool):  [Read-Write] If true, the Twist is "centered" at the Origin, ie the regions on either side of the extents are rigidly transformed. If false, the Twist begins at the start of the Lower Extents, and the "lower" region is not affected.
- ``lower_extent`` (float):  [Read-Write] Lower extent used when bSymmetricExtents = false
- ``symmetric_extents`` (bool):  [Read-Write] Symmetric extents are [-BendExtent,BendExtent], if disabled, then [-LowerExtent,BendExtent] is used

<a id="unreal.GeometryScriptTwistWarpOptions.__init__"></a>

#### __init__

```python
def __init__(symmetric_extents: bool = False,
             lower_extent: float = 0.000000,
             bidirectional: bool = False) -> None
```

<a id="unreal.GeometryScriptTwistWarpOptions.symmetric_extents"></a>

#### symmetric_extents

```python
@property
def symmetric_extents() -> bool
```

(bool):  [Read-Write] Symmetric extents are [-BendExtent,BendExtent], if disabled, then [-LowerExtent,BendExtent] is used

<a id="unreal.GeometryScriptTwistWarpOptions.symmetric_extents"></a>

#### symmetric_extents

```python
@symmetric_extents.setter
def symmetric_extents(value: bool) -> None
```

<a id="unreal.GeometryScriptTwistWarpOptions.lower_extent"></a>

#### lower_extent

```python
@property
def lower_extent() -> float
```

(float):  [Read-Write] Lower extent used when bSymmetricExtents = false

<a id="unreal.GeometryScriptTwistWarpOptions.lower_extent"></a>

#### lower_extent

```python
@lower_extent.setter
def lower_extent(value: float) -> None
```

<a id="unreal.GeometryScriptTwistWarpOptions.bidirectional"></a>

#### bidirectional

```python
@property
def bidirectional() -> bool
```

(bool):  [Read-Write] If true, the Twist is "centered" at the Origin, ie the regions on either side of the extents are rigidly transformed. If false, the Twist begins at the start of the Lower Extents, and the "lower" region is not affected.

<a id="unreal.GeometryScriptTwistWarpOptions.bidirectional"></a>

#### bidirectional

```python
@bidirectional.setter
def bidirectional(value: bool) -> None
```

<a id="unreal.GeometryScriptFlareWarpOptions"></a>