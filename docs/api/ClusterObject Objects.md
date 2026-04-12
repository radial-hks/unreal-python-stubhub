## ClusterObject Objects

```python
class ClusterObject(Object)
```

Cluster Object

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ClusterObject.h

<a id="unreal.ClusterObject.start_cluster"></a>

#### start\_cluster

```python
def start_cluster(open_on_click: bool, aggregation_limit: int, url: str,
                  mode: str, algorithm_json_string: str,
                  filters_attribute_json_string: str) -> bool
```

x.start_cluster(open_on_click, aggregation_limit, url, mode, algorithm_json_string, filters_attribute_json_string) -> bool
Start Cluster

Args:
    open_on_click (bool): 
    aggregation_limit (int32): 
    url (str): 
    mode (str): 
    algorithm_json_string (str): 
    filters_attribute_json_string (str): 

Returns:
    bool:

<a id="unreal.ClusterObject.get"></a>

#### get

```python
@classmethod
def get(cls) -> ClusterObject
```

X.get() -> ClusterObject
Get

Returns:
    ClusterObject:

<a id="unreal.ClusterObject.end_cluster"></a>

#### end\_cluster

```python
def end_cluster() -> bool
```

x.end_cluster() -> bool
End Cluster

Returns:
    bool:

<a id="unreal.ColumnarHeatMapAPI"></a>