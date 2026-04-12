## DCPCommonLibrary Objects

```python
class DCPCommonLibrary(BlueprintFunctionLibrary)
```

DCPCommon Library

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPCommonLibrary.h

<a id="unreal.DCPCommonLibrary.is_point_in_range"></a>

#### is\_point\_in\_range

```python
@classmethod
def is_point_in_range(cls, range_points: Array[Vector2D],
                      test_point: Vector2D) -> bool
```

X.is_point_in_range(range_points, test_point) -> bool
Is Point in Range

Args:
    range_points (Array[Vector2D]): 
    test_point (Vector2D): 

Returns:
    bool:

<a id="unreal.DCPCommonLibrary.get_wdp_pawn"></a>

#### get\_wdp\_pawn

```python
@classmethod
def get_wdp_pawn(cls) -> WdpBasePawn
```

X.get_wdp_pawn() -> WdpBasePawn
Get Wdp Pawn

Returns:
    WdpBasePawn:

<a id="unreal.DCPCommonLibrary.get_file_from_dir_recursively"></a>

#### get\_file\_from\_dir\_recursively

```python
@classmethod
def get_file_from_dir_recursively(cls,
                                  in_dir: str,
                                  file_type: str = "*.uasset") -> Array[str]
```

X.get_file_from_dir_recursively(in_dir, file_type="*.uasset") -> Array[str]
Get File from Dir Recursively

Args:
    in_dir (str): 
    file_type (str): 

Returns:
    Array[str]:

<a id="unreal.DCPCommonLibrary.get_file_from_dir"></a>

#### get\_file\_from\_dir

```python
@classmethod
def get_file_from_dir(cls,
                      in_dir: str,
                      file_type: str = "*.uasset") -> Array[str]
```

X.get_file_from_dir(in_dir, file_type="*.uasset") -> Array[str]
Get File from Dir

Args:
    in_dir (str): 
    file_type (str): 

Returns:
    Array[str]:

<a id="unreal.DCPCommonLibrary.get_dir_from_path_recursively"></a>

#### get\_dir\_from\_path\_recursively

```python
@classmethod
def get_dir_from_path_recursively(cls, in_path: str) -> Array[str]
```

X.get_dir_from_path_recursively(in_path) -> Array[str]
Get Dir from Path Recursively

Args:
    in_path (str): 

Returns:
    Array[str]:

<a id="unreal.DCPCommonLibrary.get_dir_from_path"></a>

#### get\_dir\_from\_path

```python
@classmethod
def get_dir_from_path(cls, in_path: str) -> Array[str]
```

X.get_dir_from_path(in_path) -> Array[str]
Get Dir from Path

Args:
    in_path (str): 

Returns:
    Array[str]:

<a id="unreal.DCPCommonLibrary.get_dcp_content_path"></a>

#### get\_dcp\_content\_path

```python
@classmethod
def get_dcp_content_path(cls) -> str
```

X.get_dcp_content_path() -> str
Get DCPContent Path

Returns:
    str:

<a id="unreal.DCPCommonLibrary.get_bim_snap_result"></a>

#### get\_bim\_snap\_result

```python
@classmethod
def get_bim_snap_result(
        cls, need_snap_type: Array[BimSnapType]) -> Optional[BimSnapResult]
```

X.get_bim_snap_result(need_snap_type) -> BimSnapResult or None
Get Bim Snap Result

Args:
    need_snap_type (Array[BimSnapType]): 

Returns:
    BimSnapResult or None: 

    out_bim_snap_result (BimSnapResult):

<a id="unreal.DCPCoreManager"></a>