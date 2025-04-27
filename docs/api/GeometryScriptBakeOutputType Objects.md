## GeometryScriptBakeOutputType Objects

```python
class GeometryScriptBakeOutputType(StructBase)
```

Geometry Script Bake Output Type

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBakeFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (GeometryScriptBakeTypeOptions):  [Read-Write]
- ``b`` (GeometryScriptBakeTypeOptions):  [Read-Write]
- ``g`` (GeometryScriptBakeTypeOptions):  [Read-Write]
- ``output_mode`` (GeometryScriptBakeOutputMode):  [Read-Write] The bake output mode
- ``r`` (GeometryScriptBakeTypeOptions):  [Read-Write]
- ``rgba`` (GeometryScriptBakeTypeOptions):  [Read-Write]

<a id="unreal.GeometryScriptBakeOutputType.__init__"></a>

#### __init__

```python
def __init__(
        output_mode: GeometryScriptBakeOutputMode = GeometryScriptBakeOutputMode
    .RGBA,
        rgba: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE],
        r: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE],
        g: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE],
        b: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE],
        a: GeometryScriptBakeTypeOptions = [GeometryScriptBakeTypes.NONE
                                            ]) -> None
```

<a id="unreal.GeometryScriptBakeOutputType.output_mode"></a>

#### output_mode

```python
@property
def output_mode() -> GeometryScriptBakeOutputMode
```

(GeometryScriptBakeOutputMode):  [Read-Write] The bake output mode

<a id="unreal.GeometryScriptBakeOutputType.output_mode"></a>

#### output_mode

```python
@output_mode.setter
def output_mode(value: GeometryScriptBakeOutputMode) -> None
```

<a id="unreal.GeometryScriptBakeOutputType.rgba"></a>

#### rgba

```python
@property
def rgba() -> GeometryScriptBakeTypeOptions
```

(GeometryScriptBakeTypeOptions):  [Read-Write]

<a id="unreal.GeometryScriptBakeOutputType.rgba"></a>

#### rgba

```python
@rgba.setter
def rgba(value: GeometryScriptBakeTypeOptions) -> None
```

<a id="unreal.GeometryScriptBakeOutputType.r"></a>

#### r

```python
@property
def r() -> GeometryScriptBakeTypeOptions
```

(GeometryScriptBakeTypeOptions):  [Read-Write]

<a id="unreal.GeometryScriptBakeOutputType.r"></a>

#### r

```python
@r.setter
def r(value: GeometryScriptBakeTypeOptions) -> None
```

<a id="unreal.GeometryScriptBakeOutputType.g"></a>

#### g

```python
@property
def g() -> GeometryScriptBakeTypeOptions
```

(GeometryScriptBakeTypeOptions):  [Read-Write]

<a id="unreal.GeometryScriptBakeOutputType.g"></a>

#### g

```python
@g.setter
def g(value: GeometryScriptBakeTypeOptions) -> None
```

<a id="unreal.GeometryScriptBakeOutputType.b"></a>

#### b

```python
@property
def b() -> GeometryScriptBakeTypeOptions
```

(GeometryScriptBakeTypeOptions):  [Read-Write]

<a id="unreal.GeometryScriptBakeOutputType.b"></a>

#### b

```python
@b.setter
def b(value: GeometryScriptBakeTypeOptions) -> None
```

<a id="unreal.GeometryScriptBakeOutputType.a"></a>

#### a

```python
@property
def a() -> GeometryScriptBakeTypeOptions
```

(GeometryScriptBakeTypeOptions):  [Read-Write]

<a id="unreal.GeometryScriptBakeOutputType.a"></a>

#### a

```python
@a.setter
def a(value: GeometryScriptBakeTypeOptions) -> None
```

<a id="unreal.GeometryScriptBakeTargetMeshOptions"></a>