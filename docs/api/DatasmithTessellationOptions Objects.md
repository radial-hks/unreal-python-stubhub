## DatasmithTessellationOptions Objects

```python
class DatasmithTessellationOptions(StructBase)
```

Datasmith Tessellation Options

**C++ Source:**

- **Plugin**: DatasmithContent
- **Module**: DatasmithContent
- **File**: DatasmithImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chord_tolerance`` (float):  [Read-Write] Maximum distance between any generated triangle and the original surface. Smaller values make more triangles.
- ``geometric_tolerance`` (double):  [Read-Write] Tolerance used to determine if a surface should be tessellated or not.
- ``max_edge_length`` (float):  [Read-Write] Maximum length of any edge in the generated triangles. Smaller values make more triangles.
- ``normal_tolerance`` (float):  [Read-Write] Maximum angle between adjacent triangles. Smaller values make more triangles.
- ``stitching_technique`` (DatasmithCADStitchingTechnique):  [Read-Write] Stitching technique applied on model before tessellation. Sewing could impact number of objects.
- ``stitching_tolerance`` (double):  [Read-Write] Tolerance used to determine if two surfaces should be stitched.

<a id="unreal.DatasmithTessellationOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(chord_tolerance: float = 0.000000,
             max_edge_length: float = 0.000000,
             normal_tolerance: float = 0.000000,
             stitching_technique:
             DatasmithCADStitchingTechnique = DatasmithCADStitchingTechnique.
             STITCHING_NONE,
             geometric_tolerance: float = 0.000000,
             stitching_tolerance: float = 0.000000) -> None
```

<a id="unreal.DatasmithTessellationOptions.chord_tolerance"></a>

#### chord\_tolerance

```python
@property
def chord_tolerance() -> float
```

(float):  [Read-Write] Maximum distance between any generated triangle and the original surface. Smaller values make more triangles.

<a id="unreal.DatasmithTessellationOptions.chord_tolerance"></a>

#### chord\_tolerance

```python
@chord_tolerance.setter
def chord_tolerance(value: float) -> None
```

<a id="unreal.DatasmithTessellationOptions.max_edge_length"></a>

#### max\_edge\_length

```python
@property
def max_edge_length() -> float
```

(float):  [Read-Write] Maximum length of any edge in the generated triangles. Smaller values make more triangles.

<a id="unreal.DatasmithTessellationOptions.max_edge_length"></a>

#### max\_edge\_length

```python
@max_edge_length.setter
def max_edge_length(value: float) -> None
```

<a id="unreal.DatasmithTessellationOptions.normal_tolerance"></a>

#### normal\_tolerance

```python
@property
def normal_tolerance() -> float
```

(float):  [Read-Write] Maximum angle between adjacent triangles. Smaller values make more triangles.

<a id="unreal.DatasmithTessellationOptions.normal_tolerance"></a>

#### normal\_tolerance

```python
@normal_tolerance.setter
def normal_tolerance(value: float) -> None
```

<a id="unreal.DatasmithTessellationOptions.stitching_technique"></a>

#### stitching\_technique

```python
@property
def stitching_technique() -> DatasmithCADStitchingTechnique
```

(DatasmithCADStitchingTechnique):  [Read-Write] Stitching technique applied on model before tessellation. Sewing could impact number of objects.

<a id="unreal.DatasmithTessellationOptions.stitching_technique"></a>

#### stitching\_technique

```python
@stitching_technique.setter
def stitching_technique(value: DatasmithCADStitchingTechnique) -> None
```

<a id="unreal.DatasmithTessellationOptions.geometric_tolerance"></a>

#### geometric\_tolerance

```python
@property
def geometric_tolerance() -> float
```

(double):  [Read-Write] Tolerance used to determine if a surface should be tessellated or not.

<a id="unreal.DatasmithTessellationOptions.geometric_tolerance"></a>

#### geometric\_tolerance

```python
@geometric_tolerance.setter
def geometric_tolerance(value: float) -> None
```

<a id="unreal.DatasmithTessellationOptions.stitching_tolerance"></a>

#### stitching\_tolerance

```python
@property
def stitching_tolerance() -> float
```

(double):  [Read-Write] Tolerance used to determine if two surfaces should be stitched.

<a id="unreal.DatasmithTessellationOptions.stitching_tolerance"></a>

#### stitching\_tolerance

```python
@stitching_tolerance.setter
def stitching_tolerance(value: float) -> None
```

<a id="unreal.DatasmithRetessellationOptions"></a>