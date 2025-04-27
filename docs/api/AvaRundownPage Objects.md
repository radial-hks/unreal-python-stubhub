## AvaRundownPage Objects

```python
class AvaRundownPage(StructBase)
```

Ava Rundown Page

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaRundownPage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_path`` (SoftObjectPath):  [Read-Only] Template property: path for this template.
- ``combined_template_ids`` (Array[int32]):  [Read-Only] Template property: For combination template, lists the templates that are combined.
  A combination template can only be created using transition logic templates.
  In order to create a combination template, the templates must be in different transition layers.
- ``enabled`` (bool):  [Read-Only]
- ``friendly_name`` (Text):  [Read-Only]
- ``has_transition_logic`` (bool):  [Read-Only] Indicate if the template asset has transition logic.
- ``instances`` (Set[int32]):  [Read-Only] Template property: List the Ids of all instances.
- ``output_channel`` (int32):  [Read-Only]
- ``page_id`` (int32):  [Read-Only]
- ``page_name`` (str):  [Read-Only]
- ``page_summary`` (Text):  [Read-Only]
- ``remote_control_values`` (AvaPlayableRemoteControlValues):  [Read-Write]
- ``template_id`` (int32):  [Read-Only] Page Instance Property: Template Id for this page.
- ``transition_layer_tag`` (AvaTagHandle):  [Read-Only] Transition Layer Tag cached from the transition tree. Cached for fast display in page/template list.
- ``transition_mode`` (AvaTransitionInstancingMode):  [Read-Only]

<a id="unreal.AvaRundownPage.__init__"></a>

#### __init__

```python
def __init__(
    enabled: bool = False,
    page_id: int = 0,
    template_id: int = 0,
    combined_template_ids: Array[int] = [],
    page_name: str = "",
    asset_path: SoftObjectPath = [""],
    instances: Set[int] = [],
    output_channel: int = 0,
    page_summary: Text = "",
    friendly_name: Text = "",
    has_transition_logic: bool = False,
    transition_mode: AvaTransitionInstancingMode = AvaTransitionInstancingMode.
    NEW
) -> None
```

<a id="unreal.AvaRundownPage.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AvaRundownPage.page_id"></a>

#### page_id

```python
@property
def page_id() -> int
```

(int32):  [Read-Only]

<a id="unreal.AvaRundownPage.template_id"></a>

#### template_id

```python
@property
def template_id() -> int
```

(int32):  [Read-Only] Page Instance Property: Template Id for this page.

<a id="unreal.AvaRundownPage.combined_template_ids"></a>

#### combined_template_ids

```python
@property
def combined_template_ids() -> Array[int]
```

(Array[int32]):  [Read-Only] Template property: For combination template, lists the templates that are combined.
A combination template can only be created using transition logic templates.
In order to create a combination template, the templates must be in different transition layers.

<a id="unreal.AvaRundownPage.page_name"></a>

#### page_name

```python
@property
def page_name() -> str
```

(str):  [Read-Only]

<a id="unreal.AvaRundownPage.asset_path"></a>

#### asset_path

```python
@property
def asset_path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only] Template property: path for this template.

<a id="unreal.AvaRundownPage.instances"></a>

#### instances

```python
@property
def instances() -> Set[int]
```

(Set[int32]):  [Read-Only] Template property: List the Ids of all instances.

<a id="unreal.AvaRundownPage.output_channel"></a>

#### output_channel

```python
@property
def output_channel() -> int
```

(int32):  [Read-Only]

<a id="unreal.AvaRundownPage.page_summary"></a>

#### page_summary

```python
@property
def page_summary() -> Text
```

(Text):  [Read-Only]

<a id="unreal.AvaRundownPage.friendly_name"></a>

#### friendly_name

```python
@property
def friendly_name() -> Text
```

(Text):  [Read-Only]

<a id="unreal.AvaRundownPage.has_transition_logic"></a>

#### has_transition_logic

```python
@property
def has_transition_logic() -> bool
```

(bool):  [Read-Only] Indicate if the template asset has transition logic.

<a id="unreal.AvaRundownPage.transition_mode"></a>

#### transition_mode

```python
@property
def transition_mode() -> AvaTransitionInstancingMode
```

(AvaTransitionInstancingMode):  [Read-Only]

<a id="unreal.AvalanchePage"></a>