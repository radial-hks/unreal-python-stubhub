## InterchangeSourceData Objects

```python
class InterchangeSourceData(Object)
```

* Helper class to be able to read different source data
* File on disk
* HTTP URL (TODO)
* Memory buffer (TODO)
* Stream (TODO)

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangeSourceData.h

<a id="unreal.InterchangeSourceData.set_filename"></a>

#### set_filename

```python
def set_filename(filename: str) -> bool
```

x.set_filename(filename) -> bool
Set Filename

Args:
    filename (str): 

Returns:
    bool:

<a id="unreal.InterchangeSourceData.get_filename"></a>

#### get_filename

```python
def get_filename() -> str
```

x.get_filename() -> str
Get Filename

Returns:
    str:

<a id="unreal.InterchangeWriterBase"></a>