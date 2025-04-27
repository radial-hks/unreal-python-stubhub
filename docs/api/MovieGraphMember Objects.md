## MovieGraphMember Objects

```python
class MovieGraphMember(MovieGraphValueContainer)
```

Movie Graph Member

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphConfig.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``description`` (str):  [Read-Write] The optional description of this member, which is user-facing.
- ``value`` (InstancedPropertyBag):  [Read-Write] The value held by this object.

<a id="unreal.MovieGraphMember.set_member_name"></a>

#### set_member_name

```python
def set_member_name(new_name: str) -> bool
```

x.set_member_name(new_name) -> bool
Sets the name of this member. Returns true if the rename was successful, else false.

Args:
    new_name (str): 

Returns:
    bool:

<a id="unreal.MovieGraphMember.get_member_name"></a>

#### get_member_name

```python
def get_member_name() -> str
```

x.get_member_name() -> str
Gets the name of this member.

Returns:
    str:

<a id="unreal.MovieGraphMember.get_guid"></a>

#### get_guid

```python
def get_guid() -> Guid
```

x.get_guid() -> Guid
Gets the GUID that uniquely identifies this member.

Returns:
    Guid:

<a id="unreal.MovieGraphVariable"></a>