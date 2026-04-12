## FontParameterValue Objects

```python
class FontParameterValue(StructBase)
```

Editable font parameter.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``font_page`` (int32):  [Read-Write]
- ``font_value`` (Font):  [Read-Write]
- ``parameter_info`` (MaterialParameterInfo):  [Read-Write]

<a id="unreal.FontParameterValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(parameter_info: MaterialParameterInfo = [
    "None", MaterialParameterAssociation.GLOBAL_PARAMETER, -1
],
             font_value: Font = None,
             font_page: int = 0) -> None
```

<a id="unreal.FontParameterValue.parameter_info"></a>

#### parameter\_info

```python
@property
def parameter_info() -> MaterialParameterInfo
```

(MaterialParameterInfo):  [Read-Write]

<a id="unreal.FontParameterValue.parameter_info"></a>

#### parameter\_info

```python
@parameter_info.setter
def parameter_info(value: MaterialParameterInfo) -> None
```

<a id="unreal.FontParameterValue.font_value"></a>

#### font\_value

```python
@property
def font_value() -> Font
```

(Font):  [Read-Write]

<a id="unreal.FontParameterValue.font_value"></a>

#### font\_value

```python
@font_value.setter
def font_value(value: Font) -> None
```

<a id="unreal.FontParameterValue.font_page"></a>

#### font\_page

```python
@property
def font_page() -> int
```

(int32):  [Read-Write]

<a id="unreal.FontParameterValue.font_page"></a>

#### font\_page

```python
@font_page.setter
def font_page(value: int) -> None
```

<a id="unreal.UserSceneTextureOverride"></a>