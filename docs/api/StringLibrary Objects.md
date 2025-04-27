## StringLibrary Objects

```python
class StringLibrary(BlueprintFunctionLibrary)
```

Kismet String Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetStringLibrary.h

<a id="unreal.StringLibrary.trim_trailing"></a>

#### trim_trailing

```python
@classmethod
def trim_trailing(cls, source_string: str) -> str
```

X.trim_trailing(source_string) -> str
Removes trailing whitespace characters

Args:
    source_string (str): 

Returns:
    str:

<a id="unreal.StringLibrary.trim"></a>

#### trim

```python
@classmethod
def trim(cls, source_string: str) -> str
```

X.trim(source_string) -> str
Removes whitespace characters from the front of this string.

Args:
    source_string (str): 

Returns:
    str:

<a id="unreal.StringLibrary.to_upper"></a>

#### to_upper

```python
@classmethod
def to_upper(cls, source_string: str) -> str
```

X.to_upper(source_string) -> str
Returns a string converted to Upper case

Args:
    source_string (str): The string to convert

Returns:
    str: The string in upper case

<a id="unreal.StringLibrary.to_lower"></a>

#### to_lower

```python
@classmethod
def to_lower(cls, source_string: str) -> str
```

X.to_lower(source_string) -> str
Returns a string converted to Lower case

Args:
    source_string (str): The string to convert

Returns:
    str: The string in lower case

<a id="unreal.StringLibrary.time_seconds_to_string"></a>

#### time_seconds_to_string

```python
@classmethod
def time_seconds_to_string(cls, seconds: float) -> str
```

X.time_seconds_to_string(seconds) -> str
Convert a number of seconds into minutes:seconds.milliseconds format string (including leading zeroes)

Args:
    seconds (float): 

Returns:
    str: A new string built from the seconds parameter

<a id="unreal.StringLibrary.starts_with"></a>

#### starts_with

```python
@classmethod
def starts_with(cls,
                source_string: str,
                prefix: str,
                search_case: SearchCase = SearchCase.IGNORE_CASE) -> bool
```

X.starts_with(source_string, prefix, search_case=SearchCase.IGNORE_CASE) -> bool
Test whether this string starts with given string.

Args:
    source_string (str): 
    prefix (str): 
    search_case (SearchCase): Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )

Returns:
    bool: true if this string begins with specified text, false otherwise

<a id="unreal.StringLibrary.split"></a>

#### split

```python
@classmethod
def split(
        cls,
        source_string: str,
        str: str,
        search_case: SearchCase = SearchCase.IGNORE_CASE,
        search_dir: SearchDir = SearchDir.FROM_START
) -> Optional[Tuple[str, str]]
```

X.split(source_string, str, search_case=SearchCase.IGNORE_CASE, search_dir=SearchDir.FROM_START) -> (left_s=str, right_s=str) or None
Splits this string at given string position case sensitive.

Args:
    source_string (str): 
    str (str): The string to search and split at
    search_case (SearchCase): Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )
    search_dir (SearchDir): Indicates whether the search starts at the begining or at the end ( defaults to ESearchDir::FromStart )

Returns:
    tuple or None: true if string is split, otherwise false

    left_s (str): out the string to the left of InStr, not updated if return is false

    right_s (str): out the string to the right of InStr, not updated if return is false

<a id="unreal.StringLibrary.right_pad"></a>

#### right_pad

```python
@classmethod
def right_pad(cls, source_string: str, ch_count: int) -> str
```

X.right_pad(source_string, ch_count) -> str
* Pad the right of this string for a specified number of characters
*

Args:
    source_string (str): The string to pad *
    ch_count (int32): Amount of padding required *

Returns:
    str: The padded string

<a id="unreal.StringLibrary.right_chop"></a>

#### right_chop

```python
@classmethod
def right_chop(cls, source_string: str, count: int) -> str
```

X.right_chop(source_string, count) -> str
Returns the string to the right of the specified location, counting forward from the left (from the beginning of the word).

Args:
    source_string (str): 
    count (int32): 

Returns:
    str:

<a id="unreal.StringLibrary.right"></a>

#### right

```python
@classmethod
def right(cls, source_string: str, count: int) -> str
```

X.right(source_string, count) -> str
Returns the string to the right of the specified location, counting back from the right (end of the word).

Args:
    source_string (str): 
    count (int32): 

Returns:
    str:

<a id="unreal.StringLibrary.reverse"></a>

#### reverse

```python
@classmethod
def reverse(cls, source_string: str) -> str
```

X.reverse(source_string) -> str
Returns a copy of this string, with the characters in reverse order

Args:
    source_string (str): 

Returns:
    str:

<a id="unreal.StringLibrary.replace_inline"></a>

#### replace_inline

```python
@classmethod
def replace_inline(
        cls,
        source_string: str,
        search_text: str,
        replacement_text: str,
        search_case: SearchCase = SearchCase.IGNORE_CASE) -> Tuple[int, str]
```

X.replace_inline(source_string, search_text, replacement_text, search_case=SearchCase.IGNORE_CASE) -> (int32, source_string=str)
Replace all occurrences of SearchText with ReplacementText in this string.

Args:
    source_string (str): 
    search_text (str): the text that should be removed from this string
    replacement_text (str): the text to insert in its place
    search_case (SearchCase): Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )

Returns:
    str: the number of occurrences of SearchText that were replaced.

    source_string (str):

<a id="unreal.StringLibrary.replace"></a>

#### replace

```python
@classmethod
def replace(cls,
            source_string: str,
            from_: str,
            to: str,
            search_case: SearchCase = SearchCase.IGNORE_CASE) -> str
```

X.replace(source_string, from_, to, search_case=SearchCase.IGNORE_CASE) -> str
Replace all occurrences of a substring in this string

Args:
    source_string (str): 
    from_ (str): substring to replace
    to (str): substring to replace From with
    search_case (SearchCase): Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )

Returns:
    str: a copy of this string with the replacement made

<a id="unreal.StringLibrary.parse_into_array"></a>

#### parse_into_array

```python
@classmethod
def parse_into_array(cls,
                     source_string: str,
                     delimiter: str = " ",
                     cull_empty_strings: bool = True) -> Array[str]
```

X.parse_into_array(source_string, delimiter=" ", cull_empty_strings=True) -> Array[str]
Gets an array of strings from a source string divided up by a separator and empty strings can optionally be culled.

Args:
    source_string (str): The string to chop up
    delimiter (str): The string to delimit on
    cull_empty_strings (bool): = true - Cull (true) empty strings or add them to the array (false)

Returns:
    Array[str]: The array of string that have been separated

<a id="unreal.StringLibrary.not_equal_str_str"></a>

#### not_equal_str_str

```python
@classmethod
def not_equal_str_str(cls, a: str, b: str) -> bool
```

X.not_equal_str_str(a, b) -> bool
Test if the input string are not equal (A != B)

Args:
    a (str): The string to compare against
    b (str): The string to compare

Returns:
    bool: Returns true if the input strings are not equal, false if they are equal

<a id="unreal.StringLibrary.not_equal_stri_stri"></a>

#### not_equal_stri_stri

```python
@classmethod
def not_equal_stri_stri(cls, a: str, b: str) -> bool
```

X.not_equal_stri_stri(a, b) -> bool
Test if the input string are not equal (A != B), ignoring case differences

Args:
    a (str): The string to compare against
    b (str): The string to compare

Returns:
    bool: Returns true if the input strings are not equal, false if they are equal

<a id="unreal.StringLibrary.mid"></a>

#### mid

```python
@classmethod
def mid(cls, source_string: str, start: int, count: int) -> str
```

X.mid(source_string, start, count) -> str
Returns the substring from Start position for Count characters.

Args:
    source_string (str): 
    start (int32): 
    count (int32): 

Returns:
    str:

<a id="unreal.StringLibrary.matches_wildcard"></a>

#### matches_wildcard

```python
@classmethod
def matches_wildcard(cls,
                     source_string: str,
                     wildcard: str,
                     search_case: SearchCase = SearchCase.IGNORE_CASE) -> bool
```

X.matches_wildcard(source_string, wildcard, search_case=SearchCase.IGNORE_CASE) -> bool
Searches this string for a given wild card
warning: This is a simple, SLOW routine. Use with caution

Args:
    source_string (str): 
    wildcard (str): *?-type wildcard
    search_case (SearchCase): Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )

Returns:
    bool: true if this string matches the *?-type wildcard given.

<a id="unreal.StringLibrary.len"></a>

#### len

```python
@classmethod
def len(cls, s: str) -> int
```

X.len(s) -> int32
Returns the number of characters in the string

Args:
    s (str): 

Returns:
    int32: The number of chars in the string

<a id="unreal.StringLibrary.left_pad"></a>

#### left_pad

```python
@classmethod
def left_pad(cls, source_string: str, ch_count: int) -> str
```

X.left_pad(source_string, ch_count) -> str
* Pad the left of this string for a specified number of characters
*

Args:
    source_string (str): The string to pad *
    ch_count (int32): Amount of padding required *

Returns:
    str: The padded string

<a id="unreal.StringLibrary.left_chop"></a>

#### left_chop

```python
@classmethod
def left_chop(cls, source_string: str, count: int) -> str
```

X.left_chop(source_string, count) -> str
Returns the left most characters from the string chopping the given number of characters from the end

Args:
    source_string (str): 
    count (int32): 

Returns:
    str:

<a id="unreal.StringLibrary.left"></a>

#### left

```python
@classmethod
def left(cls, source_string: str, count: int) -> str
```

X.left(source_string, count) -> str
Returns the left most given number of characters

Args:
    source_string (str): 
    count (int32): 

Returns:
    str:

<a id="unreal.StringLibrary.join_string_array"></a>

#### join_string_array

```python
@classmethod
def join_string_array(cls,
                      source_array: Array[str],
                      separator: str = " ") -> str
```

X.join_string_array(source_array, separator=" ") -> str
Concatenates an array of strings into a single string.

Args:
    source_array (Array[str]): The array of strings to concatenate.
    separator (str): The string used to separate each element.

Returns:
    str: The final, joined, separated string.

<a id="unreal.StringLibrary.is_numeric"></a>

#### is_numeric

```python
@classmethod
def is_numeric(cls, source_string: str) -> bool
```

X.is_numeric(source_string) -> bool
* Checks if a string contains only numeric characters
*

Args:
    source_string (str): The string to check *

Returns:
    bool: true if the string only contains numeric characters

<a id="unreal.StringLibrary.is_empty"></a>

#### is_empty

```python
@classmethod
def is_empty(cls, string: str) -> bool
```

X.is_empty(string) -> bool
Returns true if the string is empty

Args:
    string (str): The string to check

Returns:
    bool: Whether or not the string is empty

<a id="unreal.StringLibrary.get_substring"></a>

#### get_substring

```python
@classmethod
def get_substring(cls,
                  source_string: str,
                  start_index: int = 0,
                  length: int = 1) -> str
```

X.get_substring(source_string, start_index=0, length=1) -> str
Returns a substring from the string starting at the specified position

Args:
    source_string (str): The string to get the substring from
    start_index (int32): The location in SourceString to use as the start of the substring
    length (int32): The length of the requested substring

Returns:
    str: The requested substring

<a id="unreal.StringLibrary.get_character_as_number"></a>

#### get_character_as_number

```python
@classmethod
def get_character_as_number(cls, source_string: str, index: int = 0) -> int
```

X.get_character_as_number(source_string, index=0) -> int32
Gets a single character from the string (as an integer)

Args:
    source_string (str): The string to convert
    index (int32): Location of the character whose value is required

Returns:
    int32: The integer value of the character or 0 if index is out of range

<a id="unreal.StringLibrary.get_character_array_from_string"></a>

#### get_character_array_from_string

```python
@classmethod
def get_character_array_from_string(cls, source_string: str) -> Array[str]
```

X.get_character_array_from_string(source_string) -> Array[str]
Returns an array that contains one entry for each character in SourceString

Args:
    source_string (str): The string to break apart into characters

Returns:
    Array[str]: An array containing one entry for each character in SourceString

<a id="unreal.StringLibrary.find_substring"></a>

#### find_substring

```python
@classmethod
def find_substring(cls,
                   search_in: str,
                   substring: str,
                   use_case: bool = False,
                   search_from_end: bool = False,
                   start_position: int = -1) -> int
```

X.find_substring(search_in, substring, use_case=False, search_from_end=False, start_position=-1) -> int32
Finds the starting index of a substring in the a specified string

Args:
    search_in (str): The string to search within
    substring (str): The string to look for in the SearchIn string
    use_case (bool): Whether or not to be case-sensitive
    search_from_end (bool): Whether or not to start the search from the end of the string instead of the beginning
    start_position (int32): The position to start the search from

Returns:
    int32: The index (starting from 0 if bSearchFromEnd is false) of the first occurence of the substring

<a id="unreal.StringLibrary.equal_equal_str_str"></a>

#### equal_equal_str_str

```python
@classmethod
def equal_equal_str_str(cls, a: str, b: str) -> bool
```

X.equal_equal_str_str(a, b) -> bool
Test if the input strings are equal (A == B)

Args:
    a (str): The string to compare against
    b (str): The string to compare

Returns:
    bool: True if the strings are equal, false otherwise

<a id="unreal.StringLibrary.equal_equal_stri_stri"></a>

#### equal_equal_stri_stri

```python
@classmethod
def equal_equal_stri_stri(cls, a: str, b: str) -> bool
```

X.equal_equal_stri_stri(a, b) -> bool
Test if the input strings are equal (A == B), ignoring case

Args:
    a (str): The string to compare against
    b (str): The string to compare

Returns:
    bool: True if the strings are equal, false otherwise

<a id="unreal.StringLibrary.ends_with"></a>

#### ends_with

```python
@classmethod
def ends_with(cls,
              source_string: str,
              suffix: str,
              search_case: SearchCase = SearchCase.IGNORE_CASE) -> bool
```

X.ends_with(source_string, suffix, search_case=SearchCase.IGNORE_CASE) -> bool
Test whether this string ends with given string.

Args:
    source_string (str): 
    suffix (str): 
    search_case (SearchCase): Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase )

Returns:
    bool: true if this string ends with specified text, false otherwise

<a id="unreal.StringLibrary.cull_array"></a>

#### cull_array

```python
@classmethod
def cull_array(cls, source_string: str) -> Tuple[int, Array[str]]
```

X.cull_array(source_string) -> (int32, array=Array[str])
Takes an array of strings and removes any zero length entries.

Args:
    source_string (str): 

Returns:
    Array[str]: The number of elements left in InArray

    array (Array[str]): The array to cull

<a id="unreal.StringLibrary.conv_vector_to_string"></a>

#### conv_vector_to_string

```python
@classmethod
def conv_vector_to_string(cls, vec: Vector) -> str
```

X.conv_vector_to_string(vec) -> str
Converts a vector value to a string, in the form 'X= Y= Z='

Args:
    vec (Vector): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_vector3f_to_string"></a>

#### conv_vector3f_to_string

```python
@classmethod
def conv_vector3f_to_string(cls, vec: Vector3f) -> str
```

X.conv_vector3f_to_string(vec) -> str
Converts a float vector value to a string, in the form 'X= Y= Z='

Args:
    vec (Vector3f): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_vector2d_to_string"></a>

#### conv_vector2d_to_string

```python
@classmethod
def conv_vector2d_to_string(cls, vec: Vector2D) -> str
```

X.conv_vector2d_to_string(vec) -> str
Converts a vector2d value to a string, in the form 'X= Y='

Args:
    vec (Vector2D): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_transform_to_string"></a>

#### conv_transform_to_string

```python
@classmethod
def conv_transform_to_string(cls, trans: Transform) -> str
```

X.conv_transform_to_string(trans) -> str
Converts a transform value to a string, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

Args:
    trans (Transform): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_string_to_vector3f"></a>

#### conv_string_to_vector3f

```python
@classmethod
def conv_string_to_vector3f(cls, string: str) -> Tuple[Vector3f, bool]
```

X.conv_string_to_vector3f(string) -> (out_converted_vector=Vector3f, out_is_valid=bool)
Convert String Back To Float Vector. IsValid indicates whether or not the string could be successfully converted.

Args:
    string (str): 

Returns:
    tuple: 

    out_converted_vector (Vector3f): 

    out_is_valid (bool):

<a id="unreal.StringLibrary.conv_string_to_vector2d"></a>

#### conv_string_to_vector2d

```python
@classmethod
def conv_string_to_vector2d(cls, string: str) -> Tuple[Vector2D, bool]
```

X.conv_string_to_vector2d(string) -> (out_converted_vector2d=Vector2D, out_is_valid=bool)
Convert String Back To Vector2D. IsValid indicates whether or not the string could be successfully converted.

Args:
    string (str): 

Returns:
    tuple: 

    out_converted_vector2d (Vector2D): 

    out_is_valid (bool):

<a id="unreal.StringLibrary.conv_string_to_vector"></a>

#### conv_string_to_vector

```python
@classmethod
def conv_string_to_vector(cls, string: str) -> Tuple[Vector, bool]
```

X.conv_string_to_vector(string) -> (out_converted_vector=Vector, out_is_valid=bool)
Convert String Back To Vector. IsValid indicates whether or not the string could be successfully converted.

Args:
    string (str): 

Returns:
    tuple: 

    out_converted_vector (Vector): 

    out_is_valid (bool):

<a id="unreal.StringLibrary.conv_string_to_rotator"></a>

#### conv_string_to_rotator

```python
@classmethod
def conv_string_to_rotator(cls, string: str) -> Tuple[Rotator, bool]
```

X.conv_string_to_rotator(string) -> (out_converted_rotator=Rotator, out_is_valid=bool)
Convert String Back To Rotator. IsValid indicates whether or not the string could be successfully converted.

Args:
    string (str): 

Returns:
    tuple: 

    out_converted_rotator (Rotator): 

    out_is_valid (bool):

<a id="unreal.StringLibrary.conv_string_to_name"></a>

#### conv_string_to_name

```python
@classmethod
def conv_string_to_name(cls, string: str) -> Name
```

X.conv_string_to_name(string) -> Name
Converts a string to a name value

Args:
    string (str): 

Returns:
    Name:

<a id="unreal.StringLibrary.conv_string_to_int64"></a>

#### conv_string_to_int64

```python
@classmethod
def conv_string_to_int64(cls, string: str) -> int
```

X.conv_string_to_int64(string) -> int64
Converts a string to a int value

Args:
    string (str): 

Returns:
    int64:

<a id="unreal.StringLibrary.conv_string_to_int"></a>

#### conv_string_to_int

```python
@classmethod
def conv_string_to_int(cls, string: str) -> int
```

X.conv_string_to_int(string) -> int32
Converts a string to a int value

Args:
    string (str): 

Returns:
    int32:

<a id="unreal.StringLibrary.conv_string_to_double"></a>

#### conv_string_to_double

```python
@classmethod
def conv_string_to_double(cls, string: str) -> float
```

X.conv_string_to_double(string) -> double
Converts a string to a double value

Args:
    string (str): 

Returns:
    double:

<a id="unreal.StringLibrary.conv_string_to_float"></a>

#### conv_string_to_float

```python
@classmethod
def conv_string_to_float(cls, string: str) -> float
```

deprecated: 'conv_string_to_float' was renamed to 'conv_string_to_double'.

<a id="unreal.StringLibrary.conv_string_to_color"></a>

#### conv_string_to_color

```python
@classmethod
def conv_string_to_color(cls, string: str) -> Tuple[LinearColor, bool]
```

X.conv_string_to_color(string) -> (out_converted_color=LinearColor, out_is_valid=bool)
Convert String Back To Color. IsValid indicates whether or not the string could be successfully converted.

Args:
    string (str): 

Returns:
    tuple: 

    out_converted_color (LinearColor): 

    out_is_valid (bool):

<a id="unreal.StringLibrary.conv_rotator_to_string"></a>

#### conv_rotator_to_string

```python
@classmethod
def conv_rotator_to_string(cls, rot: Rotator) -> str
```

X.conv_rotator_to_string(rot) -> str
Converts a rotator value to a string, in the form 'P= Y= R='

Args:
    rot (Rotator): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_platform_user_id_to_string"></a>

#### conv_platform_user_id_to_string

```python
@classmethod
def conv_platform_user_id_to_string(cls,
                                    platform_user_id: PlatformUserId) -> str
```

X.conv_platform_user_id_to_string(platform_user_id) -> str
Converts a PlatformUserId value to a string

Args:
    platform_user_id (PlatformUserId): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_object_to_string"></a>

#### conv_object_to_string

```python
@classmethod
def conv_object_to_string(cls, obj: Object) -> str
```

X.conv_object_to_string(obj) -> str
Converts a UObject value to a string by calling the object's GetName method

Args:
    obj (Object): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_name_to_string"></a>

#### conv_name_to_string

```python
@classmethod
def conv_name_to_string(cls, name: Name) -> str
```

X.conv_name_to_string(name) -> str
Converts a name value to a string

Args:
    name (Name): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_matrix_to_string"></a>

#### conv_matrix_to_string

```python
@classmethod
def conv_matrix_to_string(cls, matrix: Matrix) -> str
```

X.conv_matrix_to_string(matrix) -> str
Converts a name value to a string

Args:
    matrix (Matrix): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_int_vector_to_string"></a>

#### conv_int_vector_to_string

```python
@classmethod
def conv_int_vector_to_string(cls, int_vec: IntVector) -> str
```

X.conv_int_vector_to_string(int_vec) -> str
Converts an IntVector value to a string, in the form 'X= Y= Z='

Args:
    int_vec (IntVector): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_int_to_string"></a>

#### conv_int_to_string

```python
@classmethod
def conv_int_to_string(cls, int: int) -> str
```

X.conv_int_to_string(int) -> str
Converts an integer value to a string

Args:
    int (int32): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_int_point_to_string"></a>

#### conv_int_point_to_string

```python
@classmethod
def conv_int_point_to_string(cls, int_point: IntPoint) -> str
```

X.conv_int_point_to_string(int_point) -> str
Converts an IntPoint value to a string, in the form 'X= Y='

Args:
    int_point (IntPoint): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_int64_to_string"></a>

#### conv_int64_to_string

```python
@classmethod
def conv_int64_to_string(cls, int: int) -> str
```

X.conv_int64_to_string(int) -> str
Converts an 64-bit integer value to a string

Args:
    int (int64): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_input_device_id_to_string"></a>

#### conv_input_device_id_to_string

```python
@classmethod
def conv_input_device_id_to_string(cls, device_id: InputDeviceId) -> str
```

X.conv_input_device_id_to_string(device_id) -> str
Converts a InputDeviceId value to a string

Args:
    device_id (InputDeviceId): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_double_to_string"></a>

#### conv_double_to_string

```python
@classmethod
def conv_double_to_string(cls, double: float) -> str
```

X.conv_double_to_string(double) -> str
Converts a double value to a string

Args:
    double (double): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_float_to_string"></a>

#### conv_float_to_string

```python
@classmethod
def conv_float_to_string(cls, double: float) -> str
```

deprecated: 'conv_float_to_string' was renamed to 'conv_double_to_string'.

<a id="unreal.StringLibrary.conv_color_to_string"></a>

#### conv_color_to_string

```python
@classmethod
def conv_color_to_string(cls, color: LinearColor) -> str
```

X.conv_color_to_string(color) -> str
Converts a linear color value to a string, in the form '(R=,G=,B=,A=)'

Args:
    color (LinearColor): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_byte_to_string"></a>

#### conv_byte_to_string

```python
@classmethod
def conv_byte_to_string(cls, byte: int) -> str
```

X.conv_byte_to_string(byte) -> str
Converts a byte value to a string

Args:
    byte (uint8): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_box_to_string"></a>

#### conv_box_to_string

```python
@classmethod
def conv_box_to_string(cls, box: Box) -> str
```

X.conv_box_to_string(box) -> str
Converts a FBox value to a string

Args:
    box (Box): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_box_center_and_extents_to_string"></a>

#### conv_box_center_and_extents_to_string

```python
@classmethod
def conv_box_center_and_extents_to_string(cls, box: Box) -> str
```

X.conv_box_center_and_extents_to_string(box) -> str
Converts a FBox value to a string of its Center and Extents values.

Args:
    box (Box): 

Returns:
    str:

<a id="unreal.StringLibrary.conv_bool_to_string"></a>

#### conv_bool_to_string

```python
@classmethod
def conv_bool_to_string(cls, bool: bool) -> str
```

X.conv_bool_to_string(bool) -> str
Converts a boolean value to a string, either 'true' or 'false'

Args:
    bool (bool): 

Returns:
    str:

<a id="unreal.StringLibrary.contains"></a>

#### contains

```python
@classmethod
def contains(cls,
             search_in: str,
             substring: str,
             use_case: bool = False,
             search_from_end: bool = False) -> bool
```

X.contains(search_in, substring, use_case=False, search_from_end=False) -> bool
Returns whether this string contains the specified substring.

Args:
    search_in (str): 
    substring (str): 
    use_case (bool): 
    search_from_end (bool): 

Returns:
    bool: Returns whether the string contains the substring

<a id="unreal.StringLibrary.concat_str_str"></a>

#### concat_str_str

```python
@classmethod
def concat_str_str(cls, a: str, b: str) -> str
```

X.concat_str_str(a, b) -> str
Concatenates two strings together to make a new string

Args:
    a (str): The original string
    b (str): The string to append to A

Returns:
    str: A new string which is the concatenation of A+B

<a id="unreal.StringLibrary.build_string_vector2d"></a>

#### build_string_vector2d

```python
@classmethod
def build_string_vector2d(cls, append_to: str, prefix: str, vector2d: Vector2D,
                          suffix: str) -> str
```

X.build_string_vector2d(append_to, prefix, vector2d, suffix) -> str
Converts a vector2d->string, creating a new string in the form AppendTo+Prefix+InVector2d+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    vector2d (Vector2D): The vector2d value to convert. Uses the standard FVector2D::ToString conversion
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_vector"></a>

#### build_string_vector

```python
@classmethod
def build_string_vector(cls, append_to: str, prefix: str, vector: Vector,
                        suffix: str) -> str
```

X.build_string_vector(append_to, prefix, vector, suffix) -> str
Converts a vector->string, creating a new string in the form AppendTo+Prefix+InVector+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    vector (Vector): The vector value to convert. Uses the standard FVector::ToString conversion
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_rotator"></a>

#### build_string_rotator

```python
@classmethod
def build_string_rotator(cls, append_to: str, prefix: str, rot: Rotator,
                         suffix: str) -> str
```

X.build_string_rotator(append_to, prefix, rot, suffix) -> str
Converts a rotator->string, creating a new string in the form AppendTo+Prefix+InRot+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    rot (Rotator): The rotator value to convert. Uses the standard ToString conversion
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_object"></a>

#### build_string_object

```python
@classmethod
def build_string_object(cls, append_to: str, prefix: str, obj: Object,
                        suffix: str) -> str
```

X.build_string_object(append_to, prefix, obj, suffix) -> str
Converts a object->string, creating a new string in the form AppendTo+Prefix+object name+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    obj (Object): The object to convert. Will insert the name of the object into the conversion string
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_name"></a>

#### build_string_name

```python
@classmethod
def build_string_name(cls, append_to: str, prefix: str, name: Name,
                      suffix: str) -> str
```

X.build_string_name(append_to, prefix, name, suffix) -> str
Converts a color->string, creating a new string in the form AppendTo+Prefix+InName+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    name (Name): The name value to convert
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_int_vector"></a>

#### build_string_int_vector

```python
@classmethod
def build_string_int_vector(cls, append_to: str, prefix: str,
                            int_vector: IntVector, suffix: str) -> str
```

X.build_string_int_vector(append_to, prefix, int_vector, suffix) -> str
Converts an IntVector->string, creating a new string in the form AppendTo+Prefix+InIntVector+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    int_vector (IntVector): The intVector value to convert. Uses the standard FVector::ToString conversion
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_int"></a>

#### build_string_int

```python
@classmethod
def build_string_int(cls, append_to: str, prefix: str, int: int,
                     suffix: str) -> str
```

X.build_string_int(append_to, prefix, int, suffix) -> str
Converts a int->string, creating a new string in the form AppendTo+Prefix+InInt+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    int (int32): The int value to convert
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_double"></a>

#### build_string_double

```python
@classmethod
def build_string_double(cls, append_to: str, prefix: str, double: float,
                        suffix: str) -> str
```

X.build_string_double(append_to, prefix, double, suffix) -> str
Converts a double->string, create a new string in the form AppendTo+Prefix+InDouble+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    double (double): The double value to convert
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_float"></a>

#### build_string_float

```python
@classmethod
def build_string_float(cls, append_to: str, prefix: str, double: float,
                       suffix: str) -> str
```

deprecated: 'build_string_float' was renamed to 'build_string_double'.

<a id="unreal.StringLibrary.build_string_color"></a>

#### build_string_color

```python
@classmethod
def build_string_color(cls, append_to: str, prefix: str, color: LinearColor,
                       suffix: str) -> str
```

X.build_string_color(append_to, prefix, color, suffix) -> str
Converts a color->string, creating a new string in the form AppendTo+Prefix+InColor+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    color (LinearColor): The linear color value to convert. Uses the standard ToString conversion
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringLibrary.build_string_bool"></a>

#### build_string_bool

```python
@classmethod
def build_string_bool(cls, append_to: str, prefix: str, bool: bool,
                      suffix: str) -> str
```

X.build_string_bool(append_to, prefix, bool, suffix) -> str
Converts a boolean->string, creating a new string in the form AppendTo+Prefix+InBool+Suffix

Args:
    append_to (str): An existing string to use as the start of the conversion string
    prefix (str): A string to use as a prefix, after the AppendTo string
    bool (bool): The bool value to convert. Will add "true" or "false" to the conversion string
    suffix (str): A suffix to append to the end of the conversion string

Returns:
    str: A new string built from the passed parameters

<a id="unreal.StringTableLibrary"></a>