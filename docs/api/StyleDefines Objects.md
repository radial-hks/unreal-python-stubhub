## StyleDefines Objects

```python
class StyleDefines(StructBase)
```

Style Defines

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISStyleTypeDef.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``line_material_path`` (str):  [Read-Write]
- ``polygon_material_path`` (str):  [Read-Write] 支持透明度表达
- ``texture_path`` (str):  [Read-Write]

<a id="unreal.StyleDefines.__init__"></a>

#### \_\_init\_\_

```python
def __init__(polygon_material_path: str = "",
             line_material_path: str = "",
             texture_path: str = "") -> None
```

<a id="unreal.StyleDefines.polygon_material_path"></a>

#### polygon\_material\_path

```python
@property
def polygon_material_path() -> str
```

(str):  [Read-Write] 支持透明度表达

<a id="unreal.StyleDefines.polygon_material_path"></a>

#### polygon\_material\_path

```python
@polygon_material_path.setter
def polygon_material_path(value: str) -> None
```

<a id="unreal.StyleDefines.line_material_path"></a>

#### line\_material\_path

```python
@property
def line_material_path() -> str
```

(str):  [Read-Write]

<a id="unreal.StyleDefines.line_material_path"></a>

#### line\_material\_path

```python
@line_material_path.setter
def line_material_path(value: str) -> None
```

<a id="unreal.StyleDefines.texture_path"></a>

#### texture\_path

```python
@property
def texture_path() -> str
```

(str):  [Read-Write]

<a id="unreal.StyleDefines.texture_path"></a>

#### texture\_path

```python
@texture_path.setter
def texture_path(value: str) -> None
```

<a id="unreal.WMSLayerDefine"></a>