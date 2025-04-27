## DatasmithRetessellationOptions Objects

```python
class DatasmithRetessellationOptions(DatasmithTessellationOptions)
```

Datasmith Retessellation Options

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chord_tolerance`` (float):  [Read-Write] Maximum distance between any generated triangle and the original surface. Smaller values make more triangles.
- ``geometric_tolerance`` (double):  [Read-Write] Tolerance used to determine if a surface should be tessellated or not.
- ``max_edge_length`` (float):  [Read-Write] Maximum length of any edge in the generated triangles. Smaller values make more triangles.
- ``normal_tolerance`` (float):  [Read-Write] Maximum angle between adjacent triangles. Smaller values make more triangles.
- ``retessellation_rule`` (DatasmithCADRetessellationRule):  [Read-Write] Regenerate deleted surfaces during retesselate or ignore them
- ``stitching_technique`` (DatasmithCADStitchingTechnique):  [Read-Write] Stitching technique applied on model before tessellation. Sewing could impact number of objects.
- ``stitching_tolerance`` (double):  [Read-Write] Tolerance used to determine if two surfaces should be stitched.

<a id="unreal.DatasmithRetessellationOptions.__init__"></a>

#### __init__

```python
def __init__(
    chord_tolerance: float = 0.000000,
    max_edge_length: float = 0.000000,
    normal_tolerance: float = 0.000000,
    stitching_technique:
    DatasmithCADStitchingTechnique = DatasmithCADStitchingTechnique.
    STITCHING_NONE,
    geometric_tolerance: float = 0.000000,
    stitching_tolerance: float = 0.000000,
    retessellation_rule:
    DatasmithCADRetessellationRule = DatasmithCADRetessellationRule.ALL
) -> None
```

<a id="unreal.DatasmithRetessellationOptions.retessellation_rule"></a>

#### retessellation_rule

```python
@property
def retessellation_rule() -> DatasmithCADRetessellationRule
```

(DatasmithCADRetessellationRule):  [Read-Write] Regenerate deleted surfaces during retesselate or ignore them

<a id="unreal.DatasmithRetessellationOptions.retessellation_rule"></a>

#### retessellation_rule

```python
@retessellation_rule.setter
def retessellation_rule(value: DatasmithCADRetessellationRule) -> None
```

<a id="unreal.GLTFExportMessages"></a>