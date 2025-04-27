## AvaRundown Objects

```python
class AvaRundown(Object)
```

This class is a container for what could be described as a "show" for broadcast purposes.

It goes beyond a simple list of items. It contains the following:
- a list of Motion Design Template Pages (or just Templates).
- a list of Motion Design Instanced Pages (or just Pages).
- a list of page views (or just Views).

Workflow:

1- Templates

The first step in the work flow consist in importing templates. The source asset is not actually imported
in the "show" container, it is just soft referenced. However, the import process will load and cache some information
about the template (exposed properties, default values, animations, transition logic layer, etc).
Given that this information is cached, it may become stale if the source asset is updated. Therefore, reimporting
the templates may be necessary within the normal work flow.
Todo: keep a hash of the source asset to determine if it has changed.

2- Pages

The pages are instances of the templates, allowing to change the exposed properties and controllers, also selecting
an output program channel for the given page. Only one program channel is allowed per page.

3- Page Views

Separate page views can be made in order to create "rundowns" for separate segments/parts of a show.

"Page Groups" Discussion:
"Page Groups" are not implemented. It would be different than page views, i.e.
pages could be grouped in either of the page list or page views.
Other applications support page grouping to emulate MOS's hierarchy.
In the MOS/NCS hierarchies: Rundown -> Stories/Segments -> Parts -> Pieces/Items
Although full emulation of MOS schema may not be necessary within the Motion Design playback framework.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaRundown.h

<a id="unreal.AvalanchePlaylist"></a>