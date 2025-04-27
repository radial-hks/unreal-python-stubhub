## KismetArrayLibrary Objects

```python
class KismetArrayLibrary(BlueprintFunctionLibrary)
```

Kismet Array Library

**C++ Source:**

- **Module**: Engine
- **File**: KismetArrayLibrary.h

<a id="unreal.KismetArrayLibrary.sort_string_array"></a>

#### sort_string_array

```python
@classmethod
def sort_string_array(
        cls,
        target_array: Array[str],
        stable_sort: bool = False,
        sort_order: ArraySortOrder = ArraySortOrder.ASCENDING) -> Array[str]
```

X.sort_string_array(target_array, stable_sort=False, sort_order=ArraySortOrder.ASCENDING) -> Array[str]
Sorts an array of strings alphabetically.

Args:
    target_array (Array[str]): The array to sort.
    stable_sort (bool): If a stable sort should be used. This preserves the order of identical elements, but is slower.
    sort_order (ArraySortOrder): If the array should be sorted in ascending or descending order.

Returns:
    Array[str]: 

    target_array (Array[str]): The array to sort.

<a id="unreal.KismetArrayLibrary.sort_name_array"></a>

#### sort_name_array

```python
@classmethod
def sort_name_array(
        cls,
        target_array: Array[Name],
        stable_sort: bool = False,
        lexical_sort: bool = True,
        sort_order: ArraySortOrder = ArraySortOrder.ASCENDING) -> Array[Name]
```

X.sort_name_array(target_array, stable_sort=False, lexical_sort=True, sort_order=ArraySortOrder.ASCENDING) -> Array[Name]
Sorts an array of FNames.

Args:
    target_array (Array[Name]): The array to sort.
    stable_sort (bool): If a stable sort should be used. This preserves the order of identical elements, but is slower.
    lexical_sort (bool): If the names should be sorted based on the string value of the name rather than the comparison index. This is slower when enabled.
    sort_order (ArraySortOrder): If the array should be sorted in ascending or descending order.

Returns:
    Array[Name]: 

    target_array (Array[Name]): The array to sort.

<a id="unreal.KismetArrayLibrary.sort_int_array"></a>

#### sort_int_array

```python
@classmethod
def sort_int_array(
        cls,
        target_array: Array[int],
        stable_sort: bool = False,
        sort_order: ArraySortOrder = ArraySortOrder.ASCENDING) -> Array[int]
```

X.sort_int_array(target_array, stable_sort=False, sort_order=ArraySortOrder.ASCENDING) -> Array[int32]
Sorts an array of integers.

Args:
    target_array (Array[int32]): The array to sort.
    stable_sort (bool): If a stable sort should be used. This preserves the order of identical elements, but is slower.
    sort_order (ArraySortOrder): If the array should be sorted in ascending or descending order.

Returns:
    Array[int32]: 

    target_array (Array[int32]): The array to sort.

<a id="unreal.KismetArrayLibrary.sort_int64_array"></a>

#### sort_int64_array

```python
@classmethod
def sort_int64_array(
        cls,
        target_array: Array[int],
        stable_sort: bool = False,
        sort_order: ArraySortOrder = ArraySortOrder.ASCENDING) -> Array[int]
```

X.sort_int64_array(target_array, stable_sort=False, sort_order=ArraySortOrder.ASCENDING) -> Array[int64]
Sorts an array of 64-bit integers.

Args:
    target_array (Array[int64]): The array to sort.
    stable_sort (bool): If a stable sort should be used. This preserves the order of identical elements, but is slower.
    sort_order (ArraySortOrder): If the array should be sorted in ascending or descending order.

Returns:
    Array[int64]: 

    target_array (Array[int64]): The array to sort.

<a id="unreal.KismetArrayLibrary.sort_float_array"></a>

#### sort_float_array

```python
@classmethod
def sort_float_array(
        cls,
        target_array: Array[float],
        stable_sort: bool = False,
        sort_order: ArraySortOrder = ArraySortOrder.ASCENDING) -> Array[float]
```

X.sort_float_array(target_array, stable_sort=False, sort_order=ArraySortOrder.ASCENDING) -> Array[double]
Sorts an array of doubles.

Args:
    target_array (Array[double]): The array to sort.
    stable_sort (bool): If a stable sort should be used. This preserves the order of identical elements, but is slower.
    sort_order (ArraySortOrder): If the array should be sorted in ascending or descending order.

Returns:
    Array[double]: 

    target_array (Array[double]): The array to sort.

<a id="unreal.KismetArrayLibrary.sort_byte_array"></a>

#### sort_byte_array

```python
@classmethod
def sort_byte_array(
        cls,
        target_array: Array[int],
        stable_sort: bool = False,
        sort_order: ArraySortOrder = ArraySortOrder.ASCENDING) -> Array[int]
```

X.sort_byte_array(target_array, stable_sort=False, sort_order=ArraySortOrder.ASCENDING) -> Array[uint8]
Sorts an array of bytes.

Args:
    target_array (Array[uint8]): The array to sort.
    stable_sort (bool): If a stable sort should be used. This preserves the order of identical elements, but is slower.
    sort_order (ArraySortOrder): If the array should be sorted in ascending or descending order.

Returns:
    Array[uint8]: 

    target_array (Array[uint8]): The array to sort.

<a id="unreal.KismetArrayLibrary.filter_array"></a>

#### filter_array

```python
@classmethod
def filter_array(cls, target_array: Array[Actor],
                 filter_class: Class) -> Array[Actor]
```

X.filter_array(target_array, filter_class) -> Array[Actor]
*Filter an array based on a Class derived from Actor.
*
*

Args:
    target_array (Array[Actor]): The array to filter from *
    filter_class (type(Class)): The Actor sub-class type that acts as the filter, only objects derived from it will be returned. *

Returns:
    Array[Actor]: 

    filtered_array (Array[Actor]):

<a id="unreal.GuidLibrary"></a>