## custompoiStyle\_label Objects

```python
class custompoiStyle_label(StructBase)
```

Custompoi Style Label

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CustomPoiAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bg_image_url`` (str):  [Read-Write]
- ``bg_offset`` (Vector2D):  [Read-Write]
- ``bg_size`` (Vector2D):  [Read-Write]
- ``content`` (custompoiStyle_label_content):  [Read-Write]

<a id="unreal.custompoiStyle_label.__init__"></a>

#### \_\_init\_\_

```python
def __init__(bg_image_url: str = "",
             bg_size: Vector2D = [0.000000, 0.000000],
             bg_offset: Vector2D = [0.000000, 0.000000],
             content: custompoiStyle_label_content = ["", "", 0]) -> None
```

<a id="unreal.custompoiStyle_label.bg_image_url"></a>

#### bg\_image\_url

```python
@property
def bg_image_url() -> str
```

(str):  [Read-Write]

<a id="unreal.custompoiStyle_label.bg_image_url"></a>

#### bg\_image\_url

```python
@bg_image_url.setter
def bg_image_url(value: str) -> None
```

<a id="unreal.custompoiStyle_label.bg_size"></a>

#### bg\_size

```python
@property
def bg_size() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.custompoiStyle_label.bg_size"></a>

#### bg\_size

```python
@bg_size.setter
def bg_size(value: Vector2D) -> None
```

<a id="unreal.custompoiStyle_label.bg_offset"></a>

#### bg\_offset

```python
@property
def bg_offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.custompoiStyle_label.bg_offset"></a>

#### bg\_offset

```python
@bg_offset.setter
def bg_offset(value: Vector2D) -> None
```

<a id="unreal.custompoiStyle_label.content"></a>

#### content

```python
@property
def content() -> custompoiStyle_label_content
```

(custompoiStyle_label_content):  [Read-Write]

<a id="unreal.custompoiStyle_label.content"></a>

#### content

```python
@content.setter
def content(value: custompoiStyle_label_content) -> None
```

<a id="unreal.custompoiStyle"></a>