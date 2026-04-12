## LowEntryRegexMatch Objects

```python
class LowEntryRegexMatch(StructBase)
```

Low Entry Regex Match

**C++ Source:**

- **Plugin**: LowEntryExtStdLib
- **Module**: LowEntryExtendedStandardLibrary
- **File**: FLowEntryRegexMatch.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``begin_index`` (int32):  [Read-Write] This is the start index of the match.
- ``capture_groups`` (Array[LowEntryRegexCaptureGroup]):  [Read-Write] These are the capture group matches of the match.
- ``end_index`` (int32):  [Read-Write] This is the end index of the match.
- ``match`` (str):  [Read-Write] This is the text of the match.
- ``match_number`` (int32):  [Read-Write] This is the number of the match, starting with 1.

<a id="unreal.LowEntryRegexMatch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(match_number: int = 0,
             begin_index: int = 0,
             end_index: int = 0,
             match: str = "",
             capture_groups: Array[LowEntryRegexCaptureGroup] = []) -> None
```

<a id="unreal.LowEntryRegexMatch.match_number"></a>

#### match\_number

```python
@property
def match_number() -> int
```

(int32):  [Read-Write] This is the number of the match, starting with 1.

<a id="unreal.LowEntryRegexMatch.match_number"></a>

#### match\_number

```python
@match_number.setter
def match_number(value: int) -> None
```

<a id="unreal.LowEntryRegexMatch.begin_index"></a>

#### begin\_index

```python
@property
def begin_index() -> int
```

(int32):  [Read-Write] This is the start index of the match.

<a id="unreal.LowEntryRegexMatch.begin_index"></a>

#### begin\_index

```python
@begin_index.setter
def begin_index(value: int) -> None
```

<a id="unreal.LowEntryRegexMatch.end_index"></a>

#### end\_index

```python
@property
def end_index() -> int
```

(int32):  [Read-Write] This is the end index of the match.

<a id="unreal.LowEntryRegexMatch.end_index"></a>

#### end\_index

```python
@end_index.setter
def end_index(value: int) -> None
```

<a id="unreal.LowEntryRegexMatch.match"></a>

#### match

```python
@property
def match() -> str
```

(str):  [Read-Write] This is the text of the match.

<a id="unreal.LowEntryRegexMatch.match"></a>

#### match

```python
@match.setter
def match(value: str) -> None
```

<a id="unreal.LowEntryRegexMatch.capture_groups"></a>

#### capture\_groups

```python
@property
def capture_groups() -> Array[LowEntryRegexCaptureGroup]
```

(Array[LowEntryRegexCaptureGroup]):  [Read-Write] These are the capture group matches of the match.

<a id="unreal.LowEntryRegexMatch.capture_groups"></a>

#### capture\_groups

```python
@capture_groups.setter
def capture_groups(value: Array[LowEntryRegexCaptureGroup]) -> None
```

<a id="unreal.ConstantQResults"></a>