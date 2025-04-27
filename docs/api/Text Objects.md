## Text Objects

```python
class Text(_WrapperBase)
```

Type for all Unreal exposed text instances

<a id="unreal.Text.__init__"></a>

#### __init__

```python
def __init__(value: Union[Text, str] = "") -> None
```

<a id="unreal.Text.cast"></a>

#### cast

```python
@classmethod
def cast(cls, object: object) -> Text
```

cast(cls, object: object) -> Text -- cast the given object to this Unreal text type

<a id="unreal.Text.as_number"></a>

#### as_number

```python
@classmethod
def as_number(cls, num: float) -> Text
```

as_number(cls, num: float) -> Text -- convert the given number to a culture correct Unreal text representation

<a id="unreal.Text.as_percent"></a>

#### as_percent

```python
@classmethod
def as_percent(cls, num: float) -> Text
```

as_percent(cls, num: float) -> Text -- convert the given number to a culture correct Unreal text percentgage representation

<a id="unreal.Text.as_currency"></a>

#### as_currency

```python
@classmethod
def as_currency(cls, val: int, code: str) -> Text
```

as_currency(cls, val: int, code: str) -> Text -- convert the given number (specified in the smallest unit for the given currency i.e. 650 for $6.50) to a culture correct Unreal text currency representation

<a id="unreal.Text.is_empty"></a>

#### is_empty

```python
def is_empty() -> bool
```

is_empty(self) -> bool -- is this Unreal text empty?

<a id="unreal.Text.is_empty_or_whitespace"></a>

#### is_empty_or_whitespace

```python
def is_empty_or_whitespace() -> bool
```

is_empty_or_whitespace(self) -> bool -- is this Unreal text empty or only whitespace?

<a id="unreal.Text.is_transient"></a>

#### is_transient

```python
def is_transient() -> bool
```

is_transient(self) -> bool -- is this Unreal text transient?

<a id="unreal.Text.is_culture_invariant"></a>

#### is_culture_invariant

```python
def is_culture_invariant() -> bool
```

is_culture_invariant(self) -> bool -- is this Unreal text culture invariant?

<a id="unreal.Text.is_from_string_table"></a>

#### is_from_string_table

```python
def is_from_string_table() -> bool
```

is_from_string_table(self) -> bool -- is this Unreal text referencing a string table entry?

<a id="unreal.Text.to_lower"></a>

#### to_lower

```python
def to_lower() -> Text
```

to_lower(self) -> Text -- convert this Unreal text to lowercase in a culture correct way

<a id="unreal.Text.to_upper"></a>

#### to_upper

```python
def to_upper() -> Text
```

to_upper(self) -> Text -- convert this Unreal text to uppercase in a culture correct way

<a id="unreal.Text.format"></a>

#### format

```python
def format(*args: Union[Mapping[str, object], object],
           **named_args: object) -> Text
```

format(self, *args: Union[Mapping[str, object], object], **named_args: object) -> Text -- use this Unreal text as a format pattern and generate a new text using the format arguments (may be a mapping[arg_name, arg] or comma separed (optionally named) arguments)

<a id="unreal.Array"></a>