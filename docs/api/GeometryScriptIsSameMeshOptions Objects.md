## GeometryScriptIsSameMeshOptions Objects

```python
class GeometryScriptIsSameMeshOptions(StructBase)
```

Geometry Script Is Same Mesh Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshComparisonFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``check_attributes`` (bool):  [Read-Write]
- ``check_colors`` (bool):  [Read-Write]
- ``check_connectivity`` (bool):  [Read-Write]
- ``check_edge_i_ds`` (bool):  [Read-Write]
- ``check_groups`` (bool):  [Read-Write]
- ``check_normals`` (bool):  [Read-Write]
- ``check_u_vs`` (bool):  [Read-Write]
- ``epsilon`` (float):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.__init__"></a>

#### __init__

```python
def __init__(check_connectivity: bool = False,
             check_edge_i_ds: bool = False,
             check_normals: bool = False,
             check_colors: bool = False,
             check_u_vs: bool = False,
             check_groups: bool = False,
             check_attributes: bool = False,
             epsilon: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptIsSameMeshOptions.check_connectivity"></a>

#### check_connectivity

```python
@property
def check_connectivity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.check_connectivity"></a>

#### check_connectivity

```python
@check_connectivity.setter
def check_connectivity(value: bool) -> None
```

<a id="unreal.GeometryScriptIsSameMeshOptions.check_edge_i_ds"></a>

#### check_edge_i_ds

```python
@property
def check_edge_i_ds() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.check_edge_i_ds"></a>

#### check_edge_i_ds

```python
@check_edge_i_ds.setter
def check_edge_i_ds(value: bool) -> None
```

<a id="unreal.GeometryScriptIsSameMeshOptions.check_normals"></a>

#### check_normals

```python
@property
def check_normals() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.check_normals"></a>

#### check_normals

```python
@check_normals.setter
def check_normals(value: bool) -> None
```

<a id="unreal.GeometryScriptIsSameMeshOptions.check_colors"></a>

#### check_colors

```python
@property
def check_colors() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.check_colors"></a>

#### check_colors

```python
@check_colors.setter
def check_colors(value: bool) -> None
```

<a id="unreal.GeometryScriptIsSameMeshOptions.check_u_vs"></a>

#### check_u_vs

```python
@property
def check_u_vs() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.check_u_vs"></a>

#### check_u_vs

```python
@check_u_vs.setter
def check_u_vs(value: bool) -> None
```

<a id="unreal.GeometryScriptIsSameMeshOptions.check_groups"></a>

#### check_groups

```python
@property
def check_groups() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.check_groups"></a>

#### check_groups

```python
@check_groups.setter
def check_groups(value: bool) -> None
```

<a id="unreal.GeometryScriptIsSameMeshOptions.check_attributes"></a>

#### check_attributes

```python
@property
def check_attributes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.check_attributes"></a>

#### check_attributes

```python
@check_attributes.setter
def check_attributes(value: bool) -> None
```

<a id="unreal.GeometryScriptIsSameMeshOptions.epsilon"></a>

#### epsilon

```python
@property
def epsilon() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptIsSameMeshOptions.epsilon"></a>

#### epsilon

```python
@epsilon.setter
def epsilon(value: float) -> None
```

<a id="unreal.GeometryScriptMeasureMeshDistanceOptions"></a>