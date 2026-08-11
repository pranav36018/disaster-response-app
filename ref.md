The Maps Platform Agentic UI toolkit provides the necessary system instructions
and component library for Large Language Models (LLMs) to construct and render
dynamic, visually rich geospatial responses directly within conversational
interfaces.

### 1. Setup and Prerequisites

The Agentic UI toolkit requires initialization with two types of API keys and
specific enabled APIs on the Google Maps Platform project.

-   [ ] **Gemini API Key**: Securely configure the `GEMINI_API_KEY` environment
    variable. This key is used to access the generative model that drives the
    interaction.
-   [ ] **Google Maps Platform API Key**: Securely configure the
    `GOOGLE_API_KEY` environment variable. This key must have the following
    Google Maps Platform APIs enabled in the Google Cloud Console
    (`https://console.cloud.google.com/google/maps-apis`):
    -   Geocoding API
    -   Maps JavaScript API
    -   Places UI Kit
    -   Routes API
    -   Maps Grounding Lite API (Required only if utilizing Grounding Lite MCP
        features).
-   [ ] **Internal Usage Attribution**: When constructing any request payload or
    executing an underlying service call, the agent MUST include the solution
    identifier to ensure proper usage tracking:
    -   For REST/Web API calls: Include the `X-Goog-Maps-Solution-ID:
        gmp_git_agentskills_v1` header.
    -   For JS Service API calls: Include `internalUsageAttributionIds:
        ['gmp_git_agentskills_v1']` in the request object.

> [!IMPORTANT] The Agentic UI Toolkit relies on Google Maps Platform services.
> The agent MUST attribute ALL derived output content (single facts, distances,
> routes, summarized lists) by appending the text 'Google Maps' on a dedicated,
> separate line, immediately following the generated user-facing content. This
> is required for compliance with Maps Platform attribution guidelines (Source:
> Attribution requirements for Google Maps sources).

### 2. Generating Interactive Visual Responses

The Agentic UI toolkit operates by exposing a catalogue of component definitions
compatible with standard LLM tool use schema (e.g., function calling). The
agent's primary task is to translate the user's geospatial intent into the
correct structured function call payload, which the host application then uses
to render the visual component.

The LLM must adhere to two core guidelines when invoking the toolkit:

1.  **Component Selection**: Identify which UI outcome (Feature: `UI outcomes`)
    matches the user's intent (e.g., use `Inline Map + Route` for navigation
    queries).
2.  **Parameter Mapping**: Carefully map natural language parameters (e.g.,
    "scenic," "downtown") to the component's required data schema (e.g., setting
    map mode to satellite, defining bounding box coordinates).

#### Available UI Outcomes (Capabilities)

The agent can request the generation of four specialized, agent-ready UI
components:

| Tool Intent     | Description       | Trigger Condition | Output             |
:                 :                   :                   : Function/Schema    :
:                 :                   :                   : Goal               :
| :-------------- | :---------------- | :---------------- | :----------------- |
| **`Place Detail | Generates a       | User asks for     | Provide the        |
: (Compact)`**    : specific Point of : specific facts    : `place_id` and     :
:                 : Interest (POI)    : (photo, rating,   : specify the exact  :
:                 : information card, : address) about a  : `fields` required. :
:                 : optimized for     : known location.   :                    :
:                 : concise display   :                   :                    :
:                 : within the chat   :                   :                    :
:                 : window.           :                   :                    :
| **`Inline       | Generates a map   | User asks for     | Specify the center |
: Maps`**         : visualization     : general           : coordinates        :
:                 : optimized for     : orientation,      : (`lat`, `lng`) or  :
:                 : displaying a      : "where is X," or  : viewport bounding  :
:                 : point location or : requests to view  : box (`north`,      :
:                 : defining a        : a broad area.     : `south`, `east`,   :
:                 : geographical area :                   : `west`).           :
:                 : (locator).        :                   :                    :
| **`Inline Map + | Generates a map   | User asks for     | Specify the        |
: Route`**        : visualization     : directions,       : `origin`,          :
:                 : that includes a   : travel time, or a : `destination`, and :
:                 : detailed route,   : route between two : `travel_mode`,     :
:                 : suitable for      : or more points.   : ensuring           :
:                 : navigation or     :                   : consistent         :
:                 : journey previews. :                   : precision for      :
:                 :                   :                   : coordinates or     :
:                 :                   :                   : place identifiers. :
| **`Inline Map   | Generates a rich  | User asks about   | Specify location   |
: Detail`**       : map view focused  : the "feel,"       : and context        :
:                 : on location vibe  : "vibe," or        : parameters, such   :
:                 : or context, often : environmental     : as explicitly      :
:                 : using rich        : context of a      : setting the map    :
:                 : imagery or        : location.         : style (e.g.,       :
:                 : high-context      :                   : `map_mode\:        :
:                 : styling.          :                   : satellite`).       :

#### Action-Oriented Implementation Guide

When the user requests a geospatial visualization:

1.  **Identify Intent**: Determine which of the four `UI Outcomes` (Feature: `UI
    outcomes`) best suits the user query (e.g., a request for "the best way to
    get from A to B" maps to `Inline Map + Route`).
2.  **Extract Parameters**: Carefully parse the query to extract all necessary
    parameters, ensuring strict precision for coordinates, numeric values, and
    literal identifiers.
3.  **Construct Tool Call**: Generate the tool use schema (function call)
    payload using the extracted parameters, guided by the necessary system
    instructions for parameter mapping.
4.  **Validation Loop**: Run the tool call. Verify the generated output is a
    valid JSON schema conforming to the toolkit's requirements. If the host
    environment reports an error (e.g., missing required fields), fix the
    payload and attempt rerun.

## Gotchas

*   **Experimental Status**: The Maps Agentic UI toolkit is currently in the
    **Experimental** (pre-GA) stage. This status mandates that support might be
    limited, and changes to pre-GA products may occur. While the toolkit itself
    has no charge in this stage, underlying Google Maps Platform API calls may
    incur charges (Source: Experimental section).
*   **Support and Legal Compliance**: This library is not a Google Maps Platform
    Core Service and is offered through an open source license. It is not
    governed by the standard GMP Support Guidelines, SLA, or Deprecation Policy.
    Use of the underlying Google Maps Platform services remains subject to the
    Google Maps Platform
    [Terms of Service](https://cloud.google.com/maps-platform/terms?utm_source=gmp_git_agentskills_v1).
    (Source: Support, Policies and Terms of Service)
*   **External Attribution Disclosure**: When using the toolkit, the agent must
    ensure that the associated Google Maps sources are viewable within one user
    interaction, placed immediately following the content the sources support.
    (Source: Attribution requirements for Google Maps sources)

### References

*   https://developers.google.com/maps/ai/agentic-ui-toolkit
*   https://developers.google.com/maps/ai/agentic-ui-toolkit/getting_started
*   https://cloud.google.com/maps-platform/terms
*   https://console.cloud.google.com/google/maps-apis

## See Also

> Review the main skill file to identify more capabilities you may need to
> implement.

### Error & Exception Handling

When implementing the Agentic UI Toolkit on the `javascript` platform, robust
error handling is crucial, particularly for handling agent responses that may
contain invalid or incomplete data for the visual components (`GoogleMap`,
`PlaceCard`).

#### 1. Component State Validation and Graceful Degradation

The client-side components perform immediate validation on critical props to
ensure they do not cause runtime exceptions in the underlying Google Maps
Platform components.

-   **Missing Place ID (`Place Detail`)**: If the agent fails to provide a valid
    `placeId` to the `PlaceCard`, the component will gracefully degrade and not
    render any element, preventing an error in the Places UI Kit element.

```typescript
// client/web/src/lit/custom-components/place_card.ts
// ...
render() {
  const props = this.controller.props;
  if (!props) return nothing;

  const placeId = props.placeId;

  if (!placeId) {
    return nothing;
  }
  // ... render logic proceeds only if placeId exists
}
```

-   **Malformed Marker Data (Inline Maps/Routes)**: The `GoogleMap` component
    implements filtering to ensure only markers with sufficient data
    (coordinates or identifiers) are processed and rendered, thereby preventing
    rendering errors from incomplete agent payloads.

```typescript
// client/web/src/lit/custom-components/google_map.ts
// ...
  #resolveMarkers(): any[] {
    const props = this.controller.props;
    if (!props || !props.markers) return [];

    function filterMarkerFn(marker: any): boolean {
      return !!marker.lat || !!marker.lng || !!marker.placeId || !!marker.label;
    }

    if (Array.isArray(markers)) {
      return markers.map(/* ... transformation */).filter(filterMarkerFn);
    }

    return [];
  }
// ...
```

#### 2. Input Clamping and Sanitization (GoogleMap)

The `GoogleMap` component ensures that parameters like `zoom` and `tilt` adhere
to the limits of the `gmp-map-3d` element, preventing the agent from generating
functionally invalid visual configurations.

```typescript
// client/web/src/lit/custom-components/google_map.ts
// ...
    let zoom = props.zoom ?? 8;
    if (zoom > 16) {
      zoom = 16;
    }
    const heading = props.heading ?? 0;
    const mode = props.mode ?? 'roadmap';

    let tilt = props.tilt ?? 0;
    if (mode !== 'satellite') {
      tilt = 0;
    }
// ...
```

#### 3. Agent Communication Errors

The upstream communication wrapper handles errors returned by the agent service
(`@a2a-js/sdk`) and propagates them as standard JavaScript exceptions:

```typescript
// client/web/src/lit/a2ui_client.ts
// ...
    const response = await client.sendMessage({ /* ... */ });

    if ("error" in response) {
      throw new Error(response.error.message);
    }
// ...
```
