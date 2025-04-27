## MovieGraphEvaluatedConfig Objects

```python
class MovieGraphEvaluatedConfig(Object)
```

An evaluated config for the current frame. Each named branch (including Globals) has its own
copy of the config, fully resolved (so there is no need to check the Globals branch when
looking at a named branch). You can use the functions to fetch a node by type from a given
branch and it will return the right object (or the CDO if the node is NOT in the config).

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphConfig.h

<a id="unreal.MovieGraphEvaluatedConfig.get_settings_for_branch"></a>

#### get_settings_for_branch

```python
def get_settings_for_branch(
        class_: Class,
        branch_name: Name,
        include_cd_os: bool = True,
        exact_match: bool = False) -> Array[MovieGraphSettingNode]
```

x.get_settings_for_branch(class_, branch_name, include_cd_os=True, exact_match=False) -> Array[MovieGraphSettingNode]
Get Settings for Branch

Args:
    class_ (type(Class)): 
    branch_name (Name): 
    include_cd_os (bool): 
    exact_match (bool): 

Returns:
    Array[MovieGraphSettingNode]:

<a id="unreal.MovieGraphEvaluatedConfig.get_setting_for_branch"></a>

#### get_setting_for_branch

```python
def get_setting_for_branch(class_: Class,
                           branch_name: Name,
                           include_cd_os: bool = True,
                           exact_match: bool = False) -> MovieGraphSettingNode
```

x.get_setting_for_branch(class_, branch_name, include_cd_os=True, exact_match=False) -> MovieGraphSettingNode
Get Setting for Branch

Args:
    class_ (type(Class)): 
    branch_name (Name): 
    include_cd_os (bool): 
    exact_match (bool): 

Returns:
    MovieGraphSettingNode:

<a id="unreal.MovieGraphEvaluatedConfig.get_branch_names"></a>

#### get_branch_names

```python
def get_branch_names() -> Array[Name]
```

x.get_branch_names() -> Array[Name]
Get Branch Names

Returns:
    Array[Name]:

<a id="unreal.MovieGraphConfig"></a>