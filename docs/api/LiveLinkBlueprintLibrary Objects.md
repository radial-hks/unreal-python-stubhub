## LiveLinkBlueprintLibrary Objects

```python
class LiveLinkBlueprintLibrary(BlueprintFunctionLibrary)
```

Live Link Blueprint Library

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkBlueprintLibrary.h

<a id="unreal.LiveLinkBlueprintLibrary.transform_names"></a>

#### transform_names

```python
@classmethod
def transform_names(
    cls, subject_frame_handle: SubjectFrameHandle
) -> Tuple[SubjectFrameHandle, Array[Name]]
```

X.transform_names(subject_frame_handle) -> (subject_frame_handle=SubjectFrameHandle, transform_names=Array[Name])
Returns an array of Transform Names stored in the Subject Frame

Args:
    subject_frame_handle (SubjectFrameHandle): 

Returns:
    tuple: 

    subject_frame_handle (SubjectFrameHandle): 

    transform_names (Array[Name]):

<a id="unreal.LiveLinkBlueprintLibrary.transform_name"></a>

#### transform_name

```python
@classmethod
def transform_name(
        cls, live_link_transform: LiveLinkTransform
) -> Tuple[LiveLinkTransform, Name]
```

X.transform_name(live_link_transform) -> (live_link_transform=LiveLinkTransform, name=Name)
Returns the Name of a given LiveLink Transform

Args:
    live_link_transform (LiveLinkTransform): 

Returns:
    tuple: 

    live_link_transform (LiveLinkTransform): 

    name (Name):

<a id="unreal.LiveLinkBlueprintLibrary.set_live_link_subject_enabled"></a>

#### set_live_link_subject_enabled

```python
@classmethod
def set_live_link_subject_enabled(cls, subject_key: LiveLinkSubjectKey,
                                  enabled: bool) -> None
```

X.set_live_link_subject_enabled(subject_key, enabled) -> None
Set the subject's from a specific source to enabled, disabling the other in the process.
Only 1 subject with the same name can be enabled.
At the start of the frame, a snapshot of the enabled subjects will be made.
That snapshot dictate which subject will be used for the duration of that frame.
SetSubjectEnabled will take effect on the next frame.

Args:
    subject_key (LiveLinkSubjectKey): 
    enabled (bool):

<a id="unreal.LiveLinkBlueprintLibrary.remove_source"></a>

#### remove_source

```python
@classmethod
def remove_source(
        cls,
        source_handle: LiveLinkSourceHandle) -> Optional[LiveLinkSourceHandle]
```

X.remove_source(source_handle) -> LiveLinkSourceHandle or None
Requests the given LiveLink Source to shut down via its handle

Args:
    source_handle (LiveLinkSourceHandle): 

Returns:
    LiveLinkSourceHandle or None: 

    source_handle (LiveLinkSourceHandle):

<a id="unreal.LiveLinkBlueprintLibrary.request_shutdown"></a>

#### request_shutdown

```python
@classmethod
def request_shutdown(
        cls,
        source_handle: LiveLinkSourceHandle) -> Optional[LiveLinkSourceHandle]
```

deprecated: 'request_shutdown' was renamed to 'remove_source'.

<a id="unreal.LiveLinkBlueprintLibrary.parent_bone_space_transform"></a>

#### parent_bone_space_transform

```python
@classmethod
def parent_bone_space_transform(
    cls, live_link_transform: LiveLinkTransform
) -> Tuple[LiveLinkTransform, Transform]
```

X.parent_bone_space_transform(live_link_transform) -> (live_link_transform=LiveLinkTransform, transform=Transform)
Returns the Transform value in Parent Space for a given LiveLink Transform

Args:
    live_link_transform (LiveLinkTransform): 

Returns:
    tuple: 

    live_link_transform (LiveLinkTransform): 

    transform (Transform):

<a id="unreal.LiveLinkBlueprintLibrary.number_of_transforms"></a>

#### number_of_transforms

```python
@classmethod
def number_of_transforms(
    cls, subject_frame_handle: SubjectFrameHandle
) -> Tuple[int, SubjectFrameHandle]
```

X.number_of_transforms(subject_frame_handle) -> (int32, subject_frame_handle=SubjectFrameHandle)
Returns the number of Transforms stored in the Subject Frame

Args:
    subject_frame_handle (SubjectFrameHandle): 

Returns:
    SubjectFrameHandle: 

    subject_frame_handle (SubjectFrameHandle):

<a id="unreal.LiveLinkBlueprintLibrary.is_specific_live_link_subject_enabled"></a>

#### is_specific_live_link_subject_enabled

```python
@classmethod
def is_specific_live_link_subject_enabled(cls, subject_key: LiveLinkSubjectKey,
                                          for_this_frame: bool) -> bool
```

X.is_specific_live_link_subject_enabled(subject_key, for_this_frame) -> bool
Whether or not a subject from the specific source is the enabled subject.
Only 1 subject with the same name can be enabled.
At the start of the frame, a snapshot of the enabled subjects will be made.
That snapshot dictate which subject will be used for the duration of that frame.

Args:
    subject_key (LiveLinkSubjectKey): 
    for_this_frame (bool): 

Returns:
    bool:

<a id="unreal.LiveLinkBlueprintLibrary.is_source_still_valid"></a>

#### is_source_still_valid

```python
@classmethod
def is_source_still_valid(
        cls,
        source_handle: LiveLinkSourceHandle) -> Optional[LiveLinkSourceHandle]
```

X.is_source_still_valid(source_handle) -> LiveLinkSourceHandle or None
Checks whether the LiveLink Source is valid via its handle

Args:
    source_handle (LiveLinkSourceHandle): 

Returns:
    LiveLinkSourceHandle or None: 

    source_handle (LiveLinkSourceHandle):

<a id="unreal.LiveLinkBlueprintLibrary.is_live_link_subject_enabled"></a>

#### is_live_link_subject_enabled

```python
@classmethod
def is_live_link_subject_enabled(cls,
                                 subject_name: LiveLinkSubjectName) -> bool
```

X.is_live_link_subject_enabled(subject_name) -> bool
Whether or not the client has a subject with this name enabled
Only 1 subject with the same name can be enabled.
At the start of the frame, a snapshot of the enabled subjects will be made.
That snapshot dictate which subject will be used for the duration of that frame.

Args:
    subject_name (LiveLinkSubjectName): 

Returns:
    bool:

<a id="unreal.LiveLinkBlueprintLibrary.has_parent"></a>

#### has_parent

```python
@classmethod
def has_parent(
        cls,
        live_link_transform: LiveLinkTransform) -> Optional[LiveLinkTransform]
```

X.has_parent(live_link_transform) -> LiveLinkTransform or None
Returns whether a given LiveLink Transform has a parent transform

Args:
    live_link_transform (LiveLinkTransform): 

Returns:
    LiveLinkTransform or None: 

    live_link_transform (LiveLinkTransform):

<a id="unreal.LiveLinkBlueprintLibrary.get_transform_by_name"></a>

#### get_transform_by_name

```python
@classmethod
def get_transform_by_name(
        cls, subject_frame_handle: SubjectFrameHandle,
        transform_name: Name) -> Tuple[SubjectFrameHandle, LiveLinkTransform]
```

X.get_transform_by_name(subject_frame_handle, transform_name) -> (subject_frame_handle=SubjectFrameHandle, live_link_transform=LiveLinkTransform)
Returns the LiveLink Transform stored in a Subject Frame with a given name. Returns an Identity transform if Transform Name is invalid.

Args:
    subject_frame_handle (SubjectFrameHandle): 
    transform_name (Name): 

Returns:
    tuple: 

    subject_frame_handle (SubjectFrameHandle): 

    live_link_transform (LiveLinkTransform):

<a id="unreal.LiveLinkBlueprintLibrary.get_transform_by_index"></a>

#### get_transform_by_index

```python
@classmethod
def get_transform_by_index(
        cls, subject_frame_handle: SubjectFrameHandle,
        transform_index: int) -> Tuple[SubjectFrameHandle, LiveLinkTransform]
```

X.get_transform_by_index(subject_frame_handle, transform_index) -> (subject_frame_handle=SubjectFrameHandle, live_link_transform=LiveLinkTransform)
Returns the LiveLink Transform stored in a Subject Frame at a given index. Returns an Identity transform if Transform Index is invalid.

Args:
    subject_frame_handle (SubjectFrameHandle): 
    transform_index (int32): 

Returns:
    tuple: 

    subject_frame_handle (SubjectFrameHandle): 

    live_link_transform (LiveLinkTransform):

<a id="unreal.LiveLinkBlueprintLibrary.get_specific_live_link_subject_role"></a>

#### get_specific_live_link_subject_role

```python
@classmethod
def get_specific_live_link_subject_role(
        cls, subject_key: LiveLinkSubjectKey) -> Class
```

X.get_specific_live_link_subject_role(subject_key) -> type(Class)
Get the role of a subject from a specific source

Args:
    subject_key (LiveLinkSubjectKey): 

Returns:
    type(Class):

<a id="unreal.LiveLinkBlueprintLibrary.get_source_type_from_guid"></a>

#### get_source_type_from_guid

```python
@classmethod
def get_source_type_from_guid(cls, source_guid: Guid) -> Text
```

X.get_source_type_from_guid(source_guid) -> Text
Get the type of a source from the given GUID

Args:
    source_guid (Guid): the GUID identifying the LiveLink Source

Returns:
    Text: The type of the Source as Text

<a id="unreal.LiveLinkBlueprintLibrary.get_source_type"></a>

#### get_source_type

```python
@classmethod
def get_source_type(
        cls, source_handle: LiveLinkSourceHandle
) -> Tuple[Text, LiveLinkSourceHandle]
```

X.get_source_type(source_handle) -> (Text, source_handle=LiveLinkSourceHandle)
Get the type of a LiveLink Source via its handle

Args:
    source_handle (LiveLinkSourceHandle): 

Returns:
    LiveLinkSourceHandle: 

    source_handle (LiveLinkSourceHandle):

<a id="unreal.LiveLinkBlueprintLibrary.get_source_status"></a>

#### get_source_status

```python
@classmethod
def get_source_status(
        cls, source_handle: LiveLinkSourceHandle
) -> Tuple[Text, LiveLinkSourceHandle]
```

X.get_source_status(source_handle) -> (Text, source_handle=LiveLinkSourceHandle)
Get the text status of a LiveLink Source via its handle

Args:
    source_handle (LiveLinkSourceHandle): 

Returns:
    LiveLinkSourceHandle: 

    source_handle (LiveLinkSourceHandle):

<a id="unreal.LiveLinkBlueprintLibrary.get_source_machine_name"></a>

#### get_source_machine_name

```python
@classmethod
def get_source_machine_name(
        cls, source_handle: LiveLinkSourceHandle
) -> Tuple[Text, LiveLinkSourceHandle]
```

X.get_source_machine_name(source_handle) -> (Text, source_handle=LiveLinkSourceHandle)
Get the machine name of a LiveLink Source via its handle

Args:
    source_handle (LiveLinkSourceHandle): 

Returns:
    LiveLinkSourceHandle: 

    source_handle (LiveLinkSourceHandle):

<a id="unreal.LiveLinkBlueprintLibrary.get_root_transform"></a>

#### get_root_transform

```python
@classmethod
def get_root_transform(
    cls, subject_frame_handle: SubjectFrameHandle
) -> Tuple[SubjectFrameHandle, LiveLinkTransform]
```

X.get_root_transform(subject_frame_handle) -> (subject_frame_handle=SubjectFrameHandle, live_link_transform=LiveLinkTransform)
Returns the Root Transform for the Subject Frame as a LiveLink Transform or the Identity if there are no transforms.

Args:
    subject_frame_handle (SubjectFrameHandle): 

Returns:
    tuple: 

    subject_frame_handle (SubjectFrameHandle): 

    live_link_transform (LiveLinkTransform):

<a id="unreal.LiveLinkBlueprintLibrary.get_property_value"></a>

#### get_property_value

```python
@classmethod
def get_property_value(
        cls, basic_data: LiveLinkBasicBlueprintData, property_name: Name
) -> Optional[Tuple[LiveLinkBasicBlueprintData, float]]
```

X.get_property_value(basic_data, property_name) -> (basic_data=LiveLinkBasicBlueprintData, value=float) or None
Returns the value of a property stored in the Subject Frame

Args:
    basic_data (LiveLinkBasicBlueprintData): 
    property_name (Name): 

Returns:
    tuple or None: 

    basic_data (LiveLinkBasicBlueprintData): 

    value (float):

<a id="unreal.LiveLinkBlueprintLibrary.get_parent"></a>

#### get_parent

```python
@classmethod
def get_parent(
    cls, live_link_transform: LiveLinkTransform
) -> Tuple[LiveLinkTransform, LiveLinkTransform]
```

X.get_parent(live_link_transform) -> (live_link_transform=LiveLinkTransform, parent=LiveLinkTransform)
Returns the Parent LiveLink Transform if one exists or an Identity transform if no parent exists

Args:
    live_link_transform (LiveLinkTransform): 

Returns:
    tuple: 

    live_link_transform (LiveLinkTransform): 

    parent (LiveLinkTransform):

<a id="unreal.LiveLinkBlueprintLibrary.get_metadata"></a>

#### get_metadata

```python
@classmethod
def get_metadata(
    cls, subject_frame_handle: SubjectFrameHandle
) -> Tuple[SubjectFrameHandle, SubjectMetadata]
```

X.get_metadata(subject_frame_handle) -> (subject_frame_handle=SubjectFrameHandle, metadata=SubjectMetadata)
Returns the Subject Metadata structure stored in the Subject Frame

Args:
    subject_frame_handle (SubjectFrameHandle): 

Returns:
    tuple: 

    subject_frame_handle (SubjectFrameHandle): 

    metadata (SubjectMetadata):

<a id="unreal.LiveLinkBlueprintLibrary.get_live_link_subject_state"></a>

#### get_live_link_subject_state

```python
@classmethod
def get_live_link_subject_state(
        cls, subject_name: LiveLinkSubjectName) -> LiveLinkSubjectState
```

X.get_live_link_subject_state(subject_name) -> LiveLinkSubjectState
Returns the state of the subject with the given name.

Args:
    subject_name (LiveLinkSubjectName): 

Returns:
    LiveLinkSubjectState:

<a id="unreal.LiveLinkBlueprintLibrary.get_live_link_subjects"></a>

#### get_live_link_subjects

```python
@classmethod
def get_live_link_subjects(
        cls, include_disabled_subject: bool,
        include_virtual_subject: bool) -> Array[LiveLinkSubjectKey]
```

X.get_live_link_subjects(include_disabled_subject, include_virtual_subject) -> Array[LiveLinkSubjectKey]
Get a list of all subjects

Args:
    include_disabled_subject (bool): 
    include_virtual_subject (bool): 

Returns:
    Array[LiveLinkSubjectKey]:

<a id="unreal.LiveLinkBlueprintLibrary.get_live_link_subject_role"></a>

#### get_live_link_subject_role

```python
@classmethod
def get_live_link_subject_role(cls,
                               subject_name: LiveLinkSubjectName) -> Class
```

X.get_live_link_subject_role(subject_name) -> type(Class)
Get the role of the subject with this name

Args:
    subject_name (LiveLinkSubjectName): 

Returns:
    type(Class):

<a id="unreal.LiveLinkBlueprintLibrary.get_live_link_enabled_subject_names"></a>

#### get_live_link_enabled_subject_names

```python
@classmethod
def get_live_link_enabled_subject_names(
        cls, include_virtual_subject: bool) -> Array[LiveLinkSubjectName]
```

X.get_live_link_enabled_subject_names(include_virtual_subject) -> Array[LiveLinkSubjectName]
Get a list of all enabled subject names

Args:
    include_virtual_subject (bool): 

Returns:
    Array[LiveLinkSubjectName]:

<a id="unreal.LiveLinkBlueprintLibrary.get_curves"></a>

#### get_curves

```python
@classmethod
def get_curves(
    cls, subject_frame_handle: SubjectFrameHandle
) -> Tuple[SubjectFrameHandle, Map[Name, float]]
```

X.get_curves(subject_frame_handle) -> (subject_frame_handle=SubjectFrameHandle, curves=Map[Name, float])
Returns the float curves stored in the Subject Frame as a map

Args:
    subject_frame_handle (SubjectFrameHandle): 

Returns:
    tuple: 

    subject_frame_handle (SubjectFrameHandle): 

    curves (Map[Name, float]):

<a id="unreal.LiveLinkBlueprintLibrary.get_children"></a>

#### get_children

```python
@classmethod
def get_children(
    cls, live_link_transform: LiveLinkTransform
) -> Tuple[LiveLinkTransform, Array[LiveLinkTransform]]
```

X.get_children(live_link_transform) -> (live_link_transform=LiveLinkTransform, children=Array[LiveLinkTransform])
Returns an array of Child LiveLink Transforms for a given LiveLink Transform

Args:
    live_link_transform (LiveLinkTransform): 

Returns:
    tuple: 

    live_link_transform (LiveLinkTransform): 

    children (Array[LiveLinkTransform]):

<a id="unreal.LiveLinkBlueprintLibrary.get_basic_data"></a>

#### get_basic_data

```python
@classmethod
def get_basic_data(
    cls, subject_frame_handle: SubjectFrameHandle
) -> Tuple[SubjectFrameHandle, LiveLinkBasicBlueprintData]
```

X.get_basic_data(subject_frame_handle) -> (subject_frame_handle=SubjectFrameHandle, basic_blueprint_data=LiveLinkBasicBlueprintData)
Returns the Subject base structure stored in the Subject Frame

Args:
    subject_frame_handle (SubjectFrameHandle): 

Returns:
    tuple: 

    subject_frame_handle (SubjectFrameHandle): 

    basic_blueprint_data (LiveLinkBasicBlueprintData):

<a id="unreal.LiveLinkBlueprintLibrary.get_animation_static_data"></a>

#### get_animation_static_data

```python
@classmethod
def get_animation_static_data(
    cls, subject_frame_handle: SubjectFrameHandle
) -> Optional[Tuple[SubjectFrameHandle, LiveLinkSkeletonStaticData]]
```

X.get_animation_static_data(subject_frame_handle) -> (subject_frame_handle=SubjectFrameHandle, animation_static_data=LiveLinkSkeletonStaticData) or None
Returns the Subject's static data stored in the Subject Frame. Returns false if no valid data found.

Args:
    subject_frame_handle (SubjectFrameHandle): 

Returns:
    tuple or None: 

    subject_frame_handle (SubjectFrameHandle): 

    animation_static_data (LiveLinkSkeletonStaticData):

<a id="unreal.LiveLinkBlueprintLibrary.get_animation_frame_data"></a>

#### get_animation_frame_data

```python
@classmethod
def get_animation_frame_data(
    cls, subject_frame_handle: SubjectFrameHandle
) -> Optional[Tuple[SubjectFrameHandle, LiveLinkAnimationFrameData]]
```

X.get_animation_frame_data(subject_frame_handle) -> (subject_frame_handle=SubjectFrameHandle, animation_frame_data=LiveLinkAnimationFrameData) or None
Returns the Subject's frame data stored in the Subject Frame. Returns false if no valid data found.

Args:
    subject_frame_handle (SubjectFrameHandle): 

Returns:
    tuple or None: 

    subject_frame_handle (SubjectFrameHandle): 

    animation_frame_data (LiveLinkAnimationFrameData):

<a id="unreal.LiveLinkBlueprintLibrary.component_space_transform"></a>

#### component_space_transform

```python
@classmethod
def component_space_transform(
    cls, live_link_transform: LiveLinkTransform
) -> Tuple[LiveLinkTransform, Transform]
```

X.component_space_transform(live_link_transform) -> (live_link_transform=LiveLinkTransform, transform=Transform)
Returns the Transform value in Root Space for a given LiveLink Transform

Args:
    live_link_transform (LiveLinkTransform): 

Returns:
    tuple: 

    live_link_transform (LiveLinkTransform): 

    transform (Transform):

<a id="unreal.LiveLinkBlueprintLibrary.child_count"></a>

#### child_count

```python
@classmethod
def child_count(
        cls, live_link_transform: LiveLinkTransform
) -> Tuple[int, LiveLinkTransform]
```

X.child_count(live_link_transform) -> (int32, live_link_transform=LiveLinkTransform)
Returns the number of Children for a given LiveLink Transform

Args:
    live_link_transform (LiveLinkTransform): 

Returns:
    LiveLinkTransform: 

    live_link_transform (LiveLinkTransform):

<a id="unreal.LiveLinkComponent"></a>