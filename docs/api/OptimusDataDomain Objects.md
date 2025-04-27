## OptimusDataDomain Objects

```python
class OptimusDataDomain(StructBase)
```

A struct to specify the domain range of a resource buffer, as defined by compute kernels and data
 interfaces. Data domains can be multi-dimensional, expression-based, or empty. Empty domains on pins imply a single
 value, like a parameter.

 Domains come in two flavors, either as a pre-defined list with a multiplier, or as an arithmetic expression. For
 domains with a multiplier, the multiplier only applies to the innermost dimension (e.g. Vertex.Bone x 2, allows
 for two values per-bone, but not two values per-bone _and_ per-vertex)

 The expression can take any execution domain, or none (e.g. "Vertex * 2 + 1", "Triangle * 2 + Vertex * 6", "1024").
 If an expression is used, the domain is one-dimensional.
 As of now, expression domain comparison is done on the string level, such that "Vertex * 2" and "2 * Vertex" are
 not marked as compatible domains.

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusDataDomain.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dimension_names`` (Array[Name]):  [Read-Write] The name of the context that this resource/kernel applies to.
- ``expression`` (str):  [Read-Write]
- ``multiplier`` (int32):  [Read-Write]
- ``type`` (OptimusDataDomainType):  [Read-Write]

<a id="unreal.OptimusDataDomain.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.OptimusMultiLevelDataDomain"></a>