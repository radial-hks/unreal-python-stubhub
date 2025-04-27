## PolyglotTextData Objects

```python
class PolyglotTextData(StructBase)
```

Polyglot data that may be registered to the text localization manager at runtime.
note: This struct is mirrored in PolyglotTextData.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (LocalizedTextSourceCategory):  [Read-Write] The category of this polyglot data.
  note: This affects when and how the data is loaded into the text localization manager.
- ``is_minimal_patch`` (bool):  [Read-Write] True if this polyglot data is a minimal patch, and that missing translations should be
  ignored (falling back to any LocRes data) rather than falling back to the native string.
- ``key`` (str):  [Read-Write] The key of the text created from this polyglot data.
  note: This must not be empty.
- ``localized_strings`` (Map[str, str]):  [Read-Write] Mapping between a culture code and its localized string.
  note: The native culture may also have a translation in this map.
- ``namespace`` (str):  [Read-Write] The namespace of the text created from this polyglot data.
  note: This may be empty.
- ``native_culture`` (str):  [Read-Write] The native culture of this polyglot data.
  note: This may be empty, and if empty, will be inferred from the native culture of the text category.
- ``native_string`` (str):  [Read-Write] The native string for this polyglot data.
  note: This must not be empty (it should be the same as the originally authored text you are trying to replace).

<a id="unreal.PolyglotTextData.__init__"></a>

#### __init__

```python
def __init__(
        category: LocalizedTextSourceCategory = LocalizedTextSourceCategory.
    GAME,
        native_culture: str = "",
        namespace: str = "",
        key: str = "",
        native_string: str = "",
        localized_strings: Map[str, str] = {},
        is_minimal_patch: bool = False) -> None
```

<a id="unreal.PolyglotTextData.category"></a>

#### category

```python
@property
def category() -> LocalizedTextSourceCategory
```

(LocalizedTextSourceCategory):  [Read-Write] The category of this polyglot data.
note: This affects when and how the data is loaded into the text localization manager.

<a id="unreal.PolyglotTextData.category"></a>

#### category

```python
@category.setter
def category(value: LocalizedTextSourceCategory) -> None
```

<a id="unreal.PolyglotTextData.native_culture"></a>

#### native_culture

```python
@property
def native_culture() -> str
```

(str):  [Read-Write] The native culture of this polyglot data.
note: This may be empty, and if empty, will be inferred from the native culture of the text category.

<a id="unreal.PolyglotTextData.native_culture"></a>

#### native_culture

```python
@native_culture.setter
def native_culture(value: str) -> None
```

<a id="unreal.PolyglotTextData.namespace"></a>

#### namespace

```python
@property
def namespace() -> str
```

(str):  [Read-Write] The namespace of the text created from this polyglot data.
note: This may be empty.

<a id="unreal.PolyglotTextData.namespace"></a>

#### namespace

```python
@namespace.setter
def namespace(value: str) -> None
```

<a id="unreal.PolyglotTextData.key"></a>

#### key

```python
@property
def key() -> str
```

(str):  [Read-Write] The key of the text created from this polyglot data.
note: This must not be empty.

<a id="unreal.PolyglotTextData.key"></a>

#### key

```python
@key.setter
def key(value: str) -> None
```

<a id="unreal.PolyglotTextData.native_string"></a>

#### native_string

```python
@property
def native_string() -> str
```

(str):  [Read-Write] The native string for this polyglot data.
note: This must not be empty (it should be the same as the originally authored text you are trying to replace).

<a id="unreal.PolyglotTextData.native_string"></a>

#### native_string

```python
@native_string.setter
def native_string(value: str) -> None
```

<a id="unreal.PolyglotTextData.localized_strings"></a>

#### localized_strings

```python
@property
def localized_strings() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] Mapping between a culture code and its localized string.
note: The native culture may also have a translation in this map.

<a id="unreal.PolyglotTextData.localized_strings"></a>

#### localized_strings

```python
@localized_strings.setter
def localized_strings(value: Map[str, str]) -> None
```

<a id="unreal.PolyglotTextData.is_minimal_patch"></a>

#### is_minimal_patch

```python
@property
def is_minimal_patch() -> bool
```

(bool):  [Read-Write] True if this polyglot data is a minimal patch, and that missing translations should be
ignored (falling back to any LocRes data) rather than falling back to the native string.

<a id="unreal.PolyglotTextData.is_minimal_patch"></a>

#### is_minimal_patch

```python
@is_minimal_patch.setter
def is_minimal_patch(value: bool) -> None
```

<a id="unreal.PrimaryAssetId"></a>