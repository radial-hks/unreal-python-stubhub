## CompassSource Objects

```python
class CompassSource(StructBase)
```

Compass Source

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CompassAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bg`` (str):  [Read-Write]
- ``needle`` (str):  [Read-Write] = TEXT("http:superapi.51aes.com/doc-static/images/static/Compass/Compass.png");

<a id="unreal.CompassSource.__init__"></a>

#### \_\_init\_\_

```python
def __init__(bg: str = "", needle: str = "") -> None
```

<a id="unreal.CompassSource.bg"></a>

#### bg

```python
@property
def bg() -> str
```

(str):  [Read-Write]

<a id="unreal.CompassSource.bg"></a>

#### bg

```python
@bg.setter
def bg(value: str) -> None
```

<a id="unreal.CompassSource.needle"></a>

#### needle

```python
@property
def needle() -> str
```

(str):  [Read-Write] = TEXT("http:superapi.51aes.com/doc-static/images/static/Compass/Compass.png");

<a id="unreal.CompassSource.needle"></a>

#### needle

```python
@needle.setter
def needle(value: str) -> None
```

<a id="unreal.CompassDisplay"></a>