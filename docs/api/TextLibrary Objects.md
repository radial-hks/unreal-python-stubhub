## TextLibrary Objects

```python
class TextLibrary(BlueprintFunctionLibrary)
```

Kismet Text Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetTextLibrary.h

<a id="unreal.TextLibrary.text_trim_trailing"></a>

#### text_trim_trailing

```python
@classmethod
def text_trim_trailing(cls, text: Text) -> Text
```

X.text_trim_trailing(text) -> Text
Removes trailing whitespace characters.

Args:
    text (Text): 

Returns:
    Text:

<a id="unreal.TextLibrary.text_trim_preceding_and_trailing"></a>

#### text_trim_preceding_and_trailing

```python
@classmethod
def text_trim_preceding_and_trailing(cls, text: Text) -> Text
```

X.text_trim_preceding_and_trailing(text) -> Text
Removes whitespace characters from the front and end of the text.

Args:
    text (Text): 

Returns:
    Text:

<a id="unreal.TextLibrary.text_trim_preceding"></a>

#### text_trim_preceding

```python
@classmethod
def text_trim_preceding(cls, text: Text) -> Text
```

X.text_trim_preceding(text) -> Text
Removes whitespace characters from the front of the text.

Args:
    text (Text): 

Returns:
    Text:

<a id="unreal.TextLibrary.text_to_upper"></a>

#### text_to_upper

```python
@classmethod
def text_to_upper(cls, text: Text) -> Text
```

X.text_to_upper(text) -> Text
Transforms the text to uppercase in a culture correct way.
note: The returned instance is linked to the original and will be rebuilt if the active culture is changed.

Args:
    text (Text): 

Returns:
    Text:

<a id="unreal.TextLibrary.text_to_lower"></a>

#### text_to_lower

```python
@classmethod
def text_to_lower(cls, text: Text) -> Text
```

X.text_to_lower(text) -> Text
Transforms the text to lowercase in a culture correct way.
note: The returned instance is linked to the original and will be rebuilt if the active culture is changed.

Args:
    text (Text): 

Returns:
    Text:

<a id="unreal.TextLibrary.text_is_transient"></a>

#### text_is_transient

```python
@classmethod
def text_is_transient(cls, text: Text) -> bool
```

X.text_is_transient(text) -> bool
Returns true if text is transient.

Args:
    text (Text): 

Returns:
    bool:

<a id="unreal.TextLibrary.text_is_from_string_table"></a>

#### text_is_from_string_table

```python
@classmethod
def text_is_from_string_table(cls, text: Text) -> bool
```

X.text_is_from_string_table(text) -> bool
Returns true if the given text is referencing a string table.

Args:
    text (Text): 

Returns:
    bool:

<a id="unreal.TextLibrary.text_is_empty"></a>

#### text_is_empty

```python
@classmethod
def text_is_empty(cls, text: Text) -> bool
```

X.text_is_empty(text) -> bool
Returns true if text is empty.

Args:
    text (Text): 

Returns:
    bool:

<a id="unreal.TextLibrary.text_is_culture_invariant"></a>

#### text_is_culture_invariant

```python
@classmethod
def text_is_culture_invariant(cls, text: Text) -> bool
```

X.text_is_culture_invariant(text) -> bool
Returns true if text is culture invariant.

Args:
    text (Text): 

Returns:
    bool:

<a id="unreal.TextLibrary.text_from_string_table"></a>

#### text_from_string_table

```python
@classmethod
def text_from_string_table(cls, table_id: Name, key: str) -> Text
```

X.text_from_string_table(table_id, key) -> Text
Attempts to create a text instance from a string table ID and key.
note: This exists to allow programmatic look-up of a string table entry from dynamic content - you should favor setting your string table reference on a text property or pin wherever possible as it is significantly more robust (see "Make Literal Text").

Args:
    table_id (Name): 
    key (str): 

Returns:
    Text: The found text, or a dummy text if the entry could not be found.

<a id="unreal.TextLibrary.string_table_id_and_key_from_text"></a>

#### string_table_id_and_key_from_text

```python
@classmethod
def string_table_id_and_key_from_text(
        cls, text: Text) -> Optional[Tuple[Name, str]]
```

X.string_table_id_and_key_from_text(text) -> (out_table_id=Name, out_key=str) or None
Attempts to get the String Table ID and key used by the given text.

Args:
    text (Text): 

Returns:
    tuple or None: True if the String Table ID and key were found, false otherwise.

    out_table_id (Name): 

    out_key (str):

<a id="unreal.TextLibrary.polyglot_data_to_text"></a>

#### polyglot_data_to_text

```python
@classmethod
def polyglot_data_to_text(cls, polyglot_data: PolyglotTextData) -> Text
```

X.polyglot_data_to_text(polyglot_data) -> Text
Get the text instance created from this polyglot data.

Args:
    polyglot_data (PolyglotTextData): 

Returns:
    Text: The text instance, or an empty text if the data is invalid.

<a id="unreal.TextLibrary.not_equal_text_text"></a>

#### not_equal_text_text

```python
@classmethod
def not_equal_text_text(cls, a: Text, b: Text) -> bool
```

X.not_equal_text_text(a, b) -> bool
Returns true if A and B are linguistically not equal (A != B).

Args:
    a (Text): 
    b (Text): 

Returns:
    bool:

<a id="unreal.TextLibrary.not_equal_ignore_case_text_text"></a>

#### not_equal_ignore_case_text_text

```python
@classmethod
def not_equal_ignore_case_text_text(cls, a: Text, b: Text) -> bool
```

X.not_equal_ignore_case_text_text(a, b) -> bool
Returns true if A and B are linguistically not equal (A != B), ignoring case.

Args:
    a (Text): 
    b (Text): 

Returns:
    bool:

<a id="unreal.TextLibrary.make_invariant_text"></a>

#### make_invariant_text

```python
@classmethod
def make_invariant_text(cls, string: str) -> Text
```

X.make_invariant_text(string) -> Text
Converts string to culture invariant text. Use 'Make Literal Text' to create localizable text, or 'Format' if concatenating localized text

Args:
    string (str): 

Returns:
    Text:

<a id="unreal.TextLibrary.is_polyglot_data_valid"></a>

#### is_polyglot_data_valid

```python
@classmethod
def is_polyglot_data_valid(
        cls, polyglot_data: PolyglotTextData) -> Tuple[bool, Text]
```

X.is_polyglot_data_valid(polyglot_data) -> (is_valid=bool, error_message=Text)
Check whether the given polyglot data is valid.

Args:
    polyglot_data (PolyglotTextData): 

Returns:
    tuple: 

    is_valid (bool): 

    error_message (Text):

<a id="unreal.TextLibrary.get_text_source_string"></a>

#### get_text_source_string

```python
@classmethod
def get_text_source_string(cls, text: Text) -> str
```

X.get_text_source_string(text) -> str
Get the (non-localized) source string of the given text.
note: For a generated text (eg, the result of a Format), this will deep build the source string as if the generation had run for the native language.

Args:
    text (Text): 

Returns:
    str:

<a id="unreal.TextLibrary.get_text_id"></a>

#### get_text_id

```python
@classmethod
def get_text_id(cls, text: Text) -> Optional[Tuple[str, str]]
```

X.get_text_id(text) -> (out_namespace=str, out_key=str) or None
Attempts to get the ID (namespace and key) used by the given text.

Args:
    text (Text): 

Returns:
    tuple or None: True if the namespace (which may be empty) and key were found, false otherwise.

    out_namespace (str): 

    out_key (str):

<a id="unreal.TextLibrary.get_empty_text"></a>

#### get_empty_text

```python
@classmethod
def get_empty_text(cls) -> Text
```

X.get_empty_text() -> Text
Returns an empty piece of text.

Returns:
    Text:

<a id="unreal.TextLibrary.find_text_in_live_table_advanced"></a>

#### find_text_in_live_table_advanced

```python
@classmethod
def find_text_in_live_table_advanced(
        cls,
        namespace: str,
        key: str,
        source_string: str = "") -> Optional[Text]
```

X.find_text_in_live_table_advanced(namespace, key, source_string="") -> Text or None
=== !! This is an ADVANCED function. USE WITH CAUTION !! ===

Attempt to dynamically reference an EXISTING Text via its active display string in the live table.
Note: This can ONLY find text that is currently localized (gathered, translated, and has an active display string in TextLocalizationManager). If you need to find a localizable but untranslated text, see 'Make Literal Text'.
Note: Direct dynamic references to Text are EXTREMELY FRAGILE, and you may want to use a string table instead!

Args:
    namespace (str): The namespace of the text to find (if any).
    key (str): The key of the text to find.
    source_string (str): If set (not empty) then the found text must also have been created from this source string.

Returns:
    Text or None: 

    out_text (Text):

<a id="unreal.TextLibrary.equal_equal_text_text"></a>

#### equal_equal_text_text

```python
@classmethod
def equal_equal_text_text(cls, a: Text, b: Text) -> bool
```

X.equal_equal_text_text(a, b) -> bool
Returns true if A and B are linguistically equal (A == B).

Args:
    a (Text): 
    b (Text): 

Returns:
    bool:

<a id="unreal.TextLibrary.equal_equal_ignore_case_text_text"></a>

#### equal_equal_ignore_case_text_text

```python
@classmethod
def equal_equal_ignore_case_text_text(cls, a: Text, b: Text) -> bool
```

X.equal_equal_ignore_case_text_text(a, b) -> bool
Returns true if A and B are linguistically equal (A == B), ignoring case.

Args:
    a (Text): 
    b (Text): 

Returns:
    bool:

<a id="unreal.TextLibrary.conv_vector_to_text"></a>

#### conv_vector_to_text

```python
@classmethod
def conv_vector_to_text(cls, vec: Vector) -> Text
```

X.conv_vector_to_text(vec) -> Text
Converts a vector value to localized formatted text, in the form 'X= Y= Z='

Args:
    vec (Vector): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_vector2d_to_text"></a>

#### conv_vector2d_to_text

```python
@classmethod
def conv_vector2d_to_text(cls, vec: Vector2D) -> Text
```

X.conv_vector2d_to_text(vec) -> Text
Converts a vector2d value to localized formatted text, in the form 'X= Y='

Args:
    vec (Vector2D): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_transform_to_text"></a>

#### conv_transform_to_text

```python
@classmethod
def conv_transform_to_text(cls, trans: Transform) -> Text
```

X.conv_transform_to_text(trans) -> Text
Converts a transform value to localized formatted text, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

Args:
    trans (Transform): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_text_to_string"></a>

#### conv_text_to_string

```python
@classmethod
def conv_text_to_string(cls, text: Text) -> str
```

X.conv_text_to_string(text) -> str
Converts localizable text to the string

Args:
    text (Text): 

Returns:
    str:

<a id="unreal.TextLibrary.conv_string_to_text"></a>

#### conv_string_to_text

```python
@classmethod
def conv_string_to_text(cls, string: str) -> Text
```

X.conv_string_to_text(string) -> Text
Converts string to culture invariant text. Use 'Make Literal Text' to create localizable text, or 'Format' if concatenating localized text

Args:
    string (str): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_rotator_to_text"></a>

#### conv_rotator_to_text

```python
@classmethod
def conv_rotator_to_text(cls, rot: Rotator) -> Text
```

X.conv_rotator_to_text(rot) -> Text
Converts a rotator value to localized formatted text, in the form 'P= Y= R='

Args:
    rot (Rotator): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_object_to_text"></a>

#### conv_object_to_text

```python
@classmethod
def conv_object_to_text(cls, obj: Object) -> Text
```

X.conv_object_to_text(obj) -> Text
Converts a UObject value to culture invariant text by calling the object's GetName method

Args:
    obj (Object): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_name_to_text"></a>

#### conv_name_to_text

```python
@classmethod
def conv_name_to_text(cls, name: Name) -> Text
```

X.conv_name_to_text(name) -> Text
Converts Name to culture invariant text

Args:
    name (Name): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_int_to_text"></a>

#### conv_int_to_text

```python
@classmethod
def conv_int_to_text(cls,
                     value: int,
                     always_sign: bool = False,
                     use_grouping: bool = True,
                     minimum_integral_digits: int = 1,
                     maximum_integral_digits: int = 324) -> Text
```

X.conv_int_to_text(value, always_sign=False, use_grouping=True, minimum_integral_digits=1, maximum_integral_digits=324) -> Text
Converts a passed in integer to text based on formatting options

Args:
    value (int32): 
    always_sign (bool): 
    use_grouping (bool): 
    minimum_integral_digits (int32): 
    maximum_integral_digits (int32): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_int64_to_text"></a>

#### conv_int64_to_text

```python
@classmethod
def conv_int64_to_text(cls,
                       value: int,
                       always_sign: bool = False,
                       use_grouping: bool = True,
                       minimum_integral_digits: int = 1,
                       maximum_integral_digits: int = 324) -> Text
```

X.conv_int64_to_text(value, always_sign=False, use_grouping=True, minimum_integral_digits=1, maximum_integral_digits=324) -> Text
Converts a passed in integer to text based on formatting options

Args:
    value (int64): 
    always_sign (bool): 
    use_grouping (bool): 
    minimum_integral_digits (int32): 
    maximum_integral_digits (int32): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_double_to_text"></a>

#### conv_double_to_text

```python
@classmethod
def conv_double_to_text(cls,
                        value: float,
                        rounding_mode: RoundingMode,
                        always_sign: bool = False,
                        use_grouping: bool = True,
                        minimum_integral_digits: int = 1,
                        maximum_integral_digits: int = 324,
                        minimum_fractional_digits: int = 0,
                        maximum_fractional_digits: int = 3) -> Text
```

X.conv_double_to_text(value, rounding_mode, always_sign=False, use_grouping=True, minimum_integral_digits=1, maximum_integral_digits=324, minimum_fractional_digits=0, maximum_fractional_digits=3) -> Text
Converts a passed in double to text based on formatting options

Args:
    value (double): 
    rounding_mode (RoundingMode): 
    always_sign (bool): 
    use_grouping (bool): 
    minimum_integral_digits (int32): 
    maximum_integral_digits (int32): 
    minimum_fractional_digits (int32): 
    maximum_fractional_digits (int32): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_float_to_text"></a>

#### conv_float_to_text

```python
@classmethod
def conv_float_to_text(cls,
                       value: float,
                       rounding_mode: RoundingMode,
                       always_sign: bool = False,
                       use_grouping: bool = True,
                       minimum_integral_digits: int = 1,
                       maximum_integral_digits: int = 324,
                       minimum_fractional_digits: int = 0,
                       maximum_fractional_digits: int = 3) -> Text
```

deprecated: 'conv_float_to_text' was renamed to 'conv_double_to_text'.

<a id="unreal.TextLibrary.conv_color_to_text"></a>

#### conv_color_to_text

```python
@classmethod
def conv_color_to_text(cls, color: LinearColor) -> Text
```

X.conv_color_to_text(color) -> Text
Converts a linear color value to localized formatted text, in the form '(R=,G=,B=,A=)'

Args:
    color (LinearColor): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_byte_to_text"></a>

#### conv_byte_to_text

```python
@classmethod
def conv_byte_to_text(cls, value: int) -> Text
```

X.conv_byte_to_text(value) -> Text
Converts a byte value to formatted text

Args:
    value (uint8): 

Returns:
    Text:

<a id="unreal.TextLibrary.conv_bool_to_text"></a>

#### conv_bool_to_text

```python
@classmethod
def conv_bool_to_text(cls, bool: bool) -> Text
```

X.conv_bool_to_text(bool) -> Text
Converts a boolean value to formatted text, either 'true' or 'false'

Args:
    bool (bool): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_time_zone_time_date_time"></a>

#### as_time_zone_time_date_time

```python
@classmethod
def as_time_zone_time_date_time(
        cls,
        date_time: DateTime,
        time_zone: str = "",
        time_style: DateTimeStyle = DateTimeStyle.DEFAULT) -> Text
```

X.as_time_zone_time_date_time(date_time, time_zone="", time_style=DateTimeStyle.DEFAULT) -> Text
Converts a passed in date & time to a text, formatted as a time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

Args:
    date_time (DateTime): 
    time_zone (str): 
    time_style (DateTimeStyle): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_time_zone_date_time_date_time"></a>

#### as_time_zone_date_time_date_time

```python
@classmethod
def as_time_zone_date_time_date_time(
        cls,
        date_time: DateTime,
        time_zone: str = "",
        date_style: DateTimeStyle = DateTimeStyle.DEFAULT,
        time_style: DateTimeStyle = DateTimeStyle.DEFAULT) -> Text
```

X.as_time_zone_date_time_date_time(date_time, time_zone="", date_style=DateTimeStyle.DEFAULT, time_style=DateTimeStyle.DEFAULT) -> Text
Converts a passed in date & time to a text, formatted as a date & time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

Args:
    date_time (DateTime): 
    time_zone (str): 
    date_style (DateTimeStyle): 
    time_style (DateTimeStyle): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_time_zone_date_date_time"></a>

#### as_time_zone_date_date_time

```python
@classmethod
def as_time_zone_date_date_time(
        cls,
        date_time: DateTime,
        time_zone: str = "",
        date_style: DateTimeStyle = DateTimeStyle.DEFAULT) -> Text
```

X.as_time_zone_date_date_time(date_time, time_zone="", date_style=DateTimeStyle.DEFAULT) -> Text
Converts a passed in date & time to a text, formatted as a date using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

Args:
    date_time (DateTime): 
    time_zone (str): 
    date_style (DateTimeStyle): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_timespan_timespan"></a>

#### as_timespan_timespan

```python
@classmethod
def as_timespan_timespan(cls, timespan: Timespan) -> Text
```

X.as_timespan_timespan(timespan) -> Text
Converts a passed in time span to a text, formatted as a time span

Args:
    timespan (Timespan): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_time_date_time"></a>

#### as_time_date_time

```python
@classmethod
def as_time_date_time(
        cls,
        in_: DateTime,
        time_style: DateTimeStyle = DateTimeStyle.DEFAULT) -> Text
```

X.as_time_date_time(in_, time_style=DateTimeStyle.DEFAULT) -> Text
Converts a passed in date & time to a text, formatted as a time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

Args:
    in_ (DateTime): 
    time_style (DateTimeStyle): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_percent_float"></a>

#### as_percent_float

```python
@classmethod
def as_percent_float(cls,
                     value: float,
                     rounding_mode: RoundingMode,
                     always_sign: bool = False,
                     use_grouping: bool = True,
                     minimum_integral_digits: int = 1,
                     maximum_integral_digits: int = 324,
                     minimum_fractional_digits: int = 0,
                     maximum_fractional_digits: int = 3) -> Text
```

X.as_percent_float(value, rounding_mode, always_sign=False, use_grouping=True, minimum_integral_digits=1, maximum_integral_digits=324, minimum_fractional_digits=0, maximum_fractional_digits=3) -> Text
Converts a passed in float to a text, formatted as a percent

Args:
    value (float): 
    rounding_mode (RoundingMode): 
    always_sign (bool): 
    use_grouping (bool): 
    minimum_integral_digits (int32): 
    maximum_integral_digits (int32): 
    minimum_fractional_digits (int32): 
    maximum_fractional_digits (int32): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_memory"></a>

#### as_memory

```python
@classmethod
def as_memory(cls,
              num_bytes: int,
              unit_standard: MemoryUnitStandard = MemoryUnitStandard.IEC,
              use_grouping: bool = True,
              minimum_integral_digits: int = 1,
              maximum_integral_digits: int = 324,
              minimum_fractional_digits: int = 0,
              maximum_fractional_digits: int = 3) -> Text
```

X.as_memory(num_bytes, unit_standard=MemoryUnitStandard.IEC, use_grouping=True, minimum_integral_digits=1, maximum_integral_digits=324, minimum_fractional_digits=0, maximum_fractional_digits=3) -> Text
Generate an FText that represents the passed number as a memory size in the current culture

Args:
    num_bytes (int64): 
    unit_standard (MemoryUnitStandard): 
    use_grouping (bool): 
    minimum_integral_digits (int32): 
    maximum_integral_digits (int32): 
    minimum_fractional_digits (int32): 
    maximum_fractional_digits (int32): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_date_time_date_time"></a>

#### as_date_time_date_time

```python
@classmethod
def as_date_time_date_time(
        cls,
        in_: DateTime,
        date_style: DateTimeStyle = DateTimeStyle.DEFAULT,
        time_style: DateTimeStyle = DateTimeStyle.DEFAULT) -> Text
```

X.as_date_time_date_time(in_, date_style=DateTimeStyle.DEFAULT, time_style=DateTimeStyle.DEFAULT) -> Text
Converts a passed in date & time to a text, formatted as a date & time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

Args:
    in_ (DateTime): 
    date_style (DateTimeStyle): 
    time_style (DateTimeStyle): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_date_date_time"></a>

#### as_date_date_time

```python
@classmethod
def as_date_date_time(
        cls,
        date_time: DateTime,
        date_style: DateTimeStyle = DateTimeStyle.DEFAULT) -> Text
```

X.as_date_date_time(date_time, date_style=DateTimeStyle.DEFAULT) -> Text
Converts a passed in date & time to a text, formatted as a date using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

Args:
    date_time (DateTime): 
    date_style (DateTimeStyle): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_currency_base"></a>

#### as_currency_base

```python
@classmethod
def as_currency_base(cls, base_value: int, currency_code: str) -> Text
```

X.as_currency_base(base_value, currency_code) -> Text
Generate an FText that represents the passed number as currency in the current culture.
BaseVal is specified in the smallest fractional value of the currency and will be converted for formatting according to the selected culture.
Keep in mind the CurrencyCode is completely independent of the culture it's displayed in (and they do not imply one another).
For example: FText::AsCurrencyBase(650, TEXT("EUR")); would return an FText of "<EUR>6.50" in most English cultures (en_US/en_UK) and "6,50<EUR>" in Spanish (es_ES) (where <EUR> is U+20AC)

Args:
    base_value (int32): 
    currency_code (str): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_currency_integer"></a>

#### as_currency_integer

```python
@classmethod
def as_currency_integer(cls,
                        value: int,
                        rounding_mode: RoundingMode,
                        always_sign: bool = False,
                        use_grouping: bool = True,
                        minimum_integral_digits: int = 1,
                        maximum_integral_digits: int = 324,
                        minimum_fractional_digits: int = 0,
                        maximum_fractional_digits: int = 3,
                        currency_code: str = "") -> Text
```

X.as_currency_integer(value, rounding_mode, always_sign=False, use_grouping=True, minimum_integral_digits=1, maximum_integral_digits=324, minimum_fractional_digits=0, maximum_fractional_digits=3, currency_code="") -> Text
Converts a passed in integer to a text formatted as a currency

Args:
    value (int32): 
    rounding_mode (RoundingMode): 
    always_sign (bool): 
    use_grouping (bool): 
    minimum_integral_digits (int32): 
    maximum_integral_digits (int32): 
    minimum_fractional_digits (int32): 
    maximum_fractional_digits (int32): 
    currency_code (str): 

Returns:
    Text:

<a id="unreal.TextLibrary.as_currency_float"></a>

#### as_currency_float

```python
@classmethod
def as_currency_float(cls,
                      value: float,
                      rounding_mode: RoundingMode,
                      always_sign: bool = False,
                      use_grouping: bool = True,
                      minimum_integral_digits: int = 1,
                      maximum_integral_digits: int = 324,
                      minimum_fractional_digits: int = 0,
                      maximum_fractional_digits: int = 3,
                      currency_code: str = "") -> Text
```

X.as_currency_float(value, rounding_mode, always_sign=False, use_grouping=True, minimum_integral_digits=1, maximum_integral_digits=324, minimum_fractional_digits=0, maximum_fractional_digits=3, currency_code="") -> Text
Converts a passed in float to a text formatted as a currency

Args:
    value (float): 
    rounding_mode (RoundingMode): 
    always_sign (bool): 
    use_grouping (bool): 
    minimum_integral_digits (int32): 
    maximum_integral_digits (int32): 
    minimum_fractional_digits (int32): 
    maximum_fractional_digits (int32): 
    currency_code (str): 

Returns:
    Text:

<a id="unreal.LevelStreaming"></a>