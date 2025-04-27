## AvaTextField Objects

```python
class AvaTextField(StructBase)
```

Ava Text Field

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheText
- **File**: AvaTextDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``count`` (int32):  [Read-Write]
- ``maximum_length`` (AvaTextLength):  [Read-Write]
- ``text`` (Text):  [Read-Write]
- ``text_case`` (AvaTextCase):  [Read-Write]

<a id="unreal.AvaTextField.__init__"></a>

#### __init__

```python
def __init__(text: Text = "",
             maximum_length: AvaTextLength = AvaTextLength.UNLIMITED,
             count: int = 0,
             text_case: AvaTextCase = AvaTextCase.REGULAR) -> None
```

<a id="unreal.AvaTextField.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write]

<a id="unreal.AvaTextField.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.AvaTextField.maximum_length"></a>

#### maximum_length

```python
@property
def maximum_length() -> AvaTextLength
```

(AvaTextLength):  [Read-Write]

<a id="unreal.AvaTextField.maximum_length"></a>

#### maximum_length

```python
@maximum_length.setter
def maximum_length(value: AvaTextLength) -> None
```

<a id="unreal.AvaTextField.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Write]

<a id="unreal.AvaTextField.count"></a>

#### count

```python
@count.setter
def count(value: int) -> None
```

<a id="unreal.AvaTextField.text_case"></a>

#### text_case

```python
@property
def text_case() -> AvaTextCase
```

(AvaTextCase):  [Read-Write]

<a id="unreal.AvaTextField.text_case"></a>

#### text_case

```python
@text_case.setter
def text_case(value: AvaTextCase) -> None
```

<a id="unreal.CEClonerGridConstraintSphere"></a>