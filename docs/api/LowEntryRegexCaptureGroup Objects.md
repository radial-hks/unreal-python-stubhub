## LowEntryRegexCaptureGroup Objects

```python
class LowEntryRegexCaptureGroup(StructBase)
```

Low Entry Regex Capture Group

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: FLowEntryRegexCaptureGroup.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``begin_index`` (int32):  [Read-Write] This is the start index of the capture group match.
- ``capture_group_number`` (int32):  [Read-Write] This is the number of the capture group, starting with 1.
- ``end_index`` (int32):  [Read-Write] This is the end index of the capture group match.
- ``match`` (str):  [Read-Write] This is the text of the capture group match.

<a id="unreal.LowEntryRegexCaptureGroup.__init__"></a>

#### \_\_init\_\_

```python
def __init__(capture_group_number: int = 0,
             begin_index: int = 0,
             end_index: int = 0,
             match: str = "") -> None
```

<a id="unreal.LowEntryRegexCaptureGroup.capture_group_number"></a>

#### capture\_group\_number

```python
@property
def capture_group_number() -> int
```

(int32):  [Read-Write] This is the number of the capture group, starting with 1.

<a id="unreal.LowEntryRegexCaptureGroup.capture_group_number"></a>

#### capture\_group\_number

```python
@capture_group_number.setter
def capture_group_number(value: int) -> None
```

<a id="unreal.LowEntryRegexCaptureGroup.begin_index"></a>

#### begin\_index

```python
@property
def begin_index() -> int
```

(int32):  [Read-Write] This is the start index of the capture group match.

<a id="unreal.LowEntryRegexCaptureGroup.begin_index"></a>

#### begin\_index

```python
@begin_index.setter
def begin_index(value: int) -> None
```

<a id="unreal.LowEntryRegexCaptureGroup.end_index"></a>

#### end\_index

```python
@property
def end_index() -> int
```

(int32):  [Read-Write] This is the end index of the capture group match.

<a id="unreal.LowEntryRegexCaptureGroup.end_index"></a>

#### end\_index

```python
@end_index.setter
def end_index(value: int) -> None
```

<a id="unreal.LowEntryRegexCaptureGroup.match"></a>

#### match

```python
@property
def match() -> str
```

(str):  [Read-Write] This is the text of the capture group match.

<a id="unreal.LowEntryRegexCaptureGroup.match"></a>

#### match

```python
@match.setter
def match(value: str) -> None
```

<a id="unreal.LowEntryRegexMatch"></a>