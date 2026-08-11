---
name: agentic-ui-toolkit-javascript
description: Use this skill for generating code using the modern Google Maps Platform JavaScript SDK. It covers implementing maps, calculating routes and distances (Route class), retrieving up-to-date place information and media (Place class), and visualizing locations with customizable markers (AdvancedMarkerElement), strictly avoiding deprecated APIs for maximum compatibility and cost efficiency.
license: Apache-2.0
metadata:
  version: 1.0.7
---

> [!IMPORTANT] **Core Dependency:** This skill requires active context from
> [google-maps-platform/SKILL.md](https://www.gstatic.com/googlemapsplatform-agent-skills/google-maps-platform/SKILL.md).

### Overview

This skill provides the comprehensive toolkit for building high-performance,
cost-efficient applications using the Google Maps Platform JavaScript SDK. It
mandates the use of modern, promise-based classes and components to replace all
legacy services, ensuring forward compatibility and access to the latest
features.

**Key Modern Components Governed by this Skill:**

*   **Maps and Markers:** Initialization of the base Map object using the
    asynchronous loader pattern, coupled with mandatory use of the
    AdvancedMarkerElement and a mapId for rich location visualization.
*   **Places API (New):** Utilizing the Place class for fetching detailed place
    information, reviews, and media (fetchFields), replacing the callback-based
    PlacesService. It also covers modern search operations like searchByText and
    searchNearby.
*   **Routes and Distance:** Implementation of the Route class for performing
    all directions and distance calculations (computeRoutes, createPolylines),
    replacing the deprecated DirectionsService and DistanceMatrixService.
*   **UX Components:** Guidance on implementing modern widgets, such as
    PlaceAutocompleteElement, while adhering to React framework specific rules
    for passing complex objects.

All generated code adheres to security best practices, cost-optimization
techniques (e.g., session token usage), and strictly avoids deprecated APIs and
legacy services (e.g., google.maps.Marker, DirectionsRenderer).

### Mandatory settings

The Agentic UI toolkit requires specific keys and API entitlements to function
correctly within the runtime environment.

#### API Keys & Environment Variables

The following keys must be available to the runtime environment for the toolkit
to function:

*   **`GEMINI_API_KEY`**: The Google Gemini API key required for the core AI
    execution. Obtainable from
    [Google AI Studio](https://aistudio.google.com/?utm_source=gmp_git_agentskills_v1).
*   **`GOOGLE_API_KEY`**: The Google Maps Platform API key required for location
    data retrieval and UI rendering.

#### Mandatory Enabled APIs

The Maps Platform API Key must have the following services enabled in the
[Google Cloud Console](https://console.cloud.google.com/google/maps-apis?utm_source=gmp_git_agentskills_v1):

*   Geocoding API
*   Places UI Kit
*   Routes API

#### Mandatory Usage Attribution

The agent MUST ensure the unique solution ID `gmp_git_agentskills_v1` is
configured for internal usage tracking whenever a map component or service
request is executed by the toolkit.

#### JavaScript Service API Calls

For JavaScript Service API calls (e.g., using a Maps Platform service client),
the solution ID is included within the request object payload.

```javascript
// Example: When requesting data or features from a Maps Platform service
const request = {
  // ... other API parameters
  internalUsageAttributionIds: ['gmp_git_agentskills_v1']
};
```

#### Standard REST/Web API Calls

When constructing any raw REST or Web API calls to Google Maps Platform
endpoints, the solution ID must be included in the HTTP header.

```http
X-Goog-Maps-Solution-ID: gmp_git_agentskills_v1
```

## 🚀 Master Orchestration Integration Workflow

Follow this multi-phase sequential integration checklist to compose features
robustly. For each phase, read the referenced capability sub-workflow file and
satisfy its *Evidence Checkpoint* before advancing.

### 📦 Phase 1: Feature Layer & Custom Enrichment (Supplemental)

#### 🗺️ Feature Module: Generative AI (Optional - Use-Case Dependent)

-   [ ] **Renders a specialized card component showing detailed information
    about a geographical place (address, reviews, contact, operating hours),
    formatted for consumption by an AI agent or direct user display.** Read
    [references/display-place-details-optimized-for-agent-responses.md](https://www.gstatic.com/googlemapsplatform-agent-skills/agentic-ui-toolkit-javascript/references/display-place-details-optimized-for-agent-responses.md).
    *Trigger Condition*: When the user asks for specific, detailed information
    about a known location or point of interest. *Evidence Checkpoint*: The
    agent successfully generates and displays the structured Place Details card
    containing requested attributes (e.g., name, address, hours) relevant to the
    specified place ID.
-   [ ] **Instantiates and displays a fully interactive map viewport component
    optimized for integration into agent interfaces, allowing users to pan,
    zoom, and interact with map features.** Read
    [references/embed-interactive-map-optimized-for-agent-responses.md](https://www.gstatic.com/googlemapsplatform-agent-skills/agentic-ui-toolkit-javascript/references/embed-interactive-map-optimized-for-agent-responses.md).
    *Trigger Condition*: When the user requests to visualize a geographic area,
    region, or set of coordinates. *Evidence Checkpoint*: The interactive map
    viewport component initializes correctly and displays the requested
    geographical area, ready for user interaction.
-   [ ] **Calculates and displays a visual route (path line and associated
    steps) between two or more geographical points on an interactive map
    component.** Read
    [references/display-route-map-optimized-for-agent-responses.md](https://www.gstatic.com/googlemapsplatform-agent-skills/agentic-ui-toolkit-javascript/references/display-route-map-optimized-for-agent-responses.md).
    *Dependencies*:
    `["references/embed-interactive-map-optimized-for-agent-responses.md"]`
    *Trigger Condition*: When the user asks for directions, routing, or
    navigation guidance between two specific locations. *Evidence Checkpoint*: A
    calculated route line segment, along with start and end markers, is
    successfully rendered overlaid on the map component.
-   [ ] **Displays rich visual media (e.g., high-quality photos, imagery, or
    Street View) associated with a specific location, integrated into an agent
    response format.** Read
    [references/show-rich-visual-location-details-optimized-for-agent-responses.md](https://www.gstatic.com/googlemapsplatform-agent-skills/agentic-ui-toolkit-javascript/references/show-rich-visual-location-details-optimized-for-agent-responses.md).
    *Trigger Condition*: When the user asks to see images, photos, or visual
    context (like Street View) for a place. *Evidence Checkpoint*:
    High-resolution visual media or a specific visual component (e.g., photo
    carousel or Street View display) related to the location is successfully
    rendered.
