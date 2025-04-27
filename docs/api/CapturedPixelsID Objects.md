## CapturedPixelsID Objects

```python
class CapturedPixelsID(StructBase)
```

Structure used as an identifier for a particular buffer within a capture.

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: UserDefinedCaptureProtocol.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``identifiers`` (Map[Name, Name]):  [Read-Write] Map of identifiers to their values for this ID.

<a id="unreal.CapturedPixelsID.__init__"></a>

#### __init__

```python
def __init__(identifiers: Map[Name, Name] = {}) -> None
```

<a id="unreal.CapturedPixelsID.identifiers"></a>

#### identifiers

```python
@property
def identifiers() -> Map[Name, Name]
```

(Map[Name, Name]):  [Read-Write] Map of identifiers to their values for this ID.

<a id="unreal.CapturedPixelsID.identifiers"></a>

#### identifiers

```python
@identifiers.setter
def identifiers(value: Map[Name, Name]) -> None
```

<a id="unreal.CapturedPixels"></a>